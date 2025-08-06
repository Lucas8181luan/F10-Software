import pyautogui
import time

def executar_disparo_whatsapp():
    """Função principal para disparo WhatsApp"""
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
        for j in range(2):
            pyautogui.press("left")
        time.sleep(2)
        pyautogui.press("space")
        time.sleep(2)
        pyautogui.press("down")
        time.sleep(2)
        for k in range(2):
            pyautogui.press("right")
        time.sleep(2)

# Executar apenas se chamado diretamente
if __name__ == "__main__":
    executar_disparo_whatsapp()

    time.sleep(30)
