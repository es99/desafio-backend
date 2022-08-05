from flask_pydantic_spec import FlaskPydanticSpec

spec = FlaskPydanticSpec('flask', title='desafio-lista')
def init_app(app):
    spec.register(app)
