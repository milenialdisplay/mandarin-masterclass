import json
import os

os.makedirs("data", exist_ok=True)

# Create vocabulary with direct integer keys
hsk_vocab = {
    1: [
        {"word": "妈妈", "pinyin": "mama", "meaning": "mother; mom", "example": "我爱妈妈"},
        {"word": "爸爸", "pinyin": "baba", "meaning": "father; dad", "example": "爸爸工作"},
        {"word": "你好", "pinyin": "ni hao", "meaning": "hello; hi", "example": "你好吗？"},
        {"word": "谢谢", "pinyin": "xiexie", "meaning": "thank you", "example": "谢谢你"},
        {"word": "再见", "pinyin": "zaijian", "meaning": "goodbye", "example": "明天再见"},
    ],
    2: [
        {"word": "电脑", "pinyin": "diannao", "meaning": "computer", "example": "用电脑"},
        {"word": "手机", "pinyin": "shouji", "meaning": "mobile phone", "example": "打电话"},
    ],
    3: [{"word": "美丽", "pinyin": "meili", "meaning": "beautiful", "example": "美丽的风景"}],
    4: [{"word": "环境", "pinyin": "huanjing", "meaning": "environment", "example": "保护环境"}],
    5: [{"word": "复杂", "pinyin": "fuza", "meaning": "complex", "example": "很复杂"}],
    6: [{"word": "和谐", "pinyin": "hexie", "meaning": "harmony", "example": "社会和谐"}],
}

# Save vocabulary
with open('data/hsk_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(hsk_vocab, f, ensure_ascii=False, indent=2)

print("✅ Created data/hsk_vocab.json")
print(f"   Level 1: {len(hsk_vocab[1])} words")
print(f"   Level 2: {len(hsk_vocab[2])} words")
print(f"   Level 3: {len(hsk_vocab[3])} words")
print(f"   Level 4: {len(hsk_vocab[4])} words")
print(f"   Level 5: {len(hsk_vocab[5])} words")
print(f"   Level 6: {len(hsk_vocab[6])} words")
print("\n✅ Done! Now run: python server.py")