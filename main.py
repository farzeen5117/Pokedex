import requests
import json

api_url = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(api_url)
print(response.json())