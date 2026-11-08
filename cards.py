from io import BytesIO
import requests
from PIL import Image, ImageDraw, ImageFont
from pokemons.pokemon import Pokemon
from pokemons.abilities import Ability
from pokemons.moves import Move
import os
import textwrap

CARD_WIDTH = 750
CARD_HEIGHT = 1050

TYPE_COLORS = {
    "Normal": "#A8A878",
    "Fire": "#F08030",
    "Water": "#6890F0",
    "Grass": "#78C850",
    "Electric": "#F8D030",
    "Ice": "#98D8D8",
    "Dark": "#705848",
    "Steel": "#B8B8D0",
    "Poison": "#A040A0",
    "Flying": "#A890F0",
    "Psychic": "#F85888",
}

def get_pokemon_image(
    pokemon_name: str,
    shiny: bool = False,
) -> Image.Image:
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    )
    response.raise_for_status()

    data = response.json()

    artwork = data["sprites"]["other"]["official-artwork"]

    image_url = (
        artwork["front_shiny"]
        if shiny
        else artwork["front_default"]
    )

    if image_url is None:
        variant = "shiny" if shiny else "normal"
        raise ValueError(
            f"No {variant} official artwork found for {pokemon_name}."
        )

    image_response = requests.get(image_url)
    image_response.raise_for_status()

    return Image.open(
        BytesIO(image_response.content)
    ).convert("RGBA")


def draw_wrapped_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    position: tuple[int, int],
    font: ImageFont.ImageFont,
    max_width: int,
    line_spacing: int = 5,
) -> int | float:
    x, y = position

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()

        bbox = draw.textbbox(
            (0, 0),
            test_line,
            font=font,
        )
        width = bbox[2] - bbox[0]

        if width <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    for line in lines:
        draw.text(
            (x, y),
            line,
            font=font,
            fill="black",
        )

        bbox = draw.textbbox(
            (0, 0),
            line,
            font=font,
        )
        line_height = bbox[3] - bbox[1]
        y += line_height + line_spacing

    return y




def draw_friendship_bar(
    draw: ImageDraw.ImageDraw,
    position: tuple[int, int],
    box_count: int = 5,
    box_width: int = 45,
    box_height: int = 24,
    spacing: int = 10,
):
    x, y = position

    for i in range(box_count):
        left = x + i * (box_width + spacing)
        top = y
        right = left + box_width
        bottom = top + box_height

        draw.rectangle(
            (left, top, right, bottom),
            outline="black",
            width=2,
        )


