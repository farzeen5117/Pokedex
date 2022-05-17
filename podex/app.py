from flask import Flask
app = Flask(__name__)
from pokemon import pokebp
app.register_blueprint(pokebp)