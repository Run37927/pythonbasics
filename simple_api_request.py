import requests

req = requests.get("https://swapi.dev/api/people/2/")
person = req.json()
print(f"name is {person['name']}")
print(f"birth year is {person['birth_year']}")