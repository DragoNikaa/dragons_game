from enum import Enum

from dragons_game.dragons.dragon_class import DragonClass


class Feature(Enum):
    EXPERIENCE_TO_NEXT_LEVEL = 1
    MAX_ENERGY = 2
    MAX_HEALTH = 3


CLASS_TO_FEATURES = {
    DragonClass.COMMON: {Feature.EXPERIENCE_TO_NEXT_LEVEL: 20, Feature.MAX_ENERGY: 2, Feature.MAX_HEALTH: 100},
    DragonClass.UNCOMMON: {Feature.EXPERIENCE_TO_NEXT_LEVEL: 30, Feature.MAX_ENERGY: 2, Feature.MAX_HEALTH: 125},
    DragonClass.RARE: {Feature.EXPERIENCE_TO_NEXT_LEVEL: 40, Feature.MAX_ENERGY: 3, Feature.MAX_HEALTH: 150},
    DragonClass.EPIC: {Feature.EXPERIENCE_TO_NEXT_LEVEL: 60, Feature.MAX_ENERGY: 3, Feature.MAX_HEALTH: 175},
    DragonClass.LEGENDARY: {Feature.EXPERIENCE_TO_NEXT_LEVEL: 80, Feature.MAX_ENERGY: 4, Feature.MAX_HEALTH: 200},
    DragonClass.MYTHICAL: {Feature.EXPERIENCE_TO_NEXT_LEVEL: 100, Feature.MAX_ENERGY: 5, Feature.MAX_HEALTH: 225}
}
