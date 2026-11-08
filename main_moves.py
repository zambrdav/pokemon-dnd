from pokemons.moves import ALL_MOVES
from cards import create_move_card
from printable import create_printable_moves_pdf


move_cards = [
    create_move_card(move)
    for move in ALL_MOVES
]


create_printable_moves_pdf(
    cards=move_cards,
    output_path="pokemon_moves.pdf",
)



