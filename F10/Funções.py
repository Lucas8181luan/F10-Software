import pyautogui
import time

#================================ ACHAR POSITION ======================================#
def achar_position():
    time.sleep(8)
    posição = pyautogui.position()
    print(f"POSITION: \033[32m{posição}\033[0m")


#=============================== PRENCHER CPF - F10 ===================================#
def prencher_cpf():
    pyautogui.press("down")
    time.sleep(0.20)
    pyautogui.press("Enter")


#================================ ACHAR CEP - F10 =====================================#
def achar_cep():
    pyautogui.press("Enter")
    time.sleep(0.10)
    for i in range(6):
        pyautogui.press("tab")


#================================== MARCAR "OK" =======================================#
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


#================================ DIRECIONAR USUÁRIO ==================================#
def Direcionar_usuário():
    print("\033[93m=" * 40)
    print("ABRA A JANELA DO \033[0m'GOOGLE CHROME'\033[0m".center(40))
    for i in range(11):
        print(f"--> {i}")
        time.sleep(1)
    print("\033[93m=" * 40)
    print("ABRA A JANELA DO \033[0m'F10'\033[0m \033[93mE PERMANECAR NELA\033[0m".center(40))
    for i in range(11):
        print(f"--> {i}")
        time.sleep(1)
    print("\033[92m=" * 40)
    print("PROGRAMA RODANDO...".center(40))
    print("\033[92m=" * 40)


#================================= ESCOLHER CONTRATO ====================================#
def Tipo_de_Contarto():
    Tipo_de_Contarto = "Bolsa"
    return pyautogui.write(Tipo_de_Contarto)


#================================= ESCOLHER MATRÍCULA ===================================#
def Matrícula(valor):
    data_do_usuário = valor
    for i in range(10):
        pyautogui.press("Backspace")
    return pyautogui.write(data_do_usuário)


#================================== ESCOLHER EVENTO =====================================#
def Evento():
    Evento = "RIO+CURSOS"
    return pyautogui.write(Evento)


#================================ ESCOLHER COORDENADOR ===================================#
def Coordenador():
    Coordenador = "Rodrigo Drumond"
    return pyautogui.write(Coordenador)


#=================================== ESCOLHER POLO =======================================#
def polo():
    for i in range(9):
        pyautogui.press("tab")
    Polo = "RIO+CURSOS"
    pyautogui.write(Polo)
    time.sleep(0.30)
    pyautogui.press("tab")
    time.sleep(0.30)
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("down")
    time.sleep(0.30)
    pyautogui.press("space")


#================================= TURMA EM ABERTO =======================================#
def turma_em_aberto():
    for i in range(8):
        pyautogui.hotkey('shift', 'tab')
    pyautogui.press("space")


#================================== OPÇÕES DE CURSOS =====================================#
def Curso(valor):
    curso_do_usuário = valor
    #========= Agente de Defesa Ambiental =========#
    if curso_do_usuário == 1:
        respt_usuário = "EAD - Agente de Defesa Ambiental"
        return pyautogui.write(respt_usuário)
    #======== EAD - Assistente de Logistica =======#
    if curso_do_usuário == 2:
        respt_usuário = "\033[37mEAD - Assistente de Logistica"
        return pyautogui.write(respt_usuário)   
    #============ EAD - Estoquista ================#
    if curso_do_usuário == 3:
        respt_usuário = "\033[37mEAD - Estoquista"
        return pyautogui.write(respt_usuário) 


#================================== BUTÃO PROXIMO - 1 =====================================#
def BUTÃO_PROXIMO_1():
    for i in range(10):
        pyautogui.press('tab')


#================================== BUTÃO PROXIMO - 2 =====================================#
def BUTÃO_PROXIMO_2():
    for i in range(6):
        pyautogui.press('tab')


#==================================== BUTÃO GRAVAR ========================================#
def BUTÃO_GRAVAR():
    for i in range(8):
        pyautogui.press('tab')
    #pyautogui.press("Enter")
