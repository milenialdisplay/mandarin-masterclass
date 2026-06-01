import os
import json

# HSK 1 Lesson Data (15 lessons)
hsk1_lessons = {
    1: {"title": "你好", "title_en": "Hello", "nav_prev": 15, "nav_next": 2},
    2: {"title": "谢谢你", "title_en": "Thank You", "nav_prev": 1, "nav_next": 3},
    3: {"title": "你叫什么名字", "title_en": "What's Your Name", "nav_prev": 2, "nav_next": 4},
    4: {"title": "她是我的汉语老师", "title_en": "She's My Chinese Teacher", "nav_prev": 3, "nav_next": 5},
    5: {"title": "她女儿今年二十岁", "title_en": "Her Daughter is 20", "nav_prev": 4, "nav_next": 6},
    6: {"title": "我会说汉语", "title_en": "I Can Speak Chinese", "nav_prev": 5, "nav_next": 7},
    7: {"title": "今天几号", "title_en": "What's the Date", "nav_prev": 6, "nav_next": 8},
    8: {"title": "我想喝茶", "title_en": "I Want Tea", "nav_prev": 7, "nav_next": 9},
    9: {"title": "你儿子在哪儿工作", "title_en": "Where Does Your Son Work", "nav_prev": 8, "nav_next": 10},
    10: {"title": "我能坐这儿吗", "title_en": "Can I Sit Here", "nav_prev": 9, "nav_next": 11},
    11: {"title": "现在几点", "title_en": "What Time Is It", "nav_prev": 10, "nav_next": 12},
    12: {"title": "明天天气怎么样", "title_en": "How's the Weather", "nav_prev": 11, "nav_next": 13},
    13: {"title": "他在学做中国菜呢", "title_en": "Learning Chinese Cooking", "nav_prev": 12, "nav_next": 14},
    14: {"title": "她买了不少衣服", "title_en": "Shopping for Clothes", "nav_prev": 13, "nav_next": 15},
    15: {"title": "我是坐飞机来的", "title_en": "I Came by Plane", "nav_prev": 14, "nav_next": 1},
}

