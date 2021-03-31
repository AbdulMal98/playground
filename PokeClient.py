import requests

pokeinfo = requests.get('https://pokeapi.co/api/v2/pokemon')

pokeinfo.text
pokeinfo.json()
