# agent.py

from openai import OpenAI
client = OpenAI(api_key="")  # Replace with your actual OpenAI API key
def start_chat(username):
    print(f"\n🧠 Chat started for {username}. Type 'exit' to quit.\n")

    history = []
    plain_history = []
    
    def print_chat_history(plain_history, username):
        print("📝 Full Conversation:\n" + "-"*50)
        for speaker, message in plain_history:
            print(f"{speaker}:")
            print(f"  {message}\n")
        print("-"*50 + "\n✅ Session Complete.\n")


    while True:
        user_input = input(f"{username}: ").strip()

        if user_input.lower() in ("exit", "quit"):
            print("\n👋 Chat ended. Here's your full chat history:\n")
            print_chat_history(plain_history, username)
            break

        history.append({"role": "user", "content": user_input})
        plain_history.append((username, user_input))

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=history
            )
            reply = response.choices[0].message.content
            print(f"AI: {reply}\n")

            history.append({"role": "assistant", "content": reply})
            plain_history.append(("AI", reply))

        except Exception as e:
            print(f"⚠️ Error: {e}")
            break

