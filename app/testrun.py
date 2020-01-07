import requests
import json

dezenas = [1,2,3,4,5,6]
listaQuinas = ([1,2,3,4,8],[4,5,6,7,8])
id_aposta = 1

data = {'id_aposta': id_aposta, 'dezenas': dezenas, 'listaQuinas':listaQuinas}

print('Total de quinas: {}'.format(len(listaQuinas)))
# quina = [1,2,3,7,8]
jsonData = json.dumps(data)

r = requests.post('http://localhost/calcQuinas', data = jsonData)
print(r.json())