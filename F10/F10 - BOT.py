import tkinter as tk
from tkinter import ttk
import pyautogui 
import time
import pytesseract
import Funções
import ctypes
import PIL
import sys
import subprocess
import pyperclip
import re

#########################################################################################################################
###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PROGRAMA INICIAR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<###
#########################################################################################################################
def F10_BOT():
    #========= NOVAS MATRÍCULAS ==========#
    RESP_Novas_matrículas = Novas_matrículas.get()
    global numero
    numero = int(RESP_Novas_matrículas)
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

    #===== QUANTIDADES DE INSCRIÇÕES =====#
    RESP_Quantidade_atual_inscrições = Quantidade_atual_inscrições.get()
    global Quantidade_inscrições
    Quantidade_inscrições = int(RESP_Quantidade_atual_inscrições)
    #=====================================#

    #======= LIMITE DE INSCRIÇÕES ========#
    RESP_Limite_de_inscrições = Limite_de_inscrições.get()
    global Limite_inscrições
    Limite_inscrições = int(RESP_Limite_de_inscrições)
    #=====================================#
    app.destroy()
#========== CRIAR APP ==========#
app = tk.Tk()
app.title("IFP") # Titulo
app.attributes("-fullscreen", True) # abri a janela em tela cheia
#===============================#

#========================================== TITULO ===============================================#
TITULO = tk.Label(app, text="F10 - BOT", bg="blue" ,fg="White", font=("Arial", 80, "bold")) # texto
TITULO.pack(pady=90) # posição text
#=================================================================================================#

#================================= BORDA - WHITE =================================#
FUNDO_BLACK = tk.Label(app, text=".", width=76, height=34, bg="White") # tamamnho do fundo
FUNDO_BLACK.place(relx=0.5, rely=0.6, anchor="center") # centralizar o fundo
#=================================================================================#

#=================================== FUNDO - RED =================================#
FUNDO_RED = tk.Label(app, text="", width=70, height=32, bg="red") # tamamnho do fundo
FUNDO_RED.place(relx=0.5, rely=0.6, anchor="center") # centralizar o fundo
#=================================================================================#

#=================================================================================================#
#============================== INPUT - NOVAS MATRÍCULAS =========================================#
texto_Novas_matrículas = tk.Label(app, text="NOVAS MATRÍCULAS", bg="red", fg="white", font=("Arial", 14, "bold")) # texto
texto_Novas_matrículas.pack(pady=10) # posição texto
Novas_matrículas = tk.Entry(app, width=55)
Novas_matrículas.pack(pady=10) # posição 
#=================================================================================================#
#=================================================================================================#

#=================================================================================================#
#=============================== INPUT - DATA DA MATRÍCULA =======================================#
texto_Data_da_matrícula = tk.Label(app, text="DATA DA MATRÍCULA", bg="red", fg="white", font=("Arial", 14, "bold")) # texto
texto_Data_da_matrícula.pack(pady=10) # posição texto
Data_da_matrícula = tk.Entry(app, width=55)
Data_da_matrícula.pack(pady=10) # posição
#=================================================================================================#
#=================================================================================================#

#=================================================================================================#
#===================================== INPUT - CURSOS ============================================#
texto_CURSOS = tk.Label(app, text="ESCOLHA O CURSO", bg="red", fg="white", font=("Arial", 14, "bold")) # text
texto_CURSOS.pack(pady=10) # posição texto
CURSOS = ttk.Combobox(app, values=["EAD - Agente de Defesa Ambiental", "EAD - Assistente de Logistica", "EAD - Estoquista", "AUXILIAR ADMINISTRATIVO", "PORTEIRO", "OPERADOR DE CAIXA", "RECEPCIONISTA", "ATENDENTE DE FARMÁCIA", "INFORMÁTICA"], width=52)
CURSOS.pack(pady=10) # posição
CURSOS.set("Selecione uma opção")
#=================================================================================================#
#=================================================================================================#

