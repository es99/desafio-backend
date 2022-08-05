import json
from flask import Blueprint, jsonify, request, url_for

api = Blueprint('api', __name__)

lst = [
    {'id': 0, 'tarefa': "Lavar os pratos"},
    {'id': 1, 'tarefa': "Arrumar o quarto"},
    {'id': 2, 'tarefa': "cozinhar"}
]


@api.route('/lista/')
def lista():
    return jsonify(lst)

@api.route('/lista/<int:id>')
def get_lista(id):
    return jsonify(lst[id])

@api.route('/lista/', methods=['POST'])
def update_list():
    record = json.loads(request.data)
    lst.append(dict(id=len(lst), tarefa=record))
    return jsonify(json.dumps(record)), 201