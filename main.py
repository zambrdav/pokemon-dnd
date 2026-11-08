from pokemons.pokemon import Pokemon
from pokemons.abilities import *
from cards import create_pokemon_card
from printable import create_printable_pokemon_pdf


# create a gyarados
gyarados = Pokemon.from_api(pokemon_name="gyarados", ability=INTIMIDATE)

# Create the card for gyarados
gyarados_card = create_pokemon_card(gyarados, output_path="gyarados_card_new.png", shiny=True)


