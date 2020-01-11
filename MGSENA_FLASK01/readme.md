# Comandos

``` 
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)

```

```
docker-compose down --rmi all
```

```
docker-compose up --build -d
```

```
docker image ls — list available images
docker container ls — list all containers
docker logs <partial container ID> — tail logs from a container
docker kill <partial container ID> — kill execution of a container
docker restart <partial container ID> — restart container
docker start <partial container ID> — start stopped container
docker stop <partial container ID> — gracefully end container
docker container prune — delete all non-running containers

docker-compose images
docker-compose ps
docker-compose stop
docker-compose up --build
docker-compose up --build -d
docker-compose logs -f nginx

```
```
uwsgi --socket 0.0.0.0:5020 --protocol=http -w wsgi:app
```

NGINX 

 

Comandos de verificação: 

nginx –v 

ps -ef | grep nginx 

curl localhost 

 

Arquivos e Diretórios 

/etc/nginx/: configuração padrõ do root 

/etc/nginx/nginx.conf: contem o entrypointpadrão do nginx. Work processes, tunning, logging, carga de módulos dinamicos,  

/etc/nginx/conf.d/: contém o padrão (default) http server configuration. Os arquivos .conf são incluídos no nginx.conf 

/var/log/nginx/: contém os arquivos de acess.log e erros.log 

 

 

# Comandos nginx: 

nginx –v 

nginx –h 

nginx –V 

nginx –t : testa a configuração 

nginx –T: Testa a configuração e apresenta na tela 

Nginx –s signal 

nginx -s reload 