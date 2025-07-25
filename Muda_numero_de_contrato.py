import pyautogui as py
import time

time.sleep(5)

c = 0

for i in range(3000):
    c += 1
    py.press("down")
    time.sleep(1)
    py.press("Enter")
    time.sleep(1)
    valor_atual = 5917
    numero = valor_atual + c
    matricula = str(numero)
    for i in range(4):
        py.press("Backspace")
    time.sleep(1)
    py.write(matricula)
    time.sleep(1)
    for i in range(29):
        py.press("tab")
    py.press("Enter")
    time.sleep(1)
