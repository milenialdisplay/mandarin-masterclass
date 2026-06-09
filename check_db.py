# check_db.py
import psycopg2
import os
from urllib.parse import urlparse

# Get DATABASE_URL from environment or enter manually
DATABASE_URL = input("Paste your Render PostgreSQL DATABASE_URL: ")

try:
    conn = psycopg2.connect(DATABASE_URL)
    c = conn.cursor()
    
    print("\n=== USERS TABLE ===")
    c.execute('SELECT email, lesson_key, passcode FROM users LIMIT 10')
    for row in c.fetchall():
        print(f"Email: {row[0]}, Lesson: {row[1]}, Passcode: '{row[2]}'")
    
    print("\n=== REQUESTS TABLE ===")
    c.execute('SELECT email, level, lesson_num, passcode, status FROM requests ORDER BY created_at DESC LIMIT 10')
    for row in c.fetchall():
        print(f"Email: {row[0]}, HSK{row[1]} L{row[2]}, Passcode: '{row[3]}', Status: {row[4]}")
    
    conn.close()
    print("\n✅ Database check complete")
    
except Exception as e:
    print(f"Error: {e}")