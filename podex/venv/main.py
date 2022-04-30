from flask import Flask
import requests
import pprint as pp

# name, base exp, abilities (??), base_stat, sprites, official-artwork(front-default) (??)

pokeurl = "https://pokeapi.co/api/v2/pokemon/"
params = {'limit': 100}

def get_pokemon():
    res = requests.get(pokeurl)
    return res

def get_pokemon_dict(url):
    res = requests.get(url)
    print(pp.pprint((res.json())))

def filter_poke_data():
    for offset in range(0, 1000, 100):
        params['offset'] = offset
        response = requests.get(pokeurl, params=params)
        if response.status_code != 200: 
            print(response.text)
        else:
            data = response.json()
            pp.pprint(data)
            for item in data['results']:
                print(item['name'])

if __name__ == "__main__":
    res = get_pokemon()
    if res:
        print(res.json())
        print("\nsuccessful\n")
    else:
        print("something went wrong :(")
    result = res.json()
    for pokemon in result["results"]:
        get_pokemon_dict(pokemon["url"])
    filter_poke_data()