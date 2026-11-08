from pokemons.pokemon import Pokemon
from pokemons.abilities import *
from pokemons.moves import *

from cards import create_pokemon_card, create_move_card, create_pokemon_token
from printable import (
    create_printable_pokemon_pdf,
    create_printable_moves_pdf,
    create_printable_tokens_pdf
)


# ============================================================
# POKEMON
# ============================================================

pokemons = [

    # --------------------------------------------------------
    # PLAYER POKEMON
    # --------------------------------------------------------

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

    Pokemon.from_api(
        pokemon_name="pikachu",
        ability=STATIC,
    ),

    Pokemon.from_api(
        pokemon_name="chikorita",
        ability=OVERGROW,
    ),

    Pokemon.from_api(
        pokemon_name="totodile",
        ability=TORRENT,
    ),

    Pokemon.from_api(
        pokemon_name="cyndaquil",
        ability=BLAZE,
    ),

    Pokemon.from_api(
        pokemon_name="mudkip",
        ability=TORRENT,
    ),

    Pokemon.from_api(
        pokemon_name="torchic",
        ability=BLAZE,
    ),

    Pokemon.from_api(
        pokemon_name="treecko",
        ability=OVERGROW,
    ),


    # --------------------------------------------------------
    # NPC POKEMON
    # --------------------------------------------------------

    Pokemon.from_api(
        pokemon_name="rattata",
        ability=GUTS,
    ),

    Pokemon.from_api(
        pokemon_name="poochyena",
        ability=INTIMIDATE,
    ),

    Pokemon.from_api(
        pokemon_name="heracross",
        ability=GUTS,
    ),

    Pokemon.from_api(
        pokemon_name="pidgey",
        ability=KEEN_EYE,
    ),

    Pokemon.from_api(
        pokemon_name="wingull",
        ability=KEEN_EYE,
    ),

    Pokemon.from_api(
        pokemon_name="beedrill",
        ability=SWARM,
    ),

    Pokemon.from_api(
        pokemon_name="vespiquen",
        ability=SWARM,
    ),

    Pokemon.from_api(
        pokemon_name="combee",
        ability=SWARM,
    ),

    Pokemon.from_api(
        pokemon_name="oddish",
        ability=CHLOROPHYLL,
    ),

    Pokemon.from_api(
        pokemon_name="paras",
        ability=EFFECT_SPORE,
    ),

    Pokemon.from_api(
        pokemon_name="araquanid",
        ability=WATER_ABSORB,
    ),

    Pokemon.from_api(
        pokemon_name="bidoof",
        ability=SIMPLE,
    ),

    Pokemon.from_api(
        pokemon_name="scyther",
        ability=SWARM,
    ),

    Pokemon.from_api(
        pokemon_name="aron",
        ability=STURDY,
    ),

    Pokemon.from_api(
        pokemon_name="geodude",
        ability=STURDY,
    ),
]


# ============================================================
# CREATE POKEMON CARDS
# ============================================================

pokemon_cards = [
    create_pokemon_card(pokemon)
    for pokemon in pokemons
]


# ============================================================
# CREATE POKEMON PDF and TOKENS
# ============================================================

create_printable_pokemon_pdf(
    cards=pokemon_cards,
    output_path="one_shot_pokemon.pdf",
    back=True,
)

tokens = [
    create_pokemon_token(pokemon)
    for pokemon in pokemons]

create_printable_tokens_pdf(
    cards=tokens,
    output_path="one_shot_tokens.pdf",
)



# # ============================================================
# # MOVE CARDS
# #
# # IMPORTANT:
# # This is intentionally NOT a set.
# #
# # Every occurrence represents one physical card to print.
# # ============================================================

# moves = [

#     # ========================================================
#     # PLAYER POKEMON
#     # ========================================================

#     # --------------------------------------------------------
#     # Bulbasaur
#     # --------------------------------------------------------
#     TACKLE,
#     VINE_WHIP,
#     LEECH_SEED,
#     PROTECT,
#     POISON_POWDER,
#     RAZOR_LEAF,

#     # --------------------------------------------------------
#     # Charmander
#     # --------------------------------------------------------
#     SCRATCH,
#     EMBER,
#     GROWL,
#     PROTECT,
#     BITE,
#     FIRE_FANG,

#     # --------------------------------------------------------
#     # Squirtle
#     # --------------------------------------------------------
#     TACKLE,
#     WATER_GUN,
#     WITHDRAW,
#     PROTECT,
#     BUBBLE,
#     BITE,

#     # --------------------------------------------------------
#     # Pikachu
#     # --------------------------------------------------------
#     QUICK_ATTACK,
#     THUNDER_SCHOCK,
#     GROWL,
#     PROTECT,
#     THUNDER_WAVE,
#     SPARK,

#     # --------------------------------------------------------
#     # Chikorita
#     # --------------------------------------------------------
#     TACKLE,
#     RAZOR_LEAF,
#     GROWL,
#     PROTECT,
#     POISON_POWDER,
#     LEECH_SEED,

