import requests
import random
from random import randint


base_url = 'https://pokeapi.co/api/v2/'

# PokeAPI makes a distinction between species and pokemon - need to fetch both for full range of data; see API for more details

def get_species():
    # Pick a random number between 1 and 807 - the national dex range
    id = str(randint(1, 807))
    r = requests.get(base_url + 'pokemon-species/' + id)
    print(base_url + 'pokemon-species/' + id)
    return r.json()


def get_pokemon_data(pokemon_species):
    # Some species have different forms i.e Wormadam, each pokemon has a default variety that can be used.
    # Wormadam has 3 forms each with their own ID so to simplify things we fetch what the API designates as the default form (in wormadams case: plant form)
    default_variety = next((v for v in pokemon_species['varieties'] if v['is_default'] is True), None)
    if default_variety is not None:
        r = requests.get(default_variety['pokemon']['url'])
        print(default_variety['pokemon']['url'])
        return r.json()
    return None


def generate_alexa_text_string(pokemon_species, pokemon):
    # Extracts english version of flavour text and compiles them into a list
    flavor_texts = list((x for x in pokemon_species['flavor_text_entries'] if x['language']['name'] == 'en'))
    flavor_text_unformatted = random.choice(flavor_texts)['flavor_text']
    # Flavor text contains /n that needs to be removed
    flavor_text = flavor_text_unformatted.replace('\n', ' ')

    # Extracts english genus
    genus = (next(x for x in pokemon_species['genera'] if x['language']['name'] == 'en'))['genus']

    colour = pokemon_species['color']['name']
    name = pokemon_species['name']

    # TODO - types string needs formatting
    types = ''
    for i in pokemon['types']:
        types = types + i['type']['name']
        types = types + ", "

    text = f"Your pokemon is {name}, the {genus}. Its colour is {colour} and is a {types} type pokemon. {flavor_text}"
    return text


# For local testing
pokemon_species = get_species()
pokemon_data = get_pokemon_data(pokemon_species)
print(generate_alexa_text_string(pokemon_species, pokemon_data))

