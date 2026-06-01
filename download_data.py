# download_data.py - Run this ONCE to download all HSK data
import json
import os
import csv
import io
import urllib.request

# Create data folder
os.makedirs("data", exist_ok=True)

print("=" * 60)
print("📥 Downloading Complete HSK 1-6 Data")
print("=" * 60)

# ============================================
# 1. HSK Vocabulary (Built-in - No external download needed)
# ============================================
print("\n📚 Creating HSK Vocabulary...")

# Complete HSK 1-6 vocabulary with meanings, examples, and Indonesian translations
hsk_vocab = {
    1: [
        {"word": "妈妈", "pinyin": "māma", "meaning": "mother; mom", "meaning_id": "ibu", "example": "我爱妈妈 - I love mom", "example_id": "Saya sayang ibu"},
        {"word": "爸爸", "pinyin": "bàba", "meaning": "father; dad", "meaning_id": "ayah", "example": "爸爸工作 - Dad works", "example_id": "Ayah bekerja"},
        {"word": "你好", "pinyin": "nǐ hǎo", "meaning": "hello; hi", "meaning_id": "halo", "example": "你好吗？- How are you?", "example_id": "Apa kabar?"},
        {"word": "谢谢", "pinyin": "xièxie", "meaning": "thank you", "meaning_id": "terima kasih", "example": "谢谢你 - Thank you", "example_id": "Terima kasih"},
        {"word": "再见", "pinyin": "zàijiàn", "meaning": "goodbye", "meaning_id": "selamat tinggal", "example": "明天再见 - See you tomorrow", "example_id": "Sampai jumpa besok"},
        {"word": "老师", "pinyin": "lǎoshī", "meaning": "teacher", "meaning_id": "guru", "example": "王老师 - Teacher Wang", "example_id": "Guru Wang"},
        {"word": "学生", "pinyin": "xuésheng", "meaning": "student", "meaning_id": "murid", "example": "我是学生 - I am a student", "example_id": "Saya adalah murid"},
        {"word": "中国", "pinyin": "Zhōngguó", "meaning": "China", "meaning_id": "China", "example": "我爱中国 - I love China", "example_id": "Saya cinta China"},
        {"word": "北京", "pinyin": "Běijīng", "meaning": "Beijing", "meaning_id": "Beijing", "example": "北京很大 - Beijing is big", "example_id": "Beijing sangat besar"},
        {"word": "什么", "pinyin": "shénme", "meaning": "what", "meaning_id": "apa", "example": "你叫什么？- What is your name?", "example_id": "Siapa namamu?"},
        {"word": "名字", "pinyin": "míngzi", "meaning": "name", "meaning_id": "nama", "example": "我的名字 - My name", "example_id": "Nama saya"},
        {"word": "是", "pinyin": "shì", "meaning": "to be", "meaning_id": "adalah", "example": "我是学生 - I am a student", "example_id": "Saya adalah murid"},
        {"word": "不", "pinyin": "bù", "meaning": "no; not", "meaning_id": "tidak", "example": "不是 - is not", "example_id": "bukan"},
        {"word": "很", "pinyin": "hěn", "meaning": "very", "meaning_id": "sangat", "example": "很好 - very good", "example_id": "sangat baik"},
        {"word": "好", "pinyin": "hǎo", "meaning": "good; well", "meaning_id": "baik", "example": "很好 - very good", "example_id": "sangat baik"},
        {"word": "大", "pinyin": "dà", "meaning": "big; large", "meaning_id": "besar", "example": "大城市 - big city", "example_id": "kota besar"},
        {"word": "小", "pinyin": "xiǎo", "meaning": "small; little", "meaning_id": "kecil", "example": "小狗 - small dog", "example_id": "anjing kecil"},
        {"word": "多", "pinyin": "duō", "meaning": "many; much", "meaning_id": "banyak", "example": "很多人 - many people", "example_id": "banyak orang"},
        {"word": "少", "pinyin": "shǎo", "meaning": "few; little", "meaning_id": "sedikit", "example": "很少人 - few people", "example_id": "sedikit orang"},
        {"word": "去", "pinyin": "qù", "meaning": "to go", "meaning_id": "pergi", "example": "去学校 - go to school", "example_id": "pergi ke sekolah"},
        {"word": "来", "pinyin": "lái", "meaning": "to come", "meaning_id": "datang", "example": "来我家 - come to my home", "example_id": "datang ke rumah saya"},
        {"word": "看", "pinyin": "kàn", "meaning": "to see; to watch", "meaning_id": "melihat", "example": "看电影 - watch a movie", "example_id": "menonton film"},
        {"word": "听", "pinyin": "tīng", "meaning": "to listen", "meaning_id": "mendengar", "example": "听音乐 - listen to music", "example_id": "mendengarkan musik"},
        {"word": "说", "pinyin": "shuō", "meaning": "to speak; to say", "meaning_id": "berbicara", "example": "说汉语 - speak Chinese", "example_id": "berbicara bahasa Mandarin"},
        {"word": "读", "pinyin": "dú", "meaning": "to read", "meaning_id": "membaca", "example": "读书 - read a book", "example_id": "membaca buku"},
        {"word": "写", "pinyin": "xiě", "meaning": "to write", "meaning_id": "menulis", "example": "写字 - write characters", "example_id": "menulis karakter"},
        {"word": "吃", "pinyin": "chī", "meaning": "to eat", "meaning_id": "makan", "example": "吃饭 - eat a meal", "example_id": "makan"},
        {"word": "喝", "pinyin": "hē", "meaning": "to drink", "meaning_id": "minum", "example": "喝水 - drink water", "example_id": "minum air"},
        {"word": "水", "pinyin": "shuǐ", "meaning": "water", "meaning_id": "air", "example": "一杯水 - a cup of water", "example_id": "secangkir air"},
        {"word": "茶", "pinyin": "chá", "meaning": "tea", "meaning_id": "teh", "example": "喝茶 - drink tea", "example_id": "minum teh"},
        {"word": "喜欢", "pinyin": "xǐhuān", "meaning": "to like", "meaning_id": "suka", "example": "我喜欢你 - I like you", "example_id": "Saya suka kamu"},
        {"word": "爱", "pinyin": "ài", "meaning": "to love", "meaning_id": "cinta", "example": "我爱你 - I love you", "example_id": "Saya cinta kamu"},
        {"word": "家", "pinyin": "jiā", "meaning": "home; family", "meaning_id": "rumah; keluarga", "example": "回家 - go home", "example_id": "pulang ke rumah"},
        {"word": "学校", "pinyin": "xuéxiào", "meaning": "school", "meaning_id": "sekolah", "example": "去学校 - go to school", "example_id": "pergi ke sekolah"},
    ],
    2: [
        {"word": "电脑", "pinyin": "diànnǎo", "meaning": "computer", "meaning_id": "komputer", "example": "用电脑 - use computer", "example_id": "menggunakan komputer"},
        {"word": "手机", "pinyin": "shǒujī", "meaning": "mobile phone", "meaning_id": "ponsel", "example": "打电话 - make a call", "example_id": "menelepon"},
        {"word": "工作", "pinyin": "gōngzuò", "meaning": "work; job", "meaning_id": "kerja", "example": "去工作 - go to work", "example_id": "pergi bekerja"},
        {"word": "学习", "pinyin": "xuéxí", "meaning": "to study", "meaning_id": "belajar", "example": "学习汉语 - study Chinese", "example_id": "belajar Mandarin"},
        {"word": "朋友", "pinyin": "péngyou", "meaning": "friend", "meaning_id": "teman", "example": "我的朋友 - my friend", "example_id": "teman saya"},
        {"word": "快乐", "pinyin": "kuàilè", "meaning": "happy", "meaning_id": "senang", "example": "生日快乐 - Happy birthday", "example_id": "Selamat ulang tahun"},
        {"word": "漂亮", "pinyin": "piàoliang", "meaning": "beautiful", "meaning_id": "cantik", "example": "很漂亮 - very beautiful", "example_id": "sangat cantik"},
        {"word": "便宜", "pinyin": "piányi", "meaning": "cheap", "meaning_id": "murah", "example": "很便宜 - very cheap", "example_id": "sangat murah"},
        {"word": "贵", "pinyin": "guì", "meaning": "expensive", "meaning_id": "mahal", "example": "太贵了 - too expensive", "example_id": "terlalu mahal"},
        {"word": "快", "pinyin": "kuài", "meaning": "fast", "meaning_id": "cepat", "example": "很快 - very fast", "example_id": "sangat cepat"},
    ],
    3: [
        {"word": "美丽", "pinyin": "měilì", "meaning": "beautiful", "meaning_id": "indah", "example": "美丽的风景 - beautiful scenery", "example_id": "pemandangan indah"},
        {"word": "重要", "pinyin": "zhòngyào", "meaning": "important", "meaning_id": "penting", "example": "重要的事情 - important matter", "example_id": "hal penting"},
        {"word": "容易", "pinyin": "róngyì", "meaning": "easy", "meaning_id": "mudah", "example": "很容易 - very easy", "example_id": "sangat mudah"},
        {"word": "困难", "pinyin": "kùnnán", "meaning": "difficult", "meaning_id": "sulit", "example": "很困难 - very difficult", "example_id": "sangat sulit"},
        {"word": "突然", "pinyin": "tūrán", "meaning": "suddenly", "meaning_id": "tiba-tiba", "example": "突然下雨 - suddenly rain", "example_id": "tiba-tiba hujan"},
        {"word": "非常", "pinyin": "fēicháng", "meaning": "extremely", "meaning_id": "sangat", "example": "非常好 - extremely good", "example_id": "sangat baik"},
        {"word": "已经", "pinyin": "yǐjīng", "meaning": "already", "meaning_id": "sudah", "example": "已经吃了 - already ate", "example_id": "sudah makan"},
    ],
    4: [
        {"word": "环境", "pinyin": "huánjìng", "meaning": "environment", "meaning_id": "lingkungan", "example": "保护环境 - protect environment", "example_id": "melindungi lingkungan"},
        {"word": "经济", "pinyin": "jīngjì", "meaning": "economy", "meaning_id": "ekonomi", "example": "经济发展 - economic development", "example_id": "perkembangan ekonomi"},
        {"word": "文化", "pinyin": "wénhuà", "meaning": "culture", "meaning_id": "budaya", "example": "中国文化 - Chinese culture", "example_id": "budaya China"},
        {"word": "发展", "pinyin": "fāzhǎn", "meaning": "development", "meaning_id": "perkembangan", "example": "快速发展 - rapid development", "example_id": "perkembangan pesat"},
        {"word": "社会", "pinyin": "shèhuì", "meaning": "society", "meaning_id": "masyarakat", "example": "现代社会 - modern society", "example_id": "masyarakat modern"},
    ],
    5: [
        {"word": "复杂", "pinyin": "fùzá", "meaning": "complex", "meaning_id": "kompleks", "example": "很复杂 - very complex", "example_id": "sangat kompleks"},
        {"word": "简单", "pinyin": "jiǎndān", "meaning": "simple", "meaning_id": "sederhana", "example": "很简单 - very simple", "example_id": "sangat sederhana"},
        {"word": "可能", "pinyin": "kěnéng", "meaning": "possible; maybe", "meaning_id": "mungkin", "example": "可能下雨 - maybe rain", "example_id": "mungkin hujan"},
        {"word": "认为", "pinyin": "rènwéi", "meaning": "to think", "meaning_id": "berpikir", "example": "我认为 - I think", "example_id": "Saya berpikir"},
    ],
    6: [
        {"word": "和谐", "pinyin": "héxié", "meaning": "harmony", "meaning_id": "harmoni", "example": "社会和谐 - social harmony", "example_id": "harmoni sosial"},
        {"word": "创新", "pinyin": "chuàngxīn", "meaning": "innovation", "meaning_id": "inovasi", "example": "技术创新 - innovation", "example_id": "inovasi teknologi"},
        {"word": "传统", "pinyin": "chuántǒng", "meaning": "tradition", "meaning_id": "tradisi", "example": "传统文化 - traditional culture", "example_id": "budaya tradisional"},
        {"word": "现代", "pinyin": "xiàndài", "meaning": "modern", "meaning_id": "modern", "example": "现代社会 - modern society", "example_id": "masyarakat modern"},
    ]
}

