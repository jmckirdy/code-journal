import subprocess
from datetime import datetime

def get_git_commit_messages():
    try:
        # Run git log command to get commit messages
        git_log = subprocess.check_output(['git', 'log', '--pretty=%s'])
        return git_log.decode('utf-8').strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return []

def append_to_log(log_file, messages):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, 'a') as file:
        file.write(f"\n\n===== {timestamp} =====\n")
        for message in messages:
            file.write(f"- {message}\n")

if __name__ == "__main__":
    log_file = "git_commit_log.txt"
    commit_messages = get_git_commit_messages()

    if commit_messages:
        append_to_log(log_file, commit_messages)
        print("Commit messages added to the log.")
    else:
        print("No commit messages found.")
