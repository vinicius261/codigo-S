
from flask import Flask
from src.routes.cadastros import cadastros
from src.routes.holetrite import holerite

app = Flask(__name__)
app.register_blueprint(cadastros)
app.register_blueprint(holerite)