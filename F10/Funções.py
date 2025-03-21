import tkinter as tk
from tkinter import ttk
import pyautogui 
import time
import pytesseract
import Funções
import ctypes
import PIL
import sys
import os
import pyperclip

#================================= ACHAR POSITION =========================================#
def achar_position():
    time.sleep(8)
    posição = pyautogui.position()
    print(f"POSITION: \033[32m{posição}\033[0m")


#=============================== PRENCHER CPF - F10 =======================================#
def prencher_cpf():
    pyautogui.press("down")
    time.sleep(0.20)
    pyautogui.press("Enter")


#================================ ACHAR CEP - F10 =========================================#
def achar_cep():
    for i in range(3):
        pyautogui.press("tab")
    time.sleep(0.50)


#================================== MARCAR "OK" ===========================================#
def marcar_ok():
    for i in range(2): 
        pyautogui.press("left")
    pyautogui.press("space")


#=============================== VOLTAR PARA O "CPF" ======================================#
def voltar_para_cpf():
    for i in range(3): 
        pyautogui.press("left") 


#================================== PROXIMO "CPF" =========================================#
def proximo_cpf():
    pyautogui.press("down")


#=================================== COPIA "CEP" ==========================================#
def copia_CEP():
    for i in range(2): 
        pyautogui.press("right") 


#=================================== APAGAR "CEP" =========================================#
def apagar_CEP():
    for i in range(10):
        pyautogui.press("Backspace")


#================================ ESCOLHER CONTRATO =======================================#
def Tipo_de_Contarto():
    Tipo_de_Contarto = "Bolsa"
    return pyautogui.write(Tipo_de_Contarto)


#================================ ESCOLHER MATRÍCULA ======================================#
def Matrícula(valor):
    data_do_usuário = valor
    for i in range(10):
        pyautogui.press("Backspace")
    return pyautogui.write(data_do_usuário)


#================================= ESCOLHER EVENTO ========================================#
def Evento():
    Evento = "RIO+CURSOS"
    return pyautogui.write(Evento)


#=============================== ESCOLHER COORDENADOR =====================================#
def Coordenador():
    Coordenador = "Rodrigo Drumond"
    return pyautogui.write(Coordenador)


#================================== ESCOLHER POLO =========================================#
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


#================================= TURMA EM ABERTO ========================================#
def turma_em_aberto():
    for i in range(8):
        pyautogui.hotkey('shift', 'tab')
    pyautogui.press("space")


#================================= OPÇÕES DE CURSOS =======================================#
def Curso(valor):
    pyperclip.copy(valor) # Copia o valor para a área de transferência
    pyautogui.hotkey('ctrl', 'v')
    return None


#================================= BUTÃO PROXIMO - 1 ======================================#
def BUTÃO_PROXIMO_1():
    for i in range(10):
        pyautogui.press('tab')


#================================= BUTÃO PROXIMO - 2 ======================================#
def BUTÃO_PROXIMO_2():
    for i in range(6):
        pyautogui.press('tab')


#================================== BUTÃO GRAVAR ==========================================#
def BUTÃO_GRAVAR():
    for i in range(8):
        pyautogui.press('tab')
    pyautogui.press("Enter")


#============================= VERIFICAR MENOR DE IDADE ===================================#
def Verificar_menor_de_idade():
    time.sleep(2)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    print_da_tela = pyautogui.screenshot() # Tira uma captura da tela
    texto = pytesseract.image_to_string(print_da_tela) # Converte a imagem em texto
    Achar_essa_menssagem = "Adicionar Titular" # Achar menssagem
    if Achar_essa_menssagem in texto:
        return True
    else:
        return False


#========================== VERIFICAR COORDENADOR NO POLO =================================#
def Verificar_coordenador_polo():
    time.sleep(8)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    print_da_tela = pyautogui.screenshot() # Tira uma captura da tela
    texto = pytesseract.image_to_string(print_da_tela)
    Achar_essa_menssagem = "AVA"
    if Achar_essa_menssagem in texto:
        return True
    else:
        return False


#============================ FECHAR PÁGINA DE CADASTRO" ==================================#
def Fechar_página_de_cadastro():
    pyautogui.hotkey('Ctrl', 'tab') # Fechar página de cadastro
    time.sleep(0.20)
    pyautogui.hotkey('alt', 'o', 'c') # Voltar para a página de cadastro


#=============================== VOLTAR E MARCA "-18" =====================================#
def Marcar_menor_de_idade():
    time.sleep(3)
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(0.20)
    for i in range(7): 
        pyautogui.press("left") 
    time.sleep(0.20)
    pyautogui.write("IDADE -18") # escrever menor de idade
    time.sleep(0.20)
    for i in range(2): 
        pyautogui.press("right")
        time.sleep(0.20)
    pyautogui.press("down")
    time.sleep(0.20)
    pyautogui.hotkey('alt', 'tab') # F10


