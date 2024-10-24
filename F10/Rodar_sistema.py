import pyautogui 
import subprocess
import time
import pandas

''' import win32gui    

def hide_cursor():
    win32gui.ShowCursor(False)

# PARTE - 1 (CONCLUIDA) 
hide_cursor()
time.sleep(0.10)  -> "OCULTAR CURSOR" '''
#====================== BUTÃO ADICIONAR (POSITION) ============================#
pyautogui.moveTo(x=-1687, y=159) # mover para o butão +
pyautogui.click() # clicar no butão +
time.sleep(5)
#====================== ====== ABRIR EXCEL ====================================#
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
url = "https://docs.google.com/spreadsheets/d/1JrIQ34CDatOb-2kFIt50inUjIt2tYcULB1NJiC94mF4/edit?gid=1579823280#gid=1579823280"  
subprocess.Popen([chrome_path, url]) # abrir a página
#===================== PRIMEIRA LINHA PARA LEITURA ============================#
pyautogui.moveTo(x=595, y=503) # mover para primeira linha de "CPF" da panilha
time.sleep(20)
pyautogui.click() # clicar
time.sleep(5)
#========================== COPIA E COLAR "CPF" ===============================#
pyautogui.hotkey('ctrl', 'c') # copia o "CPF"
time.sleep(1)
pyautogui.moveTo(x=-1685, y=454) # mover para a parte de prenhencher "CPF"
time.sleep(5)
pyautogui.click() # clicar
time.sleep(1)
pyautogui.hotkey('ctrl', 'v') # colar o "CPF" copiado
#=============================== PROXIMO ======================================#
pyautogui.moveTo(x=-797, y=659) # mover para butão OK
time.sleep(2)
pyautogui.click() # clicar
time.sleep(1)
pyautogui.moveTo(x=-830, y=865) # mover para o butão proximo
