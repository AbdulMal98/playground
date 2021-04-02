from json import JSONDecodeError

import requests
from databind.core import datamodel
from databind.json import from_json


def prompt_user():
    name = input('Type a name you want to find info: ').lower()
    try:
        pokeinfo = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        return from_json(Pokemon, pokeinfo.json())
    except JSONDecodeError:
        print("Sorry, I didn't understand that. Try again.")


@datamodel
class Pokemon:
    name: str
    base_experience: int
    height: int
    id: int
    weight: int


def displayinfo(infoforpoke):
    print(infoforpoke)
