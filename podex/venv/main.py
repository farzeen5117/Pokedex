from flask import Flask
import requests
import pprint as pp

# name, base exp, abilities (??), official-artwork(front-default) (??)

pokeurl = "https://pokeapi.co/api/v2/pokemon/"
params = {'limit': 100}

class Pokedex:
    def __init__(self, name = None, id = None):
        if name != None and id != None:
            self.name = name
            self.url = pokeurl + str(self.name)
            if id == requests.get(self.url).json()["id"]:
                self.id = id
            else:
                raise ValueError("provided id does not match pokemon")
        elif name != None and id == None:
            self.name = name
            self.url = pokeurl + str(self.name)
            self.id = requests.get(self.url).json()["id"]
        elif name == None and id != None:
            self.id = id
            self.url = pokeurl + str(id)
            self.name = requests.get(self.url).json()["name"]
        elif name == None and id == None:
            raise TypeError("no name or id provided")
        elif name == None and id == 0:
            raise ValueError("no such pokemon exists with id 000")

    def get_species(self):
        return requests.get("https://pokeapi.co/api/v2/pokemon-species/" + str(self.name)).json()["name"]

    def get_height(self):
        return requests.get(self.url).json()["height"]

    def get_weight(self):
        return requests.get(self.url).json()["weight"]

    def get_base_exp(self):
        return requests.get(self.url).json()["base_experience"]

    def get_sprites(self):
        return requests.get(self.url).json()["sprites"]

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