from SQLite import save_message, load_messages
from ollama import chat

def build_history():
    rows = load_messages()
    messages = ({
        "role" : role,
        "content" : content
    } for role, content in rows)

    return messages

def main_chat():
    return
#INCOMPLETE YET!!!!