#=================================================================================================#
#============================ INPUT - QUANTIDADE ATUAL DE INCRIÇÕES ==============================#
texto_Quantidade_atual_inscrições = tk.Label(app, text="QUANTIDADE ATUAL DE INSCRIÇÕES", bg="red", fg="white", font=("Arial", 14, "bold")) # texto
texto_Quantidade_atual_inscrições.pack(pady=10) # posição do texto
Quantidade_atual_inscrições = tk.Entry(app, width=55)
Quantidade_atual_inscrições.pack(pady=10) # posição
#=================================================================================================#
#=================================================================================================#

#=================================================================================================#
#================================ INPUT - LIMITE DE INSCRIÇÕES ===================================#
texto_Limite_de_inscrições = tk.Label(app, text="LIMITE DE INSCRIÇÕES", bg="red", fg="white", font=("Arial", 14, "bold")) # texto
texto_Limite_de_inscrições.pack(pady=10) # posição do texto
Limite_de_inscrições = tk.Entry(app, width=55)
Limite_de_inscrições.pack(pady=10) # posição
#=================================================================================================#
#=================================================================================================#

#=========================== BUTÃO PARA INICIRA A AÇÃO ===========================#
button_iniciar_programa = tk.Button(app, text="INICIAR PROGRAMA", command=F10_BOT, width=20, height=2, font=("Arial", 10, "bold"), bg="red", fg="white")
button_iniciar_programa.pack(pady=10) # posição
#=================================================================================#

