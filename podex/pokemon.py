from flask import Blueprint, redirect, render_template, url_for
import requests

pokeurl = "https://pokeapi.co/api/v2"
pokebp = Blueprint("pokemon", __name__, url_prefix="/pokemon")

@pokebp.route("/")
def get_first_pokemon():
    pass

@pokebp.route("/<int:id>")
def get_pokemon(id):
    res = requests.get(f"{pokeurl}/pokemon/{id}")
    data = res.json()
    return render_template("pokemon/pokemon.html", len = len(data.get("types")), pokemon=data)