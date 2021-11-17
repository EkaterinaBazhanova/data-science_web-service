#установка необходимых библиотек в jupyter
FROM jupyter/scipy-notebook:33add21fab64

RUN pip install numpy matplotlib seaborn pandas scipy sklearn pickle


#установка питона в докер
FROM python:latest

COPY . /root

WORKDIR /root

RUN pip install flask gunicorn numpy pandas scipy sklearn flask_wtf