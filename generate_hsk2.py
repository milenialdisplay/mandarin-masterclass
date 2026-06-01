# generate_hsk2.py - Run this to create all HSK 2 lesson files
import os

# Template for HSK 2 lessons (same structure as lesson 1)
hsk2_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>HSK 2 Lesson {num} - {title} | Mandarin Teacher</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #1a472a;
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.2); }}
        .header {{ background: linear-gradient(135deg, #1a472a, #2d6a4f); color: white; padding: 25px; text-align: center; }}
        .header h1 {{ font-size: 28px; margin-bottom: 8px; }}
        .level-indicator {{ display: inline-block; background: #ffd700; color: #1a472a; padding: 5px 15px; border-radius: 25px; font-size: 12px; margin-top: 10px; font-weight: bold; }}
        .lesson-nav {{ background: #f5f5f5; padding: 15px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px; border-bottom: 1px solid #ddd; }}
        .nav-btn {{ background: #2d6a4f; color: white; border: none; padding: 10px 20px; border-radius: 25px; cursor: pointer; font-size: 13px; font-weight: bold; }}
        .nav-btn:hover {{ background: #1a472a; }}
        .ai-teacher-box {{ background: linear-gradient(135deg, #e8f5e9, #c8e6c9); border-radius: 16px; padding: 20px; margin: 20px; border-left: 5px solid #ffd700; }}
        .ai-teacher-title {{ font-size: 18px; font-weight: bold; color: #1a472a; margin-bottom: 10px; }}
        .content {{ padding: 25px; max-height: 70vh; overflow-y: auto; }}
        .section {{ margin-bottom: 35px; background: #fafafa; border-radius: 16px; padding: 20px; border: 1px solid #eee; }}
        .section-title {{ font-size: 22px; color: #1a472a; border-left: 5px solid #ffd700; padding-left: 15px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }}
        .play-all-btn {{ background: #2d6a4f; color: white; border: none; padding: 8px 18px; border-radius: 8px; cursor: pointer; font-size: 13px; font-weight: bold; }}
        .play-all-btn:hover {{ background: #1a472a; }}
        .vocab-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 15px; }}
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
        .speak-practice-btn {{ background: #e94560; color: white; border: none; padding: 5px 12px; border-radius: 20px; cursor: pointer; font-size: 11px; margin-top: 10px; margin-right: 8px; }}
        .speak-practice-btn:hover {{ background: #c42e4a; }}
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
        .dialogue-speaker {{ font-weight: bold; margin-bottom: 5px; font-size: 14px; }}
        .speaker-male {{ color: #87CEEB; }}
        .speaker-female {{ color: #FFB6C1; }}
        .dialogue-bubble {{ background: rgba(255,255,255,0.1); border-radius: 18px; padding: 12px 18px; max-width: 90%; }}
        .dialogue-chinese {{ font-size: 18px; margin-bottom: 5px; }}
        .dialogue-pinyin {{ color: #aaa; font-size: 12px; margin-bottom: 5px; }}
        .dialogue-translation {{ color: #888; font-size: 13px; }}
        .exercise-card {{ background: white; border-radius: 12px; padding: 15px; margin-bottom: 15px; border: 1px solid #e0e0e0; }}
        .exercise-question {{ font-weight: bold; margin-bottom: 12px; }}
        .exercise-option {{ padding: 10px 15px; margin: 8px 0; background: #f5f5f5; border-radius: 10px; cursor: pointer; transition: all 0.2s; }}
        .exercise-option:hover {{ background: #e8f5e9; }}
        .exercise-option.selected {{ background: #2d6a4f; color: white; }}
        .exercise-option.correct {{ background: #d4edda; border: 1px solid #28a745; }}
        .exercise-option.wrong {{ background: #f8d7da; border: 1px solid #dc3545; }}
        .check-exercise-btn {{ background: #2d6a4f; color: white; border: none; padding: 12px 24px; border-radius: 30px; cursor: pointer; font-size: 14px; font-weight: bold; margin-top: 15px; }}
        .exercise-score {{ margin-top: 15px; padding: 12px; border-radius: 10px; text-align: center; font-weight: bold; }}
        .score-good {{ background: #d4edda; color: #28a745; }}
        .score-bad {{ background: #f8d7da; color: #dc3545; }}
        .back-btn {{ background: #6c757d; color: white; border: none; padding: 12px 24px; border-radius: 30px; cursor: pointer; font-size: 14px; font-weight: bold; margin: 0 25px 25px 25px; width: calc(100% - 50px); }}
        .back-btn:hover {{ background: #5a6268; }}
        @media (max-width: 768px) {{ .vocab-grid {{ grid-template-columns: 1fr; }} .section-title {{ font-size: 18px; flex-direction: column; align-items: flex-start; }} .dialogue-bubble {{ max-width: 100%; }} }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>HSK 2 Lesson {num}: {title}</h1>
            <p>{title_en}</p>
            <div class="level-indicator">🏆 HSK Level 2 - Intermediate</div>
        </div>
        
        <div class="lesson-nav">
            <button class="nav-btn" onclick="window.location.href='/hsk2/lesson{prev}'">◀ Previous Lesson</button>
            <button class="nav-btn" onclick="window.location.href='/lessons'">📚 All Lessons</button>
            <button class="nav-btn" onclick="window.location.href='/hsk2/lesson{next}'">Next Lesson ▶</button>
        </div>
        
        <div class="ai-teacher-box">
            <div class="ai-teacher-title">🎓 AI Teacher Assistant</div>
            <div class="ai-teacher-message">
                <strong>📖 HSK Level 2 - Lesson {num}</strong><br><br>
                In this lesson, you will learn new vocabulary, grammar patterns, and practice conversations.<br><br>
                • Click any word to hear pronunciation<br>
                • Use <strong>🎤 Speak</strong> to practice your pronunciation<br>
                • Complete the exercises at the end<br><br>
                加油！(Jiāyóu!) Keep going!
            </div>
        </div>
        
        <div class="content">
            <div class="section">
                <div class="section-title">📖 Learning Objectives</div>
                <ul style="margin-left: 20px; line-height: 1.8;">
                    <li>Learn new vocabulary words for HSK Level 2</li>
                    <li>Master intermediate grammar patterns</li>
                    <li>Practice daily conversations</li>
                </ul>
            </div>
            
            <div class="section">
                <div class="section-title">
                    📚 Vocabulary
                    <button class="play-all-btn" onclick="playVocabulary()">🔊 Play All</button>
                </div>
                <div class="vocab-grid" id="vocabGrid">
                    <p>Loading vocabulary...</p>
                </div>
            </div>
            
            <div class="section">
                <div class="section-title">
                    📖 Grammar Points
                    <button class="play-all-btn" onclick="playGrammar()">🔊 Play All</button>
                </div>
                <div id="grammarContainer"><p>Loading grammar...</p></div>
            </div>
            
            <div class="section">
                <div class="section-title">
                    💬 Conversation Practice
                    <button class="play-all-btn" onclick="playDialogue()">🔊 Play All</button>
                </div>
                <div class="dialogue-container">
                    <div class="dialogue-scene" id="dialogueContainer"><p>Loading conversation...</p></div>
                </div>
            </div>
            
            <div class="section">
                <div class="section-title">✍️ Lesson Exercises</div>
                <div id="exercisesContainer"></div>
                <button class="check-exercise-btn" onclick="checkExercises()">Check Answers</button>
                <div id="exerciseScore" class="exercise-score" style="display: none;"></div>
            </div>
        </div>
        
        <button class="back-btn" onclick="window.location.href='/lessons'">← Back to All Lessons</button>
    </div>

    <script>
        // Vocabulary for Lesson {num}
        const vocabulary = [
            {{word_data}}
        ];
        
        // Grammar for Lesson {num}
        const grammar = [
            {{grammar_data}}
        ];
        
        // Dialogue for Lesson {num}
        const dialogue = [
            {{dialogue_data}}
        ];
        
        // Exercises
        const exercises = [
            {{exercise_data}}
        ];
        
        let userAnswers = {{}};
        let recognition = null;
        
        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {{
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            recognition = new SpeechRecognition();
            recognition.lang = 'zh-CN';
        }}
        
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
        
        function startPronunciationPractice(word, pinyin) {{
            if (!recognition) {{
                alert("Speech recognition not supported.");
                return;
            }}
            recognition.start();
            recognition.onresult = function(event) {{
                const spoken = event.results[0][0].transcript;
                alert(spoken === word || spoken === pinyin ? "✅ Good pronunciation!" : "❌ Try again. Say: " + word);
            }};
        }}
        
        function renderVocabulary() {{
            const grid = document.getElementById('vocabGrid');
            if (vocabulary.length > 0) {{
                grid.innerHTML = vocabulary.map(v => `
                    <div class="vocab-card">
                        <div class="vocab-word" onclick="playAudio('${{v.word}}', 'zh')">${{v.word}}</div>
                        <div class="vocab-pinyin">${{v.pinyin}}</div>
                        <div class="vocab-meaning">${{v.meaning}}</div>
                        <div class="vocab-example">
                            <div>📝 ${{v.example}}</div>
                            <div class="vocab-example-translation">→ ${{v.example_translation}}</div>
                            <button class="audio-btn" onclick="playAudio('${{v.word}}', 'zh')">🔊 Listen</button>
                            <button class="speak-practice-btn" onclick="startPronunciationPractice('${{v.word}}', '${{v.pinyin}}')">🎤 Speak</button>
                        </div>
                    </div>
                `).join('');
            }}
        }}
        
        function renderGrammar() {{
            const container = document.getElementById('grammarContainer');
            if (grammar.length > 0) {{
                container.innerHTML = grammar.map(g => `
                    <div class="grammar-card">
                        <div class="grammar-title">${{g.point}}</div>
                        <div class="grammar-explanation">${{g.explanation}}</div>
                        <div class="grammar-examples">
                            <strong>Examples:</strong>
                            ${{g.examples.map(ex => `
                                <div class="grammar-example-item">
                                    <div>${{ex.chinese}}</div>
                                    <div>→ ${{ex.translation}}</div>
                                    <button class="audio-btn" onclick="playAudio('${{ex.chinese}}', 'zh')">🔊 Listen</button>
                                </div>
                            `).join('')}}
                        </div>
                    </div>
                `).join('');
            }}
        }}
        
        function renderDialogue() {{
            const container = document.getElementById('dialogueContainer');
            if (dialogue.length > 0) {{
                container.innerHTML = dialogue.map(line => `
                    <div class="dialogue-line">
                        <div class="dialogue-speaker ${{line.speaker === 'male' ? 'speaker-male' : 'speaker-female'}}">
                            ${{line.speaker === 'male' ? '👨' : '👩'}} ${{line.name}}:
                        </div>
                        <div class="dialogue-bubble">
                            <div class="dialogue-chinese">${{line.chinese}}</div>
                            <div class="dialogue-pinyin">${{line.pinyin}}</div>
                            <div class="dialogue-translation">→ ${{line.translation}}</div>
                            <button class="audio-btn" onclick="playAudio('${{line.chinese}}', 'zh')">🔊 Listen</button>
                        </div>
                    </div>
                `).join('');
            }}
        }}
        
        function renderExercises() {{
            const container = document.getElementById('exercisesContainer');
            container.innerHTML = exercises.map((ex, idx) => `
                <div class="exercise-card">
                    <div class="exercise-question">${{idx + 1}}. ${{ex.question}}</div>
                    ${{ex.options.map((opt, optIdx) => `
                        <div class="exercise-option" onclick="selectAnswer(${{idx}}, ${{optIdx}})">
                            ${{String.fromCharCode(65 + optIdx)}}. ${{opt}}
                        </div>
                    `).join('')}}
                </div>
            `).join('');
        }}
        
        function selectAnswer(exIdx, optIdx) {{
            userAnswers[exIdx] = optIdx;
            const options = document.querySelectorAll(`.exercise-card:nth-child($${{exIdx + 1}}) .exercise-option`);
            options.forEach(opt => opt.classList.remove('selected'));
            options[optIdx].classList.add('selected');
        }}
        
        function checkExercises() {{
            let correct = 0;
            exercises.forEach((ex, idx) => {{
                if (userAnswers[idx] === ex.correct) correct++;
            }});
            const scoreDiv = document.getElementById('exerciseScore');
            scoreDiv.style.display = 'block';
            const percent = Math.round((correct / exercises.length) * 100);
            if (percent >= 70) {{
                scoreDiv.className = 'exercise-score score-good';
                scoreDiv.innerHTML = `<strong>Score: ${{correct}}/${{exercises.length}} (${{percent}}%)</strong><br>🎉 Great job!`;
            }} else {{
                scoreDiv.className = 'exercise-score score-bad';
                scoreDiv.innerHTML = `<strong>Score: ${{correct}}/${{exercises.length}} (${{percent}}%)</strong><br>📚 Review the lesson and try again.`;
            }}
        }}
        
        function playVocabulary() {{
            let i = 0;
            function next() {{
                if (i >= vocabulary.length) return;
                playAudio(vocabulary[i].word, 'zh');
                i++;
                setTimeout(next, 1500);
            }}
            next();
        }}
        
        function playGrammar() {{
            let g = 0, e = 0;
            function next() {{
                if (g >= grammar.length) return;
                if (e === 0) {{
                    playAudio(grammar[g].point + '. ' + grammar[g].explanation, 'en');
                    e++;
                    setTimeout(next, 3000);
                }} else if (e - 1 < grammar[g].examples.length) {{
                    playAudio(grammar[g].examples[e - 1].chinese, 'zh');
                    e++;
                    setTimeout(next, 2500);
                }} else {{
                    g++;
                    e = 0;
                    setTimeout(next, 1000);
                }}
            }}
            next();
        }}
        
        function playDialogue() {{
            let i = 0;
            function next() {{
                if (i >= dialogue.length) return;
                playAudio(dialogue[i].chinese, 'zh');
                i++;
                setTimeout(next, 3500);
            }}
            next();
        }}
        
        renderVocabulary();
        renderGrammar();
        renderDialogue();
        renderExercises();
        
        window.playAudio = playAudio;
        window.startPronunciationPractice = startPronunciationPractice;
        window.selectAnswer = selectAnswer;
        window.checkExercises = checkExercises;
        window.playVocabulary = playVocabulary;
        window.playGrammar = playGrammar;
        window.playDialogue = playDialogue;
    </script>
</body>
</html>'''

# HSK 2 Lesson data
hsk2_data = {
    1: {"title": "九月去中国旅游最好", "title_en": "September is Best", "prev": 15, "next": 2},
    2: {"title": "我每天六点起床", "title_en": "I Get Up at 6", "prev": 1, "next": 3},
    3: {"title": "左边那个红色的是我的", "title_en": "The Red One is Mine", "prev": 2, "next": 4},
    4: {"title": "这个星期天我们去打球吧", "title_en": "Let's Play Ball", "prev": 3, "next": 5},
    5: {"title": "我比你高", "title_en": "I'm Taller", "prev": 4, "next": 6},
    6: {"title": "你怎么不吃了", "title_en": "Why Not Eat", "prev": 5, "next": 7},
    7: {"title": "电脑比手机贵多了", "title_en": "Computer is Pricier", "prev": 6, "next": 8},
    8: {"title": "我不太喜欢喝咖啡", "title_en": "I Don't Like Coffee", "prev": 7, "next": 9},
    9: {"title": "最近怎么样", "title_en": "How's It Going", "prev": 8, "next": 10},
    10: {"title": "别找了", "title_en": "Stop Looking", "prev": 9, "next": 11},
    11: {"title": "你习惯中国的生活了吗", "title_en": "Used to China Life", "prev": 10, "next": 12},
    12: {"title": "我都听说了", "title_en": "I've Heard", "prev": 11, "next": 13},
    13: {"title": "一边...一边...", "title_en": "While", "prev": 12, "next": 14},
    14: {"title": "越...越...", "title_en": "The More...", "prev": 13, "next": 15},
    15: {"title": "虽然...但是...", "title_en": "Although...But...", "prev": 14, "next": 1},
}

# Generate all 15 lesson files
for num in range(1, 16):
    data = hsk2_data[num]
    
    # Simplified content for lessons 2-15 (can be expanded later)
    vocab_data = '[{"word": "学习", "pinyin": "xué xí", "meaning": "to study", "example": "学习汉语", "example_translation": "study Chinese"}]'
    grammar_data = '[{"point": "Grammar Point", "explanation": "Explanation here", "examples": [{"chinese": "例子", "translation": "Example"}]}]'
    dialogue_data = '[{"speaker": "male", "name": "Student", "chinese": "你好", "pinyin": "Nǐ hǎo", "translation": "Hello"}]'
    exercise_data = '[{"question": "Sample question", "options": ["A", "B", "C", "D"], "correct": 0}]'
    
    content = hsk2_template.format(
        num=num,
        title=data["title"],
        title_en=data["title_en"],
        prev=data["prev"],
        next=data["next"],
        word_data=vocab_data,
        grammar_data=grammar_data,
        dialogue_data=dialogue_data,
        exercise_data=exercise_data
    )
    
    filename = f"templates/hsk2_lesson{num}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Created: {filename}")

print("\n🎉 All 15 HSK 2 lessons created successfully!")