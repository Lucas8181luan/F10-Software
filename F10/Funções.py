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
    print("PROGARAMA RODANDO...".center(40))
    print("\033[92m=" * 40)


#================================= ESCOLHER CURSOS ====================================#
def RESPOSTA_DO_USUÁRIO():
    data_do_usuário = str(input("DIGITE A DATA DESEJADA (USANDO / / ) = "))
    curso_do_usuário = str(input("ESCOLHA O CURSO = "))
    #==============================================#
    #======== TIPO DE CONTRATO =======#
    Tipo_de_Contarto = "Bolsa"
    #============ MATRÍCULA ==========#
    Matrícula = data_do_usuário
    #============= EVENTO ============#
    Evento = "RIO+CURSOS"
    #============= CURSOS ============#
    Curso_1 = "EAD - Agente de Defesa Ambiental"
    Curso_2 = "EAD - Assistente de Logistica"
    Curso_3 = "EAD - Estoquista"
    #=========== COORDENADOR =========#
    Coordenador = "Rodrigo Drumond"
    #==============================================#


def Tipo_de_Contarto():
    Tipo_de_Contarto = "Bolsa"
    return pyautogui.write(Tipo_de_Contarto)

