from dragons_game.dragons.attack import Attack
from dragons_game.dragons.rarity import Rarity
from dragons_game.dragons.stats import RARITY_TO_STATS, Stat
from dragons_game.utils import custom_types


class Dragon:
    def __init__(self, name: str, rarity: Rarity, image_path: str, facing: custom_types.Facing, basic_attack: Attack,
                 special_attack: Attack):
        self._name = name
        self._rarity = rarity
        self._image_path = image_path
        self._facing = facing
        self._basic_attack = basic_attack
        self._special_attack = special_attack

        self._max_health = RARITY_TO_STATS[rarity][Stat.MAX_HEALTH]
        self._current_health = self._max_health

    @property
    def name(self) -> str:
        return self._name

    @property
    def rarity(self) -> Rarity:
        return self._rarity

    @property
    def image_path(self) -> str:
        return self._image_path

    @property
    def facing(self) -> custom_types.Facing:
        return self._facing

    @property
    def basic_attack(self) -> Attack:
        return self._basic_attack

    @property
    def special_attack(self) -> Attack:
        return self._special_attack

    @property
    def max_health(self) -> int:
        return self._max_health

    @property
    def current_health(self) -> int:
        return self._current_health
