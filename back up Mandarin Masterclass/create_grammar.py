# create_grammar.py - Run this once to create hsk_grammar.json
import json

grammar_data = {
    "1": [
        {"point": "SVO word order", "pattern": "Subject + Verb + Object", "example": "我爱你", "explanation": "Chinese uses Subject-Verb-Object word order."},
        {"point": "是 (shì) - to be", "pattern": "A + 是 + B", "example": "我是学生", "explanation": "Links a noun with its identity."},
        {"point": "有 (yǒu) - to have", "pattern": "Subject + 有 + Object", "example": "我有一个哥哥", "explanation": "Indicates possession or existence."},
        {"point": "在 (zài) - to be at", "pattern": "Subject + 在 + Place", "example": "我在北京", "explanation": "Indicates location."},
        {"point": "吗 questions", "pattern": "Statement + 吗", "example": "你好吗？", "explanation": "Add 吗 to make a yes/no question."},
        {"point": "不 (bù) negation", "pattern": "不 + Verb/Adjective", "example": "我不是老师", "explanation": "Negates verbs and adjectives."}
    ],
    "2": [
        {"point": "比 (bǐ) comparison", "pattern": "A + 比 + B + Adjective", "example": "我比你高", "explanation": "Makes comparisons."},
        {"point": "会 (huì) - can", "pattern": "Subject + 会 + Verb", "example": "我会说汉语", "explanation": "Indicates learned ability."}
    ],
    "3": [
        {"point": "把 (bǎ) construction", "pattern": "Subject + 把 + Object + Verb", "example": "我把书放在桌子上", "explanation": "Emphasizes handling of an object."},
        {"point": "虽然...但是...", "pattern": "虽然 + A + 但是 + B", "example": "虽然很累，但是很开心", "explanation": "Although... but..."}
    ],
    "4": [
        {"point": "即使...也...", "pattern": "即使 + A + 也 + B", "example": "即使很难也要试", "explanation": "Even if... still..."},
        {"point": "只要...就...", "pattern": "只要 + A + 就 + B", "example": "只要努力就能成功", "explanation": "As long as... then..."}
    ],
    "5": [
        {"point": "从而", "pattern": "A + 从而 + B", "example": "从而获得成功", "explanation": "Thus / thereby."}
    ],
    "6": [
        {"point": "综上所述", "pattern": "综上所述 + Summary", "example": "综上所述，我们需要努力", "explanation": "To sum up."}
    ]
}

with open('hsk_grammar.json', 'w', encoding='utf-8') as f:
    json.dump(grammar_data, f, ensure_ascii=False, indent=2)

print("✅ hsk_grammar.json created successfully!")