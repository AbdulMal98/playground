import requests

pokeinfo = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

pokeinfo.text
pokeinfo.json()
