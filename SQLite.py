import sqlite3
import json


con = sqlite3.connect('data.db')
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT
            )
""")
    
con.commit()

def save_message(role, content):
    cur.execute(
    "INSERT INTO messages (role, content) VALUES (?, ?)",
    (role, content)
    )
    con.commit()

def load_messages():
    cur.execute("SELECT role, content FROM messages")
    return cur.fetchall()

rows = load_messages()
for role, content in rows:
    print(role, ':', content)

messages = [{
    "role" : role,
    "content" : content
} for role, content in rows]

with open('json_file.json', 'w') as f:
    json.dump(messages, f, indent=4)