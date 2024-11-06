import tkinter as tk
from tkinter import ttk
import pyautogui 
import time
import pytesseract
import Funções
import ctypes
import PIL
    
def F10_BOT():
    #====== QUANTIDADES DE USUÁRIOS ======#
    RESP_Quantidades_de_usuário = Quantidades_de_usuário.get()
    global numero
    numero = int(RESP_Quantidades_de_usuário)
    #=====================================#

    #========== DATA DA MATRÍCULA ========#
    RESP_Data_da_matrícula = Data_da_matrícula.get()
    global data
    data = str(RESP_Data_da_matrícula)
    #=====================================#

    #=============== CURSOS ==============#
    RESP_CURSOS = CURSOS.get()
    global curso
    curso = str(RESP_CURSOS)
    #=====================================#
    app.destroy()
#========== CRIAR APP ==========#
app = tk.Tk()
app.title("IFP") # Titulo
#===============================#

#========================================== TITULO ===============================================#
TITULO = tk.Label(app, text="F10 - BOT", bg="blue" ,fg="White", font=("Arial", 80, "bold")) # text
TITULO.pack(pady=132) # posição text
#=================================================================================================#

#================================= BORDA - WHITE =================================#
FUNDO_BLACK = tk.Label(app, text=".", width=55, height=25, bg="White") # tamamnho do fundo
FUNDO_BLACK.place(relx=0.5, rely=0.6, anchor="center") # centralizar o fundo
#=================================================================================#

#=================================== FUNDO - RED =================================#
FUNDO_RED = tk.Label(app, text="", width=50, height=23, bg="red") # tamamnho do fundo
FUNDO_RED.place(relx=0.5, rely=0.6, anchor="center") # centralizar o fundo
#=================================================================================#

#=================================================================================================#
#============================= INPUT - QUANTIDADES DE USUÁRIO ====================================#
texto_Quantidades_de_usuário = tk.Label(app, text="QUANTIDADES DE USUÁRIOS", bg="red", fg="white", font=("Arial", 14, "bold")) # text
texto_Quantidades_de_usuário.pack(pady=10) # posição text
Quantidades_de_usuário = tk.Entry(app, width=45)
Quantidades_de_usuário.pack(pady=10) # posição 
#=================================================================================================#
#=================================================================================================#

#=================================================================================================#
#=============================== INPUT - DATA DA MATRÍCULA =======================================#
texto_Data_da_matrícula = tk.Label(app, text="DATA DA MATRÍCULA", bg="red", fg="white", font=("Arial", 14, "bold")) # text
texto_Data_da_matrícula.pack(pady=10) # posição text
Data_da_matrícula = tk.Entry(app, width=45)
Data_da_matrícula.pack(pady=10) # posição
#=================================================================================================#
#=================================================================================================#

#=================================================================================================#
#===================================== INPUT - CURSOS ============================================#
texto_CURSOS = tk.Label(app, text="ESCOLHA O CURSO", bg="red", fg="white", font=("Arial", 14, "bold")) # text
texto_CURSOS.pack(pady=10) # posição text
CURSOS = ttk.Combobox(app, values=["EAD - Agente de Defesa Ambiental", "EAD - Assistente de Logistica", "EAD - Estoquista", "AUXILIAR ADMINISTRATIVO", "PORTEIRO", "OPERADOR DE CAIXA", "RECEPCIONISTA", "ATENDENTE DE FARMÁCIA", "INFORMÁTICA"], width=41)
CURSOS.pack(pady=10) # posição
CURSOS.set("Selecione uma opção")
#=================================================================================================#
#=================================================================================================#

#=========================== BUTÃO PARA INICIRA A AÇÃO ===========================#
button_iniciar_programa = tk.Button(app, text="INICIAR PROGRAMA", command=F10_BOT, width=20, height=3, font=("Arial", 10, "bold"), bg="red", fg="white")
button_iniciar_programa.pack(pady=33) # posição
#=================================================================================#

#====================================================================================================================================#
#============================================================== STYLE ===============================================================#
app.config(bg="blue") # cor de fundo
#====================================================================================================================================#
#====================================================================================================================================#

#========== INICIAR PROGRAMA ==========#
app.mainloop() # Abrir o aplicativo
#======================================#


