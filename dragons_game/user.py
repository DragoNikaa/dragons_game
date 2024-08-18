from dragons_game.dragons.database import dragons
from dragons_game.dragons.dragon import Dragon
from dragons_game.utils import custom_exceptions
from dragons_game.utils.observers import Observer, ObserverClass


class User:
    def __init__(self, dragons: list[Dragon] | None = None, team_dragons: list[Dragon] | None = None):
        if dragons is None:
            dragons = []
        if team_dragons is None:
            team_dragons = []

        self._dragons = list(set(dragons))

        self._dragons_sort_keys = ('name', 'rarity', 'level', 'current_energy', 'current_health')
        self._dragons_sort_key_index = 0
        self._dragons_sort_key = self._dragons_sort_keys[self._dragons_sort_key_index]
        self._dragons_sort_reverse = False

        self._team_dragons = list(set(team_dragons))
        self._check_team_dragons()

        self._dragons_observers: list[type[ObserverClass]] = []
        self._dragons_sort_key_observers: list[Observer] = []
        self._dragons_sort_reverse_observers: list[Observer] = []
        self._team_dragons_observers: list[type[ObserverClass]] = []

        self._sort_dragons()

    def _check_team_dragons(self) -> None:
        if len(self._team_dragons) > 3:
            raise custom_exceptions.TooManyDragonsError(3)

        for dragon in self._team_dragons:
            if dragon not in self._dragons:
                raise custom_exceptions.DragonNotOwnedError(dragon.name)

            dragon.in_team = True

    def add_dragon(self, dragon: Dragon) -> None:
        if dragon in self._dragons:
            raise custom_exceptions.DragonAlreadyOwnedError(dragon.name)

        if self._dragons_sort_reverse:
            dragon_lt_or_gt = getattr(dragon, self._dragons_sort_key).__lt__
        else:
            dragon_lt_or_gt = getattr(dragon, self._dragons_sort_key).__gt__

        index = 0
        while index < len(self._dragons) and dragon_lt_or_gt(getattr(self._dragons[index], self._dragons_sort_key)):
            index += 1

        self._dragons.insert(index, dragon)
        self._notify_dragons_observers(self._dragons)

    def add_team_dragon(self, dragon: Dragon, dragon_index: int = 2) -> None:
        if dragon not in self._dragons:
            raise custom_exceptions.DragonNotOwnedError(dragon.name)

        if dragon in self._team_dragons:
            raise custom_exceptions.DragonAlreadyInTeamError(dragon.name)

        if len(self._team_dragons) < 3:
            self._team_dragons.append(dragon)
            removed_team_dragon = None
        else:
            removed_team_dragon = self._team_dragons[dragon_index]
            removed_team_dragon.in_team = False
            self._team_dragons[dragon_index] = dragon

        dragon.in_team = True
        self._notify_team_dragons_observers(dragon_index, dragon)
        self._notify_dragons_observers(added_team_dragon=dragon, removed_team_dragon=removed_team_dragon)

    def _sort_dragons(self) -> None:
        self._dragons.sort(key=lambda dragon: getattr(dragon, self._dragons_sort_key),
                           reverse=self._dragons_sort_reverse)
        self._notify_dragons_observers(self._dragons)

    def change_dragons_sort_key(self) -> None:
        self._dragons_sort_key_index += 1
        if self._dragons_sort_key_index >= len(self._dragons_sort_keys):
            self._dragons_sort_key_index = 0

        self._dragons_sort_key = self._dragons_sort_keys[self._dragons_sort_key_index]

        self._sort_dragons()
        self._notify_dragons_sort_key_observers()

    def change_dragons_sort_reverse(self) -> None:
        self._dragons_sort_reverse = not self._dragons_sort_reverse
        self._dragons.reverse()

        self._notify_dragons_observers(self._dragons)
        self._notify_dragons_sort_reverse_observers()

    def add_dragons_observer(self, observer: type[ObserverClass]) -> None:
        self._dragons_observers.append(observer)
        observer.update_on_notify(self._dragons)
        for team_dragon in self._team_dragons:
            observer.update_on_notify(added_team_dragon=team_dragon)

    def _notify_dragons_observers(self, dragons: list[Dragon] | None = None, added_team_dragon: Dragon | None = None,
                                  removed_team_dragon: Dragon | None = None) -> None:
        for observer in self._dragons_observers:
            observer.update_on_notify(dragons, added_team_dragon, removed_team_dragon)

    def add_dragons_sort_key_observer(self, observer: Observer) -> None:
        self._dragons_sort_key_observers.append(observer)
        observer.update_on_notify()

    def _notify_dragons_sort_key_observers(self) -> None:
        for observer in self._dragons_sort_key_observers:
            observer.update_on_notify()

    def add_dragons_sort_reverse_observer(self, observer: Observer) -> None:
        self._dragons_sort_reverse_observers.append(observer)
        observer.update_on_notify()

    def _notify_dragons_sort_reverse_observers(self) -> None:
        for observer in self._dragons_sort_reverse_observers:
            observer.update_on_notify()

    def add_team_dragons_observer(self, observer: type[ObserverClass]) -> None:
        self._team_dragons_observers.append(observer)
        for dragon_index, dragon in enumerate(self._team_dragons):
            observer.update_on_notify(dragon_index, dragon)

    def _notify_team_dragons_observers(self, dragon_index: int, dragon: Dragon) -> None:
        for observer in self._team_dragons_observers:
            observer.update_on_notify(dragon_index, dragon)

    @property
    def dragons(self) -> list[Dragon]:
        return self._dragons

    @property
    def dragons_sort_key(self) -> str:
        return self._dragons_sort_key.replace('current_', '')

    @property
    def dragons_sort_reverse(self) -> bool:
        return self._dragons_sort_reverse

    @property
    def team_dragons(self) -> list[Dragon]:
        return self._team_dragons


user = User(
    [dragons.toothless, dragons.skyflame, dragons.prismscale, dragons.frostreaver, dragons.valentira, dragons.nyxar],
    [dragons.toothless, dragons.skyflame, dragons.frostreaver])
