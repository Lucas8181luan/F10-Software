'''import pyautogui
import time
import pyperclip

time.sleep(5)

for i in range(30):
    #=========================== BUTÃO ADICIONAR ==================================#
    pyautogui.hotkey('Alt', 'o', 'i')  
    time.sleep(2)
    #============================= ABRIR EXCEL ====================================#
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(2)
    #============================== COPIA CPF =====================================#    
    for i in range(2):                                                                          
        pyautogui.hotkey('ctrl', 'c') # copia o "CPF"
        time.sleep(1)
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab') # F10
    time.sleep(5)
    pyautogui.press("tab")
    time.sleep(7)
    pyautogui.hotkey('ctrl', 'v') # colar o "CPF" copiado
    time.sleep(4)
    pyautogui.press("Enter")
    time.sleep(2)
    #============================ BUTÃO PROXIMO - 1 ====================================#
    for i in range(19):
        pyautogui.press('tab')
    time.sleep(2)
    #================================ PARTE - 2 ========================================#
    #================ TIPO DE CONTRATO ===================#
    def Tipo_de_Contarto():
        Tipo_de_Contarto = "Bolsa"
        return pyautogui.write(Tipo_de_Contarto)                                
    time.sleep(2)
    Tipo_de_Contarto()                              
    pyautogui.press("tab")
    time.sleep(2)
    #============ OPÇÃO - DATA DA MATRÍCULA ==============#
    #================================ ESCOLHER MATRÍCULA ======================================#
    def Matrícula():
        data_do_usuário = '06/06/2025'
        for i in range(10):
            pyautogui.press("Backspace")
        return pyautogui.write(data_do_usuário)
    Matrícula() 
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("tab") 
    #================ OPÇÃO - EVENTO =====================#
    def Evento():
        Evento = "1 - Educa.Rio"
        return pyautogui.write(Evento)
    Evento()
    time.sleep(2)
    pyautogui.press("tab") # TECLA "tab"
    #================= OPÇÃO - CURSO =====================#
    valor1 = 'Educa.Rio: Híbrido - Porteiro'
    def Curso(valor1):
        pyperclip.copy(valor1) # Copia o valor para a área de transferência
        pyautogui.hotkey('ctrl', 'v')       
    Curso(valor1)
    time.sleep(2)
    pyautogui.press("tab") # TECLA "tab"
    #=============== OPÇÃO - ADIMINISTRADO =================#
    def adm():
        adm = "Lucas Luan Pereira Vieira"
        return pyautogui.write(adm)
    adm()
    time.sleep(2)
    pyautogui.press("tab") # TECLA "tab"
    #=============== OPÇÃO - COORDENADOR =================#
    def Coordenador():
        Coordenador = "Marcus Vinicius Coppola Souto"
        return pyautogui.write(Coordenador)
    Coordenador()
    time.sleep(2)
    #============================ BUTÃO PROXIMO - 2 ====================================#
    def BUTÃO_PROXIMO_2():
        for i in range(5):
            pyautogui.press('tab')
    BUTÃO_PROXIMO_2()
    time.sleep(2)
    #================================ PARTE - 3 ========================================#
    pyautogui.press('space')
    def polo():
        for i in range(2):
            pyautogui.press("tab")
        Polo = "RJ - Educa.Rio"
        pyautogui.write(Polo)
    time.sleep(2) 
    polo()                          
    #============================ BUTÃO GRAVAR ====================================# 
    def BUTÃO_GRAVAR():
        for i in range(6):
            pyautogui.press('tab')
        pyautogui.press("Enter")
    BUTÃO_GRAVAR()
    #============================================== EXCEL ====================================================#
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(3) 
    for i in range(1): 
        pyautogui.press("left")
    pyautogui.press("space")
    time.sleep(1)
    pyautogui.press("down")
    for i in range(1):
        pyautogui.press("right") # Voltar para o proximo CPF
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab') # F10
    time.sleep(5)

import pyautogui
import time
import pyperclip

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

import pyautogui
import time
import pyperclip

time.sleep(5)

for i in range(90):
    #=========================== BUTÃO ADICIONAR ==================================#
    pyautogui.hotkey('Alt', 'o', 'i')  
    time.sleep(3)
    #============================= ABRIR EXCEL ====================================#
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(3)
    #============================== COPIA CPF =====================================#
    for i in range(2):
        pyautogui.hotkey('ctrl', 'c') # copia o "CPF"
        time.sleep(1)
    time.sleep(3)
    pyautogui.hotkey('alt', 'tab') # F10
    time.sleep(12)
    pyautogui.press("tab")
    time.sleep(8)
    pyautogui.hotkey('ctrl', 'v') # colar o "CPF" copiado
    time.sleep(4)
    pyautogui.press("Enter")
    time.sleep(3)
    #============================ BUTÃO PROXIMO - 1 ====================================#
    for i in range(19):
        pyautogui.press('tab')
    time.sleep(3)
    #================================ PARTE - 2 ========================================#
    #================ TIPO DE CONTRATO ===================#
    def Tipo_de_Contarto():
        Tipo_de_Contarto = "Bolsa"
        return pyautogui.write(Tipo_de_Contarto)
    time.sleep(3)
    Tipo_de_Contarto()
    pyautogui.press("tab")
    time.sleep(3)
    #============ OPÇÃO - DATA DA MATRÍCULA ==============#
    #================================ ESCOLHER MATRÍCULA ======================================#
    def Matrícula():
        data_do_usuário = '11/06/2025'
        for i in range(10):
            pyautogui.press("Backspace")
        return pyautogui.write(data_do_usuário)
    Matrícula()
    time.sleep(3)
    pyautogui.press("tab")
    pyautogui.press("tab")  
    #================ OPÇÃO - EVENTO =====================#
    def Evento():
        Evento = "4 - Preparatório Encceja"
        return pyautogui.write(Evento)
    Evento()
    time.sleep(3)
    pyautogui.press("tab") # TECLA "tab"
    #================= OPÇÃO - CURSO =====================#
    valor1 = '1 - Preparatório Encceja: Presencial - Encceja 2025'
    def Curso(valor1):
        pyperclip.copy(valor1) # Copia o valor para a área de transferência
        pyautogui.hotkey('ctrl', 'v')
    Curso(valor1)
    time.sleep(3)
    pyautogui.press("tab") # TECLA "tab"
    #=============== OPÇÃO - ADIMINISTRADO =================#
    def adm():
        adm = "Lucas Luan Pereira Vieira"
        return pyautogui.write(adm)
    adm()
    time.sleep(3)
    pyautogui.press("tab") # TECLA "tab"
    #=============== OPÇÃO - COORDENADOR =================#
    def Coordenador():
        Coordenador = "Marcus Vinicius Coppola Souto"
        return pyautogui.write(Coordenador)
    Coordenador()
    time.sleep(2)
    #============================ BUTÃO PROXIMO - 2 ====================================#
    def BUTÃO_PROXIMO_2():
        for i in range(5):
            pyautogui.press('tab')
    BUTÃO_PROXIMO_2()
    time.sleep(3)
    #================================ PARTE - 3 ========================================#
    pyautogui.press('space')
    def polo():
        for i in range(2):
            pyautogui.press("tab")
        Polo = "RJ - Preparatório Encceja"
        pyautogui.write(Polo)
    time.sleep(3) 
    polo()                          
    #============================ BUTÃO GRAVAR ====================================# 
    def BUTÃO_GRAVAR():
        for i in range(6):
            pyautogui.press('tab')
        pyautogui.press("Enter")
    BUTÃO_GRAVAR()
    #============================================== EXCEL ====================================================#
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(3) 
    for i in range(1): 
        pyautogui.press("left")
    pyautogui.press("space")
    time.sleep(3)
    pyautogui.press("down")
    for i in range(1):
        pyautogui.press("right") # Voltar para o proximo CPF
    time.sleep(3)
    pyautogui.hotkey('alt', 'tab') # F10
    time.sleep(5)

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
    pyautogui.press("down")'''


import pyautogui
import time

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
    for i in range(2):
        pyautogui.press("left")
    time.sleep(2)
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.press("down")
    time.sleep(2)
    for i in range(2):
        pyautogui.press("right")
    time.sleep(2)

    time.sleep(30)
    