# generate_hsk2_full.py - Generate all HSK 2 lessons with complete unique content
import os
import json

# Complete HSK Level 2 Curriculum Data - Lessons 8-15
HSK2_COMPLETE_DATA = {
    1: {
        "title": "九月去中国旅游最好",
        "title_en": "September is Best to Travel to China",
        "vocabulary": [
            {"word": "旅游", "pinyin": "lǚ yóu", "meaning": "travel", "example": "去中国旅游", "example_translation": "Travel to China"},
            {"word": "最好", "pinyin": "zuì hǎo", "meaning": "best", "example": "九月最好", "example_translation": "September is best"},
            {"word": "季节", "pinyin": "jì jié", "meaning": "season", "example": "最好的季节", "example_translation": "The best season"},
            {"word": "天气", "pinyin": "tiān qì", "meaning": "weather", "example": "天气很好", "example_translation": "The weather is good"},
            {"word": "凉快", "pinyin": "liáng kuai", "meaning": "cool", "example": "天气凉快", "example_translation": "The weather is cool"},
            {"word": "合适", "pinyin": "hé shì", "meaning": "suitable", "example": "很合适", "example_translation": "Very suitable"},
            {"word": "风景", "pinyin": "fēng jǐng", "meaning": "scenery", "example": "美丽的风景", "example_translation": "Beautiful scenery"},
            {"word": "拍照", "pinyin": "pāi zhào", "meaning": "take photos", "example": "拍照留念", "example_translation": "Take photos as souvenirs"},
            {"word": "秋天", "pinyin": "qiū tiān", "meaning": "autumn", "example": "秋天很美", "example_translation": "Autumn is beautiful"},
            {"word": "舒服", "pinyin": "shū fu", "meaning": "comfortable", "example": "很舒服", "example_translation": "Very comfortable"},
            {"word": "热闹", "pinyin": "rè nao", "meaning": "lively", "example": "很热闹", "example_translation": "Very lively"},
            {"word": "景点", "pinyin": "jǐng diǎn", "meaning": "scenic spot", "example": "著名景点", "example_translation": "Famous scenic spots"}
        ],
        "grammar": [
            {
                "point": "Superlative 最 (zuì)",
                "explanation": "Use 最 before an adjective to mean 'the most' or 'the best'.",
                "examples": [
                    {"chinese": "九月去中国旅游最好", "translation": "September is the best time to travel to China"},
                    {"chinese": "我最喜欢秋天", "translation": "I like autumn the most"},
                    {"chinese": "这是最好的季节", "translation": "This is the best season"}
                ]
            },
            {
                "point": "Time Expressions with 的时候 (de shíhou)",
                "explanation": "Use 的时候 to mean 'when' or 'at the time of' an action.",
                "examples": [
                    {"chinese": "秋天的时候天气很好", "translation": "The weather is good in autumn"},
                    {"chinese": "旅游的时候要注意安全", "translation": "Be careful when traveling"},
                    {"chinese": "吃饭的时候不要说话", "translation": "Don't talk while eating"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "male", "name": "Zhang Wei", "voice": "male", "chinese": "你觉得什么时候去中国旅游最好？", "pinyin": "Nǐ juéde shénme shíhou qù Zhōngguó lǚyóu zuì hǎo?", "translation": "When do you think is the best time to travel to China?"},
            {"speaker": "female", "name": "Chen Mei", "voice": "female", "chinese": "我觉得秋天去最好，天气很舒服。", "pinyin": "Wǒ juéde qiūtiān qù zuì hǎo, tiānqì hěn shūfu.", "translation": "I think autumn is best, the weather is very comfortable."},
            {"speaker": "male", "name": "Zhang Wei", "voice": "male", "chinese": "九月还是十月？", "pinyin": "Jiǔ yuè háishì shí yuè?", "translation": "September or October?"},
            {"speaker": "female", "name": "Chen Mei", "voice": "female", "chinese": "九月最好，不冷不热。", "pinyin": "Jiǔ yuè zuì hǎo, bù lěng bù rè.", "translation": "September is best, neither cold nor hot."},
            {"speaker": "male", "name": "Zhang Wei", "voice": "male", "chinese": "太好了，我打算九月去北京。", "pinyin": "Tài hǎo le, wǒ dǎsuàn jiǔ yuè qù Běijīng.", "translation": "Great, I plan to go to Beijing in September."},
            {"speaker": "female", "name": "Chen Mei", "voice": "female", "chinese": "祝你玩得开心！记得多拍照片。", "pinyin": "Zhù nǐ wán dé kāixīn! Jìde duō pāi zhàopiàn.", "translation": "Wish you a great trip! Remember to take lots of photos."}
        ],
        "exercises": [
            {"question": "What does 旅游 mean?", "options": ["Travel", "Work", "Study", "Eat"], "correct": 0},
            {"question": "What is the pinyin for 风景?", "options": ["fēng jǐng", "fēng jìng", "fěn jǐng", "fèng jìng"], "correct": 0},
            {"question": "Complete: 天气很___ (The weather is cool)", "options": ["热", "冷", "凉快", "暖和"], "correct": 2},
            {"question": "What does 拍照 mean?", "options": ["Draw", "Write", "Take photos", "Read"], "correct": 2},
            {"question": "Choose the correct sentence using 最", "options": ["我最喜欢秋天", "我喜欢最秋天", "最我喜欢秋天", "我喜欢秋天最"], "correct": 0}
        ]
    },
    2: {
        "title": "我每天六点起床",
        "title_en": "I Get Up at 6 Every Day",
        "vocabulary": [
            {"word": "起床", "pinyin": "qǐ chuáng", "meaning": "get up", "example": "六点起床", "example_translation": "Get up at 6"},
            {"word": "每天", "pinyin": "měi tiān", "meaning": "every day", "example": "每天运动", "example_translation": "Exercise every day"},
            {"word": "早上", "pinyin": "zǎo shang", "meaning": "morning", "example": "早上好", "example_translation": "Good morning"},
            {"word": "刷牙", "pinyin": "shuā yá", "meaning": "brush teeth", "example": "刷牙洗脸", "example_translation": "Brush teeth and wash face"},
            {"word": "洗脸", "pinyin": "xǐ liǎn", "meaning": "wash face", "example": "洗脸后吃早饭", "example_translation": "Eat breakfast after washing face"},
            {"word": "吃早饭", "pinyin": "chī zǎo fàn", "meaning": "eat breakfast", "example": "七点吃早饭", "example_translation": "Eat breakfast at 7"},
            {"word": "上班", "pinyin": "shàng bān", "meaning": "go to work", "example": "八点上班", "example_translation": "Go to work at 8"},
            {"word": "下班", "pinyin": "xià bān", "meaning": "get off work", "example": "五点下班", "example_translation": "Get off work at 5"},
            {"word": "休息", "pinyin": "xiū xi", "meaning": "rest", "example": "休息一下", "example_translation": "Take a rest"},
            {"word": "睡觉", "pinyin": "shuì jiào", "meaning": "sleep", "example": "十点睡觉", "example_translation": "Sleep at 10"},
            {"word": "经常", "pinyin": "jīng cháng", "meaning": "often", "example": "经常运动", "example_translation": "Exercise often"},
            {"word": "有时候", "pinyin": "yǒu shí hou", "meaning": "sometimes", "example": "有时候很忙", "example_translation": "Sometimes very busy"}
        ],
        "grammar": [
            {
                "point": "Time Order (Time + Action)",
                "explanation": "In Chinese, time expressions come before the verb.",
                "examples": [
                    {"chinese": "我每天六点起床", "translation": "I get up at 6 every day"},
                    {"chinese": "他早上八点上班", "translation": "He goes to work at 8 in the morning"},
                    {"chinese": "我们晚上十点睡觉", "translation": "We sleep at 10 at night"}
                ]
            },
            {
                "point": "Frequency Adverbs",
                "explanation": "Place frequency adverbs before the verb to indicate how often an action occurs.",
                "examples": [
                    {"chinese": "我经常运动", "translation": "I often exercise"},
                    {"chinese": "他有时候迟到", "translation": "He is sometimes late"},
                    {"chinese": "她总是很忙", "translation": "She is always busy"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "male", "name": "Li Ming", "voice": "male", "chinese": "你每天几点起床？", "pinyin": "Nǐ měitiān jǐ diǎn qǐchuáng?", "translation": "What time do you get up every day?"},
            {"speaker": "female", "name": "Wang Fang", "voice": "female", "chinese": "我每天六点起床。你呢？", "pinyin": "Wǒ měitiān liù diǎn qǐchuáng. Nǐ ne?", "translation": "I get up at 6 every day. And you?"},
            {"speaker": "male", "name": "Li Ming", "voice": "male", "chinese": "我六点半起床。早上做什么？", "pinyin": "Wǒ liù diǎn bàn qǐchuáng. Zǎoshang zuò shénme?", "translation": "I get up at 6:30. What do you do in the morning?"},
            {"speaker": "female", "name": "Wang Fang", "voice": "female", "chinese": "我刷牙洗脸，然后吃早饭。", "pinyin": "Wǒ shuāyá xǐliǎn, ránhòu chī zǎofàn.", "translation": "I brush my teeth and wash my face, then eat breakfast."},
            {"speaker": "male", "name": "Li Ming", "voice": "male", "chinese": "你几点上班？", "pinyin": "Nǐ jǐ diǎn shàngbān?", "translation": "What time do you go to work?"},
            {"speaker": "female", "name": "Wang Fang", "voice": "female", "chinese": "八点上班。我经常走路去公司。", "pinyin": "Bā diǎn shàngbān. Wǒ jīngcháng zǒulù qù gōngsī.", "translation": "I go to work at 8. I often walk to the company."}
        ],
        "exercises": [
            {"question": "What does 起床 mean?", "options": ["Go to bed", "Get up", "Eat breakfast", "Go to work"], "correct": 1},
            {"question": "Complete: 我每天___点起床", "options": ["几", "什么", "六", "多少"], "correct": 2},
            {"question": "What is the pinyin for 睡觉?", "options": ["shuì jiào", "shuǐ jiǎo", "shuí jiào", "shuì jiǎo"], "correct": 0},
            {"question": "Choose the correct time order sentence", "options": ["我起床六点每天", "我每天六点起床", "六点起床我每天", "起床我六点每天"], "correct": 1}
        ]
    },
    3: {
        "title": "左边那个红色的是我的",
        "title_en": "The Red One on the Left is Mine",
        "vocabulary": [
            {"word": "左边", "pinyin": "zuǒ bian", "meaning": "left side", "example": "在左边", "example_translation": "On the left"},
            {"word": "右边", "pinyin": "yòu bian", "meaning": "right side", "example": "在右边", "example_translation": "On the right"},
            {"word": "红色", "pinyin": "hóng sè", "meaning": "red", "example": "红色的花", "example_translation": "Red flower"},
            {"word": "蓝色", "pinyin": "lán sè", "meaning": "blue", "example": "蓝色的天空", "example_translation": "Blue sky"},
            {"word": "白色", "pinyin": "bái sè", "meaning": "white", "example": "白色的雪", "example_translation": "White snow"},
            {"word": "黑色", "pinyin": "hēi sè", "meaning": "black", "example": "黑色的头发", "example_translation": "Black hair"},
            {"word": "颜色", "pinyin": "yán sè", "meaning": "color", "example": "什么颜色", "example_translation": "What color"},
            {"word": "我的", "pinyin": "wǒ de", "meaning": "mine", "example": "这是我的", "example_translation": "This is mine"},
            {"word": "你的", "pinyin": "nǐ de", "meaning": "yours", "example": "这是你的", "example_translation": "This is yours"},
            {"word": "他的", "pinyin": "tā de", "meaning": "his", "example": "这是他的", "example_translation": "This is his"},
            {"word": "她的", "pinyin": "tā de", "meaning": "hers", "example": "这是她的", "example_translation": "This is hers"},
            {"word": "我们的", "pinyin": "wǒ men de", "meaning": "ours", "example": "这是我们的", "example_translation": "This is ours"}
        ],
        "grammar": [
            {
                "point": "Possessive 的 (de)",
                "explanation": "Use 的 to show possession, like apostrophe-s in English.",
                "examples": [
                    {"chinese": "这是我的书", "translation": "This is my book"},
                    {"chinese": "左边那个红色的是我的", "translation": "The red one on the left is mine"},
                    {"chinese": "他的手机很新", "translation": "His phone is very new"}
                ]
            },
            {
                "point": "Position Words (左边, 右边, 中间)",
                "explanation": "Use position words to describe where something is located.",
                "examples": [
                    {"chinese": "书在桌子左边", "translation": "The book is on the left of the table"},
                    {"chinese": "银行在学校右边", "translation": "The bank is on the right of the school"},
                    {"chinese": "左边那个是我的", "translation": "The one on the left is mine"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "female", "name": "Liu Ying", "voice": "female", "chinese": "哪个是你的书包？", "pinyin": "Nǎge shì nǐ de shūbāo?", "translation": "Which one is your backpack?"},
            {"speaker": "male", "name": "Wang Tao", "voice": "male", "chinese": "左边那个红色的是我的。", "pinyin": "Zuǒbian nàge hóngsè de shì wǒ de.", "translation": "The red one on the left is mine."},
            {"speaker": "female", "name": "Liu Ying", "voice": "female", "chinese": "右边那个蓝色的是谁的呢？", "pinyin": "Yòubian nàge lánsè de shì shéi de ne?", "translation": "Whose is the blue one on the right?"},
            {"speaker": "male", "name": "Wang Tao", "voice": "male", "chinese": "那是小明的，是他的。", "pinyin": "Nà shì Xiǎo Míng de, shì tā de.", "translation": "That is Xiao Ming's, it's his."}
        ],
        "exercises": [
            {"question": "What does 左边 mean?", "options": ["Right side", "Left side", "Middle", "Front"], "correct": 1},
            {"question": "What color is 红色?", "options": ["Blue", "Green", "Red", "Yellow"], "correct": 2},
            {"question": "Complete: 左边___红色的是我的", "options": ["那个", "这个", "哪个", "这些"], "correct": 0},
            {"question": "Choose the correct possessive", "options": ["我书", "我的书", "我书的", "书我的"], "correct": 1}
        ]
    },
    4: {
        "title": "这个星期天我们去打球吧",
        "title_en": "Let's Play Ball This Sunday",
        "vocabulary": [
            {"word": "星期天", "pinyin": "xīng qī tiān", "meaning": "Sunday", "example": "星期天休息", "example_translation": "Rest on Sunday"},
            {"word": "打球", "pinyin": "dǎ qiú", "meaning": "play ball", "example": "去打篮球", "example_translation": "Go play basketball"},
            {"word": "足球", "pinyin": "zú qiú", "meaning": "soccer", "example": "踢足球", "example_translation": "Play soccer"},
            {"word": "篮球", "pinyin": "lán qiú", "meaning": "basketball", "example": "打篮球", "example_translation": "Play basketball"},
            {"word": "网球", "pinyin": "wǎng qiú", "meaning": "tennis", "example": "打网球", "example_translation": "Play tennis"},
            {"word": "运动", "pinyin": "yùn dòng", "meaning": "sports", "example": "做运动", "example_translation": "Do sports"},
            {"word": "一起", "pinyin": "yī qǐ", "meaning": "together", "example": "一起去", "example_translation": "Go together"},
            {"word": "有空", "pinyin": "yǒu kòng", "meaning": "free (time)", "example": "你有空吗", "example_translation": "Are you free?"},
            {"word": "邀请", "pinyin": "yāo qǐng", "meaning": "invite", "example": "邀请朋友", "example_translation": "Invite friends"},
            {"word": "参加", "pinyin": "cān jiā", "meaning": "participate", "example": "参加活动", "example_translation": "Join the activity"},
            {"word": "高兴", "pinyin": "gāo xìng", "meaning": "happy", "example": "很高兴", "example_translation": "Very happy"},
            {"word": "见面", "pinyin": "jiàn miàn", "meaning": "meet", "example": "见面聊天", "example_translation": "Meet and chat"}
        ],
        "grammar": [
            {
                "point": "Invitation with 吧 (ba)",
                "explanation": "Add 吧 at the end of a sentence to make a suggestion or invitation.",
                "examples": [
                    {"chinese": "我们一起去打球吧", "translation": "Let's go play ball together"},
                    {"chinese": "喝杯茶吧", "translation": "Let's have a cup of tea"},
                    {"chinese": "休息一下吧", "translation": "Let's take a rest"}
                ]
            },
            {
                "point": "Time Words (这个星期天, 下个星期)",
                "explanation": "Use 这个, 下个, 上个 to indicate specific times.",
                "examples": [
                    {"chinese": "这个星期天我们去打球", "translation": "We are playing ball this Sunday"},
                    {"chinese": "下个星期我去北京", "translation": "I'm going to Beijing next week"},
                    {"chinese": "上个星期我很忙", "translation": "I was busy last week"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "male", "name": "Chen Wei", "voice": "male", "chinese": "这个星期天你有空吗？", "pinyin": "Zhège xīngqītiān nǐ yǒu kòng ma?", "translation": "Are you free this Sunday?"},
            {"speaker": "female", "name": "Zhang Li", "voice": "female", "chinese": "有空啊，有什么事吗？", "pinyin": "Yǒu kòng a, yǒu shénme shì ma?", "translation": "Yes, I'm free. What's up?"},
            {"speaker": "male", "name": "Chen Wei", "voice": "male", "chinese": "我们去打球吧，怎么样？", "pinyin": "Wǒmen qù dǎqiú ba, zěnme yàng?", "translation": "Let's go play ball, how about it?"},
            {"speaker": "female", "name": "Zhang Li", "voice": "female", "chinese": "好啊！打什么球？", "pinyin": "Hǎo a! Dǎ shénme qiú?", "translation": "Great! What sport?"},
            {"speaker": "male", "name": "Chen Wei", "voice": "male", "chinese": "打篮球或者网球都可以。", "pinyin": "Dǎ lánqiú huòzhě wǎngqiú dōu kěyǐ.", "translation": "Basketball or tennis, both are fine."},
            {"speaker": "female", "name": "Zhang Li", "voice": "female", "chinese": "那我们就去打篮球吧！", "pinyin": "Nà wǒmen jiù qù dǎ lánqiú ba!", "translation": "Then let's go play basketball!"}
        ],
        "exercises": [
            {"question": "What does 星期天 mean?", "options": ["Monday", "Saturday", "Sunday", "Friday"], "correct": 2},
            {"question": "What does 打球 mean?", "options": ["Play ball", "Hit the ball", "Throw the ball", "Catch the ball"], "correct": 0},
            {"question": "Complete: 我们一起去___吧", "options": ["打球", "打球的", "打球了", "打球吗"], "correct": 0},
            {"question": "What is the pinyin for 邀请?", "options": ["yāo qǐng", "yào qǐng", "yāo qìng", "yào qìng"], "correct": 0}
        ]
    },
    5: {
        "title": "我比你高",
        "title_en": "I Am Taller Than You",
        "vocabulary": [
            {"word": "比", "pinyin": "bǐ", "meaning": "than (comparison)", "example": "我比你高", "example_translation": "I am taller than you"},
            {"word": "高", "pinyin": "gāo", "meaning": "tall", "example": "他很高", "example_translation": "He is very tall"},
            {"word": "矮", "pinyin": "ǎi", "meaning": "short", "example": "我不矮", "example_translation": "I am not short"},
            {"word": "胖", "pinyin": "pàng", "meaning": "fat", "example": "他很胖", "example_translation": "He is fat"},
            {"word": "瘦", "pinyin": "shòu", "meaning": "thin", "example": "她很瘦", "example_translation": "She is thin"},
            {"word": "大", "pinyin": "dà", "meaning": "big", "example": "房子很大", "example_translation": "The house is big"},
            {"word": "小", "pinyin": "xiǎo", "meaning": "small", "example": "狗很小", "example_translation": "The dog is small"},
            {"word": "快", "pinyin": "kuài", "meaning": "fast", "example": "火车很快", "example_translation": "The train is fast"},
            {"word": "慢", "pinyin": "màn", "meaning": "slow", "example": "乌龟很慢", "example_translation": "The turtle is slow"},
            {"word": "年轻", "pinyin": "nián qīng", "meaning": "young", "example": "她很年轻", "example_translation": "She is young"},
            {"word": "老", "pinyin": "lǎo", "meaning": "old", "example": "爷爷老了", "example_translation": "Grandpa is old"}
        ],
        "grammar": [
            {
                "point": "Comparisons with 比 (bǐ)",
                "explanation": "Use 比 to compare two things. A + 比 + B + Adjective",
                "examples": [
                    {"chinese": "我比你高", "translation": "I am taller than you"},
                    {"chinese": "今天比昨天冷", "translation": "Today is colder than yesterday"},
                    {"chinese": "火车比汽车快", "translation": "The train is faster than the car"},
                    {"chinese": "苹果比香蕉好吃", "translation": "Apples are more delicious than bananas"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "female", "name": "Li Na", "voice": "female", "chinese": "你多高？", "pinyin": "Nǐ duō gāo?", "translation": "How tall are you?"},
            {"speaker": "male", "name": "Wang Lei", "voice": "male", "chinese": "我一米八。你呢？", "pinyin": "Wǒ yī mǐ bā. Nǐ ne?", "translation": "I am 1.8 meters. And you?"},
            {"speaker": "female", "name": "Li Na", "voice": "female", "chinese": "我一米六五。你比我高很多。", "pinyin": "Wǒ yī mǐ liù wǔ. Nǐ bǐ wǒ gāo hěn duō.", "translation": "I am 1.65 meters. You are much taller than me."},
            {"speaker": "male", "name": "Wang Lei", "voice": "male", "chinese": "你比我瘦。", "pinyin": "Nǐ bǐ wǒ shòu.", "translation": "You are thinner than me."},
            {"speaker": "female", "name": "Li Na", "voice": "female", "chinese": "谢谢！你经常运动吗？", "pinyin": "Xièxie! Nǐ jīngcháng yùndòng ma?", "translation": "Thank you! Do you exercise often?"},
            {"speaker": "male", "name": "Wang Lei", "voice": "male", "chinese": "是的，我每天跑步。", "pinyin": "Shì de, wǒ měitiān pǎobù.", "translation": "Yes, I run every day."}
        ],
        "exercises": [
            {"question": "What does 比 mean?", "options": ["Compare", "Than", "Both A and B", "Like"], "correct": 1},
            {"question": "Complete: 我___你高", "options": ["比", "被", "把", "给"], "correct": 0},
            {"question": "What is the opposite of 高?", "options": ["大", "小", "矮", "长"], "correct": 2},
            {"question": "Choose the correct comparative sentence", "options": ["我高比你", "我比你高", "比我你高", "高我比你"], "correct": 1}
        ]
    },
    6: {
        "title": "你怎么不吃了",
        "title_en": "Why Aren't You Eating",
        "vocabulary": [
            {"word": "怎么", "pinyin": "zěn me", "meaning": "how come, why", "example": "你怎么不来", "example_translation": "Why aren't you coming"},
            {"word": "吃", "pinyin": "chī", "meaning": "eat", "example": "吃饭", "example_translation": "Eat a meal"},
            {"word": "饱", "pinyin": "bǎo", "meaning": "full", "example": "吃饱了", "example_translation": "Full from eating"},
            {"word": "饿", "pinyin": "è", "meaning": "hungry", "example": "我饿了", "example_translation": "I am hungry"},
            {"word": "好吃", "pinyin": "hǎo chī", "meaning": "delicious", "example": "很好吃", "example_translation": "Very delicious"},
            {"word": "难吃", "pinyin": "nán chī", "meaning": "not tasty", "example": "很难吃", "example_translation": "Very not tasty"},
            {"word": "喜欢", "pinyin": "xǐ huān", "meaning": "like", "example": "我喜欢吃", "example_translation": "I like to eat"},
            {"word": "不喜欢", "pinyin": "bù xǐ huān", "meaning": "dislike", "example": "我不喜欢", "example_translation": "I don't like"},
            {"word": "菜", "pinyin": "cài", "meaning": "dish", "example": "中国菜", "example_translation": "Chinese food"},
            {"word": "米饭", "pinyin": "mǐ fàn", "meaning": "rice", "example": "吃米饭", "example_translation": "Eat rice"}
        ],
        "grammar": [
            {
                "point": "Question Word 怎么 (zěnme)",
                "explanation": "Use 怎么 to ask 'why' or 'how come', often expressing surprise.",
                "examples": [
                    {"chinese": "你怎么不吃了", "translation": "Why aren't you eating"},
                    {"chinese": "你怎么来了", "translation": "How come you came"},
                    {"chinese": "你怎么知道", "translation": "How do you know"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "female", "name": "Mother", "voice": "female", "chinese": "你怎么不吃了？", "pinyin": "Nǐ zěnme bù chī le?", "translation": "Why aren't you eating?"},
            {"speaker": "male", "name": "Son", "voice": "male", "chinese": "我吃饱了。", "pinyin": "Wǒ chī bǎo le.", "translation": "I am full."},
            {"speaker": "female", "name": "Mother", "voice": "female", "chinese": "你才吃了一点。再吃一点儿吧。", "pinyin": "Nǐ cái chī le yī diǎn. Zài chī yī diǎnr ba.", "translation": "You only ate a little. Eat a bit more."},
            {"speaker": "male", "name": "Son", "voice": "male", "chinese": "这个菜不太好吃。", "pinyin": "Zhège cài bù tài hǎo chī.", "translation": "This dish is not very tasty."},
            {"speaker": "female", "name": "Mother", "voice": "female", "chinese": "你想吃什么？我给你做。", "pinyin": "Nǐ xiǎng chī shénme? Wǒ gěi nǐ zuò.", "translation": "What do you want to eat? I'll make it for you."},
            {"speaker": "male", "name": "Son", "voice": "male", "chinese": "我想吃面条。", "pinyin": "Wǒ xiǎng chī miàntiáo.", "translation": "I want to eat noodles."}
        ],
        "exercises": [
            {"question": "What does 怎么 mean in this context?", "options": ["How", "Why", "What", "Where"], "correct": 1},
            {"question": "Complete: 我吃饱了 means?", "options": ["I'm hungry", "I'm full", "I'm eating", "I'm cooking"], "correct": 1},
            {"question": "What is the opposite of 好吃?", "options": ["好吃", "难吃", "爱吃", "想吃"], "correct": 1},
            {"question": "Choose the correct response to '你怎么不吃了?'", "options": ["我吃饱了", "我饿了", "很好吃", "我喜欢"], "correct": 0}
        ]
    },
    7: {
        "title": "电脑比手机贵多了",
        "title_en": "The Computer is Much More Expensive than the Phone",
        "vocabulary": [
            {"word": "电脑", "pinyin": "diàn nǎo", "meaning": "computer", "example": "买电脑", "example_translation": "Buy a computer"},
            {"word": "手机", "pinyin": "shǒu jī", "meaning": "mobile phone", "example": "新手机", "example_translation": "New phone"},
            {"word": "贵", "pinyin": "guì", "meaning": "expensive", "example": "太贵了", "example_translation": "Too expensive"},
            {"word": "便宜", "pinyin": "pián yi", "meaning": "cheap", "example": "很便宜", "example_translation": "Very cheap"},
            {"word": "多了", "pinyin": "duō le", "meaning": "much more", "example": "大多了", "example_translation": "Much bigger"},
            {"word": "一点儿", "pinyin": "yī diǎnr", "meaning": "a little", "example": "小一点儿", "example_translation": "A little smaller"},
            {"word": "差不多", "pinyin": "chà bu duō", "meaning": "almost the same", "example": "差不多大", "example_translation": "Almost the same size"},
            {"word": "一样", "pinyin": "yí yàng", "meaning": "same", "example": "一样大", "example_translation": "The same size"},
            {"word": "比", "pinyin": "bǐ", "meaning": "than", "example": "比...贵", "example_translation": "More expensive than"},
            {"word": "价格", "pinyin": "jià gé", "meaning": "price", "example": "价格高", "example_translation": "High price"}
        ],
        "grammar": [
            {
                "point": "Degree of Difference with 多了 and 一点儿",
                "explanation": "Add 多了 after adjective for 'much more', 一点儿 for 'a little more'.",
                "examples": [
                    {"chinese": "电脑比手机贵多了", "translation": "Computer is much more expensive than phone"},
                    {"chinese": "今天比昨天冷多了", "translation": "Today is much colder than yesterday"},
                    {"chinese": "我比你高一点儿", "translation": "I am a little taller than you"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "male", "name": "Li Wei", "voice": "male", "chinese": "这个电脑多少钱？", "pinyin": "Zhège diànnǎo duōshao qián?", "translation": "How much is this computer?"},
            {"speaker": "female", "name": "Salesperson", "voice": "female", "chinese": "八千块。", "pinyin": "Bā qiān kuài.", "translation": "Eight thousand yuan."},
            {"speaker": "male", "name": "Li Wei", "voice": "male", "chinese": "那个手机呢？", "pinyin": "Nàge shǒujī ne?", "translation": "What about that phone?"},
            {"speaker": "female", "name": "Salesperson", "voice": "female", "chinese": "三千块。电脑比手机贵多了。", "pinyin": "Sān qiān kuài. Diànnǎo bǐ shǒujī guì duō le.", "translation": "Three thousand yuan. The computer is much more expensive than the phone."},
            {"speaker": "male", "name": "Li Wei", "voice": "male", "chinese": "手机比电脑便宜多了。", "pinyin": "Shǒujī bǐ diànnǎo piányi duō le.", "translation": "The phone is much cheaper than the computer."},
            {"speaker": "female", "name": "Salesperson", "voice": "female", "chinese": "是啊，你想买哪个？", "pinyin": "Shì a, nǐ xiǎng mǎi nǎge?", "translation": "Yes, which one do you want to buy?"},
            {"speaker": "male", "name": "Li Wei", "voice": "male", "chinese": "我再看看。", "pinyin": "Wǒ zài kàn kan.", "translation": "I'll look around more."}
        ],
        "exercises": [
            {"question": "What does 多了 mean in comparison?", "options": ["A little", "Much more", "Same", "Less"], "correct": 1},
            {"question": "Complete: 电脑___手机贵多了", "options": ["把", "被", "比", "给"], "correct": 2},
            {"question": "What does 差不多 mean?", "options": ["Different", "Almost the same", "Very different", "Exactly the same"], "correct": 1},
            {"question": "Choose the correct comparison", "options": ["我高一点儿你", "我比你高一点儿", "比我你高一点儿", "高一点儿我比你"], "correct": 1}
        ]
    },
    8: {
        "title": "我不太喜欢喝咖啡",
        "title_en": "I Don't Really Like Drinking Coffee",
        "vocabulary": [
            {"word": "咖啡", "pinyin": "kā fēi", "meaning": "coffee", "example": "喝咖啡", "example_translation": "Drink coffee"},
            {"word": "茶", "pinyin": "chá", "meaning": "tea", "example": "喝茶", "example_translation": "Drink tea"},
            {"word": "果汁", "pinyin": "guǒ zhī", "meaning": "juice", "example": "喝果汁", "example_translation": "Drink juice"},
            {"word": "牛奶", "pinyin": "niú nǎi", "meaning": "milk", "example": "喝牛奶", "example_translation": "Drink milk"},
            {"word": "喜欢", "pinyin": "xǐ huān", "meaning": "like", "example": "喜欢喝咖啡", "example_translation": "Like to drink coffee"},
            {"word": "不太", "pinyin": "bù tài", "meaning": "not really", "example": "不太喜欢", "example_translation": "Don't really like"},
            {"word": "比较", "pinyin": "bǐ jiào", "meaning": "relatively", "example": "比较喜欢", "example_translation": "Relatively like"},
            {"word": "最", "pinyin": "zuì", "meaning": "most", "example": "最喜欢", "example_translation": "Like the most"},
            {"word": "饮料", "pinyin": "yǐn liào", "meaning": "beverage", "example": "喜欢的饮料", "example_translation": "Favorite beverage"},
            {"word": "甜", "pinyin": "tián", "meaning": "sweet", "example": "很甜", "example_translation": "Very sweet"},
            {"word": "苦", "pinyin": "kǔ", "meaning": "bitter", "example": "有点苦", "example_translation": "A little bitter"}
        ],
        "grammar": [
            {
                "point": "不太 (bù tài) - Not really",
                "explanation": "Use 不太 before an adjective or verb to mean 'not really' or 'not very'.",
                "examples": [
                    {"chinese": "我不太喜欢喝咖啡", "translation": "I don't really like drinking coffee"},
                    {"chinese": "今天不太热", "translation": "Today is not very hot"},
                    {"chinese": "他不太高兴", "translation": "He is not very happy"}
                ]
            },
            {
                "point": "比较 (bǐ jiào) - Relatively",
                "explanation": "Use 比较 to express 'relatively' or 'comparatively'.",
                "examples": [
                    {"chinese": "我比较喜欢喝茶", "translation": "I relatively like drinking tea"},
                    {"chinese": "这个比较便宜", "translation": "This is relatively cheap"},
                    {"chinese": "他比较高", "translation": "He is relatively tall"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "male", "name": "Zhang Peng", "voice": "male", "chinese": "你想喝什么？咖啡还是茶？", "pinyin": "Nǐ xiǎng hē shénme? Kāfēi háishì chá?", "translation": "What do you want to drink? Coffee or tea?"},
            {"speaker": "female", "name": "Lin Na", "voice": "female", "chinese": "我不太喜欢喝咖啡，比较喜欢喝茶。", "pinyin": "Wǒ bù tài xǐhuān hē kāfēi, bǐjiào xǐhuān hē chá.", "translation": "I don't really like coffee, I prefer tea."},
            {"speaker": "male", "name": "Zhang Peng", "voice": "male", "chinese": "我也是，咖啡有点苦。", "pinyin": "Wǒ yě shì, kāfēi yǒudiǎn kǔ.", "translation": "Me too, coffee is a little bitter."},
            {"speaker": "female", "name": "Lin Na", "voice": "female", "chinese": "你喜欢什么茶？绿茶还是红茶？", "pinyin": "Nǐ xǐhuān shénme chá? Lǜchá háishì hóngchá?", "translation": "What tea do you like? Green tea or black tea?"},
            {"speaker": "male", "name": "Zhang Peng", "voice": "male", "chinese": "我最喜欢绿茶。", "pinyin": "Wǒ zuì xǐhuān lǜchá.", "translation": "I like green tea the most."}
        ],
        "exercises": [
            {"question": "What does 不太 mean?", "options": ["Very", "Not really", "Extremely", "Completely"], "correct": 1},
            {"question": "What is the pinyin for 咖啡?", "options": ["kā fēi", "kà fēi", "kā fèi", "kà fèi"], "correct": 0},
            {"question": "Complete: 我___喜欢喝茶", "options": ["比较", "比较了", "比较的", "比较着"], "correct": 0},
            {"question": "What does 苦 mean?", "options": ["Sweet", "Sour", "Bitter", "Salty"], "correct": 2}
        ]
    },
    9: {
        "title": "最近怎么样",
        "title_en": "How Have You Been",
        "vocabulary": [
            {"word": "最近", "pinyin": "zuì jìn", "meaning": "recently", "example": "最近好吗", "example_translation": "How are you recently"},
            {"word": "忙", "pinyin": "máng", "meaning": "busy", "example": "很忙", "example_translation": "Very busy"},
            {"word": "累", "pinyin": "lèi", "meaning": "tired", "example": "有点累", "example_translation": "A little tired"},
            {"word": "心情", "pinyin": "xīn qíng", "meaning": "mood", "example": "心情好", "example_translation": "Good mood"},
            {"word": "开心", "pinyin": "kāi xīn", "meaning": "happy", "example": "很开心", "example_translation": "Very happy"},
            {"word": "难过", "pinyin": "nán guò", "meaning": "sad", "example": "有点难过", "example_translation": "A little sad"},
            {"word": "有意思", "pinyin": "yǒu yì si", "meaning": "interesting", "example": "很有意思", "example_translation": "Very interesting"},
            {"word": "无聊", "pinyin": "wú liáo", "meaning": "boring", "example": "很无聊", "example_translation": "Very boring"},
            {"word": "变化", "pinyin": "biàn huà", "meaning": "change", "example": "有变化", "example_translation": "There is change"},
            {"word": "一样", "pinyin": "yí yàng", "meaning": "same", "example": "还是一样", "example_translation": "Still the same"},
            {"word": "最近怎么样", "pinyin": "zuì jìn zěn me yàng", "meaning": "How have you been", "example": "你最近怎么样", "example_translation": "How have you been"}
        ],
        "grammar": [
            {
                "point": "怎么样 (zěnme yàng) - How is",
                "explanation": "Use 怎么样 to ask about someone's condition or opinion.",
                "examples": [
                    {"chinese": "你最近怎么样", "translation": "How have you been lately"},
                    {"chinese": "天气怎么样", "translation": "How is the weather"},
                    {"chinese": "这个电影怎么样", "translation": "How is this movie"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "male", "name": "Wang Bin", "voice": "male", "chinese": "好久不见！最近怎么样？", "pinyin": "Hǎo jiǔ bù jiàn! Zuìjìn zěnme yàng?", "translation": "Long time no see! How have you been?"},
            {"speaker": "female", "name": "Chen Lu", "voice": "female", "chinese": "还不错，就是有点忙。你呢？", "pinyin": "Hái bùcuò, jiùshì yǒudiǎn máng. Nǐ ne?", "translation": "Not bad, just a little busy. And you?"},
            {"speaker": "male", "name": "Wang Bin", "voice": "male", "chinese": "我也一样，最近工作很忙。", "pinyin": "Wǒ yě yíyàng, zuìjìn gōngzuò hěn máng.", "translation": "Same here, work has been very busy recently."},
            {"speaker": "female", "name": "Chen Lu", "voice": "female", "chinese": "要注意休息，别太累了。", "pinyin": "Yào zhùyì xiūxi, bié tài lèi le.", "translation": "Take care of yourself, don't get too tired."},
            {"speaker": "male", "name": "Wang Bin", "voice": "male", "chinese": "谢谢！你也是。", "pinyin": "Xièxie! Nǐ yě shì.", "translation": "Thank you! You too."}
        ],
        "exercises": [
            {"question": "What does 最近 mean?", "options": ["Recently", "Today", "Tomorrow", "Yesterday"], "correct": 0},
            {"question": "How do you say 'How have you been?'", "options": ["你好吗", "你怎么样", "最近怎么样", "你最近好吗"], "correct": 2},
            {"question": "What is the opposite of 开心?", "options": ["高兴", "快乐", "难过", "愉快"], "correct": 2},
            {"question": "Complete: 工作很___ (Work is very busy)", "options": ["忙", "闲", "累", "轻松"], "correct": 0}
        ]
    },
    10: {
        "title": "别找了，手机在桌子上呢",
        "title_en": "Stop Looking, Your Phone is on the Table",
        "vocabulary": [
            {"word": "找", "pinyin": "zhǎo", "meaning": "look for", "example": "找东西", "example_translation": "Look for something"},
            {"word": "手机", "pinyin": "shǒu jī", "meaning": "mobile phone", "example": "找手机", "example_translation": "Look for phone"},
            {"word": "钥匙", "pinyin": "yào shi", "meaning": "key", "example": "找钥匙", "example_translation": "Look for keys"},
            {"word": "桌子", "pinyin": "zhuō zi", "meaning": "table", "example": "在桌子上", "example_translation": "On the table"},
            {"word": "椅子", "pinyin": "yǐ zi", "meaning": "chair", "example": "在椅子上", "example_translation": "On the chair"},
            {"word": "地上", "pinyin": "dì shang", "meaning": "on the floor", "example": "掉在地上", "example_translation": "Fell on the floor"},
            {"word": "抽屉", "pinyin": "chōu ti", "meaning": "drawer", "example": "在抽屉里", "example_translation": "In the drawer"},
            {"word": "里面", "pinyin": "lǐ miàn", "meaning": "inside", "example": "在里面", "example_translation": "Inside"},
            {"word": "外面", "pinyin": "wài miàn", "meaning": "outside", "example": "在外面", "example_translation": "Outside"},
            {"word": "旁边", "pinyin": "páng biān", "meaning": "beside", "example": "在旁边", "example_translation": "Beside"}
        ],
        "grammar": [
            {
                "point": "别 (bié) - Don't",
                "explanation": "Use 别 before a verb to mean 'don't'.",
                "examples": [
                    {"chinese": "别找了", "translation": "Stop looking"},
                    {"chinese": "别说了", "translation": "Don't speak anymore"},
                    {"chinese": "别生气", "translation": "Don't be angry"}
                ]
            },
            {
                "point": "在...上/里/旁边 (zài...shang/lǐ/pángbiān) - Location",
                "explanation": "Use these to describe where something is located.",
                "examples": [
                    {"chinese": "手机在桌子上", "translation": "The phone is on the table"},
                    {"chinese": "钥匙在抽屉里", "translation": "The keys are in the drawer"},
                    {"chinese": "书包在旁边", "translation": "The backpack is beside"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "female", "name": "Wu Fang", "voice": "female", "chinese": "我的手机呢？你看见了吗？", "pinyin": "Wǒ de shǒujī ne? Nǐ kànjiàn le ma?", "translation": "Where is my phone? Did you see it?"},
            {"speaker": "male", "name": "Zhao Lei", "voice": "male", "chinese": "别找了，手机在桌子上呢。", "pinyin": "Bié zhǎo le, shǒujī zài zhuōzi shang ne.", "translation": "Stop looking, your phone is on the table."},
            {"speaker": "female", "name": "Wu Fang", "voice": "female", "chinese": "啊，真的！我怎么没看见。", "pinyin": "A, zhēn de! Wǒ zěnme méi kànjiàn.", "translation": "Ah, really! How did I not see it?"},
            {"speaker": "male", "name": "Zhao Lei", "voice": "male", "chinese": "你总是这么着急，慢慢找。", "pinyin": "Nǐ zǒngshì zhème zhāojí, mànmàn zhǎo.", "translation": "You're always so anxious, take your time looking."},
            {"speaker": "female", "name": "Wu Fang", "voice": "female", "chinese": "谢谢你！我以后会注意的。", "pinyin": "Xièxie nǐ! Wǒ yǐhòu huì zhùyì de.", "translation": "Thank you! I'll be more careful in the future."}
        ],
        "exercises": [
            {"question": "What does 别找了 mean?", "options": ["Keep looking", "Stop looking", "Look here", "Look there"], "correct": 1},
            {"question": "Where is the phone in the dialogue?", "options": ["On the chair", "On the table", "In the drawer", "On the floor"], "correct": 1},
            {"question": "What is the pinyin for 钥匙?", "options": ["yào shi", "yáo shi", "yǎo shi", "yāo shi"], "correct": 0},
            {"question": "Complete: 手机在桌子___", "options": ["上", "里", "下", "旁边"], "correct": 0}
        ]
    },
    11: {
        "title": "你习惯中国的生活了吗",
        "title_en": "Are You Used to Life in China",
        "vocabulary": [
            {"word": "习惯", "pinyin": "xí guàn", "meaning": "get used to", "example": "习惯生活", "example_translation": "Get used to life"},
            {"word": "生活", "pinyin": "shēng huó", "meaning": "life", "example": "中国生活", "example_translation": "Life in China"},
            {"word": "已经", "pinyin": "yǐ jīng", "meaning": "already", "example": "已经习惯了", "example_translation": "Already used to it"},
            {"word": "慢慢", "pinyin": "màn màn", "meaning": "slowly", "example": "慢慢习惯", "example_translation": "Slowly get used to"},
            {"word": "文化", "pinyin": "wén huà", "meaning": "culture", "example": "中国文化", "example_translation": "Chinese culture"},
            {"word": "饮食", "pinyin": "yǐn shí", "meaning": "diet/food", "example": "饮食习惯", "example_translation": "Eating habits"},
            {"word": "交通", "pinyin": "jiāo tōng", "meaning": "transportation", "example": "交通习惯", "example_translation": "Transportation habits"},
            {"word": "时间", "pinyin": "shí jiān", "meaning": "time", "example": "时间观念", "example_translation": "Concept of time"},
            {"word": "不同", "pinyin": "bù tóng", "meaning": "different", "example": "很不同", "example_translation": "Very different"},
            {"word": "一样", "pinyin": "yí yàng", "meaning": "same", "example": "不一样", "example_translation": "Not the same"}
        ],
        "grammar": [
            {
                "point": "了 (le) - Change of state",
                "explanation": "Use 了 at the end of a sentence to indicate a change or new situation.",
                "examples": [
                    {"chinese": "你习惯中国的生活了吗", "translation": "Are you used to life in China yet"},
                    {"chinese": "我习惯了", "translation": "I am used to it now"},
                    {"chinese": "他明白了", "translation": "He understands now"}
                ]
            },
            {
                "point": "已经...了 (yǐjīng...le) - Already",
                "explanation": "Use 已经 with 了 to indicate something has already happened.",
                "examples": [
                    {"chinese": "我已经习惯了", "translation": "I am already used to it"},
                    {"chinese": "他已经来了", "translation": "He has already come"},
                    {"chinese": "我已经吃过了", "translation": "I have already eaten"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "male", "name": "David", "voice": "male", "chinese": "你在中国住了多久了？", "pinyin": "Nǐ zài Zhōngguó zhù le duō jiǔ le?", "translation": "How long have you lived in China?"},
            {"speaker": "female", "name": "Liu Yan", "voice": "female", "chinese": "一年多了。", "pinyin": "Yī nián duō le.", "translation": "Over a year."},
            {"speaker": "male", "name": "David", "voice": "male", "chinese": "你习惯中国的生活了吗？", "pinyin": "Nǐ xíguàn Zhōngguó de shēnghuó le ma?", "translation": "Are you used to life in China?"},
            {"speaker": "female", "name": "Liu Yan", "voice": "female", "chinese": "刚开始不习惯，现在已经习惯了。", "pinyin": "Gāng kāishǐ bù xíguàn, xiànzài yǐjīng xíguàn le.", "translation": "I wasn't used to it at first, but now I am."},
            {"speaker": "male", "name": "David", "voice": "male", "chinese": "你觉得什么最难习惯？", "pinyin": "Nǐ juéde shénme zuì nán xíguàn?", "translation": "What do you think is the hardest to get used to?"},
            {"speaker": "female", "name": "Liu Yan", "voice": "female", "chinese": "可能是饮食吧，不过慢慢就好了。", "pinyin": "Kěnéng shì yǐnshí ba, bùguò mànmàn jiù hǎo le.", "translation": "Probably the food, but it gets better slowly."}
        ],
        "exercises": [
            {"question": "What does 习惯 mean?", "options": ["Get used to", "Habit", "Both A and B", "Life"], "correct": 2},
            {"question": "Complete: 我已经___了", "options": ["习惯", "习惯了", "习惯着", "习惯过"], "correct": 1},
            {"question": "What is the pinyin for 饮食?", "options": ["yǐn shí", "yīn shí", "yìn shí", "yín shí"], "correct": 0},
            {"question": "Choose the correct sentence", "options": ["我习惯已经了", "我已经习惯了", "习惯了已经我", "习惯了我已经"], "correct": 1}
        ]
    },
    12: {
        "title": "这件事我都听说了",
        "title_en": "I've Heard About This Matter",
        "vocabulary": [
            {"word": "事情", "pinyin": "shì qing", "meaning": "matter", "example": "这件事", "example_translation": "This matter"},
            {"word": "听说", "pinyin": "tīng shuō", "meaning": "heard that", "example": "听说了", "example_translation": "Heard about it"},
            {"word": "新闻", "pinyin": "xīn wén", "meaning": "news", "example": "看新闻", "example_translation": "Watch news"},
            {"word": "消息", "pinyin": "xiāo xi", "meaning": "message", "example": "好消息", "example_translation": "Good news"},
            {"word": "知道", "pinyin": "zhī dào", "meaning": "know", "example": "知道了", "example_translation": "I know"},
            {"word": "了解", "pinyin": "liǎo jiě", "meaning": "understand", "example": "了解了", "example_translation": "I understand"},
            {"word": "告诉", "pinyin": "gào su", "meaning": "tell", "example": "告诉我", "example_translation": "Tell me"},
            {"word": "解释", "pinyin": "jiě shì", "meaning": "explain", "example": "解释一下", "example_translation": "Explain a bit"},
            {"word": "清楚", "pinyin": "qīng chu", "meaning": "clear", "example": "很清楚", "example_translation": "Very clear"},
            {"word": "明白", "pinyin": "míng bai", "meaning": "understand", "example": "明白了", "example_translation": "I understand"}
        ],
        "grammar": [
            {
                "point": "都 (dōu) - Emphasizing 'all/every'",
                "explanation": "Use 都 to emphasize that everyone/everything is included.",
                "examples": [
                    {"chinese": "这件事我都听说了", "translation": "I've heard about this matter too"},
                    {"chinese": "我们都知道了", "translation": "We all know"},
                    {"chinese": "他什么都明白", "translation": "He understands everything"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "female", "name": "Xu Mei", "voice": "female", "chinese": "你听说那件事了吗？", "pinyin": "Nǐ tīngshuō nà jiàn shì le ma?", "translation": "Have you heard about that matter?"},
            {"speaker": "male", "name": "Zhou Jie", "voice": "male", "chinese": "哪件事？", "pinyin": "Nǎ jiàn shì?", "translation": "Which matter?"},
            {"speaker": "female", "name": "Xu Mei", "voice": "female", "chinese": "就是公司要搬家的那件事。", "pinyin": "Jiùshì gōngsī yào bānjiā de nà jiàn shì.", "translation": "The one about the company moving."},
            {"speaker": "male", "name": "Zhou Jie", "voice": "male", "chinese": "哦，那件事啊，我都听说了。", "pinyin": "Ó, nà jiàn shì a, wǒ dōu tīngshuō le.", "translation": "Oh, that matter, I've heard about it too."},
            {"speaker": "female", "name": "Xu Mei", "voice": "female", "chinese": "你觉得怎么样？", "pinyin": "Nǐ juéde zěnme yàng?", "translation": "What do you think?"},
            {"speaker": "male", "name": "Zhou Jie", "voice": "male", "chinese": "我觉得不太好，但是没办法。", "pinyin": "Wǒ juéde bù tài hǎo, dànshì méi bànfǎ.", "translation": "I think it's not great, but there's no choice."}
        ],
        "exercises": [
            {"question": "What does 听说 mean?", "options": ["Listen and speak", "Hear that", "Tell someone", "Ask someone"], "correct": 1},
            {"question": "Complete: 这件事我___听说了", "options": ["都", "也", "还", "就"], "correct": 0},
            {"question": "What is the pinyin for 事情?", "options": ["shì qing", "shí qing", "shì qíng", "shí qíng"], "correct": 0},
            {"question": "Choose the correct response", "options": ["我都听说了", "我都听说", "我都听说了了", "我都听说吧"], "correct": 0}
        ]
    },
    13: {
        "title": "一边...一边...",
        "title_en": "Doing Two Things at Once",
        "vocabulary": [
            {"word": "一边", "pinyin": "yī biān", "meaning": "while", "example": "一边听一边写", "example_translation": "Listen while writing"},
            {"word": "听", "pinyin": "tīng", "meaning": "listen", "example": "听音乐", "example_translation": "Listen to music"},
            {"word": "写", "pinyin": "xiě", "meaning": "write", "example": "写字", "example_translation": "Write characters"},
            {"word": "看", "pinyin": "kàn", "meaning": "watch", "example": "看电视", "example_translation": "Watch TV"},
            {"word": "吃", "pinyin": "chī", "meaning": "eat", "example": "吃饭", "example_translation": "Eat a meal"},
            {"word": "聊天", "pinyin": "liáo tiān", "meaning": "chat", "example": "和朋友聊天", "example_translation": "Chat with friends"},
            {"word": "走路", "pinyin": "zǒu lù", "meaning": "walk", "example": "走路去", "example_translation": "Go by walking"},
            {"word": "唱歌", "pinyin": "chàng gē", "meaning": "sing", "example": "唱歌跳舞", "example_translation": "Sing and dance"},
            {"word": "同时", "pinyin": "tóng shí", "meaning": "at the same time", "example": "同时做", "example_translation": "Do at the same time"},
            {"word": "可以", "pinyin": "kě yǐ", "meaning": "can", "example": "可以吗", "example_translation": "Is it OK"}
        ],
        "grammar": [
            {
                "point": "一边...一边... (yībiān...yībiān...) - While",
                "explanation": "Use 一边...一边... to indicate two actions happening at the same time.",
                "examples": [
                    {"chinese": "他一边听音乐一边写作业", "translation": "He listens to music while doing homework"},
                    {"chinese": "我一边吃饭一边看电视", "translation": "I eat while watching TV"},
                    {"chinese": "她一边走路一边唱歌", "translation": "She walks while singing"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "male", "name": "Sun Hao", "voice": "male", "chinese": "你平时喜欢一边做什么一边做什么？", "pinyin": "Nǐ píngshí xǐhuān yībiān zuò shénme yībiān zuò shénme?", "translation": "What do you like to do simultaneously?"},
            {"speaker": "female", "name": "Zhou Ting", "voice": "female", "chinese": "我喜欢一边听音乐一边跑步。", "pinyin": "Wǒ xǐhuān yībiān tīng yīnyuè yībiān pǎobù.", "translation": "I like to listen to music while running."},
            {"speaker": "male", "name": "Sun Hao", "voice": "male", "chinese": "这样不累吗？", "pinyin": "Zhèyàng bù lèi ma?", "translation": "Isn't that tiring?"},
            {"speaker": "female", "name": "Zhou Ting", "voice": "female", "chinese": "不累，反而更有精神。", "pinyin": "Bù lèi, fǎn'ér gèng yǒu jīngshén.", "translation": "Not tired, more energetic instead."},
            {"speaker": "male", "name": "Sun Hao", "voice": "male", "chinese": "那我也试试一边听音乐一边工作。", "pinyin": "Nà wǒ yě shìshi yībiān tīng yīnyuè yībiān gōngzuò.", "translation": "Then I'll also try listening to music while working."},
            {"speaker": "female", "name": "Zhou Ting", "voice": "female", "chinese": "你可以试试，效率可能会更高。", "pinyin": "Nǐ kěyǐ shìshi, xiàolǜ kěnéng huì gèng gāo.", "translation": "You can try, efficiency might be higher."}
        ],
        "exercises": [
            {"question": "What does 一边...一边... mean?", "options": ["First...then...", "While...", "Because...so...", "If...then..."], "correct": 1},
            {"question": "Complete: 他一边听音乐一边___作业", "options": ["写", "写写", "写了", "写着"], "correct": 0},
            {"question": "What is the pinyin for 聊天?", "options": ["liáo tiān", "liào tiān", "liǎo tiān", "liāo tiān"], "correct": 0},
            {"question": "Choose the correct sentence", "options": ["他一边听音乐一边写作业", "他一边听音乐写一边作业", "他听音乐一边一边写作业", "他听音乐一边写作业一边"], "correct": 0}
        ]
    },
    14: {
        "title": "越...越...",
        "title_en": "The More... The More...",
        "vocabulary": [
            {"word": "越", "pinyin": "yuè", "meaning": "more", "example": "越来越好", "example_translation": "Getting better and better"},
            {"word": "越来越", "pinyin": "yuè lái yuè", "meaning": "more and more", "example": "越来越热", "example_translation": "Getting hotter and hotter"},
            {"word": "练习", "pinyin": "liàn xí", "meaning": "practice", "example": "多练习", "example_translation": "Practice more"},
            {"word": "进步", "pinyin": "jìn bù", "meaning": "progress", "example": "进步很快", "example_translation": "Progress quickly"},
            {"word": "努力", "pinyin": "nǔ lì", "meaning": "work hard", "example": "努力学习", "example_translation": "Study hard"},
            {"word": "成绩", "pinyin": "chéng jì", "meaning": "grade", "example": "成绩好", "example_translation": "Good grades"},
            {"word": "喜欢", "pinyin": "xǐ huān", "meaning": "like", "example": "越来越喜欢", "example_translation": "Like more and more"},
            {"word": "了解", "pinyin": "liǎo jiě", "meaning": "understand", "example": "越来越了解", "example_translation": "Understand more and more"},
            {"word": "熟悉", "pinyin": "shú xī", "meaning": "familiar", "example": "越来越熟悉", "example_translation": "Get more familiar"},
            {"word": "热情", "pinyin": "rè qíng", "meaning": "enthusiastic", "example": "很热情", "example_translation": "Very enthusiastic"}
        ],
        "grammar": [
            {
                "point": "越来越 (yuè lái yuè) - More and more",
                "explanation": "Use 越来越 before an adjective to mean 'more and more'.",
                "examples": [
                    {"chinese": "天气越来越热", "translation": "The weather is getting hotter and hotter"},
                    {"chinese": "汉语越来越难", "translation": "Chinese is getting more and more difficult"},
                    {"chinese": "我越来越喜欢中国", "translation": "I like China more and more"}
                ]
            },
            {
                "point": "越...越... (yuè...yuè...) - The more...the more...",
                "explanation": "Use 越...越... to express proportional change.",
                "examples": [
                    {"chinese": "越练习越好", "translation": "The more practice, the better"},
                    {"chinese": "越努力越成功", "translation": "The harder you work, the more successful you are"},
                    {"chinese": "越学越有意思", "translation": "The more you learn, the more interesting it becomes"}
                ]
            }
        ],
        "dialogue": [
            {"speaker": "female", "name": "Teacher Wang", "voice": "female", "chinese": "你的汉语最近进步很快啊！", "pinyin": "Nǐ de Hànyǔ zuìjìn jìnbù hěn kuài a!", "translation": "Your Chinese has been improving quickly lately!"},
            {"speaker": "male", "name": "Student Li", "voice": "male", "chinese": "谢谢老师！我每天都练习。", "pinyin": "Xièxie lǎoshī! Wǒ měitiān dōu liànxí.", "translation": "Thank you, teacher! I practice every day."},
            {"speaker": "female", "name": "Teacher Wang", "voice": "female", "chinese": "是啊，越练习越好。", "pinyin": "Shì a, yuè liànxí yuè hǎo.", "translation": "Yes, the more you practice, the better."},
            {"speaker": "male", "name": "Student Li", "voice": "male", "chinese": "我也觉得越来越有兴趣了。", "pinyin": "Wǒ yě juéde yuè lái yuè yǒu xìngqù le.", "translation": "I also find it more and more interesting."},
            {"speaker": "female", "name": "Teacher Wang", "voice": "female", "chinese": "坚持下去，你会越来越好的。", "pinyin": "Jiānchí xiàqù, nǐ huì yuè lái yuè hǎo de.", "translation": "Keep it up, you will get better and better."},
            {"speaker": "male", "name": "Student Li", "voice": "male", "chinese": "我会努力的，谢谢老师鼓励！", "pinyin": "Wǒ huì nǔlì de, xièxie lǎoshī gǔlì!", "translation": "I will work hard, thank you for your encouragement!"}
        ],
        "exercises": [
            {"question": "What does 越来越 mean?", "options": ["Less and less", "More and more", "Better and better", "Worse and worse"], "correct": 1},
            {"question": "Complete: 天气___热", "options": ["越来越", "越越来越", "越来越越", "越越来"], "correct": 0},
            {"question": "What is the pinyin for 努力?", "options": ["nǔ lì", "nú lì", "nǔ lǐ", "nú lǐ"], "correct": 0},
            {"question": "Choose the correct sentence", "options": ["他越努力越进步", "他努力越进步越", "越他努力越进步", "他越进步越努力"], "correct": 0}
        ]
    },
    15: {
    "title": "虽然...但是...",
    "title_en": "Although... But...",
    "vocabulary": [
        {"word": "虽然", "pinyin": "suī rán", "meaning": "although", "example": "虽然很累", "example_translation": "Although tired"},
        {"word": "但是", "pinyin": "dàn shì", "meaning": "but", "example": "但是很开心", "example_translation": "But very happy"},
        {"word": "所以", "pinyin": "suǒ yǐ", "meaning": "so", "example": "所以不去", "example_translation": "So not going"},
        {"word": "因为", "pinyin": "yīn wèi", "meaning": "because", "example": "因为下雨", "example_translation": "Because it's raining"},
        {"word": "还是", "pinyin": "hái shì", "meaning": "still", "example": "还是去了", "example_translation": "Still went"},
        {"word": "却", "pinyin": "què", "meaning": "but (formal)", "example": "却不知道", "example_translation": "But didn't know"},
        {"word": "而且", "pinyin": "ér qiě", "meaning": "moreover", "example": "而且很好", "example_translation": "Moreover very good"},
        {"word": "即使", "pinyin": "jí shǐ", "meaning": "even if", "example": "即使很难", "example_translation": "Even if difficult"},
        {"word": "也", "pinyin": "yě", "meaning": "also/still", "example": "也要试", "example_translation": "Still try"},
        {"word": "只要", "pinyin": "zhǐ yào", "meaning": "as long as", "example": "只要努力", "example_translation": "As long as work hard"}
    ],
    "grammar": [
        {
            "point": "虽然...但是... (suīrán...dànshì...) - Although...but...",
            "explanation": "Use 虽然...但是... to express contrast or concession.",
            "examples": [
                {"chinese": "虽然很累，但是很开心", "translation": "Although tired, very happy"},
                {"chinese": "虽然贵，但是质量好", "translation": "Although expensive, good quality"},
                {"chinese": "虽然他年轻，但是很有经验", "translation": "Although young, very experienced"},
                {"chinese": "虽然下雨，但是我还是去了", "translation": "Although rain, I still went"},
                {"chinese": "虽然汉语很难，但是很有意思", "translation": "Although Chinese difficult, very interesting"}
            ]
        },
        {
            "point": "因为...所以... (yīnwèi...suǒyǐ...) - Because...so...",
            "explanation": "Use 因为...所以... to express cause and effect.",
            "examples": [
                {"chinese": "因为下雨，所以不去", "translation": "Because rain, not going"},
                {"chinese": "因为努力学习，所以进步很快", "translation": "Because study hard, progress quickly"},
                {"chinese": "因为价格贵，所以没买", "translation": "Because price expensive, didn't buy"}
            ]
        },
        {
            "point": "即使...也... (jíshǐ...yě...) - Even if...still...",
            "explanation": "Use 即使...也... to express hypothetical concession.",
            "examples": [
                {"chinese": "即使很难也要试", "translation": "Even if difficult, still try"},
                {"chinese": "即使下雨也去", "translation": "Even if rain, still go"},
                {"chinese": "即使失败了也不后悔", "translation": "Even if fail, won't regret"}
            ]
        }
    ],
    "dialogue": [
        {"speaker": "male", "name": "Liu Qiang", "voice": "male", "chinese": "你觉得学汉语难吗？", "pinyin": "Nǐ juéde xué Hànyǔ nán ma?", "translation": "Do you think learning Chinese is difficult?"},
        {"speaker": "female", "name": "Wang Ying", "voice": "female", "chinese": "虽然很难，但是很有意思。", "pinyin": "Suīrán hěn nán, dànshì hěn yǒuyìsi.", "translation": "Although it's very difficult, it's very interesting."},
        {"speaker": "male", "name": "Liu Qiang", "voice": "male", "chinese": "因为汉语难，所以很多人学不会。", "pinyin": "Yīnwèi Hànyǔ nán, suǒyǐ hěn duō rén xué bù huì.", "translation": "Because Chinese is difficult, many people can't learn it well."},
        {"speaker": "female", "name": "Wang Ying", "voice": "female", "chinese": "虽然难，但是只要努力就能学会。", "pinyin": "Suīrán nán, dànshì zhǐyào nǔlì jiù néng xué huì.", "translation": "Although it's difficult, as long as you work hard, you can learn it."},
        {"speaker": "male", "name": "Liu Qiang", "voice": "male", "chinese": "即使很难，我也不会放弃。", "pinyin": "Jíshǐ hěn nán, wǒ yě bù huì fàngqì.", "translation": "Even if it's very difficult, I won't give up."},
        {"speaker": "female", "name": "Wang Ying", "voice": "female", "chinese": "对！因为坚持，所以成功。加油！", "pinyin": "Duì! Yīnwèi jiānchí, suǒyǐ chénggōng. Jiāyóu!", "translation": "Right! Because of persistence, comes success. Keep it up!"},
        {"speaker": "male", "name": "Liu Qiang", "voice": "male", "chinese": "谢谢你的鼓励！我会努力的。", "pinyin": "Xièxie nǐ de gǔlì! Wǒ huì nǔlì de.", "translation": "Thank you for your encouragement! I will work hard."}
    ],
    "exercises": [
        {"question": "What does 虽然...但是... mean?", "options": ["Because...so...", "If...then...", "Although...but...", "Not only...but also..."], "correct": 2},
        {"question": "Complete: ___很累，但是很开心", "options": ["虽然", "因为", "如果", "即使"], "correct": 0},
        {"question": "What is the correct translation of '因为...所以...'?", "options": ["Although...but...", "Because...so...", "If...then...", "Even if...still..."], "correct": 1},
        {"question": "Complete: 即使很难，我也要___", "options": ["试", "试试", "试一试", "All of the above"], "correct": 3},
        {"question": "Choose the correct sentence", "options": ["虽然很累但是很开心", "很累虽然但是很开心", "虽然但是很累很开心", "但是虽然很累很开心"], "correct": 0},
        {"question": "What does 即使 mean?", "options": ["Because", "Although", "Even if", "So"], "correct": 2},
        {"question": "Complete: 因为努力，___成功", "options": ["虽然", "但是", "所以", "即使"], "correct": 2}
    ]
}

# Lesson navigation
lesson_nav = {
    1: {"prev": 15, "next": 2},
    2: {"prev": 1, "next": 3},
    3: {"prev": 2, "next": 4},
    4: {"prev": 3, "next": 5},
    5: {"prev": 4, "next": 6},
    6: {"prev": 5, "next": 7},
    7: {"prev": 6, "next": 8},
    8: {"prev": 7, "next": 9},
    9: {"prev": 8, "next": 10},
    10: {"prev": 9, "next": 11},
    11: {"prev": 10, "next": 12},
    12: {"prev": 11, "next": 13},
    13: {"prev": 12, "next": 14},
    14: {"prev": 13, "next": 15},
    15: {"prev": 14, "next": 1},
}

# Template
TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>HSK 2 Lesson {num} - {title} | Mandarin Teacher</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #1a472a; padding: 20px; min-height: 100vh; }}
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
        .vocab-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 15px; }}
        .vocab-card {{ background: white; border-radius: 16px; padding: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); transition: all 0.2s; border: 1px solid #e0e0e0; }}
        .vocab-card:hover {{ transform: translateY(-3px); box-shadow: 0 5px 15px rgba(0,0,0,0.1); }}
        .vocab-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px; }}
        .vocab-word {{ font-size: 28px; font-weight: bold; color: #1a472a; cursor: pointer; }}
        .pronounce-btn {{ background: #ffd700; color: #1a472a; border: none; padding: 6px 14px; border-radius: 25px; cursor: pointer; font-size: 13px; font-weight: bold; }}
        .pronounce-btn:hover {{ background: #e6c200; }}
        .vocab-pinyin {{ color: #e94560; font-size: 14px; margin: 5px 0; }}
        .vocab-meaning {{ color: #666; font-size: 13px; margin-bottom: 10px; padding-bottom: 8px; border-bottom: 1px dashed #eee; }}
        .vocab-example {{ background: #f8f9fa; padding: 10px; border-radius: 10px; font-size: 13px; }}
        .example-label {{ font-size: 11px; color: #999; margin-bottom: 4px; font-weight: bold; }}
        .vocab-example-chinese {{ font-weight: 500; margin-bottom: 5px; }}
        .vocab-example-translation {{ color: #888; font-size: 12px; }}
        .audio-btn {{ background: #2d6a4f; color: white; border: none; padding: 4px 10px; border-radius: 20px; cursor: pointer; font-size: 10px; margin-top: 8px; margin-right: 8px; }}
        .audio-btn:hover {{ background: #1a472a; }}
        .speak-practice-btn {{ background: #e94560; color: white; border: none; padding: 4px 10px; border-radius: 20px; cursor: pointer; font-size: 10px; margin-top: 8px; margin-right: 8px; }}
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
                Click the <strong>Pronounce</strong> button next to the pinyin to hear the word.<br>
                Use the 🎤 Speak button to practice your pronunciation.<br>
                The 📝 Example section shows you how to use the word in a sentence.<br><br>
                加油！(Jiāyóu!) Keep going!
            </div>
        </div>
        
        <div class="content">
            <div class="section">
                <div class="section-title">📖 Vocabulary
                    <button class="play-all-btn" onclick="playVocabulary()">🔊 Play All</button>
                </div>
                <div class="vocab-grid" id="vocabGrid"></div>
            </div>
            
            <div class="section">
                <div class="section-title">📖 Grammar Points
                    <button class="play-all-btn" onclick="playGrammar()">🔊 Play All</button>
                </div>
                <div id="grammarContainer"></div>
            </div>
            
            <div class="section">
                <div class="section-title">💬 Conversation Practice
                    <button class="play-all-btn" onclick="playDialogue()">🔊 Play All</button>
                </div>
                <div class="dialogue-container">
                    <div class="dialogue-scene" id="dialogueContainer"></div>
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
        const vocabulary = {vocab_json};
        const grammar = {grammar_json};
        const dialogue = {dialogue_json};
        const exercises = {exercises_json};
        
        let userAnswers = {{}};
        let recognition = null;
        let audioQueue = [];
        let isPlaying = false;
        
        // Force male voice for male speakers by using different voice ID
        // Male voice: zh-CN-YunxiNeural, Female voice: zh-CN-XiaoxiaoNeural
        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {{
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            recognition = new SpeechRecognition();
            recognition.lang = 'zh-CN';
            recognition.continuous = false;
            recognition.interimResults = false;
        }}
        
        async function playAudio(text, language = 'zh', voice = 'female') {{
            if (!text) return;
            try {{
                // Use different voice based on speaker gender
                const voiceType = (voice === 'male') ? 'male' : 'female';
                const response = await fetch('/api/speak', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ text: text, language: language, voice: voiceType }})
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
        
        function playWord(word) {{
            playAudio(word, 'zh', 'female');
        }}
        
        function startPronunciationPractice(word, pinyin) {{
            if (!recognition) {{
                alert("Speech recognition not supported. Please use the Listen button.");
                return;
            }}
            recognition.start();
            recognition.onresult = function(event) {{
                const spoken = event.results[0][0].transcript;
                const feedbackDiv = document.getElementById('ai-teacher-message');
                if (spoken === word || spoken === pinyin || spoken.includes(word)) {{
                    feedbackDiv.innerHTML = `<span style="color:#28a745;">✅ Excellent pronunciation of "${{word}}"! Your tones are correct.</span>`;
                }} else {{
                    feedbackDiv.innerHTML = `<span style="color:#dc3545;">❌ Try again. You said "${{spoken}}". The correct pronunciation is "${{word}}" (${{pinyin}}).</span>`;
                }}
                setTimeout(() => {{
                    feedbackDiv.innerHTML = `<strong>📖 HSK Level 2 - Lesson {num}</strong><br><br>Click the <strong>Pronounce</strong> button next to the pinyin to hear the word.<br>Use the 🎤 Speak button to practice your pronunciation.<br>加油！(Jiāyóu!) Keep going!`;
                }}, 4000);
            }};
        }}
        
        function renderVocabulary() {{
            const grid = document.getElementById('vocabGrid');
            if (vocabulary.length > 0) {{
                grid.innerHTML = vocabulary.map(v => `
                    <div class="vocab-card">
                        <div class="vocab-header">
                            <div class="vocab-word" onclick="playWord('${{v.word}}')">${{v.word}}</div>
                            <button class="pronounce-btn" onclick="playWord('${{v.word}}')">🔊 Pronounce</button>
                        </div>
                        <div class="vocab-pinyin">${{v.pinyin}}</div>
                        <div class="vocab-meaning">${{v.meaning}}</div>
                        <div class="vocab-example">
                            <div class="example-label">📝 Example:</div>
                            <div class="vocab-example-chinese">${{v.example}}</div>
                            <div class="vocab-example-translation">→ ${{v.example_translation}}</div>
                            <button class="audio-btn" onclick="playAudio('${{v.example}}', 'zh', 'female')">🔊 Listen to Example</button>
                            <button class="speak-practice-btn" onclick="startPronunciationPractice('${{v.word}}', '${{v.pinyin}}')">🎤 Practice Word</button>
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
                                    <div class="grammar-example-chinese">${{ex.chinese}}</div>
                                    <div class="grammar-example-translation">→ ${{ex.translation}}</div>
                                    <button class="audio-btn" onclick="playAudio('${{ex.chinese}}', 'zh', 'female')">🔊 Listen</button>
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
                            <button class="audio-btn" onclick="playAudio('${{line.chinese}}', 'zh', '${{line.voice}}')">🔊 Listen</button>
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
                scoreDiv.innerHTML = `<strong>Score: ${{correct}}/${{exercises.length}} (${{percent}}%)</strong><br>🎉 Great job! You're ready for the next lesson!`;
            }} else {{
                scoreDiv.className = 'exercise-score score-bad';
                scoreDiv.innerHTML = `<strong>Score: ${{correct}}/${{exercises.length}} (${{percent}}%)</strong><br>📚 Review the lesson and try again. You need 70% to pass.`;
            }}
            exercises.forEach((ex, idx) => {{
                const options = document.querySelectorAll(`.exercise-card:nth-child($${{idx + 1}}) .exercise-option`);
                options.forEach((opt, optIdx) => {{
                    opt.classList.remove('correct', 'wrong');
                    if (optIdx === ex.correct) opt.classList.add('correct');
                    if (optIdx === userAnswers[idx] && userAnswers[idx] !== ex.correct) opt.classList.add('wrong');
                }});
            }});
        }}
        
        function playVocabulary() {{
            let i = 0;
            function next() {{
                if (i >= vocabulary.length) return;
                playAudio(vocabulary[i].word, 'zh', 'female');
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
                    playAudio(grammar[g].point + '. ' + grammar[g].explanation, 'en', 'female');
                    e++;
                    setTimeout(next, 3000);
                }} else if (e - 1 < grammar[g].examples.length) {{
                    playAudio(grammar[g].examples[e - 1].chinese, 'zh', 'female');
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
                const line = dialogue[i];
                playAudio(line.chinese, 'zh', line.voice);
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
        window.playWord = playWord;
        window.startPronunciationPractice = startPronunciationPractice;
        window.selectAnswer = selectAnswer;
        window.checkExercises = checkExercises;
        window.playVocabulary = playVocabulary;
        window.playGrammar = playGrammar;
        window.playDialogue = playDialogue;
    </script>
</body>
</html>'''

# Generate all lessons
for num in range(1, 16):
    data = HSK2_COMPLETE_DATA[num]
    nav = lesson_nav[num]
    
    vocab_json = json.dumps(data["vocabulary"], ensure_ascii=False)
    grammar_json = json.dumps(data["grammar"], ensure_ascii=False)
    dialogue_json = json.dumps(data["dialogue"], ensure_ascii=False)
    exercises_json = json.dumps(data["exercises"], ensure_ascii=False)
    
    content = TEMPLATE.format(
        num=num,
        title=data["title"],
        title_en=data["title_en"],
        prev=nav["prev"],
        next=nav["next"],
        vocab_json=vocab_json,
        grammar_json=grammar_json,
        dialogue_json=dialogue_json,
        exercises_json=exercises_json
    )
    
    filename = f"templates/hsk2_lesson{num}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Created: {filename}")

print("\n🎉 All 15 HSK 2 lessons generated successfully!")
print("\n📊 Lesson Summary:")
for num in range(1, 16):
    data = HSK2_COMPLETE_DATA[num]
    print(f"   Lesson {num}: {data['title']} - {len(data['vocabulary'])} vocab, {len(data['grammar'])} grammar, {len(data['dialogue'])} dialogue lines")