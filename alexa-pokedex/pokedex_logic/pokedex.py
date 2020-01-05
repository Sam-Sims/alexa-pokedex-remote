import requests
from random import randint

base_url = 'https://pokeapi.co/api/v2/'

# PokeAPI makes a distinction between species and pokemon - need to fetch both for full range of data; see API for more details

def get_species():
    # Pick a random number between 1 and 807 - the national dex range
    id = str(randint(1, 807))
    r = requests.get(base_url + 'pokemon-species/' + id)
    return r.json()


def get_pokemon_data(pokemon_species):
    # Some species have different forms i.e Wormadam, each pokemon has a default variety that can be used.
    # Wormadam has 3 forms each with their own ID so to simplify things we fetch what the API designates as the default form (in wormadams case: plant form)
    default_variety = next((v for v in pokemon_species['varieties'] if v['is_default'] is True), None)
    if default_variety is not None:
        r = requests.get(default_variety['pokemon']['url'])
        return r.json()
    return None

def generate_alexa_text_string(pokemon_species, pokemon):
    text = pokemon_species['name']
    return text

