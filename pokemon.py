import json
import requests

pokemon = input("choose a pokemon: ")
pokemon = pokemon.lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
req = requests.get(url)

data = req.json()
print(f"weight is : {data['weight']}")
print("abilities: ")

for ability in data['abilities']:
    print(ability['ability']['name'])
