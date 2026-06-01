# server.py - Complete HSK Mandarin Teacher with Dynamic Lesson System

from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
from flask_cors import CORS
import json
import os
import asyncio
import edge_tts
import hashlib
import re
import requests

app = Flask(__name__)
CORS(app)

os.makedirs("static", exist_ok=True)

# ============================================
# CONFIGURATION
# ============================================

OLLAMA_URL = "http://127.0.0.1:11434"
MODEL_NAME = "mistral:instruct"

# Lesson data path for JSON files
LESSON_DATA_PATH = os.path.join(os.path.dirname(__file__), 'templates', 'data')
os.makedirs(LESSON_DATA_PATH, exist_ok=True)

# Max lessons per level
MAX_LESSONS = {1: 15, 2: 15, 3: 20, 4: 20, 5: 36, 6: 40}

# ============================================
# COMPLETE HSK 1 VOCABULARY (150+ words)
# ============================================

HSK1_VOCAB = {
    1: [
        {"word": "妈妈", "pinyin": "ma ma", "meaning": "mother", "example": "这是我的妈妈"},
        {"word": "爸爸", "pinyin": "ba ba", "meaning": "father", "example": "爸爸去上班"},
        {"word": "你好", "pinyin": "ni hao", "meaning": "hello", "example": "你好，我叫小明"},
        {"word": "谢谢", "pinyin": "xie xie", "meaning": "thank you", "example": "谢谢你帮助我"},
        {"word": "再见", "pinyin": "zai jian", "meaning": "goodbye", "example": "明天再见"},
        {"word": "老师", "pinyin": "lao shi", "meaning": "teacher", "example": "王老师很好"},
        {"word": "学生", "pinyin": "xue sheng", "meaning": "student", "example": "我是学生"},
        {"word": "中国", "pinyin": "Zhong guo", "meaning": "China", "example": "我爱中国"},
        {"word": "北京", "pinyin": "Bei jing", "meaning": "Beijing", "example": "北京是首都"},
        {"word": "什么", "pinyin": "shen me", "meaning": "what", "example": "你叫什么名字"},
        {"word": "名字", "pinyin": "ming zi", "meaning": "name", "example": "我的名字是"},
        {"word": "是", "pinyin": "shi", "meaning": "to be", "example": "我是中国人"},
        {"word": "不", "pinyin": "bu", "meaning": "no not", "example": "不是"},
        {"word": "很", "pinyin": "hen", "meaning": "very", "example": "很好"},
        {"word": "好", "pinyin": "hao", "meaning": "good", "example": "天气很好"},
        {"word": "大", "pinyin": "da", "meaning": "big", "example": "大城市"},
        {"word": "小", "pinyin": "xiao", "meaning": "small", "example": "小狗"},
        {"word": "多", "pinyin": "duo", "meaning": "many", "example": "很多人"},
        {"word": "少", "pinyin": "shao", "meaning": "few", "example": "很少"},
        {"word": "去", "pinyin": "qu", "meaning": "to go", "example": "去学校"},
        {"word": "来", "pinyin": "lai", "meaning": "to come", "example": "来我家"},
        {"word": "看", "pinyin": "kan", "meaning": "to see", "example": "看电影"},
        {"word": "听", "pinyin": "ting", "meaning": "to listen", "example": "听音乐"},
        {"word": "说", "pinyin": "shuo", "meaning": "to speak", "example": "说汉语"},
        {"word": "吃", "pinyin": "chi", "meaning": "to eat", "example": "吃饭"},
        {"word": "喝", "pinyin": "he", "meaning": "to drink", "example": "喝水"},
        {"word": "水", "pinyin": "shui", "meaning": "water", "example": "一杯水"},
        {"word": "茶", "pinyin": "cha", "meaning": "tea", "example": "喝茶"},
        {"word": "喜欢", "pinyin": "xi huan", "meaning": "to like", "example": "我喜欢你"},
        {"word": "爱", "pinyin": "ai", "meaning": "to love", "example": "我爱你"},
        {"word": "家", "pinyin": "jia", "meaning": "home", "example": "回家"},
        {"word": "学校", "pinyin": "xue xiao", "meaning": "school", "example": "去学校"},
        {"word": "朋友", "pinyin": "peng you", "meaning": "friend", "example": "我的好朋友"},
    ],
    2: [
        {"word": "电脑", "pinyin": "dian nao", "meaning": "computer", "example": "我用电脑学习"},
        {"word": "手机", "pinyin": "shou ji", "meaning": "mobile phone", "example": "打电话用手机"},
        {"word": "工作", "pinyin": "gong zuo", "meaning": "work", "example": "我在工作"},
        {"word": "学习", "pinyin": "xue xi", "meaning": "to study", "example": "学习汉语"},
        {"word": "快乐", "pinyin": "kuai le", "meaning": "happy", "example": "生日快乐"},
        {"word": "漂亮", "pinyin": "piao liang", "meaning": "beautiful", "example": "她很漂亮"},
        {"word": "便宜", "pinyin": "pian yi", "meaning": "cheap", "example": "这个东西很便宜"},
        {"word": "贵", "pinyin": "gui", "meaning": "expensive", "example": "太贵了"},
    ],
    3: [
        {"word": "美丽", "pinyin": "mei li", "meaning": "beautiful", "example": "美丽的风景"},
        {"word": "重要", "pinyin": "zhong yao", "meaning": "important", "example": "学习很重要"},
        {"word": "容易", "pinyin": "rong yi", "meaning": "easy", "example": "汉语不容易"},
        {"word": "困难", "pinyin": "kun nan", "meaning": "difficult", "example": "这个问题很困难"},
        {"word": "非常", "pinyin": "fei chang", "meaning": "extremely", "example": "非常好"},
    ],
    4: [
        {"word": "环境", "pinyin": "huan jing", "meaning": "environment", "example": "保护环境"},
        {"word": "经济", "pinyin": "jing ji", "meaning": "economy", "example": "经济发展"},
        {"word": "文化", "pinyin": "wen hua", "meaning": "culture", "example": "中国文化"},
        {"word": "发展", "pinyin": "fa zhan", "meaning": "development", "example": "快速发展"},
    ],
    5: [
        {"word": "复杂", "pinyin": "fu za", "meaning": "complex", "example": "情况很复杂"},
        {"word": "简单", "pinyin": "jian dan", "meaning": "simple", "example": "很简单"},
        {"word": "可能", "pinyin": "ke neng", "meaning": "possible", "example": "可能会下雨"},
    ],
    6: [
        {"word": "和谐", "pinyin": "he xie", "meaning": "harmony", "example": "社会和谐"},
        {"word": "创新", "pinyin": "chuang xin", "meaning": "innovation", "example": "技术创新"},
        {"word": "传统", "pinyin": "chuan tong", "meaning": "tradition", "example": "传统文化"},
    ],
}

