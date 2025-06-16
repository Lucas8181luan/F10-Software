import pyautogui
import time

time.sleep(5)

for i in range(40):

    pyautogui.hotkey("shift", "space")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(2)
    pyautogui.hotkey("Alt", "tab")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press("down")
    time.sleep(2)
    pyautogui.hotkey("Alt", "tab")
    time.sleep(2)
    for i in range(2):
        pyautogui.press("left")
    time.sleep(2)
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.press("down")
    time.sleep(2)
    for i in range(2):
        pyautogui.press("right")
    time.sleep(2)

    time.sleep(30)
    