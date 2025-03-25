from flask import Flask, request 

app = Flask(__name__)
alunos = [
    {'id': 1, 'nome': 'maria marques'},
    {'id':2, 'nome': 'julia'}
]

@app.route("/alunos/<int:id>", methods=["GET"])
def metodo_get_por_id(id):
    for aluno in alunos:
        if aluno['id']== id:
            return aluno
    return{}    

@app.route("/alunos", methods=["GET"])
def metodo_get():
    return alunos
     

@app.route("/alunos", methods=["POST"])
def metodo_post():
    dados_recebidos = request.get_json()
    alunos.append(
        {'nome': dados_recebidos['nome']}
    )
    return {'mensagem': 'ok'}

