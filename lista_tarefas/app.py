from flask import Flask
from lista_tarefas import blueprints

def create_app():
    app = Flask(__name__)

    blueprints.init_app(app)

    return app