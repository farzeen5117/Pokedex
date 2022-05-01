from flask import Flask
import requests
import pprint as pp

# name, base exp, abilities (??), sprites, official-artwork(front-default) (??)

pokeurl = "https://pokeapi.co/api/v2/pokemon/"
#params = {'limit': 100}

def get_pokemon():
    res = requests.get(pokeurl)
    return res

#def get_pokemon_dict(url):
#    res = requests.get(url)
#    print(pp.pprint((res.json())))

def get_pokemon_name():
    response = get_pokemon()
    if response: 
        poke_dict = response.json()
        for item in poke_dict['results']:
            spec_poke_url = f"https://pokeapi.co/api/v2/pokemon/{item['name']}/"
            spec_poke_res = requests.get(spec_poke_url)
            spec_poke_dict = spec_poke_res.json()
            print(f"{item['name']}: {item['url']}")
    else:
        print("Error")

if __name__ == "__main__":
    #res = get_pokemon()
    #if res:
    #    print(res.json())
    #    print("\nsuccessful\n")
    #else:
    #    print("something went wrong :(")
    #result = res.json()
    #for pokemon in result["results"]:
    #    get_pokemon_dict(pokemon["url"])
    get_pokemon_name()