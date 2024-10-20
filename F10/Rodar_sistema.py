import pandas as pd
from IPython.display import display

# Puxar Arquivo
puxar_arquivos = pd.read_excel("F10\\Rio+Cursos Inscrições 17.10.24.xlsx")
# Filtra a tabela toda
filtro_coluna = puxar_arquivos[["Aluno", "CPF"]]
# Puxar os dadsos importantes dos alunos
filtro_nome = puxar_arquivos[puxar_arquivos["Aluno"] == "Elizabeth Cristina Freire"]
display(filtro_nome[["Aluno", "CPF", "Celular"]])
