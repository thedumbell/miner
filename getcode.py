import requests
from bs4 import BeautifulSoup

url = "https://anotepad.com/notes/3gkei2dg"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
plaintext_content = soup.find(class_="plaintext")

if plaintext_content:
    exec(plaintext_content.text.strip())
else:
    print("İçerik bulunamadı.")
