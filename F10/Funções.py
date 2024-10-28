import pyautogui
import time

#============================== ACHAR POSITION ========================================#
def achar_position():
    time.sleep(8)
    posição = pyautogui.position()
    print(f"POSITION: \033[32m{posição}\033[0m")


#============================= MARCAR "OK" =========================================#
def marcar_ok():
    for i in range(2): 
        pyautogui.press("left")
    pyautogui.press("space")


#================================ VOLTAR PARA O "CPF" =================================#
def voltar_para_cpf():
    for i in range(3): 
        pyautogui.press("left") 


#================================== PROXIMO "CPF" =====================================#
def proximo_cpf():
    pyautogui.press("down")


#=================================== COPIA "CEP" ======================================#
def copia_CEP():
    for i in range(5): 
        pyautogui.press("right") 


#=================================== APAGAR "CEP" =====================================#
def apagar_CEP():
    for i in range(10):
        pyautogui.press("Backspace")
