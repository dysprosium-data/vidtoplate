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
plates = []

def cls():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

#-- CLI
class col:
    black = "\033[0;30m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    brown = "\033[0;33m"
    blue = "\033[0;34m"
    purple = "\033[0;35m"
    cyan = "\033[0;36m"
    light_gray = "\033[0;37m"
    dark_gray = "\033[1;30m"
    light_red = "\033[1;31m"
    light_green = "\033[1;32m"
    yellow = "\033[1;33m"
    light_blue = "\033[1;34m"
    light_purple = "\033[1;35m"
    light_cyan = "\033[1;36m"
    light_white = "\033[1;37m"
    bold = "\033[1m"
    faint = "\033[2m"
    italic = "\033[3m"
    underline = "\033[4m"
    blink = "\033[5m"
    negative = "\033[7m"
    crossed = "\033[9m"
    end = "\033[0m"

class msg:
    init = col.blue + "[INIT]: " + col.end
    warn = col.red + "(WARN) " + col.end
    success = col.green + "(SUCCESS) " + col.end

#--

#-- Update script
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
                print(msg.init + "Updating vidtoplate...")
                update.update_local_file(LOCAL_FILE, github_content)
                print(msg.init + msg.success + "Update complete, restarting script")
                time.sleep(2)
            else:
                print(msg.init + msg.success + "Script up-to-date.")
        except Exception as e:
            print(msg.init + msg.warn + f"An error occurred: {e}")


def main():
    print("Starting vidtoplate")
    global updated
    updated = False
    update.main()
    if updated == True:
        os.execv(sys.executable, ['python3'] + sys.argv)
    print(msg.init + msg.success + "Update check passed")
    time.sleep(1)
    cls()
    print("Enter licence plate (BE CASE SENSITIVE)")
    plates.append(input(": "))
    while True:
        cls()
        print(f"Plates: {plates}")
        print("Enter another licence plate (or 'd' for done)")
        opt = input(": ")
        if opt == "d":
            break
        else:
            plates.append(opt)
    cls()
    print(plates)
    input("Press enter when your camera is ready")

main()
