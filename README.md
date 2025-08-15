Multi-Session Authenticated Chatbot
==================================

📌 Overview
-----------
This project implements a secure, multi-session terminal chatbot using the OpenAI GPT API.
It allows authenticated users to interact with an AI assistant in separate, concurrent chat windows, with full conversation history tracking.

The system is designed to mimic multi-agent support tools, where multiple users can engage with an AI simultaneously - a feature useful in call centers, HR helpdesks, and multi-client AI services.

🚀 Features
-----------
- User Authentication
  - Predefined username/password credentials
  - Prevents unauthorized access

- Chat Interface with Conversation History
  - AI responses generated using gpt-4o model
  - Full conversation log displayed after each session

- Multi-Session Launch
  - Launch multiple chat windows in parallel
  - OS-specific support for Windows, macOS, and Linux

- Clean Separation of Concerns
  - agent.py → Chat logic and AI communication
  - main.py → Authentication and session start
  - launcher.py → Spawns multiple terminal-based chatbots

🛠️ File Structure
-----------------
├── agent.py       # Core chat loop with AI integration
├── main.py        # User authentication and chat start logic
├── launcher.py    # Launch multiple chat sessions in parallel

📂 Code Flow
------------

1️⃣ Authentication (main.py)
- Prompts the user for username and password
- Validates against hardcoded credentials
- If valid → Starts a chat session for that user
- If invalid → Exits the program

2️⃣ Chat Loop (agent.py)
- Prints a welcome message for the authenticated user
- Maintains:
  - history → Structured chat history for OpenAI API
  - plain_history → Human-readable conversation log
- Sends user input to OpenAI GPT API
- Displays AI response
- Continues until the user types exit or quit
- On exit → Prints the entire conversation history

3️⃣ Multi-Session Launcher (launcher.py)
- Asks how many chat sessions to start
- Launches multiple terminal windows, each running an independent main.py session
- Handles OS-specific commands for:
  - Windows
  - macOS
  - Linux (Gnome)

⚙️ Installation & Usage
-----------------------

1. Clone the Repository
git clone https://github.com/<your-username>/Multi-Session-Authenticated-Chatbot.git
cd Multi-Session-Authenticated-Chatbot

2. Install Dependencies
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

pip install openai

3. Set OpenAI API Key
In agent.py, replace:
client = OpenAI(api_key="")
with:
client = OpenAI(api_key="YOUR_API_KEY")

4. Run a Single Session
python main.py

5. Run Multiple Sessions
python launcher.py

🎯 Portfolio Value
-----------------
This project demonstrates:
- Secure authentication implementation in Python
- Stateful conversation handling with LLMs
- Multi-process session management
- OS-specific scripting for automation
- Clear separation of logic for maintainability

By combining these concepts, this chatbot framework can be adapted for:
- HR policy assistants
- Multi-customer AI support tools
- Real-time AI-assisted operations
