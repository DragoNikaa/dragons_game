from enum import Enum

from dragons_game.dragons.dragon_class import DragonClass


class Feature(Enum):
    EXPERIENCE_TO_LEVEL_UP = 1
    MAX_ENERGY = 2
    MAX_HEALTH = 3


CLASS_TO_FEATURES = {
    DragonClass.COMMON: {Feature.EXPERIENCE_TO_LEVEL_UP: 25, Feature.MAX_ENERGY: 2, Feature.MAX_HEALTH: 100},
    DragonClass.UNCOMMON: {Feature.EXPERIENCE_TO_LEVEL_UP: 50, Feature.MAX_ENERGY: 2, Feature.MAX_HEALTH: 125},
    DragonClass.RARE: {Feature.EXPERIENCE_TO_LEVEL_UP: 75, Feature.MAX_ENERGY: 3, Feature.MAX_HEALTH: 150},
    DragonClass.EPIC: {Feature.EXPERIENCE_TO_LEVEL_UP: 125, Feature.MAX_ENERGY: 3, Feature.MAX_HEALTH: 175},
    DragonClass.LEGENDARY: {Feature.EXPERIENCE_TO_LEVEL_UP: 175, Feature.MAX_ENERGY: 4, Feature.MAX_HEALTH: 200},
    DragonClass.MYTHICAL: {Feature.EXPERIENCE_TO_LEVEL_UP: 225, Feature.MAX_ENERGY: 5, Feature.MAX_HEALTH: 225}
}
