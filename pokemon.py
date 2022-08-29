import json
import requests

pokemon = input("choose a pokemon: ")
pokemon = pokemon.lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
req = requests.get(url)

if req.status_code == 200:
    data = req.json()
    for ability in data['abilities']:
        print(ability['ability']['name'])
else:
    print("pokemon not found")