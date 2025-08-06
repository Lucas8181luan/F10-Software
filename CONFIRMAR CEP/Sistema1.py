import pyautogui
import time

def executar_confirmar_cep():
    """Função principal para confirmar CEP"""
    time.sleep(5)

    for i in range(400):
        pyautogui.press("Apps")
        time.sleep(1)
        for j in range(4):
            pyautogui.press("down")
        time.sleep(1)
        for k in range(2):
            pyautogui.press("Enter")
        time.sleep(1)
        pyautogui.press("Right")
        time.sleep(12)
        for l in range(5):
            pyautogui.press("Tab")
        time.sleep(1)
        pyautogui.press("Enter")
        time.sleep(1)
        pyautogui.press("down")

# Executar apenas se chamado diretamente
if __name__ == "__main__":
    executar_confirmar_cep()
