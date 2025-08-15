# main.py

import getpass
from agent import start_chat

# Hardcoded user credentials
users = {
    "dua": "1234",
    "john": "abcd",
    "alice": "xyz"
}

def authenticate():
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ").strip()

    if username in users and users[username] == password:
        print(f"✅ Welcome, {username}!\n")
        return username
    else:
        print("❌ Invalid credentials. Exiting.")
        return None

if __name__ == "__main__":
    user = authenticate()
    if user:
        start_chat(user)
