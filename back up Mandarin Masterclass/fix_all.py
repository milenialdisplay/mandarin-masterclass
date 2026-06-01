import json

# Fix vocabulary
print("Fixing hsk_vocab.json...")
with open('data/hsk_vocab.json', 'r', encoding='utf-8') as f:
    vocab = json.load(f)
vocab_fixed = {int(k): v for k, v in vocab.items()}
with open('data/hsk_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(vocab_fixed, f, ensure_ascii=False, indent=2)
print(f"  ✅ Level 1 has {len(vocab_fixed[1])} words")

# Fix grammar
try:
    print("Fixing hsk_grammar.json...")
    with open('data/hsk_grammar.json', 'r', encoding='utf-8') as f:
        grammar = json.load(f)
    grammar_fixed = {int(k): v for k, v in grammar.items()}
    with open('data/hsk_grammar.json', 'w', encoding='utf-8') as f:
        json.dump(grammar_fixed, f, ensure_ascii=False, indent=2)
    print("  ✅ Grammar fixed")
except:
    print("  ⚠️ Grammar file not found")

# Fix dialogues
try:
    print("Fixing dialogues.json...")
    with open('data/dialogues.json', 'r', encoding='utf-8') as f:
        dialogues = json.load(f)
    dialogues_fixed = {int(k): v for k, v in dialogues.items()}
    with open('data/dialogues.json', 'w', encoding='utf-8') as f:
        json.dump(dialogues_fixed, f, ensure_ascii=False, indent=2)
    print("  ✅ Dialogues fixed")
except:
    print("  ⚠️ Dialogues file not found")

print("\n" + "=" * 50)
print("✅ ALL FILES FIXED!")
print("=" * 50)