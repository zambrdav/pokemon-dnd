from typing import Literal 
from dataclasses import dataclass, field
from enum import Enum
from .types import PokemonType


class MoveType(str, Enum):
    PHYSICAL = "physical"
    SPECIAL = "special"
    STATUS = "status"
    OTHER = "other"


@dataclass(frozen=True)
class Move:
    name: str
    element_type: PokemonType
    move_type: MoveType
    accuracy: int
    PP: int
    tier: int
    hit_die: str | None = None
    description: str | None = None 

    def __post_init__(self):
        if self.move_type in (MoveType.PHYSICAL, MoveType.SPECIAL):
            if self.hit_die is None:
                raise ValueError(
                    f"{self.name}: {self.move_type.value} moves must have a hit die."
                )

        if self.move_type in (MoveType.STATUS, MoveType.OTHER):
            if not self.description:
                raise ValueError(
                    f"{self.name}: {self.move_type.value} moves must have a description."
                )

@dataclass(frozen=True)
class LearnableMove:
    move: Move
    method: Literal["level_up", "tm"]
    level: int | None = None

    def __post_init__(self):
        if self.method == "level_up" and self.level is None:
            raise ValueError(
                f"{self.move.name}: level_up moves must have a level."
            )
        if self.method == "tm" and self.level is not None:
            raise ValueError(
                f"{self.move.name}: tm moves cannot have a level."
            )
        





TACKLE = Move(
    name="Tackle",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="1d8",
    tier=1,
    description="The target is tackled with a full-body charge.",
)

QUICK_ATTACK = Move(
    name="Quick Attack",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="1d6",
    tier=1,
    description="The user attacks first. PRIORITY MOVE.",
)

GROWL = Move(
    name="Growl",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="Lowers the target's Attack modifier by 2.",
)

EMBER = Move(
    name="Ember",
    element_type=PokemonType.FIRE,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with small flames.",
)


RAZOR_LEAF = Move(
    name="Razor Leaf",
    element_type=PokemonType.GRASS,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with sharp leaves.",
)

BUBBLE = Move(
    name="Bubble",
    element_type=PokemonType.WATER,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a bubble.",
)

BITE = Move(
    name="Bite",
    element_type=PokemonType.DARK,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is bitten with sharp fangs.",
)


CRUNCH = Move(
    name="Crunch",
    element_type=PokemonType.DARK,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="3d6",
    tier=3,
    description="The target is bitten with sharp fangs.",
)


ICY_WIND = Move(
    name="Icy Wind",
    element_type=PokemonType.ICE,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a chilling wind. Target looses one spot in the initiative order.",
)

IRON_TAIL = Move(
    name="Iron Tail",
    element_type=PokemonType.STEEL,
    move_type=MoveType.PHYSICAL,
    accuracy=8,
    PP=10,
    hit_die="3d8",
    tier=2,
    description="The target is attacked with a steel-hard tail.",
)


WATER_GUN = Move(
    name="Water Gun",
    element_type=PokemonType.WATER,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a stream of water.",
)

WATER_PULSE = Move(
    name="Water Pulse",
    element_type=PokemonType.WATER,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="2d8",
    tier=2,
    description="The target is attacked with a pulse of water.",
)

AQUA_JET = Move(
    name="Aqua Jet",
    element_type=PokemonType.WATER,
    move_type=MoveType.PHYSICAL,
    accuracy=7,
    PP=10,
    hit_die="2d10",
    tier=1,
    description="The target is attacked with a jet of water. PRIORITY MOVE.",
)


HYDRO_PUMP = Move(
    name="Hydro Pump",
    element_type=PokemonType.WATER,
    move_type=MoveType.SPECIAL,
    accuracy=7,
    PP=10,
    hit_die="3d8",
    tier=2,
    description="The target is attacked with a stream of water.",
)

FIRE_PUNCH = Move(
    name="Fire Punch",
    element_type=PokemonType.FIRE,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d8",
    tier=2,
    description="The target is attacked with a fiery fist.",
)


FIRE_FANG = Move(
    name="Fire Fang",
    element_type=PokemonType.FIRE,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a fiery bite.",
)

