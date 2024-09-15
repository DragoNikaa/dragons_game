from dragons_game.dragons.attack import Attack
from dragons_game.dragons.rarity import Rarity
from dragons_game.dragons.stats import RARITY_TO_STATS, Stat
from dragons_game.utils import custom_exceptions, custom_types
from dragons_game.utils.observers import Observer


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

        self._health_observers: list[Observer] = []

    def remove_health(self, value: int) -> None:
        self._current_health -= value

        if self._current_health <= 0:
            self._current_health = 0
            self._notify_health_observers()
            raise custom_exceptions.DragonHealthError(self._name)

        self._notify_health_observers()

    def restore_health(self) -> None:
        self._current_health = self._max_health
        self._notify_health_observers()

    def add_health_observer(self, observer: Observer) -> None:
        self._health_observers.append(observer)
        observer.update_on_notify()

    def _notify_health_observers(self) -> None:
        for observer in self._health_observers:
            observer.update_on_notify()

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
