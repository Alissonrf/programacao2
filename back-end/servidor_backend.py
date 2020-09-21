from config import *
from modelo import Mouse

@app.route("/")
def inicio():
    return 'Sistema de cadastro de mouses. '+\
        '<a href="/listar_mouses">Operação listar</a>'

@app.route("/listar_mouses")
def listar_mouses():
    # obter os mouses do cadastro
    mouses = db.session.query(Mouse).all()
    # aplicar o método json que a classe Mouse possui a cada elemento da lista
    mouses_em_json = [ x.json() for x in mouses ]
    # converter a lista do python para json
    resposta = jsonify(mouses_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

# teste da rota: curl -d '{"nome":"James Kirk", "telefone":"92212-1212", "email":"jakirk@gmail.com"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_pessoa
@app.route("/incluir_mouses", methods=['post'])
def incluir_mouses():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações da nova pessoa
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    try: # tentar executar a operação
      nova = Mouse(**dados) # criar a nova pessoa
      db.session.add(nova) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
      # informar mensagem de erro
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

app.run(debug=True)