#================================ CONTA INSCRIÇÕES ========================================#
def Contar_inscrições(Contador, Valor_atual, Limite):
    Mais_uma_inscrição = Contador
    Ja_inscritos = Valor_atual
    Limite_de_inscrições = Limite

    Ja_inscritos += Mais_uma_inscrição

    if Ja_inscritos == Limite_de_inscrições:
        return True
    else:
        pass


#================================= VERIFICAR CPF ==========================================#
def Verificar_cpf():
    time.sleep(2)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    print_da_tela = pyautogui.screenshot() # Tira uma captura da tela
    texto = pytesseract.image_to_string(print_da_tela) # Converte a imagem em texto
    Achar_essa_menssagem = "CPF ou do CNP" # Achar menssagem
    if Achar_essa_menssagem in texto:
        return True
    else:
        pass


#=========================== VOLTAR E MARCA ERRO DE CPF ===================================#
def Marca_erro_de_cpf():
    time.sleep(3)
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(0.20)
    for i in range(7): 
        pyautogui.press("left") 
    time.sleep(0.20)
    pyautogui.write("ERRO! - CPF") # erro! - cpf
    time.sleep(0.20)
    for i in range(2): 
        pyautogui.press("right")
        time.sleep(0.20)
    pyautogui.press("down")
    time.sleep(0.20)
    pyautogui.hotkey('alt', 'tab') # F10


#================================= VERIFICAR CEP ==========================================#
def Verificar_cep():
    time.sleep(2)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    print_da_tela = pyautogui.screenshot() # Tira uma captura da tela
    texto = pytesseract.image_to_string(print_da_tela) # Converte a imagem em texto
    Achar_essa_menssagem = "CEP Invalido" # Achar menssagem
    if Achar_essa_menssagem in texto:
        return True
    else:
        return False


#=========================== VOLTAR E MARCA ERRO DE CEP ===================================#
def Marca_erro_de_cep():
    time.sleep(3)
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(0.20)
    for i in range(7): 
        pyautogui.press("left") 
    time.sleep(0.20)
    pyautogui.write("ERRO! - CEP") # erro! - cpf
    time.sleep(0.20)
    for i in range(2): 
        pyautogui.press("right")
        time.sleep(0.20)
    pyautogui.press("down")
    time.sleep(0.20)
    pyautogui.hotkey('alt', 'tab') # F10


#============================== VERIFICAR TELEFONE ========================================#
def Verificar_telefone():
    for i in range(4): 
        pyautogui.press("right") 
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'c') # copia o "TELEFONE"
    numero = pyperclip.paste()
    numero = numero.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    Quantidades_de_digitos = len(numero)
    time.sleep(1)
    if Quantidades_de_digitos == 11 or Quantidades_de_digitos == 12:
        pyautogui.hotkey('alt', 'tab') # F10
        time.sleep(1)
        for i in range(4):
            pyautogui.press("tab")
        time.sleep(1)
        for i in range(10):
            pyautogui.press("right") # vai pro final da aba de telefone - f10
        time.sleep(1)
        for i in range(12):
            pyautogui.press("Backspace") # apaga o telefone
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v') # colar o "TELEFONE"
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab') # Chrome
        return True
    else:
        return False

                
#======================== VOLTAR E MARCA ERRO DE TEELFONE =================================#
def Marca_erro_telefone():
    time.sleep(0.20)
    for i in range(6): 
        pyautogui.press("left") 
    time.sleep(0.20)
    pyautogui.write("ERRO! - TELEFONE") # erro! - cpf
    time.sleep(0.20)
    for i in range(2): 
        pyautogui.press("right")
        time.sleep(0.20)
    pyautogui.press("down")                                     
    time.sleep(0.20)
    pyautogui.hotkey('alt', 'tab') # F10


#============================= CADASTRO REPETIDO ==========================================#
def Cadastro_repetido():
    for i in range(2): 
        pyautogui.press("left")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c') # copia o "aba"
    Repetido = pyperclip.paste()
    if Repetido == "Repetido":
        return True
    else:
        pass


#============================== ESCONDER MAUSE ============================================#
def Esconder_tecla():
    screen_width, screen_height = pyautogui.size() # Obtém a resolução da tela (largura e altura)
    pyautogui.moveTo(screen_width // 2, screen_height // 2) # Move o cursor para o centro da tela
    pyautogui.moveTo(screen_width - 1, screen_height // 2) # Move o cursor para a borda direita da tela