#########################################################################################################################
###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SISTEMA <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<###
#########################################################################################################################
time.sleep(10)
for vezes in range(numero): 
    #=========================== BUTÃO ADICIONAR ============================#
    pyautogui.hotkey('Alt', 'o', 'i')  
    time.sleep(2)
    #============================= ABRIR EXCEL ====================================#
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'c') # copia o "CPF"
    time.sleep(0.10)
    pyautogui.hotkey('alt', 'tab') # F10
    time.sleep(5)
    Funções.prencher_cpf() #------------------------------------------------------------------------------>>>>>>>>>>>>> PRENCHER CPF - F10
    time.sleep(2)
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
    Funções.achar_cep() #------------------------------------------------------------------------------------>>>>>>>>>>>>> ACHAR CEP - F10
    time.sleep(0.10)
    Funções.apagar_CEP()   
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') # colar o "CEP"
    time.sleep(1)
    #============================ BUTÃO PROXIMO - 1 ====================================#
    Funções.BUTÃO_PROXIMO_1()
    time.sleep(2)
    #======================== VERIFICAR MENOR DE IDADE =================================#
    Resultado = Funções.Verificar_menor_de_idade() #--------------------------------------------->>>>>>>>>>>>> VERIFICA SE E MENOR DE IDADE
    time.sleep(1)
    if Resultado == True:
        Funções.Fechar_página_de_cadastro() #------------------------------------------------------->>>>>>>>>>>>> FECHAR PÁGINA DE CADASTRO
        time.sleep(1)
        Funções.Marcar_menor_de_idade() #-------------------------------------------------------------->>>>>>>>>>>>> MARCAR MENOR DE IDADES
        time.sleep(2)
        continue
    #================================ PARTE - 2 ========================================#
    #================ TIPO DE CONTRATO ==================#
    pyautogui.press("tab")
    Funções.Tipo_de_Contarto() #----------------------------------------------------------------------------->>>>>>>>>>>>> TIPO DE CONTRATO
    time.sleep(1) 
    pyautogui.press("tab") # TECLA "tab"
    #============ OPÇÃO - DATA DA MATRÍCULA ==============#
    Funções.Matrícula(data) #--------------------------------------------------------------------------------------->>>>>>>>>>>>> MATRÍCULA
    time.sleep(1)
    pyautogui.press("tab") # TECLA "tab"
    pyautogui.press("tab") # TECLA "tab"
    #================ OPÇÃO - EVENTO =====================#
    Funções.Evento() #------------------------------------------------------------------------------------------------->>>>>>>>>>>>> EVENTO
    time.sleep(1)
    pyautogui.press("tab") # TECLA "tab"
    #================= OPÇÃO - CURSO =====================#
    Funções.Curso(curso) #---------------------------------------------------------------------------------------------->>>>>>>>>>>>> CURSO
    time.sleep(2)
    pyautogui.press("tab") # TECLA "tab"
    #=============== OPÇÃO - COORDENADOR =================#
    Funções.Coordenador() #--------------------------------------------------------------------------------------->>>>>>>>>>>>> COORDENADOR
    time.sleep(1)
    #============================ BUTÃO PROXIMO - 2 ====================================#
    Funções.BUTÃO_PROXIMO_2()
    time.sleep(2)
    #=============================== PARTE - 3 =====================================#
    Funções.polo() #----------------------------------------------------------------------------------------------------->>>>>>>>>>>>> POLO
    time.sleep(2)                               
    #------
    Verificar = Funções.Verificar_coordenador_polo() #----------------------------------------------------------------->>>>>>>>>>>>> COORDENADOR - POLO
    #-------
    if Verificar == False:
        Funções.turma_em_aberto() #--------------------------------------------------------------------------->>>>>>>>>>>>> TURMA EM ABERTO
        time.sleep(2)
        #============================ BUTÃO GRAVAR ====================================# 
        Funções.BUTÃO_GRAVAR() #--------------------------------------------------------------------------------->>>>>>>>>>>>> BUTÃO GRAVAR
        time.sleep(2)
    else:
        #=========================== BUTÃO GRAVAR =====================================#
        Funções.BUTÃO_GRAVAR() #--------------------------------------------------------------------------------->>>>>>>>>>>>> BUTÃO GRAVAR
        time.sleep(2) 
    #============================================== EXCEL ====================================================#
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(3) 
    Funções.marcar_ok() # marca OK
    time.sleep(2)
    Funções.voltar_para_cpf()
    time.sleep(2) # voltar para o cpf
    Funções.proximo_cpf() # passar para o proximo cpf
    time.sleep(3)
    pyautogui.hotkey('alt', 'tab') # F10
    time.sleep(5)

F10_BOT()

# CTRL + SHIFT + PG UP 2x -> ler o dashboard
# do lado da planilha de cadastro mostar posso ver por la tambem
