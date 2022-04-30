from flask import Flask
import requests
import json

# name, base exp, abilities (??), base_stat, sprites, official-artwork(front-default) 

def get_pokemon():
    req = requests.get("https://pokeapi.co/api/v2/pokemon/")
    return req

def get_pokemon_dict(url):
    req = requests.get(url)
    print(json.dumps(req.json(), indent=2))
    

if __name__ == "__main__":
    req = get_pokemon()
    print(req.json())
    result = req.json()
    for pokemon in result["results"]:
        get_pokemon_dict(pokemon["url"])