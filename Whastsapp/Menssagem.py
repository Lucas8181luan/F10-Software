import pywhatkit
import time

def DISPARO():
    list_dados = [
        {
            "nome": "Samuel",
            "local": "Madureira",
            "dias": "Segunda, Terça",
            "horário": "19:00",
            "data": "04/07/2025",
            "telefone": "+5561994619166",
        },

        {
            "nome": "Maria",
            "local": "Copacabana",
            "dias": "Quarta, Sexta",
            "horário": "14:00",
            "data": "05/07/2025",
            "telefone": "+5561992520720",
        }
    ]

    for dados in list_dados:
        
        nome = dados["nome"]
        local = dados["local"]
        dias = dados["dias"]
        horário = dados["horário"]
        data = dados["data"]
        telefone = dados["telefone"]

        def MSG(nome, local, dias, horário, data, telefone):

            time.sleep(10)
            
            mensagem = f"""Olá, {nome}! Tudo bem? 😊

Passando aqui pra te avisar que passamos por um período com altíssima demanda de inscrições para o preparatório gratuito do ENCCEJA, oferecido pela Prefeitura do Rio, e isso gerou um pequeno atraso no processamento dos cadastros.

Mas conseguimos encaminhar todo mundo e temos uma ótima notícia: você está oficialmente matriculado(a) na turma da região de {local}! 🎉

🗓️ As aulas acontecerão às {dias}, no horário das {horário}, com início das aulas previsto para hoje, dia {data}.

Fique atento(a) às próximas mensagens por aqui, em breve traremos mais informações sobre o local das aulas e o cronograma completo.

Estamos muito felizes por ter você com a gente nessa caminhada rumo à sua certificação e aprovação no ENCCEJA! Conte conosco! 📚✨"""

            pywhatkit.sendwhatmsg_instantly(
                phone_no=telefone,
                message=mensagem,
                wait_time=15,
                tab_close=False
            )

        MSG(nome=nome, local=local, dias=dias, horário=horário, data=data, telefone=telefone)

DISPARO()