#     # --------------------------------------------------------
#     # Totodile
#     #
#     # Leer -> Growl
#     # --------------------------------------------------------
#     SCRATCH,
#     WATER_GUN,
#     GROWL,
#     PROTECT,
#     BITE,
#     AQUA_JET,

#     # --------------------------------------------------------
#     # Cyndaquil
#     # --------------------------------------------------------
#     TACKLE,
#     EMBER,
#     SMOKESCREEN,
#     PROTECT,
#     QUICK_ATTACK,
#     FIRE_FANG,

#     # --------------------------------------------------------
#     # Mudkip
#     # --------------------------------------------------------
#     TACKLE,
#     WATER_GUN,
#     GROWL,
#     PROTECT,
#     MUD_SLAP,
#     WATER_PULSE,

#     # --------------------------------------------------------
#     # Torchic
#     # --------------------------------------------------------
#     SCRATCH,
#     EMBER,
#     GROWL,
#     PROTECT,
#     QUICK_ATTACK,
#     FIRE_PUNCH,

#     # --------------------------------------------------------
#     # Treecko
#     #
#     # Pound -> Tackle
#     # Leer  -> Growl
#     # --------------------------------------------------------
#     TACKLE,
#     ABSORB,
#     GROWL,
#     PROTECT,
#     QUICK_ATTACK,
#     MEGA_DRAIN,


#     # ========================================================
#     # NPC POKEMON
#     # ========================================================

#     # --------------------------------------------------------
#     # Rattata
#     #
#     # Focus Energy -> Swords Dance
#     # --------------------------------------------------------
#     TACKLE,
#     BITE,
#     QUICK_ATTACK,
#     SWORDS_DANCE,

#     # --------------------------------------------------------
#     # Poochyena
#     # --------------------------------------------------------
#     TACKLE,
#     BITE,
#     HOWL,
#     SAND_ATTACK,

#     # --------------------------------------------------------
#     # Heracross
#     # --------------------------------------------------------
#     TACKLE,
#     HORN_ATTACK,
#     AERIAL_ACE,
#     BRICK_BREAK,

#     # --------------------------------------------------------
#     # Pidgey
#     # --------------------------------------------------------
#     TACKLE,
#     GUST,
#     QUICK_ATTACK,
#     SAND_ATTACK,

#     # --------------------------------------------------------
#     # Wingull
#     # --------------------------------------------------------
#     WATER_GUN,
#     WING_ATTACK,
#     GROWL,
#     SUPERSONIC,

#     # --------------------------------------------------------
#     # Beedrill
#     #
#     # Fury Attack  -> Twineedle
#     # Poison Sting -> Acid
#     # --------------------------------------------------------
#     TWINEEDLE,
#     TWINEEDLE,
#     ACID,
#     STRING_SHOT,

#     # --------------------------------------------------------
#     # Vespiquen
#     # --------------------------------------------------------
#     SLASH,
#     GUST,
#     DEFEND_ORDER,
#     ATTACK_ORDER,

#     # --------------------------------------------------------
#     # Combee
#     # --------------------------------------------------------
#     SWEET_SCENT,
#     GUST,
#     BUG_BITE,
#     STRUGGLE_BUG,

#     # --------------------------------------------------------
#     # Oddish
#     # --------------------------------------------------------
#     ABSORB,
#     POISON_POWDER,
#     ACID,
#     SWEET_SCENT,

#     # --------------------------------------------------------
#     # Paras
#     # --------------------------------------------------------
#     SCRATCH,
#     POISON_POWDER,
#     STUN_SPORE,
#     LEECH_LIFE,

#     # --------------------------------------------------------
#     # Araquanid
#     # --------------------------------------------------------
#     BUBBLE,
#     BUG_BITE,
#     BITE,
#     SPIDER_WEB,

#     # --------------------------------------------------------
#     # Bidoof
#     #
#     # Headbutt -> Tackle
#     # --------------------------------------------------------
#     TACKLE,
#     GROWL,
#     TACKLE,
#     ROLLOUT,

#     # --------------------------------------------------------
#     # Scyther
#     # --------------------------------------------------------
#     QUICK_ATTACK,
#     SLASH,
#     WING_ATTACK,
#     SWORDS_DANCE,

#     # --------------------------------------------------------
#     # Aron
#     #
#     # Headbutt -> Tackle
#     # --------------------------------------------------------
#     TACKLE,
#     HARDEN,
#     METAL_CLAW,
#     TACKLE,

#     # --------------------------------------------------------
#     # Geodude
#     # --------------------------------------------------------
#     TACKLE,
#     DEFENSE_CURL,
#     ROCK_THROW,
#     MUD_SLAP,

#     ## EXTRA
#     TOXIC,
# ]


# # ============================================================
# # CREATE MOVE CARDS
# # ============================================================

# move_cards = [
#     create_move_card(move)
#     for move in moves
# ]


# # ============================================================
# # CREATE MOVE PDF
# # ============================================================

# create_printable_moves_pdf(
#     cards=move_cards,
#     output_path="one_shot_moves.pdf",
# )