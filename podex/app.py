from flask import Flask
app = Flask(__name__)
import pokemon
app.register_blueprint(pokemon.bp)