from dataclasses import dataclass


@dataclass(frozen=True)
class Ability:
    name: str
    description: str


OVERGROW = Ability(
    name="Overgrow",
    description="While at 25% HP or less, Grass-type damaging moves gain one additional damage die of the same type as the move. ",
)

BLAZE = Ability(
    name="Blaze",
    description="While at 25% HP or less, Fire-type damaging moves gain one additional damage die of the same type as the move. ",
)

TORRENT = Ability(
    name="Torrent",
    description="While at 25% HP or less, Water-type damaging moves gain one additional damage die of the same type as the move. ",
)

STATIC = Ability(
    name="Static",
    description="If a Pokémon with Static is hit by a move making contact, there is a 30percent chance the foe will become paralyzed.",
)

LIGHTNING_ROD = Ability(
    name="Lightning Rod",
    description="Draws in all Electric-type moves to boost its Sp. Atk modifier by 1.",
)

STURDY = Ability(
    name="Sturdy",
    description="If this Pokémon is at full HP and would be reduced to 0 HP by a single attack, it is reduced to 1 HP instead.",
)

SYNCHRONIZE = Ability(
    name="Synchronize",
    description="When the pokemon is affected by a status condition, the foe is also affected (poison, paralysis, sleep, burn).",
)

GUTS = Ability(
    name="Guts",
    description= "While poisoned, burned, paralyzed, or otherwise under a major status condition, add one extra damage die to physical damaging moves. Ignore any physical-damage penalty caused by burn."
)

REGENERATOR = Ability(
    name="Regenerator",
    description="When this Pokémon is withdrawn from battle, it restores 1/4 of its maximum HP.",
)


INTIMIDATE = Ability(
    name="Intimidate",
    description="When this Pokémon enters battle, the Attack modifier of all opposing Pokémon is reduced by 1.",
)


SWIFT_SWIM = Ability(
    name="Swift Swim",
    description="While this Pokémon is under the effects of rain, the pokemon moves up three spots in the initiative order (over three foes) and its order cannot be changed.",
)

LEVITATE = Ability(
    name="Levitate",
    description="This Pokémon is immune to Ground-type moves.",
)

KEEN_EYE = Ability(
    name="Keen Eye",
    description="This Pokémon's accuracy cannot be lowered by opposing Pokémon.",
)


CHLOROPHYLL = Ability(
    name="Chlorophyll",
    description="While this Pokémon is under the effects of sunlight, the pokemon moves up three spots in the initiative order (over three foes) and its order cannot be changed.",
)

MOXIE = Ability(
    name="Moxie",
    description="After this Pokémon knocks out a foe, its Attack modifier is increased by 2.",
)

WATER_ABSORB = Ability(
    name="Water Absorb",
    description="If this Pokémon is hit by a Water-type move, it restores 1/4 of its maximum HP instead of taking damage.",
)

MAGIC_GUARD = Ability(
    name="Magic Guard",
    description="This Pokémon only takes damage from direct attacks. It is immune to indirect damage, such as from status conditions, weather, and entry hazards.",
)

MAGIC_BOUNCE = Ability(
    name="Magic Bounce",
    description="When an opposing Pokémon targets this Pokémon with a non-damaging move that inflicts a status condition or directly lowers its stats, that effect is reflected back at the user.",
)


PRANKSTER = Ability(
    name="Prankster",
    description="This Pokémon's status moves have their priority increased by 1.",
)

NO_GUARD = Ability(
    name="No Guard",
    description="All moves used by or against this Pokémon will always hit.",
)

SKILL_LINK = Ability(
    name="Skill Link",
    description="This Pokémon's multi-strike moves hit the maximum number of times.",
)

SIMPLE = Ability(
    name="Simple",
    description="This Pokémon's stat changes are doubled.",
)

MULTISCALE = Ability(
    name="Multiscale",
    description="If this Pokémon is at full HP, damage taken from attacks is halved.",
)

SAP_SIPPER = Ability(
    name="Sap Sipper",
    description="This Pokémon is immune to Grass-type moves, and its Attack modifier is increased by 1 when hit by one.",
)   

MOLD_BREAKER = Ability(
    name="Mold Breaker",
    description="Moves that would hit foes for 0.5 damage will hit for full damage.",
)

FLAME_BODY = Ability(
    name="Flame Body",
    description="If a Pokémon with Flame Body is hit by a move making contact, there is a 30percent chance the foe will become burned.",
)

STEAM_ENGINE = Ability(
    name="Steam Engine",
    description="If this Pokémon is hit by a Fire- or Water-type move, moves up three spots in the initiative order (over three foes) and its order cannot be changed.",
)

DEFIANT = Ability(
    name="Defiant",
    description="When this Pokémon has a stat lowered, its Attack modifier is increased by 2.",
)

SWARM = Ability(
    name="Swarm",
    description="While at 25% HP or less, Bug-type damaging moves gain one additional damage die of the same type as the move. ",
)

POISON_HEAL = Ability(
    name="Poison Heal",
    description="If this Pokémon is poisoned, it restores 1/8 of its maximum HP at the end of each turn instead of taking damage.",
)

FRISK = Ability(
    name="Frisk",
    description="Reveals the held items or the abilities of all opposing Pokémon.",
)

HEATPROOF = Ability(
    name="Heatproof",
    description="This Pokémon takes half damage from Fire-type moves.",
)

POISON_TOUCH = Ability(
    name="Poison Touch",
    description="If a Pokémon with Poison Touch hits a foe with a move making contact, there is a 30percent chance the foe will become poisoned.",
)

ROUGH_SKIN = Ability(
    name="Rough Skin",
    description="If a Pokémon with Rough Skin is hit by a move making contact, the foe takes 1/8 of its maximum HP in damage.",
)


COMPOUND_EYES = Ability(
    name="Compound Eyes",
    description="This Pokémon's moves that rely on accuracy have their accuracy increased by 30percent.",
)

PICKUP = Ability(
    name="Pickup",
    description="It has a 30percent chance of finding an item after battle.",
)

SIMPLE = Ability(
    name="Simple",
    description="This Pokémon's stat changes are doubled.",
)

EFFECT_SPORE = Ability(
    name="Effect Spore",
    description="If a Pokémon with Effect Spore is hit by a move making contact, there is a 30percent chance the foe will become poisoned, paralyzed, or fall asleep.",
)






ABILITY_DATABASE: dict[str, Ability] = {
    ability.name: ability
    for ability in (
        OVERGROW,
        BLAZE,
        TORRENT,
        STATIC,
        LIGHTNING_ROD,
        STURDY,
        SYNCHRONIZE,
        GUTS,
        REGENERATOR,
        INTIMIDATE,
        SWIFT_SWIM,
        LEVITATE,
        KEEN_EYE,
        CHLOROPHYLL,
        MOXIE,
        WATER_ABSORB,
        MAGIC_GUARD,
        MAGIC_BOUNCE,
        PRANKSTER,
        NO_GUARD,
        SKILL_LINK,
        SIMPLE,
        MULTISCALE,
        SAP_SIPPER,
        MOLD_BREAKER,
        FLAME_BODY,
        STEAM_ENGINE,
        DEFIANT,
        SWARM,
        POISON_HEAL,
        FRISK,
        HEATPROOF,
        POISON_TOUCH,
        ROUGH_SKIN,
        COMPOUND_EYES,
        PICKUP,
        EFFECT_SPORE,
    )
}





