# server.py - Complete HSK Mandarin Teacher with PostgreSQL

from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
from flask_cors import CORS
import json
import os
import asyncio
import edge_tts
import hashlib
import re
import requests
import uuid
from datetime import datetime, timedelta
import psycopg2
from psycopg2.extras import RealDictCursor
from urllib.parse import urlparse

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
# POSTGRESQL DATABASE SETUP
# ============================================

def get_db_connection():
    """Get PostgreSQL connection"""
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        # Parse Render's DATABASE_URL
        result = urlparse(database_url)
        conn = psycopg2.connect(
            database=result.path[1:],
            user=result.username,
            password=result.password,
            host=result.hostname,
            port=result.port
        )
    else:
        # Local development fallback
        conn = psycopg2.connect(
            database="mandarin_db",
            user="mandarin_user",
            password="mandarin_password",
            host="localhost",
            port=5432
        )
    return conn

def init_db():
    """Initialize database tables"""
    conn = get_db_connection()
    c = conn.cursor()
    
    # Settings table
    c.execute('''CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )''')
    
    # Users table (approved lessons)
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        email TEXT,
        lesson_key TEXT,
        passcode TEXT,
        expires_at TIMESTAMP,
        created_at TIMESTAMP,
        approved_at TIMESTAMP,
        PRIMARY KEY (email, lesson_key)
    )''')
    
    # Requests table
    c.execute('''CREATE TABLE IF NOT EXISTS requests (
        request_id TEXT PRIMARY KEY,
        email TEXT,
        level INTEGER,
        lesson_num INTEGER,
        passcode TEXT,
        status TEXT,
        created_at TIMESTAMP,
        approved_at TIMESTAMP,
        expires_at TIMESTAMP
    )''')
    
    # Devices table
    c.execute('''CREATE TABLE IF NOT EXISTS devices (
        email TEXT,
        device_fp TEXT,
        registered_at TIMESTAMP,
        PRIMARY KEY (email, device_fp)
    )''')
    
    # Insert default settings
    c.execute("INSERT INTO settings (key, value) VALUES ('default_expiry_hours', '168') ON CONFLICT (key) DO NOTHING")
    c.execute("INSERT INTO settings (key, value) VALUES ('max_devices_per_user', '2') ON CONFLICT (key) DO NOTHING")
    
    conn.commit()
    conn.close()
    print("✅ PostgreSQL database initialized")

def get_setting(key, default='168'):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT value FROM settings WHERE key = %s", (key,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else default

def save_setting(key, value):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO settings (key, value) VALUES (%s, %s) ON CONFLICT (key) DO UPDATE SET value = %s", 
              (key, str(value), str(value)))
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

# ============================================
# PASSCODE SYSTEM FUNCTIONS
# ============================================

def get_lesson_key(level, lesson_num):
    return f"hsk{level}_lesson{lesson_num}"

def generate_passcode():
    import random
    import string
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=3))
    return f"{letters}{numbers}"

def get_pending_requests():
    conn = get_db_connection()
    c = conn.cursor(cursor_factory=RealDictCursor)
    c.execute("SELECT request_id, email, level, lesson_num, passcode, created_at FROM requests WHERE status = 'pending' ORDER BY created_at DESC")
    rows = c.fetchall()
    conn.close()
    return rows

def get_all_history():
    conn = get_db_connection()
    c = conn.cursor(cursor_factory=RealDictCursor)
    c.execute("SELECT request_id, email, level, lesson_num, passcode, status, created_at, approved_at, expires_at FROM requests ORDER BY created_at DESC")
    rows = c.fetchall()
    conn.close()
    return rows

def save_request(request_id, email, level, lesson_num, passcode, status):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO requests (request_id, email, level, lesson_num, passcode, status, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)",
              (request_id, email, level, lesson_num, passcode, status, datetime.now()))
    conn.commit()
    conn.close()

def update_request_status(request_id, status, approved_at=None, expires_at=None):
    conn = get_db_connection()
    c = conn.cursor()
    if approved_at:
        c.execute("UPDATE requests SET status = %s, approved_at = %s, expires_at = %s WHERE request_id = %s", 
                  (status, approved_at, expires_at, request_id))
    else:
        c.execute("UPDATE requests SET status = %s WHERE request_id = %s", (status, request_id))
    conn.commit()
    conn.close()

def save_user_lesson(email, lesson_key, passcode, expires_at):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO users (email, lesson_key, passcode, expires_at, created_at, approved_at) VALUES (%s, %s, %s, %s, %s, %s)",
              (email, lesson_key, passcode, expires_at, datetime.now(), datetime.now()))
    conn.commit()
    conn.close()

def get_user_lesson(email, lesson_key):
    conn = get_db_connection()
    c = conn.cursor(cursor_factory=RealDictCursor)
    c.execute("SELECT passcode, expires_at FROM users WHERE email = %s AND lesson_key = %s", (email, lesson_key))
    row = c.fetchone()
    conn.close()
    return row

def register_device(email, device_fp, max_devices):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM devices WHERE email = %s", (email,))
    count = c.fetchone()[0]
    if count >= max_devices:
        conn.close()
        return False
    c.execute("INSERT INTO devices (email, device_fp, registered_at) VALUES (%s, %s, %s)",
              (email, device_fp, datetime.now()))
    conn.commit()
    conn.close()
    return True

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
# FLASK ROUTES
# ============================================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

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

# Legacy routes
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
# ADMIN API ROUTES
# ============================================

@app.route('/admin/passcodes')
def admin_passcodes():
    return render_template('admin_passcodes.html')

@app.route('/api/admin/settings', methods=['GET', 'POST'])
def api_admin_settings():
    if request.method == 'GET':
        return jsonify({
            "settings": {
                "default_expiry_hours": int(get_setting('default_expiry_hours')),
                "max_devices_per_user": int(get_setting('max_devices_per_user'))
            }
        })
    else:
        new_settings = request.json
        save_setting('default_expiry_hours', new_settings.get('default_expiry_hours', 168))
        save_setting('max_devices_per_user', new_settings.get('max_devices_per_user', 2))
        return jsonify({"success": True})

@app.route('/api/admin/pending')
def api_pending_requests():
    pending = get_pending_requests()
    return jsonify({"pending": pending})

@app.route('/api/admin/history', methods=['GET'])
def api_history_requests():
    history = get_all_history()
    return jsonify({"history": history})

@app.route('/api/admin/approve/<request_id>', methods=['POST'])
def api_approve_request(request_id):
    conn = get_db_connection()
    c = conn.cursor(cursor_factory=RealDictCursor)
    
    c.execute("SELECT * FROM requests WHERE request_id = %s", (request_id,))
    req = c.fetchone()
    
    if not req:
        conn.close()
        return jsonify({"success": False, "message": "Request not found"}), 404
    
    lesson_key = get_lesson_key(req['level'], req['lesson_num'])
    expiry_hours = int(get_setting('default_expiry_hours'))
    passcode_to_use = req['passcode']
    expires_at = datetime.now() + timedelta(hours=expiry_hours)
    
    # Save to users table
    c.execute("INSERT INTO users (email, lesson_key, passcode, expires_at, created_at, approved_at) VALUES (%s, %s, %s, %s, %s, %s)",
              (req['email'], lesson_key, passcode_to_use, expires_at, datetime.now(), datetime.now()))
    
    # Update request status
    c.execute("UPDATE requests SET status = 'approved', approved_at = %s, expires_at = %s WHERE request_id = %s",
              (datetime.now(), expires_at, request_id))
    
    conn.commit()
    conn.close()
    
    print(f"\n✅ APPROVED: {req['email']} for HSK {req['level']} Lesson {req['lesson_num']}")
    print(f"🔐 PASSCODE: {passcode_to_use}")
    print(f"⏰ Expires: {expires_at.strftime('%Y-%m-%d %H:%M')}\n")
    
    return jsonify({"success": True, "message": f"Approved! Passcode: {passcode_to_use}"})

@app.route('/api/admin/deny/<request_id>', methods=['POST'])
def api_deny_request(request_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE requests SET status = 'denied', approved_at = %s WHERE request_id = %s", (datetime.now(), request_id))
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": "Request denied"})

@app.route('/api/request-passcode', methods=['POST'])
def api_request_passcode():
    data = request.json
    email = data.get('email', '').strip().lower()
    level = data.get('level')
    lesson_num = data.get('lesson_num')
    
    if not email or '@' not in email:
        return jsonify({"success": False, "message": "Valid email required"}), 400
    
    lesson_key = get_lesson_key(level, lesson_num)
    passcode = generate_passcode()
    request_id = f"{email}_{lesson_key}_{int(datetime.now().timestamp())}"
    
    save_request(request_id, email, level, lesson_num, passcode, 'pending')
    
    print(f"\n📋 NEW REQUEST: {email} wants HSK {level} Lesson {lesson_num}")
    print(f"🔐 Generated passcode: {passcode}")
    print(f"👉 Go to /admin/passcodes to approve\n")
    
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
    
    lesson_key = get_lesson_key(level, lesson_num)
    max_devices = int(get_setting('max_devices_per_user'))
    
    user_lesson = get_user_lesson(email, lesson_key)
    
    if not user_lesson:
        return jsonify({"success": False, "message": "No access. Request first."})
    
    if user_lesson['passcode'].strip().upper() != passcode_input:
        return jsonify({"success": False, "message": "Invalid passcode."})
    
    expires_at = user_lesson['expires_at']
    if datetime.now() > expires_at:
        return jsonify({"success": False, "message": "Passcode expired. Request a new one."})
    
    # Device tracking
    device_fp = f"{device_id}_{device_type}"
    if not register_device(email, device_fp, max_devices):
        return jsonify({"success": False, "message": f"Device limit reached ({max_devices} max). Contact admin."})
    
    print(f"✅ Access granted: {email} for HSK{level} L{lesson_num}")
    return jsonify({"success": True, "message": "Access granted!", "redirect": f"/lesson/{level}/{lesson_num}"})

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
    # Simplified chat endpoint
    data = request.json
    message = data.get('message', '')
    return jsonify({"reply": f"Received: {message}"})

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"status": "ok", "message": "Server running"})

# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("HSK Mandarin Teacher - Complete Curriculum (HSK 1-6)")
    print("=" * 60)
    print("\n✅ PostgreSQL Database Ready!")
    print("\n📖 Available Routes:")
    print("   /              - Home page")
    print("   /lessons       - Main curriculum page")
    print("   /admin/passcodes - Admin dashboard")
    print("   /dashboard     - Student dashboard")
    print("\n🌐 Server running at: http://localhost:5000")
    print("=" * 60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)