# Template for each lesson
template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>HSK 1 Lesson {num}: {title} | Mandarin Teacher</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #1a472a;
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }}
        .header {{
            background: linear-gradient(135deg, #1a472a, #2d6a4f);
            color: white;
            padding: 25px;
            text-align: center;
        }}
        .header h1 {{ font-size: 28px; margin-bottom: 8px; }}
        .header p {{ font-size: 14px; opacity: 0.9; }}
        .lesson-nav {{
            background: #f5f5f5;
            padding: 15px;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
            border-bottom: 1px solid #ddd;
        }}
        .nav-btn {{
            background: #2d6a4f;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 13px;
            font-weight: bold;
        }}
        .nav-btn:hover {{ background: #1a472a; }}
        .content {{ padding: 25px; max-height: 70vh; overflow-y: auto; }}
        .section {{ margin-bottom: 35px; background: #fafafa; border-radius: 16px; padding: 20px; border: 1px solid #eee; }}
        .section-title {{ font-size: 22px; color: #1a472a; border-left: 5px solid #ffd700; padding-left: 15px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }}
        .play-all-btn {{ background: #2d6a4f; color: white; border: none; padding: 8px 18px; border-radius: 8px; cursor: pointer; font-size: 13px; font-weight: bold; }}
        .play-all-btn:hover {{ background: #1a472a; }}
        .vocab-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 15px; }}
        .vocab-card {{ background: white; border-radius: 16px; padding: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); transition: all 0.2s; border: 1px solid #e0e0e0; }}
        .vocab-card:hover {{ transform: translateY(-3px); box-shadow: 0 5px 15px rgba(0,0,0,0.1); }}
        .vocab-word {{ font-size: 28px; font-weight: bold; color: #1a472a; cursor: pointer; }}
        .vocab-pinyin {{ color: #e94560; font-size: 14px; margin: 5px 0; }}
        .vocab-meaning {{ color: #666; font-size: 13px; margin-bottom: 10px; padding-bottom: 8px; border-bottom: 1px dashed #eee; }}
        .vocab-example {{ background: #f8f9fa; padding: 10px; border-radius: 10px; font-size: 13px; }}
        .vocab-example-chinese {{ font-weight: 500; margin-bottom: 5px; }}
        .vocab-example-translation {{ color: #888; font-size: 12px; }}
        .audio-btn {{ background: #2d6a4f; color: white; border: none; padding: 5px 12px; border-radius: 20px; cursor: pointer; font-size: 11px; margin-top: 10px; margin-right: 8px; }}
        .audio-btn:hover {{ background: #1a472a; }}
        .grammar-card {{ background: white; border-radius: 12px; padding: 18px; margin-bottom: 20px; border-left: 4px solid #ffd700; }}
        .grammar-title {{ font-size: 18px; font-weight: bold; color: #1a472a; margin-bottom: 10px; }}
        .grammar-explanation {{ color: #555; margin-bottom: 15px; line-height: 1.6; }}
        .grammar-examples {{ background: #e8f5e9; padding: 15px; border-radius: 10px; margin-top: 10px; }}
        .grammar-example-item {{ margin-bottom: 12px; padding-bottom: 10px; border-bottom: 1px solid #c8e6c9; }}
        .grammar-example-item:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
        .grammar-example-chinese {{ font-size: 16px; font-weight: 500; margin-bottom: 5px; }}
        .grammar-example-translation {{ color: #666; font-size: 13px; }}
        .dialogue-container {{ background: #1a1a2e; border-radius: 16px; overflow: hidden; color: white; }}
        .dialogue-scene {{ padding: 20px; }}
        .dialogue-line {{ margin-bottom: 20px; display: flex; flex-direction: column; }}
        .dialogue-speaker {{ font-weight: bold; margin-bottom: 5px; }}
        .speaker-male {{ color: #87CEEB; }}
        .speaker-female {{ color: #FFB6C1; }}
        .dialogue-bubble {{ background: rgba(255,255,255,0.1); border-radius: 18px; padding: 12px 18px; max-width: 90%; }}
        .dialogue-chinese {{ font-size: 18px; margin-bottom: 5px; }}
        .dialogue-pinyin {{ color: #aaa; font-size: 12px; margin-bottom: 5px; }}
        .dialogue-translation {{ color: #888; font-size: 13px; }}
        .exercise-card {{ background: white; border-radius: 12px; padding: 15px; margin-bottom: 15px; }}
        .exercise-question {{ font-weight: bold; margin-bottom: 12px; }}
        .exercise-option {{ padding: 8px 12px; margin: 5px 0; background: #f5f5f5; border-radius: 8px; cursor: pointer; }}
        .exercise-option:hover {{ background: #e8f5e9; }}
        .exercise-option.selected {{ background: #2d6a4f; color: white; }}
        .back-btn {{ background: #6c757d; color: white; border: none; padding: 12px 24px; border-radius: 30px; cursor: pointer; font-size: 14px; font-weight: bold; margin: 0 25px 25px 25px; width: calc(100% - 50px); }}
        .back-btn:hover {{ background: #5a6268; }}
        @media (max-width: 768px) {{
            .vocab-grid {{ grid-template-columns: 1fr; }}
            .section-title {{ font-size: 18px; flex-direction: column; align-items: flex-start; }}
            .dialogue-bubble {{ max-width: 100%; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>HSK 1 Lesson {num}: {title}</h1>
            <p>{title_en}</p>
        </div>
        
        <div class="lesson-nav">
            <button class="nav-btn" onclick="window.location.href='/hsk1/lesson{prev}'">◀ Previous Lesson</button>
            <button class="nav-btn" onclick="window.location.href='/lessons'">📚 All Lessons</button>
            <button class="nav-btn" onclick="window.location.href='/hsk1/lesson{next}'">Next Lesson ▶</button>
        </div>
        
        <div class="content">
            <div class="section">
                <div class="section-title">
                    📖 Learning Objectives
                    <button class="play-all-btn" onclick="playAudio('Learn new vocabulary, grammar, and practice conversation for HSK 1', 'en')">🔊 Play All</button>
                </div>
                <ul style="margin-left: 20px; line-height: 1.8;">
                    <li>Learn new vocabulary words for HSK 1</li>
                    <li>Master key grammar patterns</li>
                    <li>Practice daily conversations</li>
                </ul>
            </div>
            
            <div class="section">
                <div class="section-title">
                    📚 Vocabulary
                    <button class="play-all-btn" onclick="alert('Load vocabulary from API')">🔊 Play All</button>
                </div>
                <div class="vocab-grid" id="vocabGrid">
                    <p style="grid-column:1/-1; text-align:center;">Loading vocabulary from server...</p>
                </div>
            </div>
            
            <div class="section">
                <div class="section-title">
                    📖 Grammar Points
                    <button class="play-all-btn" onclick="alert('Load grammar from API')">🔊 Play All</button>
                </div>
                <div id="grammarContainer">
                    <p>Loading grammar from server...</p>
                </div>
            </div>
            
            <div class="section">
                <div class="section-title">
                    💬 Conversation Practice
                    <button class="play-all-btn" onclick="alert('Load dialogue from API')">🔊 Play All</button>
                </div>
                <div class="dialogue-container">
                    <div class="dialogue-scene" id="dialogueContainer">
                        <p style="padding:20px;">Loading conversation from server...</p>
                    </div>
                </div>
            </div>
        </div>
        
        <button class="back-btn" onclick="window.location.href='/lessons'">← Back to All Lessons</button>
    </div>

    <script>
        let lessonNum = {num};
        
        async function playAudio(text, language = 'zh') {{
            if (!text) return;
            try {{
                const response = await fetch('/api/speak', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ text: text, language: language }})
                }});
                if (response.ok) {{
                    const audioBlob = await response.blob();
                    const audio = new Audio(URL.createObjectURL(audioBlob));
                    audio.play();
                }} else {{
                    const utterance = new SpeechSynthesisUtterance(text);
                    utterance.lang = language === 'zh' ? 'zh-CN' : 'en-US';
                    speechSynthesis.speak(utterance);
                }}
            }} catch(e) {{ console.error(e); }}
        }}
        
        async function loadLessonData() {{
            try {{
                const response = await fetch(`/api/lesson/${{lessonNum}}`);
                if (response.ok) {{
                    const lesson = await response.json();
                    
                    // Render vocabulary
                    const vocabGrid = document.getElementById('vocabGrid');
                    if (lesson.vocabulary && lesson.vocabulary.length > 0) {{
                        vocabGrid.innerHTML = lesson.vocabulary.map(v => `
                            <div class="vocab-card">
                                <div class="vocab-word" onclick="playAudio('${{v.word}}', 'zh')">${{v.word}}</div>
                                <div class="vocab-pinyin">${{v.pinyin}}</div>
                                <div class="vocab-meaning">${{v.meaning}}</div>
                                <div class="vocab-example">
                                    <div class="vocab-example-chinese">📝 ${{v.example}}</div>
                                    <button class="audio-btn" onclick="playAudio('${{v.word}}', 'zh')">🔊 Word</button>
                                    <button class="audio-btn" onclick="playAudio('${{v.example}}', 'zh')">🔊 Example</button>
                                </div>
                            </div>
                        `).join('');
                    }}
                    
                    // Render grammar
                    const grammarContainer = document.getElementById('grammarContainer');
                    if (lesson.grammar && lesson.grammar.length > 0) {{
                        grammarContainer.innerHTML = lesson.grammar.map(g => `
                            <div class="grammar-card">
                                <div class="grammar-title">${{g.point}}</div>
                                <div class="grammar-explanation">${{g.explanation}}</div>
                                <div class="grammar-examples">
                                    <strong>Examples:</strong>
                                    <div class="grammar-example-item">
                                        <div class="grammar-example-chinese">${{g.example}}</div>
                                        <button class="audio-btn" onclick="playAudio('${{g.example}}', 'zh')">🔊 Listen</button>
                                    </div>
                                </div>
                            </div>
                        `).join('');
                    }}
                    
                    // Render dialogue
                    const dialogueContainer = document.getElementById('dialogueContainer');
                    if (lesson.dialogue) {{
                        dialogueContainer.innerHTML = `
                            <div class="dialogue-line">
                                <div class="dialogue-bubble">
                                    <div class="dialogue-chinese">${{lesson.dialogue}}</div>
                                    <button class="audio-btn" onclick="playAudio('${{lesson.dialogue}}', 'zh')">🔊 Listen</button>
                                </div>
                            </div>
                        `;
                    }}
                }}
            }} catch(e) {{
                console.error('Error loading lesson:', e);
            }}
        }}
        
        loadLessonData();
        window.playAudio = playAudio;
    </script>
</body>
</html>'''

# Generate all 15 lesson files
os.makedirs("templates", exist_ok=True)

for num, data in hsk1_lessons.items():
    filename = f"templates/hsk1_lesson{num}.html"
    content = template.format(
        num=num,
        title=data["title"],
        title_en=data["title_en"],
        prev=data["nav_prev"],
        next=data["nav_next"]
    )
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Created: {filename}")

print("\n🎉 All 15 HSK 1 lessons generated successfully!")