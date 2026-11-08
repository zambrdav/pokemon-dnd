from dataclasses import dataclass, field
from .abilities import Ability
from .moves import LearnableMove
from typing import Sequence
import requests 
from .types import PokemonType





@dataclass
class Pokemon:
    name: str
    first_type: PokemonType
    HP: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int
    ability: Ability
    pokedex_number: int
    pokedex_entry: str | None = None
    second_type: PokemonType | None = None 
    learnset: Sequence[LearnableMove] = field(default_factory=list)

    attack_modifier: int = field(init=False)
    defense_modifier: int = field(init=False)
    special_attack_modifier: int = field(init=False)
    special_defense_modifier: int = field(init=False)
    speed_modifier: int = field(init=False)

    def __post_init__(self):
        self.attack_modifier = self.attack // 2
        self.defense_modifier = self.defense // 2
        self.special_attack_modifier = self.special_attack // 2
        self.special_defense_modifier = self.special_defense // 2
        self.speed_modifier = self.speed // 2


    @classmethod
    def from_api(cls, pokemon_name: str, ability: Ability, learnset: Sequence[LearnableMove] | None = None) -> "Pokemon":

        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        )
        response.raise_for_status()

        data = response.json()

        species_response = requests.get(data["species"]["url"])
        species_response.raise_for_status()
        species_data = species_response.json()

        pokedex_entry = next(
            (
                entry["flavor_text"]
                for entry in species_data["flavor_text_entries"]
                if entry["language"]["name"] == "en"
            ),
            None,
        )
        if pokedex_entry is not None:
            pokedex_entry = pokedex_entry.replace("\n", " ").replace("\f", " ")

        stats = {
            stat["stat"]["name"]: stat["base_stat"]
            for stat in data["stats"]
        }

        # divide the stats into 10 and round except for the HP stat
        for stat_name, value in stats.items():
            if stat_name != "hp":
                stats[stat_name] = convert_stat(value)
            # HP is divided by 1.5
            elif stat_name == "hp":
                stats[stat_name] = round(value / 1.5)




        types = [
            PokemonType(type_data["type"]["name"])
            for type_data in data["types"]
        ]

        first_type = types[0]
        second_type = types[1] if len(types) > 1 else None

        return cls(
            name=data["name"].capitalize(),
            pokedex_number=data["id"],
            pokedex_entry=pokedex_entry,
            first_type=first_type,
            second_type=second_type,
            HP=stats["hp"],
            attack=stats["attack"],
            defense=stats["defense"],
            special_attack=stats["special-attack"],
            special_defense=stats["special-defense"],
            speed=stats["speed"],
            ability=ability,
            learnset=learnset if learnset is not None else []
        )

    



def convert_stat(base_stat: int) -> int:
    return round(base_stat / 10)