FIRE_SPIN = Move(
    name="Fire Spin",
    element_type=PokemonType.FIRE,
    move_type=MoveType.SPECIAL,
    accuracy=7,
    PP=10,
    hit_die="3d10",
    tier=3,
    description="The target is trapped in a vortex of fire.",
)


FLAMETHROWER = Move(
    name="Flamethrower",
    element_type=PokemonType.FIRE,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="2d8",
    tier=2,
    description="The target is attacked with a stream of fire.",
)

SWORDS_DANCE = Move(
    name="Swords Dance",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=2,
    description="Raises the user's Attack modifier by 3.",
)

CALM_MIND = Move(
    name="Calm Mind",
    element_type=PokemonType.PSYCHIC,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=2,
    description="Raises the user's Special Attack and Special Defense modifiers by 2.",
)


RAIN_DANCE = Move(
    name="Rain Dance",
    element_type=PokemonType.WATER,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=2,
    description="The user summons rain for 5 turns. Water-type moves gain one additional damage die of the same type as the move. Fire-type moves lose one damage die of the same type as the move.",
)



THUNDER_WAVE = Move(
    name="Thunder Wave",
    element_type=PokemonType.ELECTRIC,
    move_type=MoveType.STATUS,
    accuracy=8,
    PP=10,
    tier=1,
    description="The target is paralyzed. Always hit if the user is electric type. ",
)

THUNDER_SCHOCK = Move(
    name="Thunder Shock",
    element_type=PokemonType.ELECTRIC,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a jolt of electricity.",
)

THUNDERBOLT = Move(
    name="Thunderbolt",
    element_type=PokemonType.ELECTRIC,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="3d6",
    tier=3,
    description="The target is attacked with a strong jolt of electricity.",
)

THUNDER = Move(
    name="Thunder",
    element_type=PokemonType.ELECTRIC,
    move_type=MoveType.SPECIAL,
    accuracy=7,
    PP=10,
    hit_die="3d10",
    tier=3,
    description="The target is attacked with a thunderbolt",)


SPARK = Move(
    name="Spark",
    element_type=PokemonType.ELECTRIC,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=3,
    description="The target is attacked with a jolt of electricity.",
)


WILD_CHARGE = Move(
    name="Wild Charge",
    element_type=PokemonType.ELECTRIC,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="3d6",
    tier=3,
    description="The target is attacked with a jolt of electricity. The user takes 1d6 damage.",
)


THUNDER_PUNCH = Move(
    name="Thunder Punch",
    element_type=PokemonType.ELECTRIC,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d8",
    tier=2,
    description="The target is attacked with an electrified fist.",
)


ICE_PUNCH = Move(
    name="Ice Punch",
    element_type=PokemonType.ICE,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d8",
    tier=2,
    description="The target is attacked with an icy fist.",
)


THUNDER_FANG = Move(
    name="Thunder Fang",
    element_type=PokemonType.ELECTRIC,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="3d6",
    tier=3,
    description="The target is attacked with an electrified bite.",
)



VINE_WHIP = Move(
    name="Vine Whip",
    element_type=PokemonType.GRASS,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a whip of vines.",
)

LEECH_SEED = Move(
    name="Leech Seed",
    element_type=PokemonType.GRASS,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="The target is seeded with a leech seed. At the end of each turn, the target loses 1d4 HP and the user gains that much HP.",
)

ABSORB = Move(
    name="Absorb",
    element_type=PokemonType.GRASS,
    move_type=MoveType.SPECIAL,
    accuracy=8,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a seed that absorbs half the HP.",
)

MEGA_DRAIN = Move(
    name="Mega Drain",
    element_type=PokemonType.GRASS,
    move_type=MoveType.SPECIAL,
    accuracy=8,
    PP=10,
    hit_die="2d8",
    tier=2,
    description="The target is attacked with a seed that absorbs half the HP.",
)

GIGA_DRAIN = Move(
    name="Giga Drain",
    element_type=PokemonType.GRASS,
    move_type=MoveType.SPECIAL,
    accuracy=8,
    PP=10,
    hit_die="3d6",
    tier=3,
    description="The target is attacked with a seed that absorbs half the HP.",
)

SEED_BOMB = Move(
    name="Seed Bomb",
    element_type=PokemonType.GRASS,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="3d6",
    tier=3,
    description="The target is attacked with a bomb made of seeds.",
)