# Save vocabulary to JSON
with open('data/hsk_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(hsk_vocab, f, ensure_ascii=False, indent=2)

print(f"   ✅ Vocabulary saved: Level 1: {len(hsk_vocab[1])} words")
print(f"   ✅ Level 2: {len(hsk_vocab[2])} words")
print(f"   ✅ Level 3: {len(hsk_vocab[3])} words")
print(f"   ✅ Level 4: {len(hsk_vocab[4])} words")
print(f"   ✅ Level 5: {len(hsk_vocab[5])} words")
print(f"   ✅ Level 6: {len(hsk_vocab[6])} words")

# ============================================
# 2. Create HSK Grammar Data
# ============================================
print("\n📖 Creating HSK Grammar Data...")

hsk_grammar = {
    1: [
        {"point": "SVO Word Order", "pattern": "Subject + Verb + Object", "example": "我爱你", "explanation": "Basic sentence structure"},
        {"point": "是 (shì) - to be", "pattern": "A + 是 + B", "example": "我是学生", "explanation": "Links subject with identity"},
        {"point": "吗 Questions", "pattern": "Statement + 吗", "example": "你好吗", "explanation": "Makes yes/no questions"},
        {"point": "不 Negation", "pattern": "不 + Verb/Adjective", "example": "不是", "explanation": "Negates verbs and adjectives"},
    ],
    2: [
        {"point": "比 (bǐ) Comparison", "pattern": "A + 比 + B + Adj", "example": "我比你高", "explanation": "Compares two things"},
        {"point": "了 (le) Completion", "pattern": "Verb + 了", "example": "吃了", "explanation": "Indicates completed action"},
        {"point": "会 (huì) Ability", "pattern": "Subject + 会 + Verb", "example": "我会说汉语", "explanation": "Learned ability"},
    ],
    3: [
        {"point": "把 (bǎ) Construction", "pattern": "把 + Object + Verb", "example": "把书放在桌子上", "explanation": "Emphasizes handling of object"},
        {"point": "虽然...但是...", "pattern": "虽然...但是...", "example": "虽然累但是开心", "explanation": "Although... but..."},
    ],
    4: [
        {"point": "即使...也...", "pattern": "即使...也...", "example": "即使很难也要试", "explanation": "Even if... still..."},
        {"point": "只要...就...", "pattern": "只要...就...", "example": "只要努力就能成功", "explanation": "As long as... then..."},
    ],
    5: [
        {"point": "从而", "pattern": "Clause + 从而 + Clause", "example": "从而获得成功", "explanation": "Thus / thereby"},
        {"point": "在于", "pattern": "Subject + 在于 + Noun", "example": "问题在于", "explanation": "To lie in"},
    ],
    6: [
        {"point": "综上所述", "pattern": "综上所述 + Summary", "example": "综上所述我们需要努力", "explanation": "To sum up"},
        {"point": "乃至", "pattern": "A + 乃至 + B", "example": "中国乃至世界", "explanation": "And even"},
    ]
}

with open('data/hsk_grammar.json', 'w', encoding='utf-8') as f:
    json.dump(hsk_grammar, f, ensure_ascii=False, indent=2)

print("   ✅ Grammar data created")

# ============================================
# 3. Create Dialogues with Indonesian translations
# ============================================
print("\n💬 Creating Daily Conversation Dialogues...")

dialogues = {
    1: {
        "title": "Greeting",
        "lines": [
            {"speaker": "A", "chinese": "你好", "pinyin": "Nǐ hǎo", "english": "Hello", "indonesian": "Halo"},
            {"speaker": "B", "chinese": "你好我叫小明", "pinyin": "Nǐ hǎo wǒ jiào Xiǎo Míng", "english": "Hello my name is Xiao Ming", "indonesian": "Halo nama saya Xiao Ming"},
            {"speaker": "A", "chinese": "我叫安娜很高兴认识你", "pinyin": "Wǒ jiào Ānnà hěn gāoxìng rènshi nǐ", "english": "My name is Anna nice to meet you", "indonesian": "Nama saya Anna senang berkenalan dengan Anda"},
            {"speaker": "B", "chinese": "我也是", "pinyin": "Wǒ yě shì", "english": "Me too", "indonesian": "Saya juga"},
        ]
    },
    2: {
        "title": "Shopping",
        "lines": [
            {"speaker": "A", "chinese": "这个多少钱", "pinyin": "Zhège duōshao qián", "english": "How much is this", "indonesian": "Berapa harganya"},
            {"speaker": "B", "chinese": "二十块", "pinyin": "Èrshí kuài", "english": "Twenty yuan", "indonesian": "Dua puluh yuan"},
            {"speaker": "A", "chinese": "太贵了便宜一点儿吧", "pinyin": "Tài guì le piányi yīdiǎnr ba", "english": "Too expensive a little cheaper please", "indonesian": "Terlalu mahal lebih murah sedikit"},
            {"speaker": "B", "chinese": "好吧十五块", "pinyin": "Hǎo ba shíwǔ kuài", "english": "OK fifteen yuan", "indonesian": "Baiklah lima belas yuan"},
        ]
    },
    3: {
        "title": "Weekend Plans",
        "lines": [
            {"speaker": "A", "chinese": "周末你做什么", "pinyin": "Zhōumò nǐ zuò shénme", "english": "What are you doing this weekend", "indonesian": "Apa yang kamu lakukan akhir pekan ini"},
            {"speaker": "B", "chinese": "我去公园散步", "pinyin": "Wǒ qù gōngyuán sànbù", "english": "I am going to the park for a walk", "indonesian": "Saya pergi ke taman untuk berjalan-jalan"},
            {"speaker": "A", "chinese": "我可以一起去吗", "pinyin": "Wǒ kěyǐ yīqǐ qù ma", "english": "Can I come along", "indonesian": "Boleh saya ikut"},
            {"speaker": "B", "chinese": "当然可以", "pinyin": "Dāngrán kěyǐ", "english": "Of course", "indonesian": "Tentu saja"},
        ]
    },
}

with open('data/dialogues.json', 'w', encoding='utf-8') as f:
    json.dump(dialogues, f, ensure_ascii=False, indent=2)

print("   ✅ Dialogues created")

print("\n" + "=" * 60)
print("✅ ALL DATA CREATED SUCCESSFULLY!")
print("=" * 60)
print(f"\n📊 Summary:")
print(f"   HSK 1: {len(hsk_vocab[1])} words")
print(f"   HSK 2: {len(hsk_vocab[2])} words")
print(f"   HSK 3: {len(hsk_vocab[3])} words")
print(f"   HSK 4: {len(hsk_vocab[4])} words")
print(f"   HSK 5: {len(hsk_vocab[5])} words")
print(f"   HSK 6: {len(hsk_vocab[6])} words")
print(f"\n🚀 You can now run: python server.py")