def create_pokemon_card(
    pokemon: Pokemon,
    shiny: bool = False,
    output_path: str | None = None,
) -> Image.Image:

    card = Image.new(
        "RGB",
        (CARD_WIDTH, CARD_HEIGHT),
        "white",
    )

    draw = ImageDraw.Draw(card)

    # -------------------------
    # Card border
    # -------------------------

    border_margin = 8

    draw.rectangle(
        (
            border_margin,
            border_margin,
            CARD_WIDTH - border_margin,
            CARD_HEIGHT - border_margin,
        ),
        outline="black",
        width=2,
    )

    # Fonts
    title_font = ImageFont.load_default(size=44)
    header_font = ImageFont.load_default(size=30)
    stat_font = ImageFont.load_default(size=32)
    normal_font = ImageFont.load_default(size=26)
    body_font = ImageFont.load_default(size=24)

    # -------------------------
    # Pokémon name and number
    # -------------------------

    draw.text(
        (35, 25),
        f"#{pokemon.pokedex_number:03d}",
        font=header_font,
        fill="black",
    )

    draw.text(
        (155, 18),
        pokemon.name.upper(),
        font=title_font,
        fill="black",
    )

    # -------------------------
    # Types
    # -------------------------

    type_text = pokemon.first_type.value.capitalize()

    if pokemon.second_type is not None:
        type_text += f" / {pokemon.second_type.value.capitalize()}"

    draw.text(
        (35, 78),
        type_text,
        font=header_font,
        fill="black",
    )

    # -------------------------
    # Friendship bar
    # -------------------------

    draw.text(
        (35, 112),
        "FRIENDSHIP",
        font=body_font,
        fill="black",
    )

    draw_friendship_bar(
        draw=draw,
        position=(205, 110),
    )

    # -------------------------
    # Artwork
    # -------------------------

    artwork = get_pokemon_image(
        pokemon.name,
        shiny=shiny,
    )

    artwork.thumbnail((320, 320))

    artwork_x = (CARD_WIDTH - artwork.width) // 2
    artwork_y = 150

    card.paste(
        artwork,
        (artwork_x, artwork_y),
        artwork,
    )

    # -------------------------
    # HP and stats
    # -------------------------

    stats_top = 485

    draw.text(
        (45, stats_top),
        f"HP: {pokemon.HP}",
        font=header_font,
        fill="black",
    )

    # 3 columns:
    # col 1 -> ATK / DEF
    # col 2 -> SpA / SpD
    # col 3 -> SPD
    col1_x = 45
    col2_x = 270
    col3_x = 515

    row1_y = stats_top + 45
    row2_y = stats_top + 85

    draw.text(
        (col1_x, row1_y),
        f"ATK: {pokemon.attack} (+{pokemon.attack_modifier})",
        font=stat_font,
        fill="black",
    )
    draw.text(
        (col1_x, row2_y),
        f"DEF: {pokemon.defense} (+{pokemon.defense_modifier})",
        font=stat_font,
        fill="black",
    )

    draw.text(
        (col2_x, row1_y),
        f"SpA: {pokemon.special_attack} (+{pokemon.special_attack_modifier})",
        font=stat_font,
        fill="black",
    )
    draw.text(
        (col2_x, row2_y),
        f"SpD: {pokemon.special_defense} (+{pokemon.special_defense_modifier})",
        font=stat_font,
        fill="black",
    )

    draw.text(
        (col3_x, row1_y + 20),
        f"SPD: {pokemon.speed} (+{pokemon.speed_modifier})",
        font=stat_font,
        fill="black",
    )

    # -------------------------
    # Ability
    # -------------------------

    ability_y = 610

    draw.text(
        (45, ability_y),
        "ABILITY",
        font=header_font,
        fill="black",
    )

    draw.text(
        (45, ability_y + 34),
        pokemon.ability.name,
        font=normal_font,
        fill="black",
    )

    ability_end_y = draw_wrapped_text(
        draw=draw,
        text=pokemon.ability.description,
        position=(45, ability_y + 68),
        font=body_font,
        max_width=660,
        line_spacing=4,
    )

    # -------------------------
    # Pokédex entry
    # -------------------------

    pokedex_y = ability_end_y + 18

    draw.text(
        (45, pokedex_y),
        "POKÉDEX ENTRY",
        font=header_font,
        fill="black",
    )

    if pokemon.pokedex_entry:
        pokedex_end_y = draw_wrapped_text(
            draw=draw,
            text=pokemon.pokedex_entry,
            position=(45, pokedex_y + 34),
            font=body_font,
            max_width=660,
            line_spacing=4,
        )
    else:
        draw.text(
            (45, pokedex_y + 34),
            "No Pokédex entry available.",
            font=body_font,
            fill="black",
        )
        pokedex_end_y = pokedex_y + 34 + 24

    # -------------------------
    # Field Ability
    # -------------------------

    field_ability_y = pokedex_end_y + 18

    draw.text(
        (45, field_ability_y),
        "FIELD ABILITY",
        font=header_font,
        fill="black",
    )

    draw.line(
        (45, field_ability_y + 42, 705, field_ability_y + 42),
        fill="black",
        width=2,
    )

    draw.line(
        (45, field_ability_y + 78, 705, field_ability_y + 78),
        fill="black",
        width=2,
    )

    # -------------------------
    # Save
    # -------------------------

    if output_path is not None:
        card.save(output_path)

    return card



