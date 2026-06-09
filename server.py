# server.py - HSK Mandarin Teacher - COMPLETE WORKING VERSION

from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
from flask_cors import CORS
import json
import os
import asyncio
import edge_tts
import hashlib
import re
import requests
import random
import string
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

os.makedirs("static", exist_ok=True)

# ============================================
# CONFIGURATION
# ============================================

OLLAMA_URL = "http://127.0.0.1:11434"
MODEL_NAME = "mistral:instruct"

MAX_LESSONS = {1: 15, 2: 15, 3: 20, 4: 20, 5: 36, 6: 40}
LESSON_DATA_PATH = os.path.join(os.path.dirname(__file__), 'templates', 'data')
os.makedirs(LESSON_DATA_PATH, exist_ok=True)

# ============================================
# SIMPLE IN-MEMORY STORAGE (Works perfectly)
# ============================================

passcodes_db = {
    "users": {},
    "requests": []
}

def generate_passcode():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=3))
    return f"{letters}{numbers}"

def get_lesson_key(level, lesson_num):
    return f"hsk{level}_lesson{lesson_num}"

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
# PAGE ROUTES
# ============================================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/lesson/<int:level>/<int:num>')
def dynamic_lesson(level, num):
    # Check if lesson exists
    if level not in MAX_LESSONS or num < 1 or num > MAX_LESSONS[level]:
        return redirect(url_for('lessons'))
    
    # Load lesson data from JSON file
    json_path = os.path.join(LESSON_DATA_PATH, f'hsk{level}_lesson{num}.json')
    lesson_data = None
    
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            lesson_data = json.load(f)
    
    # Pass the lesson data to the template
    return render_template('lesson_viewer.html', 
                         level=level, 
                         lesson_num=num,
                         lesson_data=lesson_data,
                         max_lessons=MAX_LESSONS)

# Legacy lesson routes (redirect to dynamic lesson)
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

# Other page routes
@app.route('/admin/passcodes')
def admin_passcodes():
    return render_template('admin_passcodes.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/hsk-practice')
def hsk_practice():
    return render_template('hsk_test.html')

@app.route('/hskk-speaking')
def hskk_speaking():
    return render_template('hskk_speaking.html')

@app.route('/full-lesson')
def full_lesson():
    return render_template('full_lesson.html')

@app.route('/homework')
def homework():
    return render_template('homework.html')

@app.route('/certificate')
def certificate():
    level = request.args.get('level', 1)
    score = request.args.get('score', None)
    return render_template('certificate.html', level=level, score=score)

@app.route('/test-writing')
def test_writing():
    return render_template('test_writing.html')

# ============================================
# API ROUTES - PASSCODE SYSTEM
# ============================================

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"status": "ok", "message": "Server running"})

@app.route('/api/request-passcode', methods=['POST'])
def api_request_passcode():
    try:
        data = request.get_json()
        email = data.get('email', '').strip().lower()
        level = data.get('level')
        lesson_num = data.get('lesson_num')
        
        if not email or '@' not in email:
            return jsonify({"success": False, "message": "Valid email required"}), 400
        
        passcode = generate_passcode()
        request_id = f"{email}_{level}_{lesson_num}_{int(datetime.now().timestamp())}"
        
        passcodes_db["requests"].append({
            "request_id": request_id,
            "email": email,
            "level": level,
            "lesson_num": lesson_num,
            "passcode": passcode,
            "status": "pending",
            "created_at": datetime.now().isoformat()
        })
        
        print(f"\n📋 NEW REQUEST: {email} wants HSK {level} Lesson {lesson_num}")
        print(f"🔐 Generated passcode: {passcode}")
        
        return jsonify({"success": True, "message": "Request sent! Admin will review."})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/api/admin/settings', methods=['GET', 'POST'])
def api_admin_settings():
    if request.method == 'GET':
        return jsonify({
            "settings": {
                "default_expiry_hours": 168,
                "max_devices_per_user": 2
            }
        })
    return jsonify({"success": True})

