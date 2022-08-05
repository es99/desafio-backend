from flask import Flask
from lista_tarefas import blueprints
from lista_tarefas.extensions import pydantic

def create_app():
    app = Flask(__name__)

    blueprints.init_app(app)
    pydantic.init_app(app)

    return app