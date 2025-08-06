import pyautogui
import time
import pyperclip

# Configurações de segurança do pyautogui
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

def executar_encj():
    """Função principal para executar a automação ENCJ"""
    time.sleep(5)

    for i in range(32):
        #=========================== BUTÃO ADICIONAR ==================================#                                                                Bolsa  
        pyautogui.hotkey('Alt', 'o', 'i') 
        time.sleep(0.30)
        #============================= ABRIR EXCEL ====================================#
        pyautogui.hotkey('alt', 'tab') # Chrome
        time.sleep(1)
        #============================== COPIA CPF =====================================#
        for j in range(2):
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
        #============================ BUTÃO PROXIMO - 1 ====================================#
        for k in range(17):
            pyautogui.press('tab')
        time.sleep(1)
        #=============================== PARTE - 2 =========================================#
        #================ TIPO DE CONTRATO ===================#
        def Tipo_de_Contarto():
            Tipo_de_Contarto = "Bolsa"
            return pyautogui.write(Tipo_de_Contarto)
        time.sleep(4)
        Tipo_de_Contarto()
        pyautogui.press("tab")
        time.sleep(0.5)
        #============ OPÇÃO - DATA DA MATRÍCULA ==============#
        #================================ ESCOLHER MATRÍCULA ======================================#
        def Matrícula():
            data_do_usuário = '24/07/2025'
            for m in range(10):
                pyautogui.press("Backspace")
            return pyautogui.write(data_do_usuário)
        Matrícula()
        time.sleep(0.5)
        pyautogui.press("tab")
        pyautogui.press("tab") 
        #================ OPÇÃO - EVENTO =====================#
        def Evento():
            Evento = "4 - Preparatório Encceja"
            return pyautogui.write(Evento)
        Evento()
        time.sleep(0.5)
        pyautogui.press("tab") # TECLA "tab"
        #================= OPÇÃO - CURSO =====================#
        valor1 = '1 - Preparatório Encceja: Presencial - Encceja 2025'
        def Curso(valor1):
            pyperclip.copy(valor1) # Copia o valor para a área de transferência
            pyautogui.hotkey('ctrl', 'v')
        Curso(valor1)
        time.sleep(0.5)
        pyautogui.press("tab") # TECLA "tab"
        #=============== OPÇÃO - ADIMINISTRADO =================#
        def adm():
            adm = "Lucas Luan Pereira Vieira"
            return pyautogui.write(adm)
        adm()
        time.sleep(0.5)
        pyautogui.press("tab") # TECLA "tab"
        #=============== OPÇÃO - COORDENADOR =================#
        def Coordenador():
            Coordenador = "Marcus Vinicius Coppola Souto"
            return pyautogui.write(Coordenador)
        Coordenador()
        time.sleep(0.5)
        #============================ BUTÃO PROXIMO - 2 ====================================#
        def BUTÃO_PROXIMO_2():
            for n in range(5):
                pyautogui.press('tab')
        BUTÃO_PROXIMO_2()
        time.sleep(0.30)
        #================================ PARTE - 3 ========================================#
        pyautogui.press('space')
        def polo():
            for o in range(2):
                pyautogui.press("tab")
            Polo = "RJ - Preparatório Encceja"
            pyautogui.write(Polo)
            time.sleep(0.5)
        time.sleep(0.30)
        polo()                          
        #============================ BUTÃO GRAVAR ====================================# 
        def BUTÃO_GRAVAR():
            for p in range(6):
                pyautogui.press('tab')
            pyautogui.press("Enter")
        BUTÃO_GRAVAR()
        #============================================== EXCEL ====================================================#
        pyautogui.hotkey('alt', 'tab') # Chrome
        time.sleep(3) 
        for q in range(1): 
            pyautogui.press("left")
        pyautogui.press("space")
        time.sleep(0.5)
        pyautogui.press("down")
        for r in range(1):
            pyautogui.press("right") # Voltar para o proximo CPF
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'tab') # F10
        time.sleep(0.5)

# Executar apenas se chamado diretamente
if __name__ == "__main__":
    executar_encj()
