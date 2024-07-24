from dragons_game.dragons.attack import Attack
from dragons_game.dragons.dragon_class import DragonClass
from dragons_game.dragons.features import CLASS_TO_FEATURES, Feature


class Dragon:
    def __init__(self, name: str, dragon_class: DragonClass, description: str, image_path: str, basic_attack: Attack,
                 special_attack: Attack):
        self._name = name
        self._dragon_class = dragon_class
        self._description = description
        self._image_path = image_path
        self._basic_attack = basic_attack
        self._special_attack = special_attack

        self._level = 1
        self._experience_to_next_level = CLASS_TO_FEATURES[dragon_class][Feature.EXPERIENCE_TO_NEXT_LEVEL]
        self._current_experience = 0

        self._max_energy = CLASS_TO_FEATURES[dragon_class][Feature.MAX_ENERGY]
        self._current_energy = self._max_energy

        self._max_health = CLASS_TO_FEATURES[dragon_class][Feature.MAX_HEALTH]
        self._current_health = self._max_health

        self._in_team = False

    def add_experience(self, experience: int) -> None:
        self._current_experience += experience
        while self._current_experience >= self._experience_to_next_level:
            self._level_up()

    def _level_up(self) -> None:
        self._level += 1
        self._current_experience -= self._experience_to_next_level

        self._experience_to_next_level = int(1.5 * self._experience_to_next_level)
        self._max_health = int(1.1 * self._max_health)
        if self._level % 3 == 0:
            self._max_energy += 1

    @property
    def name(self) -> str:
        return self._name

    @property
    def dragon_class(self) -> DragonClass:
        return self._dragon_class

    @property
    def description(self) -> str:
        return self._description

    @property
    def image_path(self) -> str:
        return self._image_path

    @property
    def basic_attack(self) -> Attack:
        return self._basic_attack

    @property
    def special_attack(self) -> Attack:
        return self._special_attack

    @property
    def level(self) -> int:
        return self._level

    @property
    def experience_to_next_level(self) -> int:
        return self._experience_to_next_level

    @property
    def current_experience(self) -> int:
        return self._current_experience

    @property
    def max_energy(self) -> int:
        return self._max_energy

    @property
    def current_energy(self) -> int:
        return self._current_energy

    @property
    def max_health(self) -> int:
        return self._max_health

    @property
    def current_health(self) -> int:
        return self._current_health

    @property
    def in_team(self) -> bool:
        return self._in_team