#============================== BUTÃO PARA FECHAR ================================#
button_fechar_programa = tk.Button(app, text="FECHAR PROGRAMA", command=app.quit, width=20, height=2, font=("Arial", 10, "bold"), bg="red", fg="white")
button_fechar_programa.pack(pady=5) # posição
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
Novo_cadastrado = 0 # para função (LIMITE DE INSCRIÇÕES)
time.sleep(10)
while True:
    if Quantidade_inscrições - Limite_inscrições == 0 or Quantidade_inscrições > Limite_inscrições:
        break
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
    #=========================== VERIFICAR NOME ========================================#
    Resultado_verificar_nome = Funções.Verificar_nome() #---------------------------------------------------->>>>>>>>>>>>> VERIFICA O NOME
    if Resultado_verificar_nome == False:
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab') # F10
        time.sleep(1)
        Funções.Fechar_página_de_cadastro() #------------------------------------------------------>>>>>>>>>>>>> FECHAR PÁGINA DE CADASTRO
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab') # Chrome
        time.sleep(1)
        Funções.Marca_erro_nome() #----------------------------------------------------------------------->>>>>>>>>>>>> MARCA ERRO DE NOME
        continue
    #========================= VERIFICAR TELEFONE ======================================#
    Resultado_erro_telefone = Funções.Verificar_telefone() #---------------------------------------------->>>>>>>>>>>>> VERIFICAR TELEFONE
    if Resultado_erro_telefone == False:
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab') # F10
        time.sleep(1)
        Funções.Fechar_página_de_cadastro() #------------------------------------------------------>>>>>>>>>>>>> FECHAR PÁGINA DE CADASTRO
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab') # Chrome
        time.sleep(1)
        Funções.Marca_erro_telefone() #--------------------------------------------------------------->>>>>>>>>>>>> MARCA ERRO DE TELEFONE
        continue
    #========================= COPIA E COLAR "CEP" =====================================#
    Funções.copia_CEP() #------------------------------------------------------------------------------------------>>>>>>>>>>>>> COPIA CEP
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c') # copia o "CEP"
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab') # F10
    time.sleep(2)
    Funções.achar_cep() #------------------------------------------------------------------------------------>>>>>>>>>>>>> ACHAR CEP - F10
    time.sleep(0.10)
    Funções.apagar_CEP() #-------------------------------------------------------------------------------->>>>>>>>>>>>> APAGAR E COLAR CEP
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') # colar o "CEP"
    time.sleep(1)
    #============================ BUTÃO PROXIMO - 1 ====================================#
    Funções.BUTÃO_PROXIMO_1()
    time.sleep(2)
    #============================ VERIFICAR CPF ========================================#
    Resultado_erro_cpf = Funções.Verificar_cpf() #--------------------------------------------------------------->>>>>>>>>>>>> VERIFICA CPF
    if Resultado_erro_cpf == True:
        pyautogui.press("space") # clica no butão "OK"
        time.sleep(1)
        Funções.Fechar_página_de_cadastro() #------------------------------------------------------->>>>>>>>>>>>> FECHAR PÁGINA DE CADASTRO
        time.sleep(1)
        Funções.Marca_erro_de_cpf() #----------------------------------------------------------------------->>>>>>>>>>>>> MARCA ERRO DE CPF
        time.sleep(2)
        continue
    #============================= VERIFICAR CEP =======================================#
    Resultado_erro_cep = Funções.Verificar_cep()
    if Resultado_erro_cep == True:
        pyautogui.press("space") # clica no butão "OK"
        time.sleep(1)
        Funções.Fechar_página_de_cadastro() #------------------------------------------------------->>>>>>>>>>>>> FECHAR PÁGINA DE CADASTRO
        time.sleep(1)
        Funções.Marca_erro_de_cep() #----------------------------------------------------------------------->>>>>>>>>>>>> MARCA ERRO DE CEP
        time.sleep(2)
        continue
    #======================== VERIFICAR MENOR DE IDADE =================================#
    Resultado_menor_de_idade = Funções.Verificar_menor_de_idade() #------------------------------>>>>>>>>>>>>> VERIFICA SE E MENOR DE IDADE
    time.sleep(1)
    if Resultado_menor_de_idade == True:
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
    #-------
    Verificar = Funções.Verificar_coordenador_polo() #----------------------------------------------------->>>>>>>>>>>>> COORDENADOR - POLO
    #-------
    if Verificar == False:
        Funções.turma_em_aberto() #--------------------------------------------------------------------------->>>>>>>>>>>>> TURMA EM ABERTO
        time.sleep(2)
        #============================ BUTÃO GRAVAR ====================================# 
        Funções.BUTÃO_GRAVAR() #--------------------------------------------------------------------------------->>>>>>>>>>>>> BUTÃO GRAVAR
        time.sleep(2)
        Novo_cadastrado += 1 # para cada novo aluno cadastrado
    else:
        #=========================== BUTÃO GRAVAR =====================================#
        Funções.BUTÃO_GRAVAR() #--------------------------------------------------------------------------------->>>>>>>>>>>>> BUTÃO GRAVAR
        time.sleep(2)
        Novo_cadastrado += 1 # para cada novo aluno cadastrado
    #============================================== EXCEL ====================================================#
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(3) 
    Funções.marcar_ok() # marca OK
    time.sleep(2)
    Funções.voltar_para_cpf() #--------------------------------------------------------------------->>>>>>>>>>>>> VOLTA E MARCA "CPF" ERRDO
    time.sleep(2) 
    Funções.proximo_cpf() #------------------------------------------------------------------------------------->>>>>>>>>>>>> PROXIMO "CPF"
    time.sleep(3)
    pyautogui.hotkey('alt', 'tab') # F10
    time.sleep(5)
    #======================================== VERIFICAR LIMITE ===============================================#
    Contador = Funções.Contar_inscrições(Novo_cadastrado, Quantidade_inscrições, Limite_inscrições) #---->>>>>>>>>>>>> LIMITE DE INSCRIÇÕES
    if Contador == True:
        break

#########################################################################################################################
###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> REINICIAR PROGRAMA <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<###
#########################################################################################################################
def Reiniciar_programa():
    python = sys.executable
    script = sys.argv[0]
    subprocess.call([python, script] + sys.argv[1:])

Reiniciar_programa()

#== Play ==#
F10_BOT() 
#==========#

# -> AUMENTAR OS TIMES PARA +1
# -> FINALIZAR A FERRAMENTA
