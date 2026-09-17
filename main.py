from pokemons.pokemon import Pokemon
from pokemons.abilities import *
from cards import create_pokemon_card
from printable import create_printable_pokemon_pdf


# All starter Pokémon from generations 1 to 5
pokemons = [
    # Generation 1
    Pokemon.from_api(
        pokemon_name="bulbasaur",
        ability=OVERGROW,
    ),
    Pokemon.from_api(
        pokemon_name="charmander",
        ability=BLAZE,
    ),
    Pokemon.from_api(
        pokemon_name="squirtle",
        ability=TORRENT,
    ),

    # Generation 2
    Pokemon.from_api(
        pokemon_name="chikorita",
        ability=OVERGROW,
    ),
    Pokemon.from_api(
        pokemon_name="cyndaquil",
        ability=BLAZE,
    ),
    Pokemon.from_api(
        pokemon_name="totodile",
        ability=TORRENT,
    ),

    # Generation 3
    Pokemon.from_api(
        pokemon_name="treecko",
        ability=OVERGROW,
    ),
    Pokemon.from_api(
        pokemon_name="torchic",
        ability=BLAZE,
    ),
    Pokemon.from_api(
        pokemon_name="mudkip",
        ability=TORRENT,
    ),

    # Generation 4
    Pokemon.from_api(
        pokemon_name="turtwig",
        ability=OVERGROW,
    ),
    Pokemon.from_api(
        pokemon_name="chimchar",
        ability=BLAZE,
    ),
    Pokemon.from_api(
        pokemon_name="piplup",
        ability=TORRENT,
    ),

    # Generation 5
    Pokemon.from_api(
        pokemon_name="snivy",
        ability=OVERGROW,
    ),
    Pokemon.from_api(
        pokemon_name="tepig",
        ability=BLAZE,
    ),
    Pokemon.from_api(
        pokemon_name="oshawott",
        ability=TORRENT,
    ),
]


# Generate the individual card images in memory
pokemon_cards = [
    create_pokemon_card(pokemon)
    for pokemon in pokemons
]


# Generate a multi-page printable A4 PDF
create_printable_pokemon_pdf(
    cards=pokemon_cards,
    output_path="starter_pokemon_gen_1_to_5_v4.pdf",
)