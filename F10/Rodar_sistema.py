import pyautogui 
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
    time.sleep(10) # colocar contagem aqui (chrome) -> (f10) abrir
    for vezes in range(3): 
        #====================== BUTÃO ADICIONAR (POSITION) ============================#
        pyautogui.moveTo(x=-1687, y=159) # mover para o butão + >>>>>(CORDENADAS)<<<<< 1º
        pyautogui.click() # clicar no butão +
        time.sleep(5)
        #============================= ABRIR EXCEL ====================================#
        if vezes == 0: # rodar 1º vez
            pyautogui.hotkey('alt', 'tab') # Chrome
        #===================== PRIMEIRA LINHA PARA LEITURA ============================#
            pyautogui.moveTo(x=-1109, y=556) # mover para primeira linha de "CPF" da panilha >>>>>(CORDENADAS)<<<<< 2º
            time.sleep(5)
            pyautogui.click() # clicar
        #=============================== PARTE - 1 =====================================#
        if vezes > 0: # rodar o resto do programa todo
            pyautogui.hotkey('alt', 'tab') # Chrome
        pyautogui.hotkey('ctrl', 'c') # copia o "CPF"
        time.sleep(0.10)
        pyautogui.hotkey('alt', 'tab') # F10
        time.sleep(5)
        pyautogui.moveTo(x=-1685, y=454) # mover para a parte de prenhencher "CPF" >>>>>(CORDENADAS)<<<<< 3º
        time.sleep(3)
        pyautogui.click() # clicar
        pyautogui.hotkey('ctrl', 'v') # colar o "CPF" copiado
        pyautogui.moveTo(x=-797, y=659) # mover para butão OK >>>>>(CORDENADAS)<<<<< 4º
        time.sleep(3)
        pyautogui.click() # clicar
        time.sleep(2)
        pyautogui.hotkey('alt', 'tab') # Chrome
        time.sleep(2)
        Funções.copia_CEP()
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c') # copia o "CEP"
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab') # F10
        time.sleep(2)
        pyautogui.moveTo(x=-1590, y=631) # move para o CEP >>>>>(CORDENADAS)<<<<< º
        time.sleep(2)
        pyautogui.click() # click
        time.sleep(2)
        Funções.apagar_CEP()
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v') # colar o "CEP"
        #============================ BUTÃO PROXIMO ====================================#
        time.sleep(2)
        pyautogui.moveTo(x=-830, y=865) # mover para o butão proximo >>>>>(CORDENADAS)<<<<< 5º
        pyautogui.click() # clicar
        time.sleep(3)
        #=============================== PARTE - 2 =====================================#
        #================ TIPO DE CONTRATO ==================#
        pyautogui.moveTo(x=-1438, y=413) # butão escolher tipo de contrato >>>>>(CORDENADAS)<<<<< 6º
        pyautogui.click() # clicar
        time.sleep(3)
        pyautogui.moveTo(x=-1545, y=436) # opção - "bolsa" >>>>>(CORDENADAS)<<<<< 7º
        pyautogui.click() # clicar
        time.sleep(3)
        #============ OPÇÃO - DATA DA MATRÍCULA ==============#
        pyautogui.moveTo(x=-1409, y=474) # butão escolher a data da matrícula >>>>>(CORDENADAS)<<<<< 8º
        pyautogui.click() # clicar
        time.sleep(3)
        pyautogui.moveTo(x=-1404, y=556) # DATA DEJESADA <-------------- >>>>>(CORDENADAS)<<<<< 9º
        pyautogui.click() # clicar
        time.sleep(3)
        #================ OPÇÃO - EVENTO =====================#
        pyautogui.moveTo(x=-1287, y=530) # butaõ escolher evento >>>>>(CORDENADAS)<<<<< 10º
        pyautogui.click() # clicar
        time.sleep(3)
        pyautogui.moveTo(x=-1290, y=579) # opção - RIO + CURSOS >>>>>(CORDENADAS)<<<<< 11º
        pyautogui.click() # clicar
        time.sleep(3)
        #================= OPÇÃO - CURSO =====================#
        pyautogui.moveTo(x=-1293, y=588) # butão escolher opção curso >>>>>(CORDENADAS)<<<<< 12º
        pyautogui.click() # clicar
        time.sleep(3)
        pyautogui.moveTo(x=-1428, y=615) # CURSO DEJESADO <-------------- >>>>>(CORDENADAS)<<<<< 13º
        pyautogui.click() # clicar
        time.sleep(3)
        #=============== OPÇÃO - COORDENADOR =================#
        pyautogui.moveTo(x=-1290, y=640) # butão escolher opção coordenador >>>>>(CORDENADAS)<<<<< 14º
        pyautogui.click() # clicar
        pyautogui.moveTo(x=-1422, y=728) # COORDENADOR DESEJADO <-------------- >>>>>(CORDENADAS)<<<<< 15º
        pyautogui.click() # clicar
        #============================ BUTÃO PROXIMO ====================================#
        time.sleep(2)
        pyautogui.moveTo(x=-672, y=870) # mover para o 2º butão proximo >>>>>(CORDENADAS)<<<<< 16º
        pyautogui.click() # clicar
        time.sleep(3)
        #=============================== PARTE - 3 =====================================#
        pyautogui.moveTo(x=-469, y=453) # butão escolher polo >>>>>(CORDENADAS)<<<<< 17º
        pyautogui.click() # clicar
        time.sleep(3)
        pyautogui.moveTo(x=-700, y=473) # opção - rio + curso >>>>>(CORDENADAS)<<<<< 18º
        pyautogui.click() # clicar
        time.sleep(3)
        pyautogui.moveTo(x=-1635, y=546) # opção de turma (para verificar a captura de tela) >>>>>(CORDENADAS)<<<<< 19º
        time.sleep(3)
        #------
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # especifique o caminho do Tesseract, se necessário
        captura_de_tela = pyautogui.screenshot() # captura o espaço
        text = pytesseract.image_to_string(captura_de_tela) # converte a imagem em texto
        #-------
        if text == "":
            pyautogui.moveTo(x=-1659, y=383) # deixar turma em aberto >>>>>(CORDENADAS)<<<<< 20º
            pyautogui.click() # clicar
            #============================ BUTÃO PROXIMO ====================================#
            time.sleep(2)
            pyautogui.moveTo(x=-672, y=870) # mover para o butão gravar >>>>>(CORDENADAS)<<<<< 21º
            pyautogui.click() # clicar090.531.867-60
            time.sleep(3)
        else:
            pyautogui.moveTo(x=-1669, y=546) # escolher turma AVA >>>>>(CORDENADAS)<<<<< 22º
            pyautogui.click() # clicar
            #=========================== BUTÃO GRAVAR =====================================#
            time.sleep(3)
            pyautogui.moveTo(x=-589, y=868) # mover para o butão gravar >>>>>(CORDENADAS)<<<<< 23º
            #pyautogui.click() # clicar
            time.sleep(10) ##### ------ colocar para "5"
#================================================= EXCEL ====================================================#
        pyautogui.hotkey('alt', 'tab') # Chrome
        time.sleep(2)
        pyautogui.moveTo(x=-488, y=85) # clique na página >>>>>(CORDENADAS)<<<<< 24º
        pyautogui.click() # clicar
        time.sleep(2)
        Funções.marcar_ok() # marca OK
        time.sleep(2)
        Funções.voltar_para_cpf()
        time.sleep(2) # voltar para o cpf
        Funções.proximo_cpf() # passar para o proximo cpf
        time.sleep(5)
        pyautogui.hotkey('alt', 'tab') # F10
        time.sleep(5)

print("\033[31mPROGRAMA ENCERRADO!\033[0m")
