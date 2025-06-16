import pyautogui
import time

time.sleep(5)

for i in range(400):

    pyautogui.press("Apps")
    time.sleep(1)
    for i in range(4):
        pyautogui.press("down")
    time.sleep(1)
    for i in range(2):
        pyautogui.press("Enter")
    time.sleep(1)
    pyautogui.press("Right")
    time.sleep(12)
    for i in range(5):
        pyautogui.press("Tab")
    time.sleep(1)
    pyautogui.press("Enter")
    time.sleep(1)
    pyautogui.press("down")
