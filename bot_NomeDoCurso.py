import pyautogui as py
import time

def executar_bot_curso():
    """Função principal para executar o bot de nome do curso"""
    time.sleep(5)

    py.press("Enter")
    time.sleep(1)

    py.press("tab")
    time.sleep(1)

    py.hotkey("ctrl", "v")
    time.sleep(1)

    for i in range(28):
        py.press("tab")
    time.sleep(1)

    for i in range(2):
        py.press("Enter")
    time.sleep(1)

    py.press("down")
    time.sleep(1)

# Executar apenas se chamado diretamente
if __name__ == "__main__":
    executar_bot_curso()
