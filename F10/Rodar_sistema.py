def RODAR_SISTEMA():

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
    quantidades_de_repetições = int(input("\033[34mQuantas vezes e pra rodar o programa = \033[0m")) # quantidades de vezes para rodar o programa
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
        for vezes in range(quantidades_de_repetições): 
            #====================== BUTÃO ADICIONAR ============================#
            pyautogui.hotkey('Alt', 'o') 
            time.sleep(1)
            pyautogui.press('i') 
            time.sleep(2)
            #============================= ABRIR EXCEL ====================================#
            pyautogui.hotkey('alt', 'tab') # Chrome
            time.sleep(4)
            pyautogui.hotkey('ctrl', 'c') # copia o "CPF"
            time.sleep(0.10)
            pyautogui.hotkey('alt', 'tab') # F1
            time.sleep(5)
            Funções.prencher_cpf() #------------------------------------------------------------------------------->>>>>>>>>>>>> PRENCHER CPF - F10
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v') # colar o "CPF" copiado
            time.sleep(1)
            pyautogui.press("Enter")
            time.sleep(1)
            pyautogui.hotkey('alt', 'tab') # Chrome
            time.sleep(2)
            Funções.copia_CEP()
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c') # copia o "CEP"
            time.sleep(1)
            pyautogui.hotkey('alt', 'tab') # F10
            time.sleep(2)
            Funções.achar_cep() #-------------------------------------------------------------------------------------->>>>>>>>>>>>> ACHAR CEP - F10
            time.sleep(0.10)
            Funções.apagar_CEP()   
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v') # colar o "CEP"
            time.sleep(1)
            #============================ BUTÃO PROXIMO - 1 ====================================#
            Funções.BUTÃO_PROXIMO_1()
            time.sleep(2)
            #=============================== PARTE - 2 =====================================#
            #================ TIPO DE CONTRATO ==================#
            pyautogui.press("tab")
            Funções.Tipo_de_Contarto() #--------------------------------------------------------------------------->>>>>>>>>>>>> TIPO DE CONTRATO
            time.sleep(1) 
            pyautogui.press("tab") # TECLA "tab"
            #============ OPÇÃO - DATA DA MATRÍCULA ==============#
            Funções.Matrícula(data_do_usuário) #-------------------------------------------------------------------------->>>>>>>>>>>>> MATRÍCULA
            time.sleep(1)
            pyautogui.press("tab") # TECLA "tab"
            pyautogui.press("tab") # TECLA "tab"
            #================ OPÇÃO - EVENTO =====================#
            Funções.Evento() #----------------------------------------------------------------------------------------------->>>>>>>>>>>>> EVENTO
            time.sleep(1)
            pyautogui.press("tab") # TECLA "tab"
            #================= OPÇÃO - CURSO =====================#
            Funções.Curso(curso_do_usuário) #--------------------------------------------------------------------------------->>>>>>>>>>>>> CURSO
            time.sleep(1)
            pyautogui.press("tab") # TECLA "tab"
            #=============== OPÇÃO - COORDENADOR =================#
            Funções.Coordenador() #-------------------------------------------------------------------------------------->>>>>>>>>>>>> COORDENADOR
            time.sleep(1)
            #============================ BUTÃO PROXIMO - 2 ====================================#
            Funções.BUTÃO_PROXIMO_2()
            time.sleep(2)
            #=============================== PARTE - 3 =====================================#
            Funções.polo() #--------------------------------------------------------------------------------------------------->>>>>>>>>>>>> POLO
            time.sleep(2)                               
            #------
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # especifique o caminho do Tesseract, se necessário
            captura_de_tela = pyautogui.screenshot() # captura o espaço
            text = pytesseract.image_to_string(captura_de_tela) # converte a imagem em texto
            #-------
            if text == "":
                Funções.turma_em_aberto() #-------------------------------------------------------------------------->>>>>>>>>>>>> TURMA EM ABERTO
                time.sleep(2)
                #============================ BUTÃO GRAVAR ====================================# 
                Funções.BUTÃO_GRAVAR() #-------------------------------------------------------------------------------->>>>>>>>>>>>> BUTÃO GRAVAR
                time.sleep(2)
            else:
                #=========================== BUTÃO GRAVAR =====================================#
                Funções.BUTÃO_GRAVAR() #-------------------------------------------------------------------------------->>>>>>>>>>>>> BUTÃO GRAVAR
                time.sleep(2)
            #============================================== EXCEL ====================================================#
            pyautogui.hotkey('alt', 'tab') # Chrome
            time.sleep(8) #--------------------------------------------------- COLOCAR PARA 3
            Funções.marcar_ok() # marca OK
            time.sleep(2)
            Funções.voltar_para_cpf()
            time.sleep(2) # voltar para o cpf
            Funções.proximo_cpf() # passar para o proximo cpf
            time.sleep(3)
            pyautogui.hotkey('alt', 'tab') # F10
            time.sleep(5)

    #=====================================#
    #======== PROGRAMA FINALIZADO ========#
    print("\033[31m=" * 40)
    print("PROGRAMA ENCERRADO!".center(40))
    print("=" * 40)
    #=====================================#
    #=====================================#
