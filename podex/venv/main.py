from flask import Flask
import requests
import pprint as pp

# name, base exp, abilities (??), official-artwork(front-default) (??)

pokeurl = "https://pokeapi.co/api/v2/pokemon/"
params = {'limit': 100}

def get_pokemon():
    res = requests.get(pokeurl)
    return res

#def get_pokemon_dict(url):
#    res = requests.get(url)
#    print(pp.pprint((res.json())))

def get_pokemon_name():
    for offset in range(0, 1000, 100):
        params['offset'] = offset
        response = requests.get(pokeurl, params=params)
        if response:  
            poke_dict = response.json()
            for item in poke_dict['results']:
                spec_poke_url = f"https://pokeapi.co/api/v2/pokemon/{item['name']}/"
                spec_poke_res = requests.get(spec_poke_url)
                if spec_poke_res:
                    spec_poke_dict = spec_poke_res.json()
                else:
                    print("Error in retrieveing specific pokemon")
                print(f"{spec_poke_dict['id']}: {item['name']}, {item['url']}, height: {spec_poke_dict['height']}, weight: {spec_poke_dict['weight']}, base exp: {spec_poke_dict['base_experience']}")
        else:
            print("Error in get_pokemon()")

if __name__ == "__main__":
    get_pokemon_name()