import pyautogui
import time
import pyperclip

time.sleep(5)

for i in range(32):
    #=========================== BUTÃO ADICIONAR ==================================#
    pyautogui.hotkey('Alt', 'o', 'i')  
    time.sleep(1)
    #============================= ABRIR EXCEL ====================================#
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(1)
    #============================== COPIA CPF =====================================#
    for i in range(2):
        pyautogui.hotkey('ctrl', 'c') # copia o "CPF"
        time.sleep(1)
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab') # F10
    time.sleep(1)     
    pyautogui.press("tab") 
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') # colar o "CPF" copiado
    time.sleep(1)
    pyautogui.press("Enter")
    time.sleep(1)
    #============================ BUTÃO PROXIMO - 1 ====================================#
    for i in range(17):
        pyautogui.press('tab')
    time.sleep(2)
    #================================ PARTE - 2 ========================================#
    #================ TIPO DE CONTRATO ===================#
    def Tipo_de_Contarto():
        Tipo_de_Contarto = "Bolsa"
        return pyautogui.write(Tipo_de_Contarto)
    time.sleep(4)
    Tipo_de_Contarto()
    pyautogui.press("tab")
    time.sleep(0.10)
    #============ OPÇÃO - DATA DA MATRÍCULA ==============#
    #================================ ESCOLHER MATRÍCULA ======================================#
    def Matrícula():
        data_do_usuário = '27/06/2025'
        for i in range(10):
            pyautogui.press("Backspace")
        return pyautogui.write(data_do_usuário)
    Matrícula() 
    time.sleep(0.10)
    pyautogui.press("tab")
    pyautogui.press("tab") 
    #================ OPÇÃO - EVENTO =====================#
    def Evento():
        Evento = "1 - Educa.Rio"
        return pyautogui.write(Evento)
    Evento()
    time.sleep(0.10)
    pyautogui.press("tab") # TECLA "tab"
    #================= OPÇÃO - CURSO =====================#
    #======== COPIA CURSO =========#
    pyautogui.hotkey('alt', 'tab') # Chrome
    for i in range(2):
        pyautogui.press("left")
    time.sleep(0.10)
    for i in range(2):
        pyautogui.hotkey('ctrl', 'c') # copia o "Curso"
    x = pyperclip.paste()
    if x == "FALSE":
        pyautogui.press("left")
        pyautogui.hotkey('ctrl', 'c') # copia o "Curso"
        x = pyperclip.paste()
    time.sleep(0.10)
    for i in range(2):
        pyautogui.press("Right")
    pyautogui.hotkey('alt', 'tab') # F10
    time.sleep(0.10)
    valor1 = x
    def Curso(v):
        valor = str(v)
        print(valor)
        pyautogui.press("space")
        if valor == "EAD - AGENTE DE DEFESA AMBIENTAL":
            return pyautogui.write("Educa.Rio: EAD - Agente de Defesa Ambiental")
        if valor == "EAD - ASSISTENTE DE LOGÍSTICA":
            return pyautogui.write("Educa.Rio: EAD - Assistente de Logistica")
        if valor == "EAD - ESTOQUISTA":
            return pyautogui.write("Educa.Rio: EAD - Estoquista")
        if valor == "HÍBRIDO - AUXILIAR ADMINISTRATIVO":
            return pyautogui.write("Educa.Rio: Hibrido - Auxiliar Administrativo")
        if valor == "HÍBRIDO - AUXILIAR DE COZINHA (BOTECO)" or valor == "PRESENCIAL - AUXILIAR DE COZINHA":
            return pyautogui.write("Educa.Rio: Presencial - Auxiliar de Cozinha")
        if valor == "HÍBRIDO - CUIDADOR DE IDOSO":
            return pyautogui.write("Educa.Rio: Hibrido - Cuidador de Idosos")
        if valor == "HÍBRIDO - DESIGNER DE SOBRANCELHA":
            return pyautogui.write("Educa.Rio: Hibrido - Designer de Sombrancelhas")
        if valor == "HÍBRIDO - INSTALADOR DE CARRO  ELÉTRICO":
            return pyautogui.write("Educa.Rio: Hibrido - Instalador de Carregador Veicular")
        if valor == "HÍBRIDO - MAQUIAGEM":
            return pyautogui.write("Educa.Rio: Hibrido - Maquiagem") 
        if valor == "HÍBRIDO - RECEPCIONISTA":
            return pyautogui.write("Educa.Rio: Hibrido - Recepcionista")
        if valor == "HÍBRIDO - OPERADOR DE CAIXA":
            return pyautogui.write("Educa.Rio: Hibrido - Operador de Caixa")
        if valor == "HÍBRIDO - PORTEIRO":
            return pyautogui.write("Educa.Rio: Hibrido - Porteiro")
        if valor == "HÍBRIDO - ATENDIMENTO DE FARMÁCIA":
            return pyautogui.write("Educa.Rio: Hibrido - Atendente de Farmacia")
        if valor == "HÍBRIDO - INSTALADOR FOTOVOLTAICO":
            return pyautogui.write("Educa.Rio: Hibrido - Instalador de Fotovoltaico")
        if valor == "HÍBRIDO - INFORMÁTICA":
            return pyautogui.write("Educa.Rio: Hibrido - Informatica")
        if valor == "PRESENCIAL - CUMIN":
            return pyautogui.write("Educa.Rio: Presencial - Cumin")
        if valor == "PRESENCIAL - GARÇOM":
            return pyautogui.write("Educa.Rio: Presencial - Garcom")
    Curso(valor1)
    time.sleep(0.10)
    pyautogui.press("tab") # TECLA "tab"
    #=============== OPÇÃO - ADIMINISTRADO =================#
    def adm():
        adm = "Lucas Luan Pereira Vieira"
        return pyautogui.write(adm)
    adm()
    time.sleep(0.10)
    pyautogui.press("tab") # TECLA "tab"
    #=============== OPÇÃO - COORDENADOR =================#
    def Coordenador():
        Coordenador = "Marcus Vinicius Coppola Souto"
        return pyautogui.write(Coordenador)
    Coordenador()
    time.sleep(0.10)
    #============================ BUTÃO PROXIMO - 2 ====================================#
    def BUTÃO_PROXIMO_2():
        for i in range(5):
            pyautogui.press('tab')
    BUTÃO_PROXIMO_2()
    time.sleep(1)
    #================================ PARTE - 3 ========================================#
    pyautogui.press('space')
    def polo():
        for i in range(2):
            pyautogui.press("tab")
        Polo = "RJ - Educa.Rio"
        pyautogui.write(Polo)
    time.sleep(0.10) 
    polo()                          
    #============================ BUTÃO GRAVAR ====================================# 
    def BUTÃO_GRAVAR():
        for i in range(6):
            pyautogui.press('tab')
        pyautogui.press("Enter")
    BUTÃO_GRAVAR()
    #============================================== EXCEL ====================================================#
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(1) 
    for i in range(1): 
        pyautogui.press("left")
    pyautogui.press("space")
    time.sleep(1)
    pyautogui.press("down")
    for i in range(1):
        pyautogui.press("right") # Voltar para o proximo CPF
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab') # F10
    time.sleep(1)
