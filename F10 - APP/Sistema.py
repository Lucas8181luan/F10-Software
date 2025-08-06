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

#########################################################################################################################
###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PROGRAMA INICIAR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<###
#########################################################################################################################
def F10_BOT():
    #========= NOVAS MATRÍCULAS ==========#
    RESP_Novas_matrículas = Novas_matrículas.get()
    global Nova_matrícula
    Nova_matrícula = int(RESP_Novas_matrículas)
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
TITULO = tk.Label(app, text="F10 - BOT", bg="black" ,fg="White", font=("Arial", 80, "bold")) # texto
TITULO.pack(pady=25) # posição text
#=================================================================================================#

#================================= BORDA - WHITE =================================#
FUNDO_BLACK = tk.Label(app, text=".", width=86, height=39, bg="White") # tamamnho do fundo
FUNDO_BLACK.place(relx=0.5, rely=0.6, anchor="center") # centralizar o fundo
#=================================================================================#

#=================================== FUNDO - BLACK =================================#
FUNDO_RED = tk.Label(app, text="", width=80, height=37, bg="black") # tamamnho do fundo
FUNDO_RED.place(relx=0.5, rely=0.6, anchor="center") # centralizar o fundo
#=================================================================================#

#=================================================================================================#
#============================== INPUT - NOVAS MATRÍCULAS =========================================#
texto_Novas_matrículas = tk.Label(app, text="NOVAS MATRÍCULAS", bg="black", fg="white", font=("Arial", 14, "bold")) # texto
texto_Novas_matrículas.pack(pady=10) # posição texto
Novas_matrículas = tk.Entry(app, width=55)
Novas_matrículas.pack(pady=10) # posição 
#=================================================================================================#
#=================================================================================================#

#=================================================================================================#
#=============================== INPUT - DATA DA MATRÍCULA =======================================#
texto_Data_da_matrícula = tk.Label(app, text="DATA DA MATRÍCULA", bg="black", fg="white", font=("Arial", 14, "bold")) # texto
texto_Data_da_matrícula.pack(pady=10) # posição texto
Data_da_matrícula = tk.Entry(app, width=55)
Data_da_matrícula.pack(pady=10) # posição
#=================================================================================================#
#=================================================================================================#

#=================================================================================================#
#===================================== INPUT - CURSOS ============================================#
texto_CURSOS = tk.Label(app, text="ESCOLHA O CURSO", bg="black", fg="white", font=("Arial", 14, "bold")) # text
texto_CURSOS.pack(pady=10) # posição texto
CURSOS = ttk.Combobox(app, values=["EAD - Agente de Defesa Ambiental", "EAD - Assistente de Logistica", "EAD - Estoquista", "Híbrido - Auxiliar Administrativo", "Híbrido - Designer de Sombrancelhas", "Híbrido - Maquiagem", "Híbrido - Operador de Caixa", "Híbrido - Porteiro", "Híbrido - Recepcionista", "Presencial - Cuidador de Idoso", "Presencial - Informática"], width=52)
CURSOS.pack(pady=10) # posição
CURSOS.set("Selecione uma opção")
#=================================================================================================#
#=================================================================================================#

#=================================================================================================#
#============================ INPUT - QUANTIDADE ATUAL DE INCRIÇÕES ==============================#
texto_Quantidade_atual_inscrições = tk.Label(app, text="QUANTIDADE ATUAL DE INSCRIÇÕES", bg="black", fg="white", font=("Arial", 14, "bold")) # texto
texto_Quantidade_atual_inscrições.pack(pady=10) # posição do texto
Quantidade_atual_inscrições = tk.Entry(app, width=55)
Quantidade_atual_inscrições.pack(pady=10) # posição
#=================================================================================================#
#=================================================================================================#

#=================================================================================================#
#================================ INPUT - LIMITE DE INSCRIÇÕES ===================================#
texto_Limite_de_inscrições = tk.Label(app, text="LIMITE DE INSCRIÇÕES", bg="black", fg="white", font=("Arial", 14, "bold")) # texto
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
app.config(bg="black") # cor de fundo
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
    if Quantidade_inscrições - Limite_inscrições == 0 or Quantidade_inscrições > Limite_inscrições or Novo_cadastrado == Nova_matrícula:
        break
    Funções.Esconder_tecla() #--------------------------------------------------------------------------------->>>>>>>>>>>>> ESCONDER TECLA
    #=========================== BUTÃO ADICIONAR ==================================#
    pyautogui.hotkey('Alt', 'o', 'i')  
    time.sleep(2)
    #============================= ABRIR EXCEL ====================================#
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(4)
    #========================= VERIFICAR SE E REPETIDO =================================#
    Resultado_verificar_repetido = Funções.Cadastro_repetido() #-------------------------------------------->>>>>>>>>>>>> CADASTRO REPETIDO
    if Resultado_verificar_repetido == True:
        time.sleep(1)
        for i in range(): 
            pyautogui.press("right")
        time.sleep(1)
        pyautogui.press("down")
    else:
        for i in range(2):
            pyautogui.press("right")
        time.sleep(1)
    #===================================================================================#
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c') # copia o "CPF"
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab') # F10
    time.sleep(5)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') # colar o "CPF" copiado
    time.sleep(1)
    pyautogui.press("Enter")
    #============================ BUTÃO PROXIMO - 1 ====================================#
    for i in range(16):
        pyautogui.press('tab')
    #================================ PARTE - 2 ========================================#
    #================ TIPO DE CONTRATO ===================#
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
    time.sleep(5)
    pyautogui.press("tab") # TECLA "tab"
    #=============== OPÇÃO - COORDENADOR =================#
    Funções.Coordenador() #--------------------------------------------------------------------------------------->>>>>>>>>>>>> COORDENADOR
    time.sleep(1)
    #============================ BUTÃO PROXIMO - 2 ====================================#
    Funções.BUTÃO_PROXIMO_2() #------------------------------------------------------------------------------->>>>>>>>>>>>> BUTÃO PROXIMO 2
    time.sleep(2)
    #================================ PARTE - 3 ========================================#
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
        Novo_cadastrado += 1
    else:
        #============================ BUTÃO GRAVAR ====================================#
        Funções.BUTÃO_GRAVAR() #--------------------------------------------------------------------------------->>>>>>>>>>>>> BUTÃO GRAVAR
        time.sleep(2)
        Novo_cadastrado += 1
    #============================================== EXCEL ====================================================#
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(3) 
    for i in range(3): 
        pyautogui.press("right")
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.press("down")
    for i in range(3):
        time.sleep(1)
        pyautogui.press("left") # Voltar para o proximo CPF
    time.sleep(2)
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

def executar_app():
    """Função principal para executar APP"""
    Reiniciar_programa()
    F10_BOT() 

# Executar apenas se chamado diretamente
if __name__ == "__main__":
    executar_app()
