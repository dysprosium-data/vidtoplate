# vidtoplate
# Simple program to find licence plates from
# video stream
import requests
import os
import hashlib
import sys
import platform
import time
import datetime
class update:

    def get_github_file_content(repo, path):
        url = f"https://raw.githubusercontent.com/{repo}/main/{path}"
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def get_local_file_content(path):
        with open(path, 'r') as file:
            return file.read()

    def get_hash(content):
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    def update_local_file(path, content):
        with open(path, 'w') as file:
            file.write(content)

    def main():
        global updated
        GITHUB_REPO = "dysprosium-data/vidtoplate"
        FILE_PATH = "vidtoplate.py"
        LOCAL_FILE = "vidtoplate.py"


        try:
            github_content = update.get_github_file_content(GITHUB_REPO, FILE_PATH)
            local_content = update.get_local_file_content(LOCAL_FILE)
            
            if update.get_hash(github_content) != update.get_hash(local_content):
                print("Updating vidtoplate...")
                update.update_local_file(LOCAL_FILE, github_content)
                print("Update complete, restarting script")
                time.sleep(2)
            else:
                print("Script up-to-date.")
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    global updated
    updated = False
    update.main()
    if updated == True:
        os.execv(sys.executable, ['python3'] + sys.argv)

main()
