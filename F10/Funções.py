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
import re

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
    pyautogui.press("Enter")
    time.sleep(0.10)
    for i in range(6):
        pyautogui.press("tab")


#================================== MARCAR "OK" ===========================================#
def marcar_ok():
    for i in range(2): 
        pyautogui.press("left")
    pyautogui.press("space")


#================================ VOLTAR PARA O "CPF" =====================================#
def voltar_para_cpf():
    for i in range(3): 
        pyautogui.press("left") 


#================================== PROXIMO "CPF" =========================================#
def proximo_cpf():
    pyautogui.press("down")


#=================================== COPIA "CEP" ==========================================#
def copia_CEP():
    for i in range(1): 
        pyautogui.press("right") 


#=================================== APAGAR "CEP" =========================================#
def apagar_CEP():
    for i in range(10):
        pyautogui.press("Backspace")


#================================= ESCOLHER CONTRATO ======================================#
def Tipo_de_Contarto():
    Tipo_de_Contarto = "Bolsa"
    return pyautogui.write(Tipo_de_Contarto)


#================================= ESCOLHER MATRÍCULA =====================================#
def Matrícula(valor):
    data_do_usuário = valor
    for i in range(10):
        pyautogui.press("Backspace")
    return pyautogui.write(data_do_usuário)


#================================== ESCOLHER EVENTO =======================================#
def Evento():
    Evento = "RIO+CURSOS"
    return pyautogui.write(Evento)


#================================ ESCOLHER COORDENADOR ====================================#
def Coordenador():
    Coordenador = "Rodrigo Drumond"
    return pyautogui.write(Coordenador)


#=================================== ESCOLHER POLO ========================================#
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


#================================== TURMA EM ABERTO =======================================#
def turma_em_aberto():
    for i in range(8):
        pyautogui.hotkey('shift', 'tab')
    pyautogui.press("space")


#================================== OPÇÕES DE CURSOS ======================================#
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


#=================================== BUTÃO GRAVAR =========================================#
def BUTÃO_GRAVAR():
    for i in range(8):
        pyautogui.press('tab')
        time.sleep(1) #=============================== EXCLUIR
    #pyautogui.press("Enter")


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
    Achar_essa_menssagem = "AVA"
    if Achar_essa_menssagem in texto:
        return True
    else:
        return False


#============================== FECHAR PÁGINA DE CADASTRO" ================================#
def Fechar_página_de_cadastro():
    pyautogui.hotkey('Ctrl', 'tab') # Fechar página de cadastro
    time.sleep(0.20)
    pyautogui.hotkey('alt', 'o', 'c') # Voltar para a página de cadastro


#================================ VOLTAR E MARCA "-18" ====================================#
def Marcar_menor_de_idade():
    time.sleep(3)
    pyautogui.hotkey('alt', 'tab') # Chrome
    time.sleep(0.20)
    for i in range(7): 
        pyautogui.press("left") 
    time.sleep(0.20)
    pyautogui.write("-18") # escrever menor de idade
    time.sleep(0.20)
    for i in range(2): 
        pyautogui.press("right")
        time.sleep(0.20)
    pyautogui.press("down") # proximo "CPF"
    time.sleep(0.20)
    pyautogui.hotkey('alt', 'tab') # F10


#================================= CONTA INSCRIÇÕES =======================================#
def Contar_inscrições(Contador, Valor_atual, Limite):
    Mais_uma_inscrição = Contador
    Ja_inscritos = Valor_atual
    Limite_de_inscrições = Limite

    Ja_inscritos += Mais_uma_inscrição

    if Ja_inscritos == Limite_de_inscrições:
        return True
    else:
        pass


#================================== VERIFICAR CPF =========================================#
def Verificar_cpf():
    time.sleep(2)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    print_da_tela = pyautogui.screenshot() # Tira uma captura da tela
    texto = pytesseract.image_to_string(print_da_tela) # Converte a imagem em texto
    Achar_essa_menssagem = "CPF ou do CNJ" # Achar menssagem
    if Achar_essa_menssagem in texto:
        return True
    else:
        pass


#============================ VOLTAR E MARCA ERRO DE CPF ==================================#
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
    pyautogui.press("down") # proximo "CPF"
    time.sleep(0.20)
    pyautogui.hotkey('alt', 'tab') # F10


#================================== VERIFICAR CEP =========================================#
def Verificar_cep():
    time.sleep(1)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    print_da_tela = pyautogui.screenshot() # Tira uma captura da tela
    texto = pytesseract.image_to_string(print_da_tela) # Converte a imagem em texto
    Achar_essa_menssagem = "CEP Invalido" # Achar menssagem
    if Achar_essa_menssagem in texto:
        return True
    else:
        pass


#============================ VOLTAR E MARCA ERRO DE CEP ==================================#
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
    pyautogui.press("down") # proximo "CPF"
    time.sleep(0.20)
    pyautogui.hotkey('alt', 'tab') # F10


#=============================== VERIFICAR TELEFONE =======================================#
def Verificar_telefone():
    for i in range(3): 
        pyautogui.press("right") 
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'c') # copia o "TELEFONE"
    numero = pyperclip.paste()
    numero = numero.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    Quantidades_de_digitos = len(numero)
    if Quantidades_de_digitos == 11:
        return True
    else:
        return False


#========================= VOLTAR E MARCA ERRO DE TELEFONE ================================#
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
    pyautogui.press("down") # proximo "CPF"
    time.sleep(0.20)
    pyautogui.hotkey('alt', 'tab') # F10


#================================ CORRIGIR NOME ===========================================#
def Verificar_nome():
    for i in range(1): 
        pyautogui.press("right") 
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'c') # copia o "NOME"
    nome = pyperclip.paste()
    nome_limpo = re.sub(r'[^a-zA-ZáéíóúàèìòùãõâêîôûÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛÇç\s]', '', nome)
    if nome == nome_limpo:
        return True
    else:
        return False


#========================== VOLTAR E MARCA ERRO DE NOME ===================================#
def Marca_erro_nome():
    time.sleep(3)
    for i in range(3): 
        pyautogui.press("left") 
    time.sleep(0.20)
    pyautogui.write("ERRO! - NOME") # erro! - cpf
    time.sleep(0.20)
    for i in range(2): 
        pyautogui.press("right")
        time.sleep(0.20)
    pyautogui.press("down") # proximo "CPF"
    time.sleep(0.20)
    pyautogui.hotkey('alt', 'tab') # F10


#=========================== VERIFICAR REMOVER TITULAR ====================================#
def Verificar_remover_titular():
    time.sleep(2)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    print_da_tela = pyautogui.screenshot() # Tira uma captura da tela
    texto = pytesseract.image_to_string(print_da_tela) # Converte a imagem em texto
    Achar_essa_menssagem = "Dados do Contrato" # Achar menssagem
    if Achar_essa_menssagem in texto:
        return True
    else:
        pass


#=============================== REMOVER TITULAR ==========================================#
def Remover_titular():
    time.sleep(1)
    for i in range(1):
        pyautogui.press("tab")
    pyautogui.press("Enter")
    time.sleep(0.20)
    pyautogui.press("tab")
    for i in range(1):
        pyautogui.hotkey('Ctrl', 'tab')