# ============================================
# HSK 1 LESSONS DATA (For backward compatibility)
# ============================================

HSK1_LESSONS = {
    1: {"number": 1, "title": "你好", "title_en": "Hello", "objectives": ["Learn to greet people", "Introduce yourself", "Say goodbye"]},
    2: {"number": 2, "title": "谢谢你", "title_en": "Thank You", "objectives": ["Express thanks", "Apologize", "Use polite expressions"]},
    3: {"number": 3, "title": "你叫什么名字", "title_en": "What's Your Name", "objectives": ["Ask and answer about names", "Use question words", "Introduce family"]},
    4: {"number": 4, "title": "她是我的汉语老师", "title_en": "She's My Chinese Teacher", "objectives": ["Describe people", "Use possessive 的", "Talk about nationalities"]},
    5: {"number": 5, "title": "她女儿今年二十岁", "title_en": "Her Daughter is 20 Years Old", "objectives": ["Talk about age", "Use numbers 1-100", "Ask 'how old'"]},
    6: {"number": 6, "title": "我会说汉语", "title_en": "I Can Speak Chinese", "objectives": ["Talk about abilities", "Use modal verb 会", "Discuss language skills"]},
    7: {"number": 7, "title": "今天几号", "title_en": "What's the Date Today", "objectives": ["Ask and tell the date", "Use days of the week", "Talk about schedules"]},
    8: {"number": 8, "title": "我想喝茶", "title_en": "I Want to Drink Tea", "objectives": ["Express wants", "Use 想 (want)", "Order food and drinks"]},
    9: {"number": 9, "title": "你儿子在哪儿工作", "title_en": "Where Does Your Son Work", "objectives": ["Ask and tell location", "Use 在 for location", "Talk about workplaces"]},
    10: {"number": 10, "title": "我能坐这儿吗", "title_en": "Can I Sit Here", "objectives": ["Ask for permission", "Use 能 for permission", "Use measure words"]},
    11: {"number": 11, "title": "现在几点", "title_en": "What Time Is It Now", "objectives": ["Tell time", "Ask for the time", "Talk about daily schedules"]},
    12: {"number": 12, "title": "明天天气怎么样", "title_en": "How's the Weather Tomorrow", "objectives": ["Talk about weather", "Ask about weather", "Describe temperature"]},
    13: {"number": 13, "title": "他在学做中国菜呢", "title_en": "He's Learning to Cook Chinese Food", "objectives": ["Express ongoing actions", "Use progressive 在", "Talk about cooking"]},
    14: {"number": 14, "title": "她买了不少衣服", "title_en": "She Bought Quite a Few Clothes", "objectives": ["Talk about completed actions", "Use particle 了", "Discuss shopping"]},
    15: {"number": 15, "title": "我是坐飞机来的", "title_en": "I Came by Plane", "objectives": ["Talk about transportation", "Use 是...的 construction", "Describe past actions"]},
}

