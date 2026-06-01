# Mandarin Masterclass

Complete HSK 1-6 Chinese learning platform with:
- Passcode access system (admin approval)
- Expiry settings (hours/days/weeks)
- Device limit (2 devices per user)
- History tracking
- AI teacher assistant
- Text-to-speech pronunciation
- Writing practice with HanziWriter

## Tech Stack
- Flask backend
- JSON lesson files (146 lessons total)
- edge-tts for audio
- DeepSeek/Ollama for AI

## Deployment
- Render.com (free tier available)
- See render.yaml for config

## Files
- server.py - Main application
- templates/ - All HTML templates
- templates/data/ - HSK 1-6 lesson JSON files