POWER_WHIP = Move(
    name="Power Whip",
    element_type=PokemonType.GRASS,
    move_type=MoveType.PHYSICAL,
    accuracy=7,
    PP=10,
    hit_die="3d10",
    tier=3,
    description="The target is attacked with a whip of vines.",
)


POISON_POWDER = Move(
    name="Poison Powder",
    element_type=PokemonType.POISON,
    move_type=MoveType.STATUS,
    accuracy=7,
    PP=10,
    tier=1,
    description="The target is poisoned.",
)

SLEEP_POWDER = Move(
    name="Sleep Powder",
    element_type=PokemonType.GRASS,
    move_type=MoveType.STATUS,
    accuracy=7,
    PP=10,
    tier=1,
    description="The target is put to sleep.",
)

SCRATCH = Move(
    name="Scratch",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=15,
    hit_die="2d6",
    tier=1,
    description="Scratches the target with sharp, hard claws.",
)

WITHDRAW = Move(
    name="Withdraw",
    element_type=PokemonType.WATER,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="The user withdraws into its shell, raising its Defense modifier by 2.",
)

SLASH = Move(
    name="Slash",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d8",
    tier=2,
    description="A fierce slashing strike. Scores a critical hit on an accuracy roll of 1 or 2.",
)

SLUDGE = Move(
    name="Sludge",
    element_type=PokemonType.POISON,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="2d8",
    tier=2,
    description="Unsanitary sludge is hurled at the target. Roll 1d10: on a 1-3, poisons the target.",
)

AIR_SLASH = Move(
    name="Air Slash",
    element_type=PokemonType.FLYING,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="2d8",
    tier=2,
    description="The user attacks with a blade of air that slices through the sky. Grants Flying-type STAB.",
)

SOLAR_BEAM = Move(
    name="Solar Beam",
    element_type=PokemonType.GRASS,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=5,
    hit_die="3d10",
    tier=3,
    description="A two-turn strike. Turn 1: user absorbs sunlight. Turn 2: fires a concentrated beam of light. Fires instantly in harsh sunlight.",
)

BLAST_BURN = Move(
    name="Blast Burn",
    element_type=PokemonType.FIRE,
    move_type=MoveType.SPECIAL,
    accuracy=8,
    PP=5,
    hit_die="3d10",
    tier=3,
    description="The target is razed by a fiery explosion. The user cannot take a Move Action on the following turn to cool down.",
)

HYDRO_CANNON = Move(
    name="Hydro Cannon",
    element_type=PokemonType.WATER,
    move_type=MoveType.SPECIAL,
    accuracy=8,
    PP=5,
    hit_die="3d10",
    tier=3,
    description="The target is hit with a watery blast from high-pressure cannons. The user cannot take a Move Action on the following turn to recover.",
)


PROTECT = Move(
    name="Protect",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="The user shields itself from incoming harm. PRIORITY MOVE (+3). Negates all direct damage and targeted status effects from moves used against the user this round. Automatically succeeds on its first use. If used on consecutive turns, roll 1d10: succeeds only on a 1–3, failing on a 4–10.",
)

STUN_SPORE = Move(
    name="Stun Spore",
    element_type=PokemonType.GRASS,
    move_type=MoveType.STATUS,
    accuracy=7,
    PP=10,
    tier=1,
    description="The target is paralyzed.",
)

SMOKESCREEN = Move(
    name="Smokescreen",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="The target's accuracy is lowered by 2.",
)


MUD_SLAP = Move(
    name="Mud-Slap",
    element_type=PokemonType.GROUND,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a mud projectile. The target's accuracy is lowered by 1.",
)

HOWL = Move(
    name="Howl",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="Raises the user's Attack modifier by 2.",
)

SAND_ATTACK = Move(
    name="Sand Attack",
    element_type=PokemonType.GROUND,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="The target's accuracy is lowered by 2.",
)

HORN_ATTACK = Move(
    name="Horn Attack",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d8",
    tier=2,
    description="The target is attacked with a horn.",
)

AERIAL_ACE = Move(
    name="Aerial Ace",
    element_type=PokemonType.FLYING,
    move_type=MoveType.PHYSICAL,
    accuracy=100,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a flurry of blades. This attack never misses.",
)

