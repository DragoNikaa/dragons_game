from enum import Enum

from dragons_game.dragons.rarity import Rarity


class Feature(Enum):
    EXPERIENCE_TO_NEXT_LEVEL = 1
    MAX_ENERGY = 2
    MAX_HEALTH = 3


RARITY_TO_FEATURES = {
    Rarity.COMMON: {Feature.EXPERIENCE_TO_NEXT_LEVEL: 20, Feature.MAX_ENERGY: 2, Feature.MAX_HEALTH: 100},
    Rarity.UNCOMMON: {Feature.EXPERIENCE_TO_NEXT_LEVEL: 30, Feature.MAX_ENERGY: 2, Feature.MAX_HEALTH: 125},
    Rarity.RARE: {Feature.EXPERIENCE_TO_NEXT_LEVEL: 40, Feature.MAX_ENERGY: 3, Feature.MAX_HEALTH: 150},
    Rarity.EPIC: {Feature.EXPERIENCE_TO_NEXT_LEVEL: 60, Feature.MAX_ENERGY: 3, Feature.MAX_HEALTH: 175},
    Rarity.LEGENDARY: {Feature.EXPERIENCE_TO_NEXT_LEVEL: 80, Feature.MAX_ENERGY: 4, Feature.MAX_HEALTH: 200},
    Rarity.MYTHICAL: {Feature.EXPERIENCE_TO_NEXT_LEVEL: 100, Feature.MAX_ENERGY: 5, Feature.MAX_HEALTH: 225}
}
