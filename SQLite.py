import sqlite3
import json

#variables we will need here
con = sqlite3.connect('data.db')
cur = con.cursor()

#creates the db (database)
cur.execute("""
    CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT
            )
""")
    
con.commit()

#function to save the messages. We will use this in the Main.py file
def save_message(role, content):
    cur.execute(
    "INSERT INTO messages (role, content) VALUES (?, ?)",
    (role, content)
    )
    con.commit()
#loads the messages. We will also use this function in the Main.py file
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

#Creates a .json file.
with open('json_file.json', 'w') as f:
    json.dump(messages, f, indent=4)