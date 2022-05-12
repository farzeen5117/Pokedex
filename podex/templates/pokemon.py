from flask import Blueprint, redirect, render_template, url_for
import requests

pokeurl = "https://pokeapi.co/api/v2"
bp = Blueprint("pokemon", __name__, url_prefix="/pokemon")

@bp.route("/")
def get_first_pokemon():
    pass

@bp.route("/<int:id>")
def get_pokemon(id):
    res = requests.get(f"{pokeurl}/pokemon/{id}")
    data = res.json()
    return render_template("pokemon/pokemon.html", pokemon=data)