import requests
import json
import progressbar
import multiprocessing

from multiprocessing.dummy import Pool

pool = Pool(16)
futures = []

dezenas = [1,2,3,4,5,6]
id_aposta = 1
dados = []
data = {'id_aposta': id_aposta, 'dezenas': dezenas}

dados.append(data)

jsonData = json.dumps(dados)

QtdePalpites = 10

def multiReqs():
    print("Inicio")
    bar = progressbar.ProgressBar(maxval=QtdePalpites, \
    widgets=[progressbar.Bar('=', '[', ']'), 'Processando ... ', progressbar.Percentage()])    
    bar.start()

    bar1 = progressbar.ProgressBar(maxval=QtdePalpites, \
    widgets=[progressbar.Bar('*', '[', ']'), 'Requests ... ', progressbar.Percentage()])    
    bar1.start()

    # r = requests.post('http://localhost:8090/calcQuinas', data = jsonData)
    # r = requests.post('http://localhost/calcQuinasInt', data = jsonData)
    for i in range(QtdePalpites):
        # r = requests.post('http://0.0.0.0:8090/calcQuinasInt', data = jsonData)
        # r = requests.get('http://0.0.0.0:8090')
        # futures.append(pool.apply_async(requests.post,['http://localhost/calcQuinasInt'],{'data': jsonData} ))
        futures.append(pool.apply_async(requests.get,['http://localhost:8090']))
        bar.update(i)
        # print(r.json())
    bar.finish()

    i = 0
    for future in futures:
        i += 1
        bar1.update(i)
        # r = future.get().json()
        r = future.get()
    bar1.finish()
    print("fim")

def simpleReqs():
    print("Inicio")
    bar = progressbar.ProgressBar(maxval=QtdePalpites, \
    widgets=[progressbar.Bar('=', '[', ']'), 'Processando ... ', progressbar.Percentage()])    
    bar.start()

    # r = requests.post('http://localhost:8090/calcQuinas', data = jsonData)
    # r = requests.post('http://localhost/calcQuinasInt', data = jsonData)
    for i in range(QtdePalpites):
        # r = requests.post('http://0.0.0.0:8090/calcQuinasInt', data = jsonData)
        r = requests.get('http://localhost:8090')
        bar.update(i)
        # print(r.json())
    bar.finish()
    print("fim")

if __name__ == '__main__':
    multiReqs()
    # simpleReqs()