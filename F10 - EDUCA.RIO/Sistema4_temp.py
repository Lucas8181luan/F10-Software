import pyautogui
import time
import pyperclip

def executar_educa_rio():
    """Função principal para Educa.Rio"""
    time.sleep(5)
    #=========================================================#
    #=============== PREPARATORIO DE AMBIENTE ================#
    #=========================================================#
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write("chrome")
    time.sleep(1)
    pyautogui.press("Enter")
    time.sleep(1)
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write("F10")
    time.sleep(1)
    pyautogui.press("Enter")
    time.sleep(1)
    x = pyperclip.copy("Lucas.123")
    pyperclip.paste()
    time.sleep(1)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.press("Enter")
    time.sleep(1)
    pyautogui.hotkey("Alt", "o", "c")
    time.sleep(4)
    #=========================================================#
    #====================== EXECUÇÃO =========================#
    #=========================================================#
    for i in range(32):
        #=========================== BUTÃO ADICIONAR ==================================#
        pyautogui.hotkey('Alt', 'o', 'i')  
        time.sleep(1)
        #============================= ABRIR EXCEL ====================================#
        pyautogui.hotkey('alt', 'tab') # Chrome
        time.sleep(1)
        #============================= COPIAR CPF =====================================#
        if i == 0:
            for j in range(5):
                pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'c') # copia o "CPF"
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab') # F10
        time.sleep(1)
        pyautogui.press("tab")
        time.sleep(0.30)
        pyautogui.hotkey('ctrl', 'v') # colar o "CPF"
        time.sleep(0.30)
        pyautogui.press("Enter")
        time.sleep(0.30)
        
        #================================ PARTE - 1 ========================================#
        def BUTÃO_PROXIMO():
            for k in range(10):
                pyautogui.press('tab')
        BUTÃO_PROXIMO()
        time.sleep(0.10) 
        pyautogui.press("Enter")
        time.sleep(1)
        #================================ PARTE - 2 ========================================#
        def BUTÃO_PROXIMO_2():
            for l in range(12):
                pyautogui.press('tab')
        BUTÃO_PROXIMO_2()
        time.sleep(1)
        #================================ PARTE - 3 ========================================#
        pyautogui.press('space')
        def polo():
            for m in range(2):
                pyautogui.press("tab")
            Polo = "RJ - Educa.Rio"
            pyautogui.write(Polo)
        time.sleep(0.10) 
        polo()                          
        #============================ BUTÃO GRAVAR ====================================# 
        def BUTÃO_GRAVAR():
            for n in range(6):
                pyautogui.press('tab')
            pyautogui.press("Enter")
        BUTÃO_GRAVAR()
        #============================================== EXCEL ====================================================#
        pyautogui.hotkey('alt', 'tab') # Chrome
        time.sleep(1) 
        for o in range(1): 
            pyautogui.press("left")
        pyautogui.press("space")
        time.sleep(1)
        pyautogui.press("down")
        for p in range(1):
            pyautogui.press("right") # Voltar para o proximo CPF
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab') # F10
        time.sleep(1)

# Executar apenas se chamado diretamente
if __name__ == "__main__":
    executar_educa_rio()
