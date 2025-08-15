import subprocess
import sys
import os

def launch_chat_sessions(num_sessions):
    project_dir = os.path.dirname(os.path.abspath(__file__))  # full path to current directory

    for i in range(num_sessions):
        if sys.platform.startswith('win'):
            # Windows
            subprocess.Popen(
                ['start', 'cmd', '/k', f'venv\\Scripts\\python main.py'],
                cwd=project_dir,
                shell=True
            )
        elif sys.platform.startswith('darwin'):
            # macOS
            subprocess.Popen(
                ['open', '-a', 'Terminal.app', 'main.py'],
                cwd=project_dir
            )
        elif sys.platform.startswith('linux'):
            # Linux (Gnome-based)
            subprocess.Popen(
                ['gnome-terminal', '--', 'python3', 'main.py'],
                cwd=project_dir
            )
        else:
            print("❌ Unsupported OS.")
            return

if __name__ == "__main__":
    try:
        count = int(input("🔢 How many chat sessions do you want to start? ").strip())
        if count <= 0:
            print("❌ Please enter a number greater than 0.")
        else:
            launch_chat_sessions(count)
    except ValueError:
        print("❌ Invalid number. Please enter an integer.")
