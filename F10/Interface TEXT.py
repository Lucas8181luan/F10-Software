import tkinter as tk

def Bot_F10():
    tk.Label.config(text="Olá, mundo!")

app = tk.Tk()
app.title("IFP") # Titulo

button_iniciar_programa = tk.Button(app, text="Inicia Programar")
button_iniciar_programa.pack()

# VER COMO FAZER UM INPUT PARA CONSEGUIR A RESPOSTA
pergunta = tk.Entry(app)
pergunta.pack(pady=10)

app.mainloop() # Abrir o aplicativo
