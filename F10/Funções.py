import pyautogui
import time

#============================== ACHAR POSITION ========================================#
def achar_position():
    time.sleep(5)
    posição = pyautogui.position()
    print(f"POSITION: \033[32m{posição}\033[0m")


#================================ MARCAR "OK" =========================================#
def marcar_ok():
    for i in range(3): 
        pyautogui.press("right")
    pyautogui.press("space")


#================================ VOLTAR PARA O "CPF" =================================#
def voltar_para_cpf():
    for i in range(3): 
        pyautogui.press("left") 


#================================== PROXIMO "CPF" =====================================#
def proximo_cpf():
    pyautogui.press("down")
