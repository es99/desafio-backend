import json
from flask import Blueprint, jsonify, request
from pydantic import BaseModel
from flask_pydantic_spec import Response, Request
from lista_tarefas.extensions.pydantic import spec
from tinydb import TinyDB, Query

api = Blueprint('api', __name__)
database = TinyDB('database.json')

class Lista(BaseModel):
    id: int
    tarefa: str

@api.route('/')
def index():
    return '<h1>Teste</h1>'

@api.route('/lista')
#@spec.validate(resp=Response(HTTP_200=Lista))
def exibir_lista():
    """Exibe a lista completa"""
    return jsonify(database.all())


@api.route('/lista', methods=['POST'])
@spec.validate(body=Request(Lista), resp=Response(HTTP_200=Lista))
def inserir_item_na_lista():
    """Insere um item de tarefa na lista de tarefas."""
    body = request.context.body.dict()
    database.insert(body)
    return body

@api.route('/lista/<int:id>')
def retorna_item_da_lista(id):
    return jsonify(lista[id])