from SQLite import save_message, load_messages
from ollama import chat

def build_history():
    #builds history (ofc dummy)
    rows = load_messages()
    messages = [{
        "role" : role,
        "content" : content
    } for role, content in rows]

    return messages

def main_chat():
    #Building the AI's personality
    messages = build_history()

    messages.insert(0, {
        "role" : "system",
        "content" : "You are a calm AI therapist. Don't diagnose. Ask thoughtful questions. If someone says they're thinking of doing self-harm, redirect them to not do that them to talk to an trusted adult. Tell them to not use you as a replacement for real therapy. Don't judge for someone being themselves. Also be straight-forward. Dont confuse the user."
    })


    #real loop (the thing that the user will see)
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            break

        if user_input == "":
            continue
        
        print("Greg is loading a response to you. Please do not exit or close the terminal.")

        messages.append({
            "role" : "user",
            "content" : user_input
        })

        response = chat(
            model="qwen2.5:3b",
            messages=messages
        )
        #removes the messy stuff the LLM outputs to.
        reply = response["message"]["content"]

        #prints the AI response
        print() #for a cleaner look
        print(f'Greg: {reply}')
        #saves the AI response
        save_message("assistant:" ,reply)
        messages.append({"role" : "assistant", "content" : reply})

#Runs the program
if __name__ == '__main__':
    main_chat()