HSK_GRAMMAR = {
    1: [
        {"point": "SVO Word Order", "explanation": "Subject + Verb + Object", "example": "我爱你"},
        {"point": "是 (shì) - to be", "explanation": "Links subject with identity", "example": "我是学生"},
        {"point": "吗 Questions", "explanation": "Add 吗 to make questions", "example": "你好吗"},
        {"point": "不 Negation", "explanation": "Place 不 before verb", "example": "不是"},
    ],
}

HSK_CONVERSATIONS = {
    1: [
        {"title": "Greeting", "dialogue": "A: 你好！ B: 你好！ A: 你叫什么名字？ B: 我叫小明。"},
        {"title": "Shopping", "dialogue": "A: 这个多少钱？ B: 五十块。 A: 太贵了！"},
    ],
}

# ============================================
# TTS FUNCTION
# ============================================

async def text_to_speech_edge(text, filename, voice="zh-CN-XiaoxiaoNeural"):
    try:
        clean_text = re.sub(r'[^\w\s\u4e00-\u9fff]', ' ', text)
        communicate = edge_tts.Communicate(clean_text, voice, rate="-25%")
        await communicate.save(filename)
        return True
    except Exception as e:
        print(f"TTS Error: {e}")
        return False

@app.route('/api/speak', methods=['POST'])
def speak():
    try:
        data = request.json
        text = data.get('text', '')
        voice_type = data.get('voice', 'female')
        
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        clean_text = re.sub(r'[^\w\s\u4e00-\u9fff]', ' ', text)
        voice_name = "zh-CN-YunxiNeural" if voice_type == 'male' else "zh-CN-XiaoxiaoNeural"
        text_hash = hashlib.md5(f"{clean_text}_{voice_type}".encode()).hexdigest()[:10]
        filename = f"static/speech_{text_hash}.mp3"
        
        if not os.path.exists(filename):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            success = loop.run_until_complete(text_to_speech_edge(clean_text, filename, voice_name))
            loop.close()
            if not success:
                return jsonify({"error": "TTS failed"}), 500
        
        return send_file(filename, mimetype="audio/mpeg")
    except Exception as e:
        print(f"TTS error: {e}")
        return jsonify({"error": str(e)}), 500

# ============================================
# STUDENT PROGRESS
# ============================================

student_progress = {}

# ============================================
# FLASK ROUTES
# ============================================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

# ============================================
# DYNAMIC LESSON VIEWER (Main)
# ============================================

@app.route('/lesson/<int:level>/<int:num>')
def dynamic_lesson(level, num):
    if level not in MAX_LESSONS or num < 1 or num > MAX_LESSONS[level]:
        return redirect(url_for('lessons'))
    
    json_path = os.path.join(LESSON_DATA_PATH, f'hsk{level}_lesson{num}.json')
    lesson_data = None
    
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            lesson_data = json.load(f)
    
    return render_template('lesson_viewer.html', 
                         level=level, 
                         lesson_num=num,
                         lesson_data=lesson_data,
                         max_lessons=MAX_LESSONS)

# ============================================
# LEGACY ROUTES (Redirect to dynamic viewer)
# ============================================

@app.route('/hsk1/lesson<int:num>')
def hsk1_lesson(num):
    if 1 <= num <= 15:
        return redirect(url_for('dynamic_lesson', level=1, num=num))
    return redirect(url_for('lessons'))

