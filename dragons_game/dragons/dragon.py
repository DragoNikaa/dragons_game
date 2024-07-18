from dragons_game.dragons.attack import Attack
from dragons_game.dragons.dragon_class import DragonClass
from dragons_game.dragons.features_configuration import CLASS_TO_FEATURES, Feature


class Dragon:
    def __init__(self, name: str, description: str, dragon_class: DragonClass, image: str, basic_attack: Attack,
                 special_attack: Attack):
        self._name = name
        self._description = description
        self._dragon_class = dragon_class
        self._image = image
        self._basic_attack = basic_attack
        self._special_attack = special_attack

        self._level = 1
        self._experience_to_level_up = CLASS_TO_FEATURES[self._dragon_class][Feature.EXPERIENCE_TO_LEVEL_UP]
        self._current_experience = 0

        self._max_energy = CLASS_TO_FEATURES[self._dragon_class][Feature.MAX_ENERGY]
        self._current_energy = self._max_energy

        self._max_health = CLASS_TO_FEATURES[self._dragon_class][Feature.MAX_HEALTH]
        self._current_health = self._max_health

        self._in_team = False

    def add_experience(self, experience: int) -> None:
        self._current_experience += experience
        if self._current_experience >= self._experience_to_level_up:
            self._level_up()

    def _level_up(self) -> None:
        self._level += 1
        self._current_experience -= self._experience_to_level_up

        self._experience_to_level_up = int(1.5 * self._experience_to_level_up)
        self._max_health = int(1.1 * self._max_health)
        if self._level % 3 == 0:
            self._max_energy += 1
