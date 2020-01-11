import requests
import json

dezenas = [1,2,3,4,5,6]
# listaQuinas = ([1,2,3,4,8],[4,5,6,7,8])
id_aposta = 1
dados = []
# data = {'id_aposta': id_aposta, 'dezenas': dezenas, 'listaQuinas':listaQuinas}
data = {'id_aposta': id_aposta, 'dezenas': dezenas}

dados.append(data)


# print('Total de quinas: {}'.format(len(listaQuinas)))
# quina = [1,2,3,7,8]
jsonData = json.dumps(dados)

# r = requests.post('http://localhost:8090/calcQuinas', data = jsonData)
# r = requests.post('http://localhost:8090/calcQuinasInt', data = jsonData)
r = requests.post('http://0.0.0.0:5000/calcQuinasInt', data = jsonData)
print(r.json())