@app.route('/hsk2/lesson<int:num>')
def hsk2_lesson(num):
    if 1 <= num <= 15:
        return redirect(url_for('dynamic_lesson', level=2, num=num))
    return redirect(url_for('lessons'))

@app.route('/hsk3/lesson<int:num>')
def hsk3_lesson(num):
    if 1 <= num <= 20:
        return redirect(url_for('dynamic_lesson', level=3, num=num))
    return redirect(url_for('lessons'))

@app.route('/hsk4/lesson<int:num>')
def hsk4_lesson(num):
    if 1 <= num <= 20:
        return redirect(url_for('dynamic_lesson', level=4, num=num))
    return redirect(url_for('lessons'))

@app.route('/hsk5/lesson<int:num>')
def hsk5_lesson(num):
    if 1 <= num <= 36:
        return redirect(url_for('dynamic_lesson', level=5, num=num))
    return redirect(url_for('lessons'))

@app.route('/hsk6/lesson<int:num>')
def hsk6_lesson(num):
    if 1 <= num <= 40:
        return redirect(url_for('dynamic_lesson', level=6, num=num))
    return redirect(url_for('lessons'))

# ============================================
# OTHER PAGE ROUTES
# ============================================

@app.route('/full-lesson')
def full_lesson():
    return render_template('full_lesson.html')

@app.route('/hskk-speaking')
def hskk_speaking():
    return render_template('hskk_speaking.html')

@app.route('/hsk-practice')
def hsk_practice():
    return render_template('hsk_test.html')

@app.route('/homework')
def homework():
    return render_template('homework.html')

@app.route('/certificate')
def certificate():
    level = request.args.get('level', 1)
    score = request.args.get('score', None)
    return render_template('certificate.html', level=level, score=score)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/test-writing')
def test_writing():
    return render_template('test_writing.html')

# ============================================
# API ROUTES
# ============================================

@app.route('/api/lesson/<int:lesson_num>', methods=['GET'])
def get_lesson_api(lesson_num):
    if 1 <= lesson_num <= 15:
        return jsonify(HSK1_LESSONS.get(lesson_num))
    return jsonify({"error": "Lesson not found"}), 404

@app.route('/api/lessons', methods=['GET'])
def list_lessons():
    lessons = [{"number": i, "title": HSK1_LESSONS[i]["title"], "title_en": HSK1_LESSONS[i]["title_en"]} for i in range(1, 16)]
    return jsonify({"level": 1, "total_lessons": 15, "lessons": lessons})

