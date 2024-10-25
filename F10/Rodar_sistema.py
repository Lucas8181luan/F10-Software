import pyautogui 
import subprocess
import time
import pytesseract
import Funções
import ctypes

# >> Instalador do Tesseract para Windows <<
# >> Deixar página do F10 aberta

#======================= INICIAR PROGRAMRA ====================================#
USUÁRIO = input('\033[34mDigite "OK" para iniciar programar = \033[0m').upper().strip() # resposta do usuário
# -> START
if USUÁRIO == "OK": # condição para rodar o programar
    for vezes in range(3):
        #====================== BUTÃO ADICIONAR (POSITION) ============================#
        pyautogui.moveTo(x=-1687, y=159) # mover para o butão +
        pyautogui.click() # clicar no butão +
        time.sleep(5)
        #============================= ABRIR EXCEL ====================================#
        if vezes == 0:
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            url = "https://docs.google.com/spreadsheets/d/1JrIQ34CDatOb-2kFIt50inUjIt2tYcULB1NJiC94mF4/edit?gid=1579823280#gid=1579823280"  
            subprocess.Popen([chrome_path, url]) # abrir a página
        #===================== PRIMEIRA LINHA PARA LEITURA ============================#
            pyautogui.moveTo(x=-1109, y=556) # mover para primeira linha de "CPF" da panilha
            time.sleep(20)
            pyautogui.click() # clicar
        #====================== PROXIMA LINHA PARA LEITURA ============================#
        else:
            pass
        #=============================== PARTE - 1 =====================================#
        pyautogui.hotkey('ctrl', 'c') # copia o "CPF"
        time.sleep(0.20)
        pyautogui.hotkey('alt', 'tab') # F10
        time.sleep(5)
        pyautogui.moveTo(x=-1685, y=454) # mover para a parte de prenhencher "CPF"
        time.sleep(5)
        pyautogui.click() # clicar
        pyautogui.hotkey('ctrl', 'v') # colar o "CPF" copiado
        pyautogui.moveTo(x=-797, y=659) # mover para butão OK
        time.sleep(5)
        pyautogui.click() # clicar
        #============================ BUTÃO PROXIMO ====================================#
        time.sleep(2)
        pyautogui.moveTo(x=-830, y=865) # mover para o butão proximo
        pyautogui.click() # clicar
        time.sleep(5)
        #=============================== PARTE - 2 =====================================#
        #================ TIPO DE CONTRATO ==================#
        pyautogui.moveTo(x=-1438, y=413) # escolher tipo de contrato
        pyautogui.click() # clicar
        time.sleep(3)
        pyautogui.moveTo(x=-1545, y=436) # opção - "bolsa"
        pyautogui.click() # clicar
        time.sleep(3)
        #============ OPÇÃO - DATA DA MATRÍCULA ==============#
        pyautogui.moveTo(x=-1409, y=474) # escolher a data da matrícula
        pyautogui.click() # clicar
        time.sleep(3)
        pyautogui.moveTo(x=-1364, y=591) # DATA DEJESADA <--------------
        pyautogui.click() # clicar
        time.sleep(3)
        #================ OPÇÃO - EVENTO =====================#
        pyautogui.moveTo(x=-1287, y=530) # escolher evento
        pyautogui.click() # clicar
        time.sleep(3)
        pyautogui.moveTo(x=-1290, y=579) # opção - RIO + CURSOS
        pyautogui.click() # clicar
        time.sleep(3)
        #================= OPÇÃO - CURSO =====================#
        pyautogui.moveTo(x=-1293, y=588) # escolher opção curso
        pyautogui.click() # clicar
        time.sleep(3)
        pyautogui.moveTo(x=-1428, y=615) # CURSO DEJESAD0 <--------------
        pyautogui.click() # clicar
        time.sleep(3)
        #=============== OPÇÃO - COORDENADOR =================#
        pyautogui.moveTo(x=-1290, y=640) # escolher opção coordenador
        pyautogui.click() # clicar
        pyautogui.moveTo(x=-1422, y=728) # COORDENADOR DESEJAD0 <--------------
        pyautogui.click() # clicar
        #============================ BUTÃO PROXIMO ====================================#
        time.sleep(2)
        pyautogui.moveTo(x=-672, y=870) # mover para o butão proximo
        pyautogui.click() # clicar
        time.sleep(5)
        #=============================== PARTE - 3 =====================================#
        pyautogui.moveTo(x=-469, y=453) # escolher polo
        pyautogui.click() # clicar
        time.sleep(5)
        pyautogui.moveTo(x=-700, y=473) # opção - rio + curso
        pyautogui.click() # clicar
        time.sleep(5)
        pyautogui.moveTo(x=-1635, y=546) # opção de turma (para verificar a captura de tela)
        time.sleep(3)
        #------
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # especifique o caminho do Tesseract, se necessário
        captura_de_tela = pyautogui.screenshot() # captura o espaço
        text = pytesseract.image_to_string(captura_de_tela) # converte a imagem em texto
        #-------
        if text == "":
            pyautogui.moveTo(x=-1659, y=383) # deixar turma em aberto
            pyautogui.click() # clicar
            #============================ BUTÃO PROXIMO ====================================#
            time.sleep(2)
            pyautogui.moveTo(x=-672, y=870) # mover para o butão proximo
            pyautogui.click() # clicar
            time.sleep(5)
        else:
            pyautogui.moveTo(x=-1669, y=546) # escolher turma AVA
            pyautogui.click() # clicar
            #=========================== BUTÃO GRAVAR =====================================#
            time.sleep(3)
            pyautogui.moveTo(x=-589, y=868) # mover para o butão proximo
            #pyautogui.click() # clicar
            time.sleep(5)
#================================================= EXCEL ====================================================#
        pyautogui.hotkey('alt', 'tab') # Chrome
        time.sleep(2)
        pyautogui.moveTo(x=-559, y=89) # clique na página
        pyautogui.click() # clicar
        time.sleep(5)
        Funções.marcar_ok() # marca OK
        time.sleep(2)
        Funções.voltar_para_cpf()
        time.sleep(2) # voltar para o cpf
        Funções.proximo_cpf() # passar para proximo cpf
        time.sleep(10)
        pyautogui.hotkey('alt', 'tab') # F10
