from dragons_game.dragons.attack import Attack
from dragons_game.dragons.rarity import Rarity
from dragons_game.dragons.stats import RARITY_TO_STATS, Stat


class Dragon:
    def __init__(self, name: str, rarity: Rarity, description: str, image_path: str, basic_attack: Attack,
                 special_attack: Attack):
        self._name = name
        self._rarity = rarity
        self._description = description
        self._image_path = image_path
        self._basic_attack = basic_attack
        self._special_attack = special_attack

        self._level = 1
        self._experience_to_next_level = RARITY_TO_STATS[rarity][Stat.EXPERIENCE_TO_NEXT_LEVEL]
        self._current_experience = 0

        self._max_energy = RARITY_TO_STATS[rarity][Stat.MAX_ENERGY]
        self._current_energy = self._max_energy

        self._max_health = RARITY_TO_STATS[rarity][Stat.MAX_HEALTH]
        self._current_health = self._max_health

    def add_experience(self, experience: int) -> None:
        self._current_experience += experience
        while self._current_experience >= self._experience_to_next_level:
            self._level_up()

    def _level_up(self) -> None:
        self._level += 1
        self._current_experience -= self._experience_to_next_level

        self._experience_to_next_level = round(1.5 * self._experience_to_next_level)
        self._max_health = round(1.1 * self._max_health)
        if self._level % 3 == 0:
            self._max_energy += 1

    @property
    def name(self) -> str:
        return self._name

    @property
    def rarity(self) -> Rarity:
        return self._rarity

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