@app.route('/api/ai-assistant', methods=['POST'])
def ai_assistant():
    data = request.json
    user_message = data.get('message', '').strip()
    level = data.get('level', 1)
    conversation_history = data.get('history', [])
    
    system_prompt = f"""You are a helpful Mandarin Chinese teacher for HSK Level {level} students.

Guidelines:
1. Keep responses short and clear (2-3 sentences max)
2. Use pinyin with tone marks when introducing new words
3. Be encouraging and patient
4. If asked for translation, provide Chinese characters, pinyin, and meaning
5. If student makes a mistake, correct gently with example

Student level: HSK {level}
"""
    
    messages = [
        {"role": "system", "content": system_prompt},
        *conversation_history[-10:],
        {"role": "user", "content": user_message}
    ]
    
    # Try DeepSeek first
    DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
    reply = None
    
    if DEEPSEEK_API_KEY:
        try:
            response = requests.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}", "Content-Type": "application/json"},
                json={"model": "deepseek-chat", "messages": messages, "temperature": 0.7, "max_tokens": 500},
                timeout=30
            )
            if response.status_code == 200:
                reply = response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"DeepSeek error: {e}")
    
    # Fallback to Ollama
    if not reply:
        try:
            ollama_response = requests.post(
                f"{OLLAMA_URL}/api/chat",
                json={"model": MODEL_NAME, "messages": messages, "stream": False},
                timeout=30
            )
            if ollama_response.status_code == 200:
                reply = ollama_response.json()["message"]["content"]
        except Exception as e:
            print(f"Ollama error: {e}")
            reply = "I'm here to help you learn Chinese! Please ask me about vocabulary, grammar, or pronunciation."
    
    return jsonify({"reply": reply, "tts_text": reply[:200]})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '').strip().lower()
    level = data.get('level', 1)
    session_id = request.remote_addr
    
    if session_id not in student_progress:
        student_progress[session_id] = {
            'level': level,
            'word_index': 0,
            'correct_count': 0,
            'mastered_words': [],
            'vocab_list': HSK1_VOCAB.get(level, [])
        }
    
    progress = student_progress[session_id]
    vocab_list = progress['vocab_list']
    
    if user_message in ['yes', 'y', 'start', 'begin']:
        if not vocab_list:
            return jsonify({"reply": "No vocabulary found."})
        
        if progress['word_index'] >= len(vocab_list):
            return jsonify({"reply": f"Congratulations! You've mastered all words in HSK Level {level}!\n\nType 'next level' to continue."})
        
        word = vocab_list[progress['word_index']]
        reply = f"New Word: {word['word']} ({word['pinyin']})\nMeaning: {word['meaning']}\nExample: {word['example']}\n\nType '{word['word']}' or '{word['pinyin']}' to practice."
        return jsonify({"reply": reply, "suggestions": [word['word'], word['pinyin']]})
    
    if 'next level' in user_message and level < 6:
        new_level = level + 1
        student_progress[session_id] = {
            'level': new_level,
            'word_index': 0,
            'correct_count': 0,
            'mastered_words': [],
            'vocab_list': HSK1_VOCAB.get(new_level, [])
        }
        return jsonify({"reply": f"Congratulations! You've advanced to HSK Level {new_level}!\n\nType 'yes' to begin."})
    
    if vocab_list and progress['word_index'] < len(vocab_list):
        word = vocab_list[progress['word_index']]
        target_word = word['word']
        
        if user_message == target_word.lower():
            progress['correct_count'] += 1
            if progress['correct_count'] >= 3:
                progress['mastered_words'].append(target_word)
                progress['correct_count'] = 0
                progress['word_index'] += 1
                if progress['word_index'] >= len(vocab_list):
                    reply = f"Excellent! You've mastered '{target_word}'!\n\nCongratulations! You've completed HSK Level {level}!"
                else:
                    next_word = vocab_list[progress['word_index']]
                    reply = f"Excellent! You've mastered '{target_word}'!\n\nNext word: {next_word['word']} ({next_word['pinyin']})\nMeaning: {next_word['meaning']}"
            else:
                remaining = 3 - progress['correct_count']
                reply = f"Correct! That's attempt {progress['correct_count']} of 3.\nNeed {remaining} more to master '{target_word}'."
        else:
            progress['correct_count'] = 0
            reply = f"Not quite. The correct word is '{target_word}'.\n\nPlease try again."
        
        return jsonify({"reply": reply})
    
    return jsonify({"reply": "Type 'yes' to begin your lesson!"})

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"status": "ok", "message": "Server running"})

# ============================================
# MAIN
# ============================================

# ============================================
# PASSCODE SYSTEM (COMPLETE REPLACEMENT)
# ============================================

import uuid
from datetime import datetime, timedelta

PASSCODES_FILE = os.path.join(os.path.dirname(__file__), 'passcodes.json')

