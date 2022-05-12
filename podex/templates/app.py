from flask import Flask
app = Flask(__name__)
from . import pokemon
app.register_blueprint(pokemon.bp)