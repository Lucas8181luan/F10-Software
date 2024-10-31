#=============================================================================================#
#=========================================== SITE ============================================#
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

# rota
app = Flask(__name__)
@app.route("/") # página principal
def homepage():
    return render_template("Site-bot.html") # página html

# QUANTIDADE DE VEZES PARA RODA O PROGRAMA
@app.route("/RespostaUsuário", methods=["POST"]) # rota
def Quantidades_de_usuário():
    Resposta_Quantidades = request.form.get("quantidades_usuário") # RESPOSTA
    return redirect("/") # Volta para a página inicial

# ESCOLHER A DATA DE CADASTRO DO USUÁRIO
@app.route("/RespostaUsuário2", methods=["POST"]) # rota
def Data_de_cadastro():
    Resposta_Data = request.form.get("data_de_cadastro") # RESPOSTA
    return redirect("/") # Volta para a página inicial

@app.route("/RespostaUsuário3", methods=["POST"]) # rota
def Opções_de_cursos():
    Resposta_Curso = request.form.get("CURSOS") # RESPOSTA
    return redirect("/") # Volta para a página inicial

@app.route("/RespostaUsuário4", methods=["POST"]) # rota
def Butão_iniciar_programa():
    Resposta_Butão = request.form.get("INICIAR PROGRAMA")
    return redirect("/") # Volta para a página inicial

if __name__ == "__main__":
    app.run(debug=True) # atualizar automaticamente
