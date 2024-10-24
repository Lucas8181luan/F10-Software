import pyautogui
import time

time.sleep(0.30)

posição = pyautogui.position()
print(f"POSITION: \033[32m{posição}\033[0m")
