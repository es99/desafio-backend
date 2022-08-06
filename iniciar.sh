#!/bin/sh
echo setando variavel de ambiente FLASK_APP
sleep 2
export FLASK_APP=flasky.py
echo setando variavel de ambiente FLASK_ENV para ambiente de desenvolvimento
sleep 2
export FLASK_DEBUG=1
echo DONE!
sleep 2
echo Iniciando a aplicacao na porta 5000
sleep 2
flask run

