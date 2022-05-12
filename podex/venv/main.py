from flask import Flask
import requests
import pprint as pp

# name, base exp, abilities (??), official-artwork(front-default) (??)

# def get_pokemon_name():
#     for offset in range(0, 1000, 100):
#         params['offset'] = offset
#         response = requests.get(pokeurl, params=params)
#         if response:  
#             poke_dict = response.json()
#             for item in poke_dict['results']:
#                 spec_poke_url = f"https://pokeapi.co/api/v2/pokemon/{item['name']}/"
#                 spec_poke_res = requests.get(spec_poke_url)
#                 if spec_poke_res:
#                     spec_poke_dict = spec_poke_res.json()
#                 else:
#                     print("Error in retrieveing specific pokemon")
#                 print(f"{spec_poke_dict['id']}: {item['name']}, {item['url']}, height: {spec_poke_dict['height']}, weight: {spec_poke_dict['weight']}, base exp: {spec_poke_dict['base_experience']}")
#         else:
#             print("Error in get_pokemon()")

pokeurl = "https://pokeapi.co/api/v2/pokemon/"
params = {'limit': 1000}

class Pokedex:
    # name => pokemon name
    # id => pokemon id
    # error => error code definition for Pokedex
    # error = 1    (No URL response)
    # error = 2    (Name and ID not matching)
    # error = 3    (No Name or ID provided)
    def __init__(self, name = None, id = None, error = None):
        self.name = name
        self.id = id
        self.error = error
        if name != None and id != None:
            self.url = pokeurl + str(self.name)
            res = requests.get(self.url, params=params)
            if res:
                if id == requests.get(self.url, params=params).json()["id"]:
                    self.id = id
                else:
                    self.error = 2
                    # print("provided id does not match pokemon :(")
            else:
                self.error = 1
                # print("response failed :(")
        elif name != None and id == None:
            self.url = pokeurl + str(self.name)
            res = requests.get(self.url, params=params)
            if res:
                self.id == requests.get(self.url, params=params).json()["id"]
            else:
                self.error = 1
                # print("response failed :(")
        elif name == None and id != None:
            self.url = pokeurl + str(id)
            res = requests.get(self.url, params=params)
            if res:
                self.name == requests.get(self.url, params=params).json()["name"]
            else:
                self.error = 1
                # print("response failed :(")
        elif name == None and id == None:
            self.error = 3
            # print("no name or id provided")
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

def test_name():
    poke = Pokedex("jlkjkljljlkjlj")
    if poke.error == 1:
        return "pass"
    else:
        return "fail"

def test_name_number():
    poke = Pokedex("bulbasaur", 25)
    if poke.error == 2:
        return "pass"
    else:
        return "fail"

def test_no_args():
    poke = Pokedex()
    if poke.error == 3:
        return "pass"
    else:
        return "fail"

def test_number():
    poke = Pokedex(id=394309809838508934095840)
    if poke.error == 1:
        return "pass"
    else:
        return "fail"

if __name__ == "__main__":
    print(test_name())
    print(test_name_number())
    print(test_no_args())
    print(test_number())