from flask import Flask
import requests
import pprint as pp

# name, base exp, abilities (??), official-artwork(front-default) (??)

pokeurl = "https://pokeapi.co/api/v2/pokemon/"
params = {'limit': 1000}

class Pokedex:
    # name => pokemon name
    # id => pokemon id
    # output => error code definition for Pokedex
    # output = 1    (No URL response)
    # output = 2    (Name and ID not matching)
    # output = 3    ()
    def __init__(self, name = None, id = None, output = None):
        if name != None and id != None:
            self.name = name
            self.url = pokeurl + str(self.name)
            res = requests.get(self.url, params=params)
            if res:
                if id == requests.get(self.url, params=params).json()["id"]:
                    self.id = id
                else:
                    print("provided id does not match pokemon :(")
            else:
                self.output = 1
                print("response failed :(")
        elif name != None and id == None:
            self.name = name
            self.url = pokeurl + str(self.name)
            res = requests.get(self.url, params=params)
            if res:
                self.id == requests.get(self.url, params=params).json()["id"]
            else:
                self.output = 1
                print("response failed :(")
        elif name == None and id != None:
            self.id = id
            self.url = pokeurl + str(id)
            self.name = requests.get(self.url).json()["name"]
        elif name == None and id == None:
            print("no name or id provided")
        elif name == None and id == 0:
            print("no such pokemon exists with id 000")

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

def output_1():
    poke = Pokedex("jsdkjcfhsdklvc")
    if poke.output == 1:
        return "pass"
    else:
        return "fail"

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
    print(output_1())