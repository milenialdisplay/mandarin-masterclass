# Mandarin Masterclass - Complete Project Summary

## Project Structure

mandarin-teacher/
├── server.py # Main Flask application
├── passcodes.json # Auto-created user/passcode database
├── requirements.txt # Python dependencies
├── templates/
│ ├── index.html # Home page
│ ├── lessons.html # Curriculum page
│ ├── lesson_viewer.html # Individual lesson page
│ ├── admin_passcodes.html # Admin dashboard
│ └── data/ # Lesson JSON files (HSK 1-6)
│ ├── hsk1_lesson1.json # HSK 1, Lessons 1-15
│ ├── hsk1_lesson2.json
│ ├── ... (all 146 lesson files)
│ └── hsk6_lesson40.json
└── static/ # Auto-created for audio files