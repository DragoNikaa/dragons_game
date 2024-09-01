from dragons_game.dragons.attack import Attack
from dragons_game.dragons.dragon import Dragon
from dragons_game.dragons.rarity import Rarity
from dragons_game.dragons.stats import RARITY_TO_STATS, Stat
from dragons_game.utils import custom_types
from dragons_game.utils.observers import Observer


class UserDragon(Dragon):
    def __init__(self, name: str, rarity: Rarity, description: str, image_path: str, facing: custom_types.Facing,
                 basic_attack: Attack, special_attack: Attack):
        super().__init__(name, rarity, image_path, facing, basic_attack, special_attack)

        self._description = description

        self._level = 1
        self._experience_to_next_level = RARITY_TO_STATS[rarity][Stat.EXPERIENCE_TO_NEXT_LEVEL]
        self._current_experience = 0

        self._max_energy = RARITY_TO_STATS[rarity][Stat.MAX_ENERGY]
        self._current_energy = self._max_energy

        self._in_team = False
        self._in_team_observers: list[Observer] = []

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

    def add_in_team_observer(self, observer: Observer) -> None:
        self._in_team_observers.append(observer)
        observer.update_on_notify()

    def _notify_in_team_observers(self) -> None:
        for observer in self._in_team_observers:
            observer.update_on_notify()

    @property
    def description(self) -> str:
        return self._description

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
    def in_team(self) -> bool:
        return self._in_team

    @in_team.setter
    def in_team(self, value: bool) -> None:
        self._in_team = value
        self._notify_in_team_observers()
