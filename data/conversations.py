# data/conversations.py - Complete Conversation Dialogues by HSK Level

HSK_CONVERSATIONS = {
    1: [
        {
            "id": 1,
            "title": "Meeting Someone for the First Time",
            "dialogues": [
                {"speaker": "A", "chinese": "你好", "pinyin": "Ni hao", "english": "Hello", "indonesian": "Halo"},
                {"speaker": "B", "chinese": "你好", "pinyin": "Ni hao", "english": "Hello", "indonesian": "Halo"},
                {"speaker": "A", "chinese": "你叫什么名字", "pinyin": "Ni jiao shenme mingzi", "english": "What is your name", "indonesian": "Siapa namamu"},
                {"speaker": "B", "chinese": "我叫小明", "pinyin": "Wo jiao Xiao Ming", "english": "My name is Xiao Ming", "indonesian": "Nama saya Xiao Ming"},
                {"speaker": "A", "chinese": "很高兴认识你", "pinyin": "Hen gaoxing renshi ni", "english": "Nice to meet you", "indonesian": "Senang berkenalan denganmu"},
                {"speaker": "B", "chinese": "我也是", "pinyin": "Wo ye shi", "english": "Me too", "indonesian": "Saya juga"}
            ]
        },
        {
            "id": 2,
            "title": "Ordering Food",
            "dialogues": [
                {"speaker": "A", "chinese": "你想吃什么", "pinyin": "Ni xiang chi shenme", "english": "What would you like to eat", "indonesian": "Kamu mau makan apa"},
                {"speaker": "B", "chinese": "我想吃面条", "pinyin": "Wo xiang chi miantiao", "english": "I would like noodles", "indonesian": "Saya mau mie"},
                {"speaker": "A", "chinese": "喝什么", "pinyin": "He shenme", "english": "What to drink", "indonesian": "Minum apa"},
                {"speaker": "B", "chinese": "一杯茶", "pinyin": "Yi bei cha", "english": "A cup of tea", "indonesian": "Secangkir teh"}
            ]
        },
        {
            "id": 3,
            "title": "Asking for Directions",
            "dialogues": [
                {"speaker": "A", "chinese": "请问，厕所在哪儿", "pinyin": "Qingwen, cesuo zai nar", "english": "Excuse me, where is the bathroom", "indonesian": "Permisi, di mana toilet"},
                {"speaker": "B", "chinese": "在那边", "pinyin": "Zai na bian", "english": "Over there", "indonesian": "Di sana"},
                {"speaker": "A", "chinese": "谢谢", "pinyin": "Xiexie", "english": "Thank you", "indonesian": "Terima kasih"}
            ]
        }
    ],
    2: [
        {
            "id": 1,
            "title": "Shopping",
            "dialogues": [
                {"speaker": "A", "chinese": "这个多少钱", "pinyin": "Zhege duoshao qian", "english": "How much is this", "indonesian": "Berapa harganya"},
                {"speaker": "B", "chinese": "五十块", "pinyin": "Wushi kuai", "english": "Fifty yuan", "indonesian": "Lima puluh yuan"},
                {"speaker": "A", "chinese": "太贵了，便宜一点吧", "pinyin": "Tai gui le, pianyi yidian ba", "english": "Too expensive, a little cheaper please", "indonesian": "Terlalu mahal, lebih murah sedikit"},
                {"speaker": "B", "chinese": "好吧，四十块", "pinyin": "Hao ba, sishi kuai", "english": "OK, forty yuan", "indonesian": "Baiklah, empat puluh yuan"}
            ]
        },
        {
            "id": 2,
            "title": "Talking About Daily Routine",
            "dialogues": [
                {"speaker": "A", "chinese": "你每天几点起床", "pinyin": "Ni meitian jidian qichuang", "english": "What time do you wake up every day", "indonesian": "Jam berapa kamu bangun setiap hari"},
                {"speaker": "B", "chinese": "我七点起床", "pinyin": "Wo qi dian qichuang", "english": "I wake up at 7", "indonesian": "Saya bangun jam 7"},
                {"speaker": "A", "chinese": "然后呢", "pinyin": "Ranhou ne", "english": "And then", "indonesian": "Lalu"},
                {"speaker": "B", "chinese": "然后吃早饭，去上班", "pinyin": "Ranhou chi zaofan, qu shangban", "english": "Then eat breakfast and go to work", "indonesian": "Lalu makan sarapan dan pergi kerja"}
            ]
        }
    ],
    3: [
        {
            "id": 1,
            "title": "Making Plans",
            "dialogues": [
                {"speaker": "A", "chinese": "周末你有什么打算", "pinyin": "Zhoumo ni you sheme dasuan", "english": "What are your plans for the weekend", "indonesian": "Apa rencanamu untuk akhir pekan"},
                {"speaker": "B", "chinese": "我想去公园散步", "pinyin": "Wo xiang qu gongyuan sanbu", "english": "I want to go for a walk in the park", "indonesian": "Saya ingin jalan-jalan di taman"},
                {"speaker": "A", "chinese": "我可以一起去吗", "pinyin": "Wo keyi yiqi qu ma", "english": "Can I come along", "indonesian": "Boleh saya ikut"},
                {"speaker": "B", "chinese": "当然可以", "pinyin": "Dangran keyi", "english": "Of course", "indonesian": "Tentu saja"}
            ]
        }
    ],
}

def get_conversations(level):
    return HSK_CONVERSATIONS.get(level, [])

def get_conversation_count(level):
    return len(HSK_CONVERSATIONS.get(level, []))