def init_passcodes_file():
    """Initialize passcodes.json if it doesn't exist"""
    if not os.path.exists(PASSCODES_FILE):
        initial_data = {
            "settings": {
                "default_expiry_hours": 168,
                "max_devices_per_user": 2
            },
            "users": {},
            "requests": {},
            "history": []  # NEW: Separate history array
        }
        with open(PASSCODES_FILE, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Created {PASSCODES_FILE}")
    return True

def load_passcodes():
    init_passcodes_file()
    with open(PASSCODES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_passcodes(data):
    with open(PASSCODES_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_lesson_key(level, lesson_num):
    return f"hsk{level}_lesson{lesson_num}"

def generate_passcode():
    import random
    import string
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=3))
    return f"{letters}{numbers}"

@app.route('/admin/passcodes')
def admin_passcodes():
    return render_template('admin_passcodes.html')

@app.route('/api/admin/settings', methods=['GET', 'POST'])
def api_admin_settings():
    data = load_passcodes()
    if request.method == 'GET':
        return jsonify({"settings": data["settings"]})
    else:
        new_settings = request.json
        data["settings"]["default_expiry_hours"] = new_settings.get("default_expiry_hours", 168)
        data["settings"]["max_devices_per_user"] = new_settings.get("max_devices_per_user", 2)
        save_passcodes(data)
        return jsonify({"success": True})

@app.route('/api/admin/pending')
def api_pending_requests():
    data = load_passcodes()
    pending = []
    for req_id, req in data.get("requests", {}).items():
        if req.get("status") == "pending":
            pending.append({
                "request_id": req_id,
                "email": req["email"],
                "level": req["level"],
                "lesson_num": req["lesson_num"],
                "passcode": req["passcode"],
                "created_at": req["created_at"]
            })
    return jsonify({"pending": pending})

@app.route('/api/admin/history', methods=['GET'])
def api_history_requests():
    """Get ALL history (approved and denied requests)"""
    data = load_passcodes()
    
    # Get history from separate array, or build from requests if empty
    history = data.get("history", [])
    
    # Also include any approved/denied requests not yet in history
    for req_id, req in data.get("requests", {}).items():
        if req.get("status") in ["approved", "denied"]:
            # Check if already in history
            already_in_history = False
            for h in history:
                if h.get("request_id") == req_id:
                    already_in_history = True
                    break
            if not already_in_history:
                history.append({
                    "request_id": req_id,
                    "email": req["email"],
                    "level": req["level"],
                    "lesson_num": req["lesson_num"],
                    "passcode": req["passcode"],
                    "status": req.get("status"),
                    "created_at": req["created_at"],
                    "approved_at": req.get("approved_at"),
                    "expires_at": req.get("expires_at")
                })
    
    # Sort by created_at descending
    history.sort(key=lambda x: x["created_at"], reverse=True)
    
    print(f"\n📜 HISTORY: {len(history)} total records")
    for h in history[:5]:  # Show first 5
        print(f"   - {h['email']} | {h['status']}")
    
    return jsonify({"history": history})

@app.route('/api/admin/approve/<request_id>', methods=['POST'])
def api_approve_request(request_id):
    data = load_passcodes()
    if request_id not in data.get("requests", {}):
        return jsonify({"success": False, "message": "Request not found"}), 404
    
    req = data["requests"][request_id]
    lesson_key = get_lesson_key(req["level"], req["lesson_num"])
    expiry_hours = data["settings"]["default_expiry_hours"]
    passcode_to_use = req["passcode"]
    
    print(f"\n✅ APPROVING: {req['email']} for HSK{req['level']} L{req['lesson_num']}")
    print(f"   Passcode: {passcode_to_use}")
    
    if req["email"] not in data["users"]:
        data["users"][req["email"]] = {"active_lessons": {}, "devices": []}
    
    expires_at = datetime.now() + timedelta(hours=expiry_hours)
    
    # Store in active lessons
    data["users"][req["email"]]["active_lessons"][lesson_key] = {
        "passcode": passcode_to_use,
        "expires_at": expires_at.isoformat(),
        "expiry_hours": expiry_hours,
        "approved_at": datetime.now().isoformat()
    }
    
    # Update request status
    data["requests"][request_id]["status"] = "approved"
    data["requests"][request_id]["approved_at"] = datetime.now().isoformat()
    data["requests"][request_id]["expires_at"] = expires_at.isoformat()
    
    # Add to history array
    if "history" not in data:
        data["history"] = []
    
    data["history"].append({
        "request_id": request_id,
        "email": req["email"],
        "level": req["level"],
        "lesson_num": req["lesson_num"],
        "passcode": passcode_to_use,
        "status": "approved",
        "created_at": req["created_at"],
        "approved_at": datetime.now().isoformat(),
        "expires_at": expires_at.isoformat()
    })
    
    save_passcodes(data)
    
    print(f"✅ SAVED to history! Total history records: {len(data['history'])}")
    
    return jsonify({"success": True, "message": f"Approved! Passcode: {passcode_to_use}"})

@app.route('/api/admin/deny/<request_id>', methods=['POST'])
def api_deny_request(request_id):
    data = load_passcodes()
    if request_id not in data.get("requests", {}):
        return jsonify({"success": False, "message": "Request not found"}), 404
    
    req = data["requests"][request_id]
    
    data["requests"][request_id]["status"] = "denied"
    data["requests"][request_id]["denied_at"] = datetime.now().isoformat()
    
    # Add to history array
    if "history" not in data:
        data["history"] = []
    
    data["history"].append({
        "request_id": request_id,
        "email": req["email"],
        "level": req["level"],
        "lesson_num": req["lesson_num"],
        "passcode": req["passcode"],
        "status": "denied",
        "created_at": req["created_at"],
        "denied_at": datetime.now().isoformat()
    })
    
    save_passcodes(data)
    
    print(f"❌ DENIED and saved to history: {req['email']}")
    
    return jsonify({"success": True, "message": "Request denied"})

@app.route('/api/request-passcode', methods=['POST'])
def api_request_passcode():
    data = request.json
    email = data.get('email', '').strip().lower()
    level = data.get('level')
    lesson_num = data.get('lesson_num')
    
    if not email or '@' not in email:
        return jsonify({"success": False, "message": "Valid email required"}), 400
    
    passcodes_data = load_passcodes()
    lesson_key = get_lesson_key(level, lesson_num)
    passcode = generate_passcode()
    
    request_id = f"{email}_{lesson_key}_{int(datetime.now().timestamp())}"
    passcodes_data["requests"][request_id] = {
        "email": email,
        "level": level,
        "lesson_num": lesson_num,
        "passcode": passcode,
        "created_at": datetime.now().isoformat(),
        "status": "pending"
    }
    save_passcodes(passcodes_data)
    
    print(f"\n📋 NEW REQUEST: {email} wants HSK {level} Lesson {lesson_num}")
    print(f"🔐 Generated passcode: {passcode}")
    print(f"👉 Go to http://localhost:5000/admin/passcodes to approve\n")
    
    return jsonify({"success": True, "message": "Request sent! Admin will review."})

@app.route('/api/verify-passcode', methods=['POST'])
def api_verify_passcode():
    data = request.json
    email = data.get('email', '').strip().lower()
    passcode_input = data.get('passcode', '').strip().upper()
    level = data.get('level')
    lesson_num = data.get('lesson_num')
    device_id = data.get('device_id', 'unknown')
    device_type = data.get('device_type', 'desktop')
    
    print(f"\n🔍 VERIFY: {email} trying passcode: {passcode_input} for HSK{level} L{lesson_num}")
    
    passcodes_data = load_passcodes()
    lesson_key = get_lesson_key(level, lesson_num)
    
    if email not in passcodes_data.get("users", {}):
        print(f"   ❌ User not found")
        return jsonify({"success": False, "message": "No access. Request first."})
    
    if lesson_key not in passcodes_data["users"][email].get("active_lessons", {}):
        print(f"   ❌ Lesson not found")
        return jsonify({"success": False, "message": "No access for this lesson. Request first."})
    
    stored = passcodes_data["users"][email]["active_lessons"][lesson_key]
    stored_passcode = stored["passcode"].strip().upper()
    
    print(f"   Stored passcode: {stored_passcode}")
    print(f"   Match: {passcode_input == stored_passcode}")
    
    if stored_passcode != passcode_input:
        return jsonify({"success": False, "message": f"Invalid passcode."})
    
    expires_at = datetime.fromisoformat(stored["expires_at"])
    if datetime.now() > expires_at:
        print(f"   ❌ Expired")
        return jsonify({"success": False, "message": "Passcode expired. Request a new one."})
    
    print(f"   ✅ Access GRANTED!")
    return jsonify({"success": True, "message": "Access granted!", "redirect": f"/lesson/{level}/{lesson_num}"})

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("HSK Mandarin Teacher - Complete Curriculum (HSK 1-6)")
    print("=" * 60)
    print("\n✅ Dynamic Lesson System Ready!")
    print("   - JSON files in templates/data/")
    print("   - All HSK lessons redirect to dynamic viewer")
    print("\n📖 Available Routes:")
    print("   /              - Home page")
    print("   /lessons       - Main curriculum page")
    print("   /dashboard     - Student dashboard")
    print("   /hsk-practice  - Practice test")
    print("   /hskk-speaking - Speaking test")
    print("\n📚 Direct Lesson Access:")
    print("   /hsk1/lesson1  through /hsk1/lesson15")
    print("   /hsk2/lesson1  through /hsk2/lesson15")
    print("   /hsk3/lesson1  through /hsk3/lesson20")
    print("   /hsk4/lesson1  through /hsk4/lesson20")
    print("   /hsk5/lesson1  through /hsk5/lesson36")
    print("   /hsk6/lesson1  through /hsk6/lesson40")
    print("\n🌐 Server running at: http://localhost:5000")
    print("=" * 60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)