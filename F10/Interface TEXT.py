import tkinter as tk
from tkinter import ttk

def F10_BOT():
    #====== QUANTIDADES DE USUÁRIOS ======#
    RESP_Quantidades_de_usuário = Quantidades_de_usuário.get()
    #=====================================#

    #========== DATA DA MATRÍCULA ========#
    RESP_Data_da_matrícula = Data_da_matrícula.get()
    #=====================================#

    #=============== CURSOS ==============#
    RESP_CURSOS = CURSOS.get()
    print(RESP_CURSOS)
    #=====================================#

#========== CRIAR APP ==========#
app = tk.Tk()
app.title("IFP") # Titulo
#===============================#

#========================================== TITULO ===============================================#
TITULO = tk.Label(app, text="F10 - BOT", bg="blue" ,fg="White", font=("Arial", 80, "bold")) # text
TITULO.pack(pady=95) # posição text
#=================================================================================================#

#================================= BORDA - WHITE =================================#
FUNDO_BLACK = tk.Label(app, text=".", width=54, height=28, bg="White") # tamamnho do fundo
FUNDO_BLACK.place(relx=0.5, rely=0.6, anchor="center") # centralizar o fundo
#=================================================================================#

#=================================== FUNDO - RED =================================#
FUNDO_RED = tk.Label(app, text="", width=50, height=26, bg="red") # tamamnho do fundo
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
CURSOS = ttk.Combobox(app, values=["EAD - Agente de Defesa Ambiental", "EAD - Assistente de Logistica", "EAD - Estoquista"], width=41)
CURSOS.pack(pady=10) # posição
CURSOS.set("Selecione uma opção")
#=================================================================================================#
#=================================================================================================#

#=========================== BUTÃO PARA INICIRA A AÇÃO ===========================#
button_iniciar_programa = tk.Button(app, text="INICIAR PROGRAMA", command=F10_BOT, width=20, height=3, font=("Arial", 10, "bold"), bg="red", fg="white")
button_iniciar_programa.pack(pady=33) # posição
#=================================================================================#

#======================================================================================================================================#
#=============================================================== STYLE ================================================================#
app.config(bg="blue") # cor de fundo
#======================================================================================================================================#
#======================================================================================================================================#

#========== INICIAR PROGRAMA ==========#
app.mainloop() # Abrir o aplicativo
#======================================#
