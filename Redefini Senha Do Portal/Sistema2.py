import pyautogui
import time
import pyperclip

def executar_redefinir_senha():
    """Função principal para redefinir senha"""
    for i in range(3):
        pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("Apps")
    time.sleep(2)
    for i in range(3):
        pyautogui.press("down")
    time.sleep(2)
    for i in range(5):
        pyautogui.press("Enter")
    time.sleep(2)
    pyautogui.press("Right")
    time.sleep(2)
    pyautogui.press("Enter")
    time.sleep(2)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.press("down")
    time.sleep(2)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(2)
    pyautogui.press("down")
    time.sleep(2)

# Executar apenas se chamado diretamente
if __name__ == "__main__":
    executar_redefinir_senha()