BRICK_BREAK = Move(
    name="Brick Break",
    element_type=PokemonType.FIGHTING,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d8",
    tier=2,
    description="The target is attacked with a strong punch.",
)

GUST = Move(
    name="Gust",
    element_type=PokemonType.FLYING,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a gust of wind.",
)

WING_ATTACK = Move(
    name="Wing Attack",
    element_type=PokemonType.FLYING,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d8",
    tier=2,
    description="The target is attacked with a flurry of wings.",
)


SUPERSONIC = Move(
    name="Supersonic",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="The target becomes confused.",
)

TWINEEDLE = Move(
    name="Twineedle",
    element_type=PokemonType.BUG,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with two needles.",
)

STRING_SHOT = Move(
    name="String Shot",
    element_type=PokemonType.BUG,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="The target's initiative is lowered by 2.",
)

DEFEND_ORDER = Move(
    name="Defend Order",
    element_type=PokemonType.BUG,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="Raises the user's Defense modifier by 3.",
)

ATTACK_ORDER = Move(
    name="Attack Order",
    element_type=PokemonType.BUG,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="Raises the user's Attack modifier by 3.",
)

SWEET_SCENT = Move(
    name="Sweet Scent",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="Lowers the target's Defense modifier by 2.",
)

BUG_BITE = Move(
    name="Bug Bite",
    element_type=PokemonType.BUG,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a bite.",
)

STRUGGLE_BUG = Move(
    name="Struggle Bug",
    element_type=PokemonType.BUG,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a bug.",
)

ACID = Move(
    name="Acid",
    element_type=PokemonType.POISON,
    move_type=MoveType.SPECIAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a spray of acid.",
)

TOXIC = Move(
    name="Toxic",
    element_type=PokemonType.POISON,
    move_type=MoveType.STATUS,
    accuracy=8,
    PP=10,
    tier=1,
    description="The target is badly poisoned. (The target takes 1d4 damage at the end of each turn, and the damage increases by 1d4 each turn)",
)

LEECH_LIFE = Move(
    name="Leech Life",
    element_type=PokemonType.BUG,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a bite that drains the target's HP.",
)

SPIDER_WEB = Move(
    name="Spider Web",
    element_type=PokemonType.BUG,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="The target is trapped in a spider web. The target cannot escape.",
)

ROLLOUT = Move(
    name="Rollout",
    element_type=PokemonType.ROCK,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a rolling rock.",
)

HARDEN = Move(
    name="Harden",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="Raises the user's Defense modifier by 2.",
)

METAL_CLAW = Move(
    name="Metal Claw",
    element_type=PokemonType.STEEL,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a steel-hard claw.",
)

DEFENSE_CURL = Move(
    name="Defense Curl",
    element_type=PokemonType.NORMAL,
    move_type=MoveType.STATUS,
    accuracy=10,
    PP=10,
    tier=1,
    description="Raises the user's Defense modifier by 2.",
)


ROCK_THROW = Move(
    name="Rock Throw",
    element_type=PokemonType.ROCK,
    move_type=MoveType.PHYSICAL,
    accuracy=10,
    PP=10,
    hit_die="2d6",
    tier=1,
    description="The target is attacked with a rock.",
)






ALL_MOVES = [
    TACKLE,
    QUICK_ATTACK,
    GROWL,
    EMBER,
    RAZOR_LEAF,
    BUBBLE,
    BITE,
    CRUNCH,
    ICY_WIND,
    IRON_TAIL,
    WATER_GUN,
    WATER_PULSE,
    AQUA_JET,
    HYDRO_PUMP,
    FIRE_PUNCH,
    FIRE_FANG,
    FIRE_SPIN,
    FLAMETHROWER,
    SWORDS_DANCE,
    CALM_MIND,
    RAIN_DANCE,
    THUNDER_WAVE,
    THUNDER_SCHOCK,
    THUNDERBOLT,
    THUNDER,
    SPARK,
    WILD_CHARGE,
    THUNDER_PUNCH,
    ICE_PUNCH,
    THUNDER_FANG,
    VINE_WHIP,
    LEECH_SEED,
    ABSORB,
    MEGA_DRAIN,
    GIGA_DRAIN,
    SEED_BOMB,
    POWER_WHIP,
    POISON_POWDER,
    SLEEP_POWDER,
]

