import pyautogui as py
import pyperclip
import time

time.sleep(5)

def valor_copiado():
    py.hotkey("ctrl", "c")
    valor = pyperclip.paste()
    lista_palavras = valor.split()
    return lista_palavras

c = 0
x = py.position()
print(x)
while True: 
    c += 1
    if c > 1:
        py.hotkey('Alt', 'tab')
        time.sleep(1)
        py.click(x=210, y=203)
        py.hotkey('Alt', 'tab')
    time.sleep(0.30)
    py.hotkey('ctrl', 'c')
    time.sleep(1)
    py.hotkey('Alt', 'tab')
    time.sleep(1)
    py.press("f4")
    time.sleep(1)
    for i in range(14):   
        py.press("tab")
    time.sleep(1)
    py.hotkey('ctrl', 'v')
    time.sleep(1)
    for i in range(21):
        py.press("Enter")
    time.sleep(1)
    py.press("down")
    time.sleep(1)
    py.hotkey("ctrl", "c")
    time.sleep(1)
    py.hotkey('Alt', 'tab')
    time.sleep(1)
    for i in range(16):
        py.press("Right")
    time.sleep(1)
    py.hotkey("ctrl", "v")
    time.sleep(1)
    py.press("down")
    time.sleep(1)
    py.hotkey("ctrl", "c")
    time.sleep(1)
    py.press("up")
    time.sleep(1)
    py.hotkey('Alt', 'tab')
    time.sleep(1)
    py.click(x=406, y=201)
    time.sleep(1)
    py.press("f4")
    time.sleep(2)
    py.press("tab")
    time.sleep(1)               
    py.hotkey('ctrl', 'v')
    time.sleep(1)
    py.press("Enter")
    time.sleep(1)    
    py.press("down")
    time.sleep(3)
    x = valor_copiado()
    time.sleep(1)
    if "Preparatório" not in x:
        c -= 1
        py.hotkey('Alt', 'tab')
        time.sleep(1)
        for i in range(16):
            py.press("Left")
        time.sleep(1)
        py.press("down")
        time.sleep(1)
        py.hotkey('Alt', 'tab')
        time.sleep(1)
        py.click(x=210, y=203)
        time.sleep(1)
        py.hotkey('Alt', 'tab')
        time.sleep(1)
        continue    
    py.press("apps")
    time.sleep(1)
    for i in range(7):
        py.press("down")
    py.press("Enter")
    time.sleep(1)
    py.press("down")
    time.sleep(1)
    py.press("Enter")
    time.sleep(1)
    for i in range(4):
        py.press("tab")
    py.press("Enter")
    py.press("Enter")
    time.sleep(1)
    py.press("Esc")
    time.sleep(1)
    py.hotkey('Alt', 'tab')
    time.sleep(1)
    for i in range(18):
        py.press("Left")
    time.sleep(1)
    py.press("space")
    time.sleep(1)
    py.press("down")
    time.sleep(1)
    for i in range(2):
        py.press("Right")
    time.sleep(1)
    if c == 40:
        break
