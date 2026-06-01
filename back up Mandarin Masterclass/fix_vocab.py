import json

# Load the vocabulary file
with open('data/hsk_vocab.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Convert string keys to integers
fixed_data = {}
for key, value in data.items():
    fixed_data[int(key)] = value

# Save back to file
with open('data/hsk_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(fixed_data, f, ensure_ascii=False, indent=2)

print('=' * 50)
print('✅ Fixed! Now keys are integers')
print('=' * 50)
print('Keys:', list(fixed_data.keys()))
print('Level 1 has', len(fixed_data[1]), 'words')
print('=' * 50)