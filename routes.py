from flask import Flask, request
from main import insertUsuario

app = Flask("Youtuber")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return { "ola" : "mundo" }

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():
    body = request.get_json()
    usuario = insertUsuario(body['nome'], body['email'], body['senha'])
    return geraResponse(200, "Usuário criado!", "user", usuario)
    

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem
    if (nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response

app.run()