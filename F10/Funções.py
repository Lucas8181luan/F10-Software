import tkinter as tk
from tkinter import ttk
import pyautogui 
import time
import pytesseract
import Funções
import ctypes
import PIL

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
    return pyautogui.write(curso_do_usuário)


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
        time.sleep(5) #=============================== EXCLUIR
    #pyautogui.press("Enter")


#================================= FINALIZAR PROGRAMA =====================================#
def FINALIZAR_PROGRAMA():
    #=====================================#
    #======== PROGRAMA FINALIZADO ========#
    print("\033[31m=" * 40)
    print("PROGRAMA ENCERRADO!".center(40))
    print("=" * 40)
    #=====================================#
    #=====================================#


#============================== VERIFICAR MENOR DE IDADE ==================================#
def Verificar_menor_de_idade():
    time.sleep(2)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    print_da_tela = pyautogui.screenshot() # Tira uma captura da tela
    texto = pytesseract.image_to_string(print_da_tela) # Converte a imagem em texto
    Achar_essa_menssagem = "Adicionar Titular (Responsavel pelo Contrato)" # Achar menssagem
    if Achar_essa_menssagem in texto:
        return True
    else:
        return False


#============================ VERIFICAR COORDENADOR NO POLO ===============================#
def Verificar_coordenador_polo():
    time.sleep(8)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    print_da_tela = pyautogui.screenshot() # Tira uma captura da tela
    texto = pytesseract.image_to_string(print_da_tela)
    Achar_essa_menssagem = "04:00:00"
    if Achar_essa_menssagem in texto:
        return True
    else:
        return False


#============================== FECHAR PÁGINA DE CADASTRO" ================================#
def Fechar_página_de_cadastro():
    pyautogui.hotkey('Ctrl', 'tab') # Fechar página de cadastro
    time.sleep(0.20)
    pyautogui.hotkey('alt', 'o', 'c') # Voltar para a página de cadastro


#============================ VOLTAR E MARCA "Menor de idade" =============================#
def Marcar_menor_de_idade():
    time.sleep(3)
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(0.20)
    for i in range(7): 
        pyautogui.press("left") 
    time.sleep(0.20)
    pyautogui.write("Menor de idade ") # escrever menor de idade
    time.sleep(0.20)
    for i in range(2): 
        pyautogui.press("right")
        time.sleep(0.20)
    pyautogui.press("down")
    time.sleep(0.20)
    pyautogui.hotkey('alt', 'tab') # F10
