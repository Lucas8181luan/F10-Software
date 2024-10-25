import pyautogui
import time

#============================== ACHAR POSITION ========================================#
def achar_position():
    time.sleep(5)
    posição = pyautogui.position()
    print(f"POSITION: \033[32m{posição}\033[0m")


def marcar_ok():
    for i in range(3): 
        pyautogui.press("right") # mover para marca OK
    pyautogui.press("space")


def voltar_para_cpf():
    for i in range(3): 
        pyautogui.press("left") # voltar para o cpf 


def proximo_cpf():
    pyautogui.press("down")

achar_position()
 