@app.route('/api/admin/pending', methods=['GET'])
def api_pending_requests():
    pending = [r for r in passcodes_db["requests"] if r["status"] == "pending"]
    return jsonify({"pending": pending})

@app.route('/api/admin/history', methods=['GET'])
def api_history_requests():
    return jsonify({"history": passcodes_db["requests"]})

@app.route('/api/admin/approve/<request_id>', methods=['POST'])
def api_approve_request(request_id):
    for req in passcodes_db["requests"]:
        if req["request_id"] == request_id:
            req["status"] = "approved"
            req["approved_at"] = datetime.now().isoformat()
            
            lesson_key = get_lesson_key(req["level"], req["lesson_num"])
            user_key = f"{req['email']}_{lesson_key}"
            expires_at = datetime.now() + timedelta(days=7)
            
            passcodes_db["users"][user_key] = {
                "email": req["email"],
                "lesson_key": lesson_key,
                "passcode": req["passcode"].upper(),
                "expires_at": expires_at.isoformat()
            }
            
            print(f"\n✅ APPROVED: {req['email']} for HSK {req['level']} Lesson {req['lesson_num']}")
            print(f"🔐 PASSCODE: {req['passcode']}")
            print(f"⏰ Expires: {expires_at.strftime('%Y-%m-%d %H:%M')}\n")
            
            return jsonify({"success": True, "message": f"Approved! Passcode: {req['passcode']}"})
    
    return jsonify({"success": False, "message": "Request not found"}), 404

@app.route('/api/admin/deny/<request_id>', methods=['POST'])
def api_deny_request(request_id):
    for req in passcodes_db["requests"]:
        if req["request_id"] == request_id:
            req["status"] = "denied"
            return jsonify({"success": True, "message": "Request denied"})
    return jsonify({"success": False, "message": "Request not found"}), 404

@app.route('/api/verify-passcode', methods=['POST'])
def api_verify_passcode():
    try:
        data = request.get_json()
        email = data.get('email', '').strip().lower()
        passcode_input = data.get('passcode', '').strip().upper()
        level = data.get('level')
        lesson_num = data.get('lesson_num')
        device_id = data.get('device_id', 'unknown')
        device_type = data.get('device_type', 'desktop')
        
        lesson_key = get_lesson_key(level, lesson_num)
        user_key = f"{email}_{lesson_key}"
        
        user_lesson = passcodes_db["users"].get(user_key)
        
        if not user_lesson:
            return jsonify({"success": False, "message": "No access. Request first."})
        
        if user_lesson["passcode"] != passcode_input:
            return jsonify({"success": False, "message": "Invalid passcode."})
        
        expires_at = datetime.fromisoformat(user_lesson["expires_at"])
        if datetime.now() > expires_at:
            return jsonify({"success": False, "message": "Passcode expired. Request a new one."})
        
        remaining = expires_at - datetime.now()
        remaining_days = remaining.days
        
        if remaining_days > 0:
            expiry_message = f"This passcode will expire in {remaining_days} days."
        else:
            remaining_hours = remaining.seconds // 3600
            expiry_message = f"This passcode will expire in {remaining_hours} hours."
        
        print(f"✅ Access granted: {email} for HSK{level} L{lesson_num}")
        
        return jsonify({
            "success": True,
            "message": f"✓ Access granted! {expiry_message}",
            "redirect": f"/lesson/{level}/{lesson_num}"
        })
    except Exception as e:
        print(f"Error in verify: {e}")
        return jsonify({"success": False, "message": str(e)}), 500

# ============================================
# AI ASSISTANT API
# ============================================

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
    message = data.get('message', '')
    return jsonify({"reply": f"Received: {message}"})

# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("HSK Mandarin Teacher - Complete Curriculum (HSK 1-6)")
    print("=" * 60)
    print("\n✅ Server Ready!")
    print("\n📖 Available Routes:")
    print("   /              - Home page")
    print("   /lessons       - Main curriculum page")
    print("   /admin/passcodes - Admin dashboard")
    print("   /dashboard     - Student dashboard")
    print("\n🌐 Server running at: http://localhost:5000")
    print("=" * 60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
    