def create_move_card(
    move: Move,
    output_path: str | None = None,
) -> Image.Image:
    MOVE_CARD_WIDTH = 400
    MOVE_CARD_HEIGHT = 500

    card = Image.new(
        "RGB",
        (MOVE_CARD_WIDTH, MOVE_CARD_HEIGHT),
        "white",
    )

    draw = ImageDraw.Draw(card)

    # Fonts
    title_font = ImageFont.load_default(size=34)
    header_font = ImageFont.load_default(size=26)
    normal_font = ImageFont.load_default(size=22)
    small_font = ImageFont.load_default(size=22)

    # -------------------------
    # Border
    # -------------------------

    draw.rectangle(
        (10, 10, MOVE_CARD_WIDTH - 10, MOVE_CARD_HEIGHT - 10),
        outline="black",
        width=3,
    )

    # -------------------------
    # Move name
    # -------------------------

    draw.text(
        (30, 30),
        move.name.upper(),
        font=title_font,
        fill="black",
    )

    # -------------------------
    # Type and category
    # -------------------------

    type_line = (
        f"{move.element_type.value.capitalize()} • "
        f"{move.move_type.value.capitalize()}"
    )

    draw.text(
        (30, 80),
        type_line,
        font=header_font,
        fill="black",
    )

    # -------------------------
    # Main stats
    # -------------------------

    y = 120

    if move.hit_die is not None:
        draw.text(
            (30, y),
            f"Damage: {move.hit_die}",
            font=normal_font,
            fill="black",
        )
        y += 35

    draw.text(
        (30, y),
        f"Accuracy: {move.accuracy}",
        font=normal_font,
        fill="black",
    )



    y += 50

    # -------------------------
    # Description
    # -------------------------

    draw.text(
        (30, y),
        "DESCRIPTION",
        font=header_font,
        fill="black",
    )
    y += 35

    description_text = (
        move.description
        if move.description is not None
        else "No description available."
    )

    draw_wrapped_text(
        draw=draw,
        text=description_text,
        position=(30, y),
        font=small_font,
        max_width=340,
    )

    # -------------------------
    # Save
    # -------------------------

    if output_path is not None:
        card.save(output_path)

    return card

    img = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    type_name = getattr(move.element_type, "name", str(move.element_type)).capitalize()
    color = TYPE_COLORS.get(type_name, "#777777")

    # Card border & header background
    draw.rectangle([0, 0, CARD_WIDTH, CARD_HEIGHT], fill="#F8F9FA", outline="#222222", width=12)
    draw.rectangle([20, 20, CARD_WIDTH - 20, 160], fill=color)

    # Fonts (fallback to default if ttf not available)
    try:
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 46)
        sub_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 28)
        body_font = ImageFont.truetype("DejaVuSans.ttf", 26)
    except IOError:
        title_font = sub_font = body_font = ImageFont.load_default()

    # Title & Type Banner
    draw.text((40, 45), move.name, fill="#FFFFFF", font=title_font)
    draw.text((40, 110), f"{type_name} • {move.move_type.name}", fill="#F0F0F0", font=sub_font)

    # Stat Row Box
    draw.rectangle([40, 180, CARD_WIDTH - 40, 270], fill="#E9ECEF", outline="#CED4DA", width=2)
    
    # Handle hit die / status display
    dmg = getattr(move, "hit_die", "Status")
    acc_text = f"Acc: {move.accuracy}/10" if move.accuracy <= 10 else f"Acc: {move.accuracy}%"
    tier_text = f"Tier {getattr(move, 'tier', 1)}"
    
    draw.text((60, 210), f"Damage: {dmg}", fill="#212529", font=sub_font)
    draw.text((330, 210), acc_text, fill="#212529", font=sub_font)
    draw.text((540, 210), tier_text, fill="#495057", font=sub_font)

    # Description Box
    draw.rectangle([40, 300, CARD_WIDTH - 40, 950], fill="#FFFFFF", outline="#DEE2E6", width=2)
    
    # Text wrapping
    lines = textwrap.wrap(move.description, width=38)
    y_offset = 340
    for line in lines:
        draw.text((65, y_offset), line, fill="#212529", font=body_font)
        y_offset += 42

    # Save
    if output_path is not None:
        img.save(output_path)
    return img