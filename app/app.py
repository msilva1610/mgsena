from flask import Flask, jsonify, request
from flask.views import MethodView
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"

    return "Hello from Flask"

@app.route('/calcQuinas', methods=['POST'])
def calc():
    print ('is json: {}'.format(request.is_json))
    # j = request.get_json()
    # print(j['dezenas'])
    jsonData = request.get_json(force=True)
    retorno = []
    for r in jsonData:
        qtdeTernos, qtdeQuadras, qtdeQuinas = 0,0,0
        dezenas = r['dezenas']
        listaQuinas = r['listaQuinas']
        id_aposta = r['id_aposta']
    
        qtdeTernos, qtdeQuadras, qtdeQuinas = contaQuinas(dezenas, listaQuinas)
        retorno.append({'id_aposta': id_aposta, 'Ternos': qtdeTernos, 'Quadras':qtdeQuadras, 'Quinas': qtdeQuinas})
    print(jsonify(retorno))
    return jsonify(retorno)

def contaQuinas(dezenas, listaQuinas):
    print('Total de quinas: {}'.format(len(listaQuinas)))
    qtde = 0
    qtdeTernos,qtdeQuadras,qtdeQuinas = 0,0,0
    for quina in listaQuinas:
        qtde = 0
        for d in dezenas:
            if d in quina:
                qtde += 1
                if qtde == 3:
                    qtdeTernos += 1
                elif qtde == 4:
                    qtdeQuadras += 1
                elif qtde == 5:
                    qtdeQuinas += 1
    return qtdeTernos, qtdeQuadras, qtdeQuinas


if __name__ == '__main__':
    # app.run(host='0.0.0.0',debug=True)
    app.run(host='0.0.0.0')