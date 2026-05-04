import sys
import os
import subprocess

def get_local_context():
    """Reads all Python files in the current folder to give Gemini context."""
    context = ""
    for file in os.listdir('.'):
        # We read other .py files, but NOT oracle.py itself
        if file.endswith('.py') and file != 'oracle.py':
            with open(file, 'r', encoding='utf-8') as f:
                context += f"\n--- FILE: {file} ---\n{f.read()}"
    return context

def run_oracle():
    # 1. Capture the error from the 'pipe' (|)
    print("🔮 The Oracle is listening to the terminal...")
    error_data = sys.stdin.read()
    
    if not error_data.strip():
        print(" No error detected in the pipe. Usage: [command] 2>&1 | python oracle.py")
        return

    # 2. Gather the project code
    code_context = get_local_context()

    # 3. Build the prompt
    prompt = (
        "ACT AS A SENIOR DEBUGGER. Below is a terminal error and my project code.\n"
        f"ERROR:\n{error_data}\n\n"
        f"PROJECT CODE:\n{code_context}\n\n"
        "IDENTIFY: Which file and line caused the error?\n"
        "FIX: Provide the corrected code block and a 1-sentence explanation."
    )

    # 4. Ask Gemini
    print(" Consulting the AI Oracle...")
    # 'shell=True' is needed for Windows to find the 'gemini' command
    subprocess.run(['gemini', prompt], shell=True)

if __name__ == "__main__":
    run_oracle()