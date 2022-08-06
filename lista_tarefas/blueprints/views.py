from itertools import count
from typing import Optional
from flask import Blueprint, jsonify, request
from pydantic import BaseModel, Field
from flask_pydantic_spec import Response, Request
from lista_tarefas.extensions.pydantic import spec
from tinydb import TinyDB, Query

api = Blueprint('api', __name__)
database = TinyDB('database.json')
c = count()

class Item(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(c))
    tarefa: str

class Itens(BaseModel):
    itens: list[Item]
    count: int


@api.route('/lista')
@spec.validate(resp=Response(HTTP_200=Itens))
def exibir_lista():
    """Exibe a lista completa junto com um contador de número de itens na lista"""
    return jsonify(
        Itens(
            itens=database.all(),
            count=len(database.all())
        ).dict()
    )

@api.route('/lista', methods=['POST'])
@spec.validate(body=Request(Item), resp=Response(HTTP_201=Item))
def inserir_item_na_lista():
    """Insere um item de tarefa na lista de tarefas."""
    body = request.context.body.dict()
    database.insert(body)
    return body

@api.route('/lista/<int:id>')
@spec.validate(resp=Response(HTTP_200=Item))
def buscar_item_lista(id):
    """Retorna um item da lista de tarefas passando na url seu id"""
    try:
        item = database.search(Query().id == id)[0]
    except IndexError:
        return {'message': 'Item not found'}, 404
    return jsonify(item)

@api.route('/lista/<int:id>', methods=['PUT'])
@spec.validate(body=Request(Item), resp=Response(HTTP_201=Item))
def altera_pessoa(id):
    """Altera os itens da lista baseado no id do item"""
    Item = Query()
    body = request.context.body.dict()
    database.update(body, Item.id == id)
    return jsonify(body)

@api.route('/lista/<int:id>', methods=['DELETE'])
@spec.validate(resp=Response('HTTP_204'))
def deleta_item(id):
    """Deleta um item da lista através do id repassado na URL do recurso"""
    Item = Query()
    database.remove(Item.id == id)
    return jsonify({})   