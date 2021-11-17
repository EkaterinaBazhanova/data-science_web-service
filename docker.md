#Загрузка папки в докер

#1.создание/запуск контейнера c jypiter
docker run -p 8888:8888 jupyter/scipy-notebook:33add21fab64

#2.открытие контейнера (по ссылке)

#3.просмотр контейнеров
docker ps

#4.заходим в контейнер 92f4fb353b5f
docker exec -it 92f4fb353b5f bash
#заглушить контейнер 
Ctrl + C

#5.копируем датасет Mall_Customers.csv в контейнер 92f4fb353b5f (запускать на своей локальной машине)
#датасет сохранить в папку с контейнером
docker cp Mall_Customers.csv 92f4fb353b5f:/home/jovyan/Mall_Customers.csv

#6.запуск моего контейра (создание volume -- подключение папки к контейнеру)
#jupyter notebook
#Сначала все-все останови, потом запускай
docker run -v C:\Users\BazhanovaEN\Desktop\docker:/home/jovyan -p 8888:8888 jupyter/scipy-notebook:33add21fab64 
jupyter notebook

#установка из Dockerfile
docker build .
#writing image sha256:7be5de2183aced0261addb257b673f6a837392693
docker run -v C:\Users\BazhanovaEN\Desktop\docker:/home/jovyan -p 8888:8888 jupyter/scipy-notebook:33add21fab64

#flask

#1. Запуск докер-compose
docker compose up --build 
#открыть как http://127.0.0.1:5000/

#2. Зайти в контейнер с flask
docker exec -it docker-flask-1 bash

#Загрузка на гит
#1. Команды в терминале
git init
git add .
git commit -m 'initial commit'

#2.Переходим на github:
#2.1.создаем новый репозиторий (имя из readme, public, не ставить галочку на Readme)
#2.2. копируем в терминал по очереди команды из...push an existing repository from the command line
#2.3. проверяем, что все загрузилось