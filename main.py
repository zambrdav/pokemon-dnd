from pokemons.pokemon import Pokemon, PokemonType
from pokemons.abilities import *
from pokemons.moves import ALL_MOVES, EMBER
from cards import get_pokemon_image, create_pokemon_card, create_move_card



pikachu_ability = STATIC

pokemon_name = "Pikachu"

pokemon = Pokemon.from_api(pokemon_name, ability=pikachu_ability)
card_image = create_pokemon_card(pokemon, shiny=True)
card_image.save(f"cards/pokemons/{pokemon_name}_card.png")



# Generate the cards for all moves in ALL_MOVES
for move in ALL_MOVES:
    move_card = create_move_card(move, output_path=f"cards/moves/{move.name}_card.png")









