# data/lessons.py - Complete HSK 1 Curriculum (15 Lessons)
# Following official "HSK Standard Course" textbook

HSK1_LESSONS = {
    1: {
        "number": 1,
        "title": "你好",
        "title_en": "Hello",
        "title_id": "Halo",
        "objectives": [
            "Learn to greet people",
            "Introduce yourself",
            "Say goodbye"
        ],
        "vocabulary": [
            {"word": "你", "pinyin": "nǐ", "meaning_en": "you", "meaning_id": "kamu", "example": "你好", "tone": 3},
            {"word": "好", "pinyin": "hǎo", "meaning_en": "good, well", "meaning_id": "baik", "example": "很好", "tone": 3},
            {"word": "你好", "pinyin": "nǐ hǎo", "meaning_en": "hello", "meaning_id": "halo", "example": "你好!", "tone": "3,3"},
            {"word": "我", "pinyin": "wǒ", "meaning_en": "I, me", "meaning_id": "saya", "example": "我是学生", "tone": 3},
            {"word": "叫", "pinyin": "jiào", "meaning_en": "to be called", "meaning_id": "bernama", "example": "我叫小明", "tone": 4},
            {"word": "什么", "pinyin": "shén me", "meaning_en": "what", "meaning_id": "apa", "example": "你叫什么", "tone": "2,0"},
            {"word": "名字", "pinyin": "míng zi", "meaning_en": "name", "meaning_id": "nama", "example": "我的名字", "tone": "2,0"},
            {"word": "是", "pinyin": "shì", "meaning_en": "to be", "meaning_id": "adalah", "example": "我是老师", "tone": 4},
            {"word": "学生", "pinyin": "xué sheng", "meaning_en": "student", "meaning_id": "murid", "example": "我是学生", "tone": "2,0"},
            {"word": "老师", "pinyin": "lǎo shī", "meaning_en": "teacher", "meaning_id": "guru", "example": "王老师", "tone": "3,1"},
            {"word": "再见", "pinyin": "zài jiàn", "meaning_en": "goodbye", "meaning_id": "selamat tinggal", "example": "明天再见", "tone": "4,4"},
            {"word": "谢谢", "pinyin": "xiè xie", "meaning_en": "thank you", "meaning_id": "terima kasih", "example": "谢谢您", "tone": "4,0"},
        ],
        "grammar": [
            {
                "point": "Basic SVO Word Order",
                "explanation_en": "Chinese uses Subject-Verb-Object word order, just like English.",
                "explanation_id": "Bahasa Mandarin menggunakan urutan Subjek-Predikat-Objek, sama seperti bahasa Inggris.",
                "examples": [
                    {"chinese": "我爱你", "pinyin": "wǒ ài nǐ", "meaning_en": "I love you", "meaning_id": "Saya cinta kamu"},
                    {"chinese": "他吃饭", "pinyin": "tā chī fàn", "meaning_en": "He eats rice", "meaning_id": "Dia makan nasi"},
                ],
                "exercise": "Make a sentence using SVO pattern",
                "exercise_id": "Buat kalimat dengan pola SPO"
            },
            {
                "point": "Questions with 吗 (ma)",
                "explanation_en": "Add 吗 at the end of a statement to make it a yes/no question.",
                "explanation_id": "Tambahkan 吗 di akhir pernyataan untuk membuat pertanyaan ya/tidak.",
                "examples": [
                    {"chinese": "你好吗", "pinyin": "nǐ hǎo ma", "meaning_en": "How are you", "meaning_id": "Apa kabar"},
                    {"chinese": "你是学生吗", "pinyin": "nǐ shì xué sheng ma", "meaning_en": "Are you a student", "meaning_id": "Apakah kamu murid"},
                ],
                "exercise": "Turn statements into questions using 吗",
                "exercise_id": "Ubah pernyataan menjadi pertanyaan dengan 吗"
            }
        ],
        "dialogue": {
            "title": "Meeting Someone New",
            "title_id": "Bertemu Orang Baru",
            "conversation": [
                {"speaker": "A", "chinese": "你好！", "pinyin": "Nǐ hǎo!", "meaning_en": "Hello!", "meaning_id": "Halo!"},
                {"speaker": "B", "chinese": "你好！", "pinyin": "Nǐ hǎo!", "meaning_en": "Hello!", "meaning_id": "Halo!"},
                {"speaker": "A", "chinese": "你叫什么名字？", "pinyin": "Nǐ jiào shénme míngzi?", "meaning_en": "What is your name?", "meaning_id": "Siapa namamu?"},
                {"speaker": "B", "chinese": "我叫小明。你呢？", "pinyin": "Wǒ jiào Xiǎo Míng. Nǐ ne?", "meaning_en": "My name is Xiao Ming. And you?", "meaning_id": "Nama saya Xiao Ming. Kamu?"},
                {"speaker": "A", "chinese": "我叫安娜。很高兴认识你。", "pinyin": "Wǒ jiào Ānnà. Hěn gāoxìng rènshi nǐ.", "meaning_en": "My name is Anna. Nice to meet you.", "meaning_id": "Nama saya Anna. Senang berkenalan denganmu."},
                {"speaker": "B", "chinese": "我也是。再见！", "pinyin": "Wǒ yě shì. Zàijiàn!", "meaning_en": "Me too. Goodbye!", "meaning_id": "Saya juga. Selamat tinggal!"},
                {"speaker": "A", "chinese": "再见！", "pinyin": "Zàijiàn!", "meaning_en": "Goodbye!", "meaning_id": "Selamat tinggal!"}
            ]
        },
        "pronunciation": {
            "initials": ["b", "p", "m", "f", "d", "t", "n", "l"],
            "finals": ["a", "o", "e", "i", "u", "ü"],
            "tones": [
                {"tone": 1, "mark": "ā", "description": "high and flat", "example": "mā"},
                {"tone": 2, "mark": "á", "description": "rising", "example": "má"},
                {"tone": 3, "mark": "ǎ", "description": "falling then rising", "example": "mǎ"},
                {"tone": 4, "mark": "à", "description": "sharp falling", "example": "mà"}
            ]
        },
        "exercises": [
            {"type": "match", "question": "Match the Chinese word to its meaning", "items": [
                {"chinese": "你好", "options": ["hello", "goodbye", "thank you", "teacher"]},
                {"chinese": "谢谢", "options": ["hello", "goodbye", "thank you", "student"]},
                {"chinese": "再见", "options": ["hello", "goodbye", "thank you", "name"]},
            ]},
            {"type": "fill_blank", "question": "Fill in the blank: 我___学生 (I am a student)", "answer": "是"},
            {"type": "rearrange", "question": "Rearrange: 你 / 吗 / 好", "answer": "你好吗"}
        ],
        "culture_note": {
            "title": "Greetings in China",
            "content": "In China, people often greet each other by asking 'Have you eaten?' (你吃了吗？) rather than talking about the weather. Handshakes are common in formal settings, while friends may just wave or nod."
        }
    },
    2: {
        "number": 2,
        "title": "谢谢你",
        "title_en": "Thank You",
        "title_id": "Terima Kasih",
        "objectives": [
            "Express thanks and apologies",
            "Ask about someone's identity",
            "Use basic adjectives"
        ],
        "vocabulary": [
            {"word": "不客气", "pinyin": "bù kè qi", "meaning_en": "you're welcome", "meaning_id": "sama-sama", "example": "不客气", "tone": "4,4,0"},
            {"word": "对不起", "pinyin": "duì bu qǐ", "meaning_en": "sorry", "meaning_id": "maaf", "example": "对不起", "tone": "4,0,3"},
            {"word": "没关系", "pinyin": "méi guān xi", "meaning_en": "it's okay", "meaning_id": "tidak apa-apa", "example": "没关系", "tone": "2,1,0"},
            {"word": "您", "pinyin": "nín", "meaning_en": "you (polite)", "meaning_id": "Anda", "example": "您好", "tone": 2},
            {"word": "请", "pinyin": "qǐng", "meaning_en": "please", "meaning_id": "mohon", "example": "请进", "tone": 3},
            {"word": "问", "pinyin": "wèn", "meaning_en": "to ask", "meaning_id": "bertanya", "example": "请问", "tone": 4},
            {"word": "姓", "pinyin": "xìng", "meaning_en": "family name", "meaning_id": "nama keluarga", "example": "我姓王", "tone": 4},
            {"word": "叫", "pinyin": "jiào", "meaning_en": "to be called", "meaning_id": "bernama", "example": "他叫李明", "tone": 4},
            {"word": "贵姓", "pinyin": "guì xìng", "meaning_en": "your surname (polite)", "meaning_id": "nama keluarga Anda", "example": "您贵姓", "tone": "4,4"},
            {"word": "呢", "pinyin": "ne", "meaning_en": "particle for follow-up question", "meaning_id": "kata tanya", "example": "你呢", "tone": 0},
            {"word": "很", "pinyin": "hěn", "meaning_en": "very", "meaning_id": "sangat", "example": "很好", "tone": 3},
            {"word": "好", "pinyin": "hǎo", "meaning_en": "good", "meaning_id": "baik", "example": "很好", "tone": 3},
        ],
        "grammar": [
            {
                "point": "Adjectives as Predicates",
                "explanation_en": "Adjectives can directly follow the subject without a linking verb like 'to be'.",
                "explanation_id": "Kata sifat dapat langsung mengikuti subjek tanpa kata kerja penghubung.",
                "examples": [
                    {"chinese": "天气很好", "pinyin": "tiānqì hěn hǎo", "meaning_en": "The weather is good", "meaning_id": "Cuacanya baik"},
                    {"chinese": "她漂亮", "pinyin": "tā piàoliang", "meaning_en": "She is beautiful", "meaning_id": "Dia cantik"},
                ],
                "exercise": "Make sentences using adjectives",
                "exercise_id": "Buat kalimat menggunakan kata sifat"
            }
        ],
        "dialogue": {
            "title": "Expressing Thanks",
            "title_id": "Mengungkapkan Terima Kasih",
            "conversation": [
                {"speaker": "A", "chinese": "谢谢您！", "pinyin": "Xièxie nín!", "meaning_en": "Thank you!", "meaning_id": "Terima kasih!"},
                {"speaker": "B", "chinese": "不客气。", "pinyin": "Bù kèqi.", "meaning_en": "You're welcome.", "meaning_id": "Sama-sama."},
                {"speaker": "A", "chinese": "对不起，我迟到了。", "pinyin": "Duìbuqǐ, wǒ chídào le.", "meaning_en": "Sorry, I'm late.", "meaning_id": "Maaf, saya terlambat."},
                {"speaker": "B", "chinese": "没关系。", "pinyin": "Méiguānxi.", "meaning_en": "It's okay.", "meaning_id": "Tidak apa-apa."}
            ]
        },
        "exercises": [
            {"type": "match", "question": "Match the expression to its usage", "items": [
                {"chinese": "谢谢", "usage": "when someone helps you"},
                {"chinese": "对不起", "usage": "when you make a mistake"},
                {"chinese": "不客气", "usage": "response to thank you"},
            ]}
        ]
    },
    3: {
        "number": 3,
        "title": "你叫什么名字",
        "title_en": "What's Your Name",
        "title_id": "Siapa Namamu",
        "objectives": [
            "Ask and answer about names",
            "Use question words",
            "Introduce family members"
        ],
        "vocabulary": [
            {"word": "什么", "pinyin": "shén me", "meaning_en": "what", "meaning_id": "apa", "example": "你叫什么", "tone": "2,0"},
            {"word": "名字", "pinyin": "míng zi", "meaning_en": "name", "meaning_id": "nama", "example": "我的名字", "tone": "2,0"},
            {"word": "叫", "pinyin": "jiào", "meaning_en": "to be called", "meaning_id": "bernama", "example": "我叫小华", "tone": 4},
            {"word": "爸爸", "pinyin": "bà ba", "meaning_en": "father", "meaning_id": "ayah", "example": "我爸爸", "tone": "4,0"},
            {"word": "妈妈", "pinyin": "mā ma", "meaning_en": "mother", "meaning_id": "ibu", "example": "我妈妈", "tone": "1,0"},
            {"word": "哥哥", "pinyin": "gē ge", "meaning_en": "older brother", "meaning_id": "kakak laki-laki", "example": "我哥哥", "tone": "1,0"},
            {"word": "姐姐", "pinyin": "jiě jie", "meaning_en": "older sister", "meaning_id": "kakak perempuan", "example": "我姐姐", "tone": "3,0"},
            {"word": "弟弟", "pinyin": "dì di", "meaning_en": "younger brother", "meaning_id": "adik laki-laki", "example": "我弟弟", "tone": "4,0"},
            {"word": "妹妹", "pinyin": "mèi mei", "meaning_en": "younger sister", "meaning_id": "adik perempuan", "example": "我妹妹", "tone": "4,0"},
        ],
        "grammar": [
            {
                "point": "Question Words (谁, 什么, 哪)",
                "explanation_en": "Question words stay in the same position as the answer would be.",
                "explanation_id": "Kata tanya tetap di posisi yang sama dengan jawabannya.",
                "examples": [
                    {"chinese": "你叫什么", "pinyin": "nǐ jiào shénme", "meaning_en": "What is your name", "meaning_id": "Siapa namamu"},
                    {"chinese": "他是谁", "pinyin": "tā shì shéi", "meaning_en": "Who is he", "meaning_id": "Dia siapa"},
                ],
                "exercise": "Create questions using 什么 and 谁",
                "exercise_id": "Buat pertanyaan dengan 什么 dan 谁"
            }
        ],
        "dialogue": {
            "title": "Introducing Family",
            "title_id": "Memperkenalkan Keluarga",
            "conversation": [
                {"speaker": "A", "chinese": "你家有几口人？", "pinyin": "Nǐ jiā yǒu jǐ kǒu rén?", "meaning_en": "How many people in your family?", "meaning_id": "Berapa orang di keluargamu?"},
                {"speaker": "B", "chinese": "我家有四口人。爸爸、妈妈、哥哥和我。", "pinyin": "Wǒ jiā yǒu sì kǒu rén. Bàba, māma, gēge hé wǒ.", "meaning_en": "There are four people. Father, mother, older brother, and me.", "meaning_id": "Ada empat orang. Ayah, ibu, kakak laki-laki, dan saya."}
            ]
        }
    },
    4: {
        "number": 4,
        "title": "她是我的汉语老师",
        "title_en": "She's My Chinese Teacher",
        "title_id": "Dia Guru Mandarin Saya",
        "objectives": [
            "Describe people and occupations",
            "Use possessive particle 的",
            "Ask about identity"
        ],
        "vocabulary": [
            {"word": "的", "pinyin": "de", "meaning_en": "possessive particle", "meaning_id": "kata kepunyaan", "example": "我的书", "tone": 0},
            {"word": "谁", "pinyin": "shéi", "meaning_en": "who", "meaning_id": "siapa", "example": "他是谁", "tone": 2},
            {"word": "哪", "pinyin": "nǎ", "meaning_en": "which", "meaning_id": "yang mana", "example": "哪个人", "tone": 3},
            {"word": "汉语", "pinyin": "Hàn yǔ", "meaning_en": "Chinese language", "meaning_id": "bahasa Mandarin", "example": "学汉语", "tone": "4,3"},
            {"word": "英语", "pinyin": "Yīng yǔ", "meaning_en": "English", "meaning_id": "bahasa Inggris", "example": "说英语", "tone": "1,3"},
            {"word": "国", "pinyin": "guó", "meaning_en": "country", "meaning_id": "negara", "example": "中国", "tone": 2},
            {"word": "人", "pinyin": "rén", "meaning_en": "person", "meaning_id": "orang", "example": "中国人", "tone": 2},
            {"word": "美国", "pinyin": "Měi guó", "meaning_en": "America", "meaning_id": "Amerika", "example": "美国人", "tone": "3,2"},
            {"word": "法国", "pinyin": "Fà guó", "meaning_en": "France", "meaning_id": "Prancis", "example": "法国人", "tone": "4,2"},
            {"word": "德国", "pinyin": "Dé guó", "meaning_en": "Germany", "meaning_id": "Jerman", "example": "德国人", "tone": "2,2"},
        ],
        "grammar": [
            {
                "point": "Possessive 的 (de)",
                "explanation_en": "Use 的 to show possession, like apostrophe-s in English.",
                "explanation_id": "Gunakan 的 untuk menunjukkan kepemilikan.",
                "examples": [
                    {"chinese": "我的书", "pinyin": "wǒ de shū", "meaning_en": "my book", "meaning_id": "buku saya"},
                    {"chinese": "老师的笔", "pinyin": "lǎoshī de bǐ", "meaning_en": "teacher's pen", "meaning_id": "pulpen guru"},
                ],
                "exercise": "Show possession using 的",
                "exercise_id": "Tunjukkan kepemilikan dengan 的"
            }
        ],
        "dialogue": {
            "title": "Introducing Someone",
            "title_id": "Memperkenalkan Seseorang",
            "conversation": [
                {"speaker": "A", "chinese": "她是谁？", "pinyin": "Tā shì shéi?", "meaning_en": "Who is she?", "meaning_id": "Dia siapa?"},
                {"speaker": "B", "chinese": "她是我的汉语老师。", "pinyin": "Tā shì wǒ de Hànyǔ lǎoshī.", "meaning_en": "She is my Chinese teacher.", "meaning_id": "Dia guru Mandarin saya."},
                {"speaker": "A", "chinese": "她是从哪国来的？", "pinyin": "Tā shì cóng nǎ guó lái de?", "meaning_en": "Which country is she from?", "meaning_id": "Dari negara mana dia?"},
                {"speaker": "B", "chinese": "她是从中国来的。", "pinyin": "Tā shì cóng Zhōngguó lái de.", "meaning_en": "She is from China.", "meaning_id": "Dia dari China."}
            ]
        }
    },
    5: {
        "number": 5,
        "title": "她女儿今年二十岁",
        "title_en": "Her Daughter is 20 Years Old",
        "title_id": "Putrinya Berusia 20 Tahun",
        "objectives": [
            "Talk about age and numbers",
            "Use numbers 1-100",
            "Ask 'how old'"
        ],
        "vocabulary": [
            {"word": "一", "pinyin": "yī", "meaning_en": "one", "meaning_id": "satu", "example": "一个人", "tone": 1},
            {"word": "二", "pinyin": "èr", "meaning_en": "two", "meaning_id": "dua", "example": "两个人", "tone": 4},
            {"word": "三", "pinyin": "sān", "meaning_en": "three", "meaning_id": "tiga", "example": "三个人", "tone": 1},
            {"word": "四", "pinyin": "sì", "meaning_en": "four", "meaning_id": "empat", "example": "四个人", "tone": 4},
            {"word": "五", "pinyin": "wǔ", "meaning_en": "five", "meaning_id": "lima", "example": "五本书", "tone": 3},
            {"word": "六", "pinyin": "liù", "meaning_en": "six", "meaning_id": "enam", "example": "六个人", "tone": 4},
            {"word": "七", "pinyin": "qī", "meaning_en": "seven", "meaning_id": "tujuh", "example": "七天", "tone": 1},
            {"word": "八", "pinyin": "bā", "meaning_en": "eight", "meaning_id": "delapan", "example": "八块钱", "tone": 1},
            {"word": "九", "pinyin": "jiǔ", "meaning_en": "nine", "meaning_id": "sembilan", "example": "九点", "tone": 3},
            {"word": "十", "pinyin": "shí", "meaning_en": "ten", "meaning_id": "sepuluh", "example": "十个人", "tone": 2},
            {"word": "百", "pinyin": "bǎi", "meaning_en": "hundred", "meaning_id": "ratus", "example": "一百", "tone": 3},
            {"word": "岁", "pinyin": "suì", "meaning_en": "years old", "meaning_id": "tahun (usia)", "example": "二十岁", "tone": 4},
            {"word": "今年", "pinyin": "jīn nián", "meaning_en": "this year", "meaning_id": "tahun ini", "example": "今年二十岁", "tone": "1,2"},
            {"word": "女儿", "pinyin": "nǚ ér", "meaning_en": "daughter", "meaning_id": "putri", "example": "她的女儿", "tone": "3,2"},
            {"word": "儿子", "pinyin": "ér zi", "meaning_en": "son", "meaning_id": "putra", "example": "他的儿子", "tone": "2,0"},
        ],
        "grammar": [
            {
                "point": "Numbers 1-100",
                "explanation_en": "Numbers are formed by combining digits 1-10. 11 is 十一 (10+1), 20 is 二十 (2×10).",
                "explanation_id": "Angka dibentuk dengan menggabungkan digit 1-10. 11 adalah 十一 (10+1), 20 adalah 二十 (2×10).",
                "examples": [
                    {"chinese": "十一", "pinyin": "shí yī", "meaning_en": "eleven", "meaning_id": "sebelas"},
                    {"chinese": "二十", "pinyin": "èr shí", "meaning_en": "twenty", "meaning_id": "dua puluh"},
                    {"chinese": "九十九", "pinyin": "jiǔ shí jiǔ", "meaning_en": "ninety-nine", "meaning_id": "sembilan puluh sembilan"},
                ],
                "exercise": "Write the numbers: 15, 27, 43, 58, 100",
                "exercise_id": "Tulis angka: 15, 27, 43, 58, 100"
            }
        ],
        "dialogue": {
            "title": "Asking About Age",
            "title_id": "Bertanya Tentang Usia",
            "conversation": [
                {"speaker": "A", "chinese": "你女儿今年多大？", "pinyin": "Nǐ nǚ'ér jīnnián duō dà?", "meaning_en": "How old is your daughter?", "meaning_id": "Berapa usia putrimu?"},
                {"speaker": "B", "chinese": "她今年二十岁。", "pinyin": "Tā jīnnián èrshí suì.", "meaning_en": "She is twenty years old this year.", "meaning_id": "Dua puluh tahun tahun ini."},
                {"speaker": "A", "chinese": "她上大学了吗？", "pinyin": "Tā shàng dàxué le ma?", "meaning_en": "Does she go to university?", "meaning_id": "Apakah dia kuliah?"},
                {"speaker": "B", "chinese": "是的，她上大学了。", "pinyin": "Shì de, tā shàng dàxué le.", "meaning_en": "Yes, she goes to university.", "meaning_id": "Ya, dia kuliah."}
            ]
        }
    },
    6: {
        "number": 6,
        "title": "我会说汉语",
        "title_en": "I Can Speak Chinese",
        "title_id": "Saya Bisa Berbahasa Mandarin",
        "objectives": [
            "Talk about abilities",
            "Use the modal verb 会 (can)",
            "Discuss language skills"
        ],
        "vocabulary": [
            {"word": "会", "pinyin": "huì", "meaning_en": "can, be able to", "meaning_id": "bisa", "example": "我会说汉语", "tone": 4},
            {"word": "说", "pinyin": "shuō", "meaning_en": "to speak", "meaning_id": "berbicara", "example": "说话", "tone": 1},
            {"word": "汉语", "pinyin": "Hàn yǔ", "meaning_en": "Chinese language", "meaning_id": "bahasa Mandarin", "example": "学汉语", "tone": "4,3"},
            {"word": "英语", "pinyin": "Yīng yǔ", "meaning_en": "English", "meaning_id": "bahasa Inggris", "example": "说英语", "tone": "1,3"},
            {"word": "日语", "pinyin": "Rì yǔ", "meaning_en": "Japanese", "meaning_id": "bahasa Jepang", "example": "日语", "tone": "4,3"},
            {"word": "法语", "pinyin": "Fǎ yǔ", "meaning_en": "French", "meaning_id": "bahasa Prancis", "example": "法语", "tone": "3,3"},
            {"word": "德语", "pinyin": "Dé yǔ", "meaning_en": "German", "meaning_id": "bahasa Jerman", "example": "德语", "tone": "2,3"},
            {"word": "一点", "pinyin": "yī diǎn", "meaning_en": "a little", "meaning_id": "sedikit", "example": "会一点", "tone": "1,3"},
            {"word": "但是", "pinyin": "dàn shì", "meaning_en": "but", "meaning_id": "tetapi", "example": "但是不会", "tone": "4,4"},
        ],
        "grammar": [
            {
                "point": "Modal Verb 会 (huì)",
                "explanation_en": "Use 会 to express ability learned through study or practice.",
                "explanation_id": "Gunakan 会 untuk menyatakan kemampuan yang dipelajari.",
                "examples": [
                    {"chinese": "我会说汉语", "pinyin": "wǒ huì shuō Hànyǔ", "meaning_en": "I can speak Chinese", "meaning_id": "Saya bisa berbahasa Mandarin"},
                    {"chinese": "他不会开车", "pinyin": "tā bù huì kāichē", "meaning_en": "He can't drive", "meaning_id": "Dia tidak bisa menyetir"},
                ],
                "exercise": "Talk about languages you can speak",
                "exercise_id": "Bicara tentang bahasa yang bisa kamu ucapkan"
            }
        ],
        "dialogue": {
            "title": "Discussing Language Abilities",
            "title_id": "Mendiskusikan Kemampuan Bahasa",
            "conversation": [
                {"speaker": "A", "chinese": "你会说汉语吗？", "pinyin": "Nǐ huì shuō Hànyǔ ma?", "meaning_en": "Can you speak Chinese?", "meaning_id": "Apakah kamu bisa berbahasa Mandarin?"},
                {"speaker": "B", "chinese": "我会说一点，但是说得不好。", "pinyin": "Wǒ huì shuō yīdiǎn, dànshì shuō de bù hǎo.", "meaning_en": "I can speak a little, but not well.", "meaning_id": "Saya bisa sedikit, tapi tidak baik."},
                {"speaker": "A", "chinese": "没关系，多练习就会好。", "pinyin": "Méiguānxi, duō liànxí jiù huì hǎo.", "meaning_en": "It's okay, more practice will make it better.", "meaning_id": "Tidak apa-apa, lebih banyak latihan akan membuat lebih baik."}
            ]
        }
    },
    7: {
        "number": 7,
        "title": "今天几号",
        "title_en": "What's the Date Today",
        "title_id": "Tanggal Berapa Hari Ini",
        "objectives": [
            "Ask and tell the date",
            "Use days of the week",
            "Talk about schedules"
        ],
        "vocabulary": [
            {"word": "今天", "pinyin": "jīn tiān", "meaning_en": "today", "meaning_id": "hari ini", "example": "今天星期几", "tone": "1,1"},
            {"word": "明天", "pinyin": "míng tiān", "meaning_en": "tomorrow", "meaning_id": "besok", "example": "明天见", "tone": "2,1"},
            {"word": "昨天", "pinyin": "zuó tiān", "meaning_en": "yesterday", "meaning_id": "kemarin", "example": "昨天去了", "tone": "2,1"},
            {"word": "星期", "pinyin": "xīng qī", "meaning_en": "week", "meaning_id": "minggu", "example": "星期一", "tone": "1,1"},
            {"word": "星期一", "pinyin": "xīng qī yī", "meaning_en": "Monday", "meaning_id": "Senin", "example": "星期一", "tone": "1,1,1"},
            {"word": "星期二", "pinyin": "xīng qī èr", "meaning_en": "Tuesday", "meaning_id": "Selasa", "example": "星期二", "tone": "1,1,4"},
            {"word": "星期三", "pinyin": "xīng qī sān", "meaning_en": "Wednesday", "meaning_id": "Rabu", "example": "星期三", "tone": "1,1,1"},
            {"word": "星期四", "pinyin": "xīng qī sì", "meaning_en": "Thursday", "meaning_id": "Kamis", "example": "星期四", "tone": "1,1,4"},
            {"word": "星期五", "pinyin": "xīng qī wǔ", "meaning_en": "Friday", "meaning_id": "Jumat", "example": "星期五", "tone": "1,1,3"},
            {"word": "星期六", "pinyin": "xīng qī liù", "meaning_en": "Saturday", "meaning_id": "Sabtu", "example": "星期六", "tone": "1,1,4"},
            {"word": "星期日", "pinyin": "xīng qī rì", "meaning_en": "Sunday", "meaning_id": "Minggu", "example": "星期日", "tone": "1,1,4"},
            {"word": "号", "pinyin": "hào", "meaning_en": "date (of month)", "meaning_id": "tanggal", "example": "几号", "tone": 4},
            {"word": "月", "pinyin": "yuè", "meaning_en": "month", "meaning_id": "bulan", "example": "一月", "tone": 4},
            {"word": "年", "pinyin": "nián", "meaning_en": "year", "meaning_id": "tahun", "example": "今年", "tone": 2},
        ],
        "grammar": [
            {
                "point": "Dates and Time Expressions",
                "explanation_en": "Date order: Year → Month → Day. Weekday: 星期 + number.",
                "explanation_id": "Urutan tanggal: Tahun → Bulan → Tanggal. Hari: 星期 + angka.",
                "examples": [
                    {"chinese": "今天是2024年5月15日", "pinyin": "jīntiān shì 2024 nián 5 yuè 15 rì", "meaning_en": "Today is May 15, 2024", "meaning_id": "Hari ini tanggal 15 Mei 2024"},
                    {"chinese": "今天是星期三", "pinyin": "jīntiān shì xīngqī sān", "meaning_en": "Today is Wednesday", "meaning_id": "Hari ini Rabu"},
                ],
                "exercise": "What day is today? What is tomorrow's date?",
                "exercise_id": "Hari ini hari apa? Tanggal berapa besok?"
            }
        ],
        "dialogue": {
            "title": "Talking About Dates",
            "title_id": "Membicarakan Tanggal",
            "conversation": [
                {"speaker": "A", "chinese": "今天几月几号？", "pinyin": "Jīntiān jǐ yuè jǐ hào?", "meaning_en": "What's the date today?", "meaning_id": "Tanggal berapa hari ini?"},
                {"speaker": "B", "chinese": "今天五月十五号。", "pinyin": "Jīntiān wǔ yuè shíwǔ hào.", "meaning_en": "Today is May 15th.", "meaning_id": "Hari ini tanggal 15 Mei."},
                {"speaker": "A", "chinese": "今天星期几？", "pinyin": "Jīntiān xīngqī jǐ?", "meaning_en": "What day is today?", "meaning_id": "Hari ini hari apa?"},
                {"speaker": "B", "chinese": "今天是星期三。", "pinyin": "Jīntiān shì xīngqī sān.", "meaning_en": "Today is Wednesday.", "meaning_id": "Hari ini Rabu."}
            ]
        }
    },
    8: {
        "number": 8,
        "title": "我想喝茶",
        "title_en": "I Want to Drink Tea",
        "title_id": "Saya Ingin Minum Teh",
        "objectives": [
            "Express wants and desires",
            "Use the verb 想 (want)",
            "Order food and drinks"
        ],
        "vocabulary": [
            {"word": "想", "pinyin": "xiǎng", "meaning_en": "to want, would like", "meaning_id": "ingin", "example": "我想喝茶", "tone": 3},
            {"word": "要", "pinyin": "yào", "meaning_en": "to want, will", "meaning_id": "mau", "example": "我要这个", "tone": 4},
            {"word": "喝茶", "pinyin": "hē chá", "meaning_en": "to drink tea", "meaning_id": "minum teh", "example": "喝茶", "tone": "1,2"},
            {"word": "喝水", "pinyin": "hē shuǐ", "meaning_en": "to drink water", "meaning_id": "minum air", "example": "喝水", "tone": "1,3"},
            {"word": "喝咖啡", "pinyin": "hē kā fēi", "meaning_en": "to drink coffee", "meaning_id": "minum kopi", "example": "喝咖啡", "tone": "1,1,1"},
            {"word": "吃饭", "pinyin": "chī fàn", "meaning_en": "to eat", "meaning_id": "makan", "example": "吃饭", "tone": "1,4"},
            {"word": "吃面条", "pinyin": "chī miàn tiáo", "meaning_en": "to eat noodles", "meaning_id": "makan mie", "example": "吃面条", "tone": "1,4,2"},
            {"word": "吃米饭", "pinyin": "chī mǐ fàn", "meaning_en": "to eat rice", "meaning_id": "makan nasi", "example": "吃米饭", "tone": "1,3,4"},
            {"word": "水果", "pinyin": "shuǐ guǒ", "meaning_en": "fruit", "meaning_id": "buah", "example": "吃水果", "tone": "3,3"},
            {"word": "苹果", "pinyin": "píng guǒ", "meaning_en": "apple", "meaning_id": "apel", "example": "一个苹果", "tone": "2,3"},
        ],
        "grammar": [
            {
                "point": "Modal Verb 想 (xiǎng)",
                "explanation_en": "Use 想 to express a wish or desire to do something.",
                "explanation_id": "Gunakan 想 untuk menyatakan keinginan melakukan sesuatu.",
                "examples": [
                    {"chinese": "我想喝茶", "pinyin": "wǒ xiǎng hē chá", "meaning_en": "I want to drink tea", "meaning_id": "Saya ingin minum teh"},
                    {"chinese": "你想吃什么", "pinyin": "nǐ xiǎng chī shénme", "meaning_en": "What would you like to eat", "meaning_id": "Kamu ingin makan apa"},
                ],
                "exercise": "Order food using 想",
                "exercise_id": "Pesan makanan menggunakan 想"
            }
        ],
        "dialogue": {
            "title": "Ordering at a Cafe",
            "title_id": "Memesan di Kafe",
            "conversation": [
                {"speaker": "服务员", "chinese": "您想喝什么？", "pinyin": "Nín xiǎng hē shénme?", "meaning_en": "What would you like to drink?", "meaning_id": "Anda ingin minum apa?"},
                {"speaker": "客人", "chinese": "我想喝茶。", "pinyin": "Wǒ xiǎng hē chá.", "meaning_en": "I would like tea.", "meaning_id": "Saya ingin minum teh."},
                {"speaker": "服务员", "chinese": "您想吃什么？", "pinyin": "Nín xiǎng chī shénme?", "meaning_en": "What would you like to eat?", "meaning_id": "Anda ingin makan apa?"},
                {"speaker": "客人", "chinese": "我想吃面条。", "pinyin": "Wǒ xiǎng chī miàntiáo.", "meaning_en": "I would like noodles.", "meaning_id": "Saya ingin makan mie."}
            ]
        }
    },
    9: {
        "number": 9,
        "title": "你儿子在哪儿工作",
        "title_en": "Where Does Your Son Work",
        "title_id": "Di Mana Putramu Bekerja",
        "objectives": [
            "Ask and tell location",
            "Use 在 (zài) for location",
            "Talk about workplaces"
        ],
        "vocabulary": [
            {"word": "在", "pinyin": "zài", "meaning_en": "to be at, in, on", "meaning_id": "di", "example": "在北京", "tone": 4},
            {"word": "哪儿", "pinyin": "nǎr", "meaning_en": "where", "meaning_id": "di mana", "example": "在哪儿", "tone": 3},
            {"word": "这里", "pinyin": "zhè lǐ", "meaning_en": "here", "meaning_id": "di sini", "example": "在这里", "tone": "4,3"},
            {"word": "那里", "pinyin": "nà lǐ", "meaning_en": "there", "meaning_id": "di sana", "example": "在那里", "tone": "4,3"},
            {"word": "工作", "pinyin": "gōng zuò", "meaning_en": "to work, job", "meaning_id": "bekerja", "example": "在银行工作", "tone": "1,4"},
            {"word": "银行", "pinyin": "yín háng", "meaning_en": "bank", "meaning_id": "bank", "example": "去银行", "tone": "2,2"},
            {"word": "公司", "pinyin": "gōng sī", "meaning_en": "company", "meaning_id": "perusahaan", "example": "在公司", "tone": "1,1"},
            {"word": "学校", "pinyin": "xué xiào", "meaning_en": "school", "meaning_id": "sekolah", "example": "在学校", "tone": "2,4"},
            {"word": "医院", "pinyin": "yī yuàn", "meaning_en": "hospital", "meaning_id": "rumah sakit", "example": "在医院", "tone": "1,4"},
            {"word": "商店", "pinyin": "shāng diàn", "meaning_en": "store", "meaning_id": "toko", "example": "在商店", "tone": "1,4"},
            {"word": "家", "pinyin": "jiā", "meaning_en": "home", "meaning_id": "rumah", "example": "在家", "tone": 1},
            {"word": "左边", "pinyin": "zuǒ biān", "meaning_en": "left side", "meaning_id": "sisi kiri", "example": "在左边", "tone": "3,1"},
            {"word": "右边", "pinyin": "yòu biān", "meaning_en": "right side", "meaning_id": "sisi kanan", "example": "在右边", "tone": "4,1"},
        ],
        "grammar": [
            {
                "point": "Location with 在 (zài)",
                "explanation_en": "Use 在 to indicate where someone or something is located.",
                "explanation_id": "Gunakan 在 untuk menunjukkan lokasi seseorang atau sesuatu.",
                "examples": [
                    {"chinese": "我在北京", "pinyin": "wǒ zài Běijīng", "meaning_en": "I am in Beijing", "meaning_id": "Saya di Beijing"},
                    {"chinese": "书在桌子上", "pinyin": "shū zài zhuōzi shàng", "meaning_en": "The book is on the table", "meaning_id": "Buku di atas meja"},
                ],
                "exercise": "Describe where things are using 在",
                "exercise_id": "Deskripsikan di mana benda berada menggunakan 在"
            }
        ],
        "dialogue": {
            "title": "Talking About Work",
            "title_id": "Membicarakan Pekerjaan",
            "conversation": [
                {"speaker": "A", "chinese": "你儿子在哪儿工作？", "pinyin": "Nǐ érzi zài nǎr gōngzuò?", "meaning_en": "Where does your son work?", "meaning_id": "Di mana putramu bekerja?"},
                {"speaker": "B", "chinese": "他在银行工作。", "pinyin": "Tā zài yínháng gōngzuò.", "meaning_en": "He works at a bank.", "meaning_id": "Dia bekerja di bank."},
                {"speaker": "A", "chinese": "银行在哪儿？", "pinyin": "Yínháng zài nǎr?", "meaning_en": "Where is the bank?", "meaning_id": "Di mana banknya?"},
                {"speaker": "B", "chinese": "银行在学校左边。", "pinyin": "Yínháng zài xuéxiào zuǒbiān.", "meaning_en": "The bank is to the left of the school.", "meaning_id": "Bank di sebelah kiri sekolah."}
            ]
        }
    },
    10: {
        "number": 10,
        "title": "我能坐这儿吗",
        "title_en": "Can I Sit Here",
        "title_id": "Bisakah Saya Duduk di Sini",
        "objectives": [
            "Ask for permission",
            "Use 能 (néng) for permission",
            "Use measure words"
        ],
        "vocabulary": [
            {"word": "能", "pinyin": "néng", "meaning_en": "can, may", "meaning_id": "bisa", "example": "能去吗", "tone": 2},
            {"word": "可以", "pinyin": "kě yǐ", "meaning_en": "may, can", "meaning_id": "boleh", "example": "可以进来吗", "tone": "3,3"},
            {"word": "坐", "pinyin": "zuò", "meaning_en": "to sit", "meaning_id": "duduk", "example": "请坐", "tone": 4},
            {"word": "站", "pinyin": "zhàn", "meaning_en": "to stand", "meaning_id": "berdiri", "example": "站起来", "tone": 4},
            {"word": "来", "pinyin": "lái", "meaning_en": "to come", "meaning_id": "datang", "example": "来这儿", "tone": 2},
            {"word": "去", "pinyin": "qù", "meaning_en": "to go", "meaning_id": "pergi", "example": "去那儿", "tone": 4},
            {"word": "进", "pinyin": "jìn", "meaning_en": "to enter", "meaning_id": "masuk", "example": "请进", "tone": 4},
            {"word": "出", "pinyin": "chū", "meaning_en": "to exit", "meaning_id": "keluar", "example": "出去", "tone": 1},
            {"word": "开门", "pinyin": "kāi mén", "meaning_en": "to open the door", "meaning_id": "buka pintu", "example": "开门", "tone": "1,2"},
            {"word": "关门", "pinyin": "guān mén", "meaning_en": "to close the door", "meaning_id": "tutup pintu", "example": "关门", "tone": "1,2"},
            {"word": "个", "pinyin": "gè", "meaning_en": "general measure word", "meaning_id": "kata bilangan umum", "example": "一个人", "tone": 4},
            {"word": "本", "pinyin": "běn", "meaning_en": "measure word for books", "meaning_id": "untuk buku", "example": "一本书", "tone": 3},
            {"word": "张", "pinyin": "zhāng", "meaning_en": "measure word for flat objects", "meaning_id": "untuk benda datar", "example": "一张纸", "tone": 1},
            {"word": "杯", "pinyin": "bēi", "meaning_en": "measure word for cups", "meaning_id": "untuk cangkir", "example": "一杯茶", "tone": 1},
        ],
        "grammar": [
            {
                "point": "Permission with 能 (néng) and 可以 (kěyǐ)",
                "explanation_en": "Use 能 or 可以 to ask for or give permission.",
                "explanation_id": "Gunakan 能 atau 可以 untuk meminta atau memberi izin.",
                "examples": [
                    {"chinese": "我能进来吗", "pinyin": "wǒ néng jìnlái ma", "meaning_en": "May I come in", "meaning_id": "Bolehkah saya masuk"},
                    {"chinese": "可以坐这儿吗", "pinyin": "kěyǐ zuò zhèr ma", "meaning_en": "May I sit here", "meaning_id": "Bolehkah duduk di sini"},
                ],
                "exercise": "Ask for permission to do things",
                "exercise_id": "Minta izin untuk melakukan sesuatu"
            }
        ],
        "dialogue": {
            "title": "Asking for Permission",
            "title_id": "Meminta Izin",
            "conversation": [
                {"speaker": "A", "chinese": "请问，我能坐这儿吗？", "pinyin": "Qǐngwèn, wǒ néng zuò zhèr ma?", "meaning_en": "Excuse me, may I sit here?", "meaning_id": "Permisi, bolehkah saya duduk di sini?"},
                {"speaker": "B", "chinese": "可以，请坐。", "pinyin": "Kěyǐ, qǐng zuò.", "meaning_en": "Yes, please sit.", "meaning_id": "Boleh, silakan duduk."},
                {"speaker": "A", "chinese": "谢谢！", "pinyin": "Xièxie!", "meaning_en": "Thank you!", "meaning_id": "Terima kasih!"}
            ]
        }
    },
    11: {
        "number": 11,
        "title": "现在几点",
        "title_en": "What Time Is It Now",
        "title_id": "Sekarang Jam Berapa",
        "objectives": [
            "Tell time",
            "Ask for the time",
            "Talk about daily schedules"
        ],
        "vocabulary": [
            {"word": "点", "pinyin": "diǎn", "meaning_en": "o'clock", "meaning_id": "jam", "example": "三点", "tone": 3},
            {"word": "半", "pinyin": "bàn", "meaning_en": "half", "meaning_id": "setengah", "example": "点半", "tone": 4},
            {"word": "分", "pinyin": "fēn", "meaning_en": "minute", "meaning_id": "menit", "example": "五分", "tone": 1},
            {"word": "刻", "pinyin": "kè", "meaning_en": "quarter", "meaning_id": "seperempat", "example": "一刻", "tone": 4},
            {"word": "早上", "pinyin": "zǎo shang", "meaning_en": "morning", "meaning_id": "pagi", "example": "早上好", "tone": "3,0"},
            {"word": "上午", "pinyin": "shàng wǔ", "meaning_en": "before noon", "meaning_id": "sebelum siang", "example": "上午十点", "tone": "4,3"},
            {"word": "中午", "pinyin": "zhōng wǔ", "meaning_en": "noon", "meaning_id": "siang", "example": "中午十二点", "tone": "1,3"},
            {"word": "下午", "pinyin": "xià wǔ", "meaning_en": "afternoon", "meaning_id": "sore", "example": "下午三点", "tone": "4,3"},
            {"word": "晚上", "pinyin": "wǎn shang", "meaning_en": "evening", "meaning_id": "malam", "example": "晚上好", "tone": "3,0"},
            {"word": "现在", "pinyin": "xiàn zài", "meaning_en": "now", "meaning_id": "sekarang", "example": "现在几点", "tone": "4,4"},
            {"word": "时间", "pinyin": "shí jiān", "meaning_en": "time", "meaning_id": "waktu", "example": "没有时间", "tone": "2,1"},
        ],
        "grammar": [
            {
                "point": "Telling Time",
                "explanation_en": "Time order: hour + 点 + minute + 分. Half past: 点 + 半.",
                "explanation_id": "Urutan waktu: jam + 点 + menit + 分. Setengah: 点 + 半.",
                "examples": [
                    {"chinese": "现在三点", "pinyin": "xiànzài sān diǎn", "meaning_en": "It's 3 o'clock", "meaning_id": "Sekarang jam 3"},
                    {"chinese": "现在三点半", "pinyin": "xiànzài sān diǎn bàn", "meaning_en": "It's 3:30", "meaning_id": "Sekarang jam setengah 4"},
                    {"chinese": "现在三点十五分", "pinyin": "xiànzài sān diǎn shíwǔ fēn", "meaning_en": "It's 3:15", "meaning_id": "Sekarang jam 3 lewat 15 menit"},
                ],
                "exercise": "What time is it now? Tell the time.",
                "exercise_id": "Sekarang jam berapa? Sebutkan waktunya."
            }
        ],
        "dialogue": {
            "title": "Asking the Time",
            "title_id": "Bertanya Waktu",
            "conversation": [
                {"speaker": "A", "chinese": "打扰一下，现在几点？", "pinyin": "Dǎrǎo yīxià, xiànzài jǐ diǎn?", "meaning_en": "Excuse me, what time is it now?", "meaning_id": "Permisi, sekarang jam berapa?"},
                {"speaker": "B", "chinese": "现在下午两点半。", "pinyin": "Xiànzài xiàwǔ liǎng diǎn bàn.", "meaning_en": "It's 2:30 in the afternoon.", "meaning_id": "Sekarang jam setengah 3 sore."},
                {"speaker": "A", "chinese": "谢谢！", "pinyin": "Xièxie!", "meaning_en": "Thank you!", "meaning_id": "Terima kasih!"}
            ]
        }
    },
    12: {
        "number": 12,
        "title": "明天天气怎么样",
        "title_en": "How's the Weather Tomorrow",
        "title_id": "Bagaimana Cuaca Besok",
        "objectives": [
            "Talk about weather",
            "Ask about the weather",
            "Describe temperature"
        ],
        "vocabulary": [
            {"word": "天气", "pinyin": "tiān qì", "meaning_en": "weather", "meaning_id": "cuaca", "example": "好天气", "tone": "1,4"},
            {"word": "怎么样", "pinyin": "zěn me yàng", "meaning_en": "how is", "meaning_id": "bagaimana", "example": "怎么样", "tone": "3,0,4"},
            {"word": "好", "pinyin": "hǎo", "meaning_en": "good", "meaning_id": "baik", "example": "很好", "tone": 3},
            {"word": "坏", "pinyin": "huài", "meaning_en": "bad", "meaning_id": "buruk", "example": "坏了", "tone": 4},
            {"word": "热", "pinyin": "rè", "meaning_en": "hot", "meaning_id": "panas", "example": "很热", "tone": 4},
            {"word": "冷", "pinyin": "lěng", "meaning_en": "cold", "meaning_id": "dingin", "example": "很冷", "tone": 3},
            {"word": "下雨", "pinyin": "xià yǔ", "meaning_en": "to rain", "meaning_id": "hujan", "example": "下雨了", "tone": "4,3"},
            {"word": "下雪", "pinyin": "xià xuě", "meaning_en": "to snow", "meaning_id": "salju", "example": "下雪了", "tone": "4,3"},
            {"word": "晴天", "pinyin": "qíng tiān", "meaning_en": "sunny", "meaning_id": "cerah", "example": "晴天", "tone": "2,1"},
            {"word": "阴天", "pinyin": "yīn tiān", "meaning_en": "cloudy", "meaning_id": "berawan", "example": "阴天", "tone": "1,1"},
            {"word": "刮风", "pinyin": "guā fēng", "meaning_en": "windy", "meaning_id": "berangin", "example": "刮风", "tone": "1,1"},
            {"word": "温度", "pinyin": "wēn dù", "meaning_en": "temperature", "meaning_id": "suhu", "example": "温度高", "tone": "1,4"},
            {"word": "度", "pinyin": "dù", "meaning_en": "degree", "meaning_id": "derajat", "example": "三十度", "tone": 4},
        ],
        "grammar": [
            {
                "point": "The Pattern 怎么样 (zěnme yàng)",
                "explanation_en": "Use 怎么样 to ask 'how is' something.",
                "explanation_id": "Gunakan 怎么样 untuk bertanya 'bagaimana' sesuatu.",
                "examples": [
                    {"chinese": "天气怎么样", "pinyin": "tiānqì zěnme yàng", "meaning_en": "How is the weather", "meaning_id": "Bagaimana cuacanya"},
                    {"chinese": "你最近怎么样", "pinyin": "nǐ zuìjìn zěnme yàng", "meaning_en": "How have you been lately", "meaning_id": "Bagaimana kabarmu akhir-akhir ini"},
                ],
                "exercise": "Ask about the weather using 怎么样",
                "exercise_id": "Tanya tentang cuaca menggunakan 怎么样"
            }
        ],
        "dialogue": {
            "title": "Talking About Weather",
            "title_id": "Membicarakan Cuaca",
            "conversation": [
                {"speaker": "A", "chinese": "明天天气怎么样？", "pinyin": "Míngtiān tiānqì zěnme yàng?", "meaning_en": "How's the weather tomorrow?", "meaning_id": "Bagaimana cuaca besok?"},
                {"speaker": "B", "chinese": "明天会下雨，温度二十度。", "pinyin": "Míngtiān huì xiàyǔ, wēndù èrshí dù.", "meaning_en": "It will rain tomorrow, temperature 20 degrees.", "meaning_id": "Besok akan hujan, suhu 20 derajat."},
                {"speaker": "A", "chinese": "要多穿点衣服。", "pinyin": "Yào duō chuān diǎn yīfu.", "meaning_en": "You should wear more clothes.", "meaning_id": "Kamu harus memakai lebih banyak baju."}
            ]
        }
    },
    13: {
        "number": 13,
        "title": "他在学做中国菜呢",
        "title_en": "He's Learning to Cook Chinese Food",
        "title_id": "Dia Sedang Belajar Masak Masakan China",
        "objectives": [
            "Express ongoing actions",
            "Use the progressive aspect 在",
            "Talk about cooking and food"
        ],
        "vocabulary": [
            {"word": "在", "pinyin": "zài", "meaning_en": "in progress (auxiliary)", "meaning_id": "sedang", "example": "在吃饭", "tone": 4},
            {"word": "呢", "pinyin": "ne", "meaning_en": "ongoing action particle", "meaning_id": "sedang", "example": "在吃饭呢", "tone": 0},
            {"word": "学", "pinyin": "xué", "meaning_en": "to learn", "meaning_id": "belajar", "example": "学汉语", "tone": 2},
            {"word": "做", "pinyin": "zuò", "meaning_en": "to do, to make", "meaning_id": "membuat", "example": "做饭", "tone": 4},
            {"word": "菜", "pinyin": "cài", "meaning_en": "dish, food", "meaning_id": "masakan", "example": "中国菜", "tone": 4},
            {"word": "中国菜", "pinyin": "Zhōng guó cài", "meaning_en": "Chinese food", "meaning_id": "masakan China", "example": "爱吃中国菜", "tone": "1,2,4"},
            {"word": "米饭", "pinyin": "mǐ fàn", "meaning_en": "rice", "meaning_id": "nasi", "example": "吃米饭", "tone": "3,4"},
            {"word": "面条", "pinyin": "miàn tiáo", "meaning_en": "noodles", "meaning_id": "mie", "example": "吃面条", "tone": "4,2"},
            {"word": "饺子", "pinyin": "jiǎo zi", "meaning_en": "dumplings", "meaning_id": "pangsit", "example": "包饺子", "tone": "3,0"},
            {"word": "汤", "pinyin": "tāng", "meaning_en": "soup", "meaning_id": "sup", "example": "喝汤", "tone": 1},
            {"word": "好吃", "pinyin": "hǎo chī", "meaning_en": "delicious", "meaning_id": "enak", "example": "很好吃", "tone": "3,1"},
            {"word": "难吃", "pinyin": "nán chī", "meaning_en": "not tasty", "meaning_id": "tidak enak", "example": "很难吃", "tone": "2,1"},
        ],
        "grammar": [
            {
                "point": "Progressive Aspect 在 (zài)",
                "explanation_en": "Use 在 before the verb to indicate an action in progress.",
                "explanation_id": "Gunakan 在 sebelum kata kerja untuk menunjukkan aksi sedang berlangsung.",
                "examples": [
                    {"chinese": "他在吃饭", "pinyin": "tā zài chī fàn", "meaning_en": "He is eating", "meaning_id": "Dia sedang makan"},
                    {"chinese": "我在学汉语", "pinyin": "wǒ zài xué Hànyǔ", "meaning_en": "I am studying Chinese", "meaning_id": "Saya sedang belajar Mandarin"},
                ],
                "exercise": "Describe what you are doing right now",
                "exercise_id": "Deskripsikan apa yang sedang kamu lakukan sekarang"
            }
        ],
        "dialogue": {
            "title": "Cooking Chinese Food",
            "title_id": "Memasak Masakan China",
            "conversation": [
                {"speaker": "A", "chinese": "他在做什么呢？", "pinyin": "Tā zài zuò shénme ne?", "meaning_en": "What is he doing?", "meaning_id": "Dia sedang melakukan apa?"},
                {"speaker": "B", "chinese": "他在学做中国菜呢。", "pinyin": "Tā zài xué zuò Zhōngguó cài ne.", "meaning_en": "He's learning to cook Chinese food.", "meaning_id": "Dia sedang belajar masak masakan China."},
                {"speaker": "A", "chinese": "做的是什么菜？", "pinyin": "Zuò de shì shénme cài?", "meaning_en": "What dish is he making?", "meaning_id": "Masakan apa yang dia buat?"},
                {"speaker": "B", "chinese": "他在做饺子。很好吃！", "pinyin": "Tā zài zuò jiǎozi. Hěn hǎochī!", "meaning_en": "He's making dumplings. Very delicious!", "meaning_id": "Dia sedang membuat pangsit. Sangat enak!"}
            ]
        }
    },
    14: {
        "number": 14,
        "title": "她买了不少衣服",
        "title_en": "She Bought Quite a Few Clothes",
        "title_id": "Dia Membeli Banyak Pakaian",
        "objectives": [
            "Talk about completed actions",
            "Use the particle 了 (le)",
            "Discuss shopping"
        ],
        "vocabulary": [
            {"word": "了", "pinyin": "le", "meaning_en": "completed action particle", "meaning_id": "telah", "example": "吃了", "tone": 0},
            {"word": "买", "pinyin": "mǎi", "meaning_en": "to buy", "meaning_id": "membeli", "example": "买东西", "tone": 3},
            {"word": "卖", "pinyin": "mài", "meaning_en": "to sell", "meaning_id": "menjual", "example": "卖东西", "tone": 4},
            {"word": "衣服", "pinyin": "yī fu", "meaning_en": "clothes", "meaning_id": "pakaian", "example": "买衣服", "tone": "1,0"},
            {"word": "裤子", "pinyin": "kù zi", "meaning_en": "pants", "meaning_id": "celana", "example": "一条裤子", "tone": "4,0"},
            {"word": "裙子", "pinyin": "qún zi", "meaning_en": "skirt", "meaning_id": "rok", "example": "一条裙子", "tone": "2,0"},
            {"word": "鞋子", "pinyin": "xié zi", "meaning_en": "shoes", "meaning_id": "sepatu", "example": "一双鞋子", "tone": "2,0"},
            {"word": "颜色", "pinyin": "yán sè", "meaning_en": "color", "meaning_id": "warna", "example": "什么颜色", "tone": "2,4"},
            {"word": "红色", "pinyin": "hóng sè", "meaning_en": "red", "meaning_id": "merah", "example": "红色衣服", "tone": "2,4"},
            {"word": "蓝色", "pinyin": "lán sè", "meaning_en": "blue", "meaning_id": "biru", "example": "蓝色", "tone": "2,4"},
            {"word": "白色", "pinyin": "bái sè", "meaning_en": "white", "meaning_id": "putih", "example": "白色", "tone": "2,4"},
            {"word": "黑色", "pinyin": "hēi sè", "meaning_en": "black", "meaning_id": "hitam", "example": "黑色", "tone": "1,4"},
            {"word": "钱", "pinyin": "qián", "meaning_en": "money", "meaning_id": "uang", "example": "多少钱", "tone": 2},
            {"word": "块", "pinyin": "kuài", "meaning_en": "unit of currency", "meaning_id": "yuan", "example": "十块钱", "tone": 4},
        ],
        "grammar": [
            {
                "point": "Completed Action with 了 (le)",
                "explanation_en": "Place 了 after the verb to indicate an action has been completed.",
                "explanation_id": "Letakkan 了 setelah kata kerja untuk menunjukkan aksi telah selesai.",
                "examples": [
                    {"chinese": "我吃了饭", "pinyin": "wǒ chī le fàn", "meaning_en": "I ate (the meal)", "meaning_id": "Saya sudah makan"},
                    {"chinese": "她买了衣服", "pinyin": "tā mǎi le yīfu", "meaning_en": "She bought clothes", "meaning_id": "Dia sudah membeli pakaian"},
                ],
                "exercise": "Describe what you did yesterday using 了",
                "exercise_id": "Deskripsikan apa yang kamu lakukan kemarin menggunakan 了"
            }
        ],
        "dialogue": {
            "title": "Shopping for Clothes",
            "title_id": "Berbelanja Pakaian",
            "conversation": [
                {"speaker": "A", "chinese": "你买了什么？", "pinyin": "Nǐ mǎi le shénme?", "meaning_en": "What did you buy?", "meaning_id": "Kamu membeli apa?"},
                {"speaker": "B", "chinese": "我买了一件红色衣服。", "pinyin": "Wǒ mǎi le yī jiàn hóngsè yīfu.", "meaning_en": "I bought a red dress.", "meaning_id": "Saya membeli baju merah."},
                {"speaker": "A", "chinese": "花了多少钱？", "pinyin": "Huā le duōshao qián?", "meaning_en": "How much did you spend?", "meaning_id": "Berapa banyak kamu menghabiskan uang?"},
                {"speaker": "B", "chinese": "花了一百块。", "pinyin": "Huā le yī bǎi kuài.", "meaning_en": "Spent 100 yuan.", "meaning_id": "Menghabiskan 100 yuan."}
            ]
        }
    },
    15: {
        "number": 15,
        "title": "我是坐飞机来的",
        "title_en": "I Came by Plane",
        "title_id": "Saya Datang dengan Pesawat",
        "objectives": [
            "Talk about means of transportation",
            "Use the 是...的 construction",
            "Describe past actions"
        ],
        "vocabulary": [
            {"word": "坐", "pinyin": "zuò", "meaning_en": "to travel by", "meaning_id": "naik", "example": "坐车", "tone": 4},
            {"word": "飞机", "pinyin": "fēi jī", "meaning_en": "airplane", "meaning_id": "pesawat", "example": "坐飞机", "tone": "1,1"},
            {"word": "火车", "pinyin": "huǒ chē", "meaning_en": "train", "meaning_id": "kereta api", "example": "坐火车", "tone": "3,1"},
            {"word": "汽车", "pinyin": "qì chē", "meaning_en": "car", "meaning_id": "mobil", "example": "开车", "tone": "4,1"},
            {"word": "出租车", "pinyin": "chū zū chē", "meaning_en": "taxi", "meaning_id": "taksi", "example": "打出租车", "tone": "1,1,1"},
            {"word": "自行车", "pinyin": "zì xíng chē", "meaning_en": "bicycle", "meaning_id": "sepeda", "example": "骑自行车", "tone": "4,2,1"},
            {"word": "地铁", "pinyin": "dì tiě", "meaning_en": "subway", "meaning_id": "kereta bawah tanah", "example": "坐地铁", "tone": "4,3"},
            {"word": "走路", "pinyin": "zǒu lù", "meaning_en": "to walk", "meaning_id": "berjalan", "example": "走路去", "tone": "3,4"},
            {"word": "怎么", "pinyin": "zěn me", "meaning_en": "how", "meaning_id": "bagaimana", "example": "怎么去", "tone": "3,0"},
            {"word": "为什么", "pinyin": "wèi shén me", "meaning_en": "why", "meaning_id": "mengapa", "example": "为什么", "tone": "4,2,0"},
            {"word": "因为", "pinyin": "yīn wèi", "meaning_en": "because", "meaning_id": "karena", "example": "因为", "tone": "1,4"},
        ],
        "grammar": [
            {
                "point": "The 是...的 (shì...de) Construction",
                "explanation_en": "Use 是...的 to emphasize details about a past event.",
                "explanation_id": "Gunakan 是...的 untuk menekankan detail tentang kejadian masa lalu.",
                "examples": [
                    {"chinese": "我是坐飞机来的", "pinyin": "wǒ shì zuò fēijī lái de", "meaning_en": "I came by plane", "meaning_id": "Saya datang dengan pesawat"},
                    {"chinese": "他是在北京出生的", "pinyin": "tā shì zài Běijīng chūshēng de", "meaning_en": "He was born in Beijing", "meaning_id": "Dia lahir di Beijing"},
                ],
                "exercise": "How did you come here today? Answer using 是...的",
                "exercise_id": "Bagaimana kamu datang ke sini hari ini? Jawab menggunakan 是...的"
            }
        ],
        "dialogue": {
            "title": "Talking About Transportation",
            "title_id": "Membicarakan Transportasi",
            "conversation": [
                {"speaker": "A", "chinese": "你是怎么来的？", "pinyin": "Nǐ shì zěnme lái de?", "meaning_en": "How did you come?", "meaning_id": "Bagaimana kamu datang?"},
                {"speaker": "B", "chinese": "我是坐飞机来的。", "pinyin": "Wǒ shì zuò fēijī lái de.", "meaning_en": "I came by plane.", "meaning_id": "Saya datang dengan pesawat."},
                {"speaker": "A", "chinese": "为什么坐飞机？", "pinyin": "Wèishénme zuò fēijī?", "meaning_en": "Why by plane?", "meaning_id": "Mengapa dengan pesawat?"},
                {"speaker": "B", "chinese": "因为坐火车太慢了。", "pinyin": "Yīnwèi zuò huǒchē tài màn le.", "meaning_en": "Because the train is too slow.", "meaning_id": "Karena kereta terlalu lambat."}
            ]
        }
    }
}

# Helper functions
def get_lesson(level, lesson_num):
    """Get a specific lesson"""
    if level == 1 and 1 <= lesson_num <= 15:
        return HSK1_LESSONS.get(lesson_num)
    return None

def get_lesson_count(level=1):
    """Get total number of lessons for a level"""
    return len(HSK1_LESSONS)

def get_lesson_preview(level):
    """Get list of all lessons with titles"""
    return [{
        "number": data["number"],
        "title": data["title"],
        "title_en": data["title_en"],
        "vocab_count": len(data.get("vocabulary", []))
    } for data in HSK1_LESSONS.values()]