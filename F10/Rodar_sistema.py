import pyautogui 
import time
import pytesseract
import Funções
import ctypes

# >> Instalador do Tesseract para Windows <<
# >> Deixar página do F10 aberta

#=============================================================================================#
#=================================== INICIAR PROGRAMRA =======================================#
print("\033[34m=" * 40)
USUÁRIO = input('\033[34mDigite \033[97m"OK\033[0m" \033[34mpara iniciar programar = \033[0m'.center(40)).upper().strip() # resposta do usuário
print("\033[34m=\033[0m" * 40)
data_do_usuário = str(input("DIGITE A DATA DE CADASTRO DA MATRÍCULA (USANDO / / ) = ")) # pede para o usuário escolher a data de cadastro
CURSOS = ["EAD - Agente de Defesa Ambiental", "EAD - Assistente de Logistica", "EAD - Estoquista"] # CURSOS
n = 0
for i in CURSOS: # mostra as opções de cursos
    n += 1
    print("=" * 40)
    print(f"--> {n}º {i}")
    print("=" * 40)
curso_do_usuário = int(input("ESCOLHA O CURSO = ")) # pede para o usuário escolher o curso de cadastro
time.sleep(2)
Funções.Direcionar_usuário() # indicar o passo a passo antes de rodar o programa
time.sleep(2)
#=============================================================================================#
#=============================================================================================#
# -> START
if USUÁRIO == "OK": # condição para rodar o programar
    time.sleep(2) 
    for vezes in range(5): 
        #====================== BUTÃO ADICIONAR ============================#
        pyautogui.hotkey('Alt', 'o') 
        time.sleep(1)
        pyautogui.press('i') 
        #============================= ABRIR EXCEL ====================================#
        if vezes == 0: # rodar 1º vez
            pyautogui.hotkey('alt', 'tab') # Chrome
            time.sleep(4)
        #===================== PRIMEIRA LINHA PARA LEITURA ============================#
            pyautogui.moveTo(x=-1109, y=556) # mover para primeira linha de "CPF" da panilha >>>>>(CORDENADAS)<<<<< 1º
            time.sleep(3)
            pyautogui.click() # clicar
        #=============================== PARTE - 1 =====================================#
        if vezes > 0: # rodar o resto do programa todo
            pyautogui.hotkey('alt', 'tab') # Chrome
            time.sleep(4)
        pyautogui.hotkey('ctrl', 'c') # copia o "CPF"
        time.sleep(0.10)
        pyautogui.hotkey('alt', 'tab') # F10
        time.sleep(5)
        pyautogui.moveTo(x=-1685, y=454) # mover para a parte de prenhencher "CPF" >>>>>(CORDENADAS)<<<<< 2º
        time.sleep(4)
        pyautogui.click() # clicar
        pyautogui.hotkey('ctrl', 'v') # colar o "CPF" copiado
        pyautogui.moveTo(x=-797, y=659) # mover para butão OK >>>>>(CORDENADAS)<<<<< 3º
        time.sleep(2)
        pyautogui.click() # clicar
        time.sleep(2)
        pyautogui.hotkey('alt', 'tab') # Chrome
        time.sleep(2)
        Funções.copia_CEP()
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c') # copia o "CEP"
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab') # F10
        time.sleep(2)
        pyautogui.moveTo(x=-1590, y=631) # move para o CEP >>>>>(CORDENADAS)<<<<< 4º
        time.sleep(2)
        pyautogui.click() # click
        time.sleep(2)
        Funções.apagar_CEP()
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v') # colar o "CEP"
        time.sleep(1)
        #============================ BUTÃO PROXIMO ====================================#
        pyautogui.moveTo(x=-830, y=865) # mover para o butão proximo >>>>>(CORDENADAS)<<<<< 5º
        pyautogui.click() # clicar
        time.sleep(2)
        #=============================== PARTE - 2 =====================================#
        #================ TIPO DE CONTRATO ==================#
        pyautogui.moveTo(x=-1438, y=413) # butão escolher tipo de contrato >>>>>(CORDENADAS)<<<<< 6º
        pyautogui.click() # clicar
        time.sleep(1)
        Funções.Tipo_de_Contarto() #--------------------------------------------------------------------------->>>>>>>>>>>>> TIPO DE CONTRATO
        time.sleep(2) 
        pyautogui.press("tab") # TECLA "tab"
        #============ OPÇÃO - DATA DA MATRÍCULA ==============#
        Funções.Matrícula(data_do_usuário) #-------------------------------------------------------------------------->>>>>>>>>>>>> MATRÍCULA
        time.sleep(2)
        pyautogui.press("tab") # TECLA "tab"
        pyautogui.press("tab") # TECLA "tab"
        #================ OPÇÃO - EVENTO =====================#
        Funções.Evento() #----------------------------------------------------------------------------------------------->>>>>>>>>>>>> EVENTO
        time.sleep(2)
        pyautogui.press("tab") # TECLA "tab"
        #================= OPÇÃO - CURSO =====================#
        Funções.Curso(curso_do_usuário) #--------------------------------------------------------------------------------->>>>>>>>>>>>> CURSO
        time.sleep(2)
        pyautogui.press("tab") # TECLA "tab"
        #=============== OPÇÃO - COORDENADOR =================#
        Funções.Coordenador() #-------------------------------------------------------------------------------------->>>>>>>>>>>>> COORDENADOR
        time.sleep(2)
        #============================ BUTÃO PROXIMO ====================================#
        pyautogui.moveTo(x=-672, y=870) # mover para o 2º butão proximo >>>>>(CORDENADAS)<<<<< 7º
        pyautogui.click() # clicar
        time.sleep(2)
        #=============================== PARTE - 3 =====================================#
        Funções.polo() #--------------------------------------------------------------------------------------------------->>>>>>>>>>>>> POLO
        time.sleep(2)
        pyautogui.moveTo(x=-1635, y=546) # opção de turma (para verificar a captura de tela) >>>>>(CORDENADAS)<<<<< 8º
        time.sleep(3)
        #------
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # especifique o caminho do Tesseract, se necessário
        captura_de_tela = pyautogui.screenshot() # captura o espaço
        text = pytesseract.image_to_string(captura_de_tela) # converte a imagem em texto
        #-------
        if text == "":
            pyautogui.moveTo(x=-1659, y=383) # deixar turma em aberto >>>>>(CORDENADAS)<<<<< 9º
            pyautogui.click() # clicar
            #============================ BUTÃO PROXIMO ====================================# 
            time.sleep(2)
            pyautogui.moveTo(x=-672, y=870) # mover para o butão gravar >>>>>(CORDENADAS)<<<<< 10º
            pyautogui.click() # clicar090.531.867-60
            time.sleep(3)
        else:
            pyautogui.moveTo(x=-1669, y=546) # escolher turma AVA >>>>>(CORDENADAS)<<<<< 11º
            pyautogui.click() # clicar
            #=========================== BUTÃO GRAVAR =====================================#
            time.sleep(3)
            pyautogui.moveTo(x=-589, y=868) # mover para o butão gravar >>>>>(CORDENADAS)<<<<< 12º
            #pyautogui.click() # clicar
            time.sleep(10) ##### ------ colocar para "5"
        #============================================== EXCEL ====================================================#
        pyautogui.hotkey('alt', 'tab') # Chrome
        time.sleep(2)
        pyautogui.moveTo(x=-488, y=85) # clique na página >>>>>(CORDENADAS)<<<<< 13º
        pyautogui.click() # clicar
        time.sleep(2)
        Funções.marcar_ok() # marca OK
        time.sleep(2)
        Funções.voltar_para_cpf()
        time.sleep(2) # voltar para o cpf
        Funções.proximo_cpf() # passar para o proximo cpf
        time.sleep(5)
        pyautogui.hotkey('alt', 'tab') # F10
        time.sleep(5)

#=====================================#
#======== PROGRAMA FINALIZADO ========#
print("\033[31m=" * 40)
print("PROGRAMA ENCERRADO!".center(40))
print("=" * 40)
#=====================================#
#=====================================#
