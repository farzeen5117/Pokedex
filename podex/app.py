from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)
from pokemon import pokebp
app.register_blueprint(pokebp)

@app.route("/")
def index():
    return redirect(url_for("pokemon.get_pokemon", id=1))

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404-not-found.html"), 404