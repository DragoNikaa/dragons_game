from dragons_game.dragons.database import dragons
from dragons_game.dragons.dragon import Dragon
from dragons_game.utils import custom_exceptions, custom_types
from dragons_game.utils.observers import ObserverClass


class User:
    def __init__(self, dragons: list[Dragon] | None = None, team_dragons: list[Dragon] | None = None):
        if dragons is None:
            dragons = []
        if team_dragons is None:
            team_dragons = []

        self._dragons = list(set(dragons))
        self._dragons_sort_key: custom_types.DragonsSortKey | None = None
        self._dragons_sort_reverse = False

        self._team_dragons = list(set(team_dragons))
        self._check_team_dragons()

        self._dragons_observers: list[type[ObserverClass]] = []
        self._team_dragons_observers: list[type[ObserverClass]] = []

    def _check_team_dragons(self) -> None:
        if len(self._team_dragons) > 3:
            raise custom_exceptions.TooManyDragonsError(3)

        for dragon in self._team_dragons:
            if dragon not in self._dragons:
                raise custom_exceptions.DragonNotOwnedError(dragon.name)

    def add_dragon(self, dragon: Dragon) -> None:
        if dragon in self._dragons:
            raise custom_exceptions.DragonAlreadyOwnedError(dragon.name)

        if self._dragons_sort_key:
            if self._dragons_sort_reverse:
                dragon_lt_or_gt = getattr(dragon, self._dragons_sort_key).__lt__
            else:
                dragon_lt_or_gt = getattr(dragon, self._dragons_sort_key).__gt__

            index = 0
            while index < len(self._dragons) and dragon_lt_or_gt(
                    getattr(self._dragons[index], self._dragons_sort_key)):
                index += 1

            self._dragons.insert(index, dragon)
        else:
            self._dragons.append(dragon)

        self.notify_dragons_observers()

    def add_team_dragon(self, dragon_to_add: Dragon, dragon_to_remove_index: int = 2) -> None:
        if dragon_to_add not in self._dragons:
            raise custom_exceptions.DragonNotOwnedError(dragon_to_add.name)

        if dragon_to_add in self._team_dragons:
            raise custom_exceptions.DragonAlreadyInTeamError(dragon_to_add.name)

        if len(self._team_dragons) < 3:
            self._team_dragons.append(dragon_to_add)
        else:
            self._team_dragons[dragon_to_remove_index] = dragon_to_add

        self.notify_team_dragons_observers()

    def sort_dragons(self, key: custom_types.DragonsSortKey, reverse: bool = False) -> None:
        self._dragons_sort_key = key
        self._dragons_sort_reverse = reverse

        self._dragons.sort(key=lambda dragon: getattr(dragon, key), reverse=reverse)
        self.notify_dragons_observers()

    def add_dragons_observer(self, observer: type[ObserverClass]) -> None:
        self._dragons_observers.append(observer)
        observer.update_on_notify(self._dragons)

    def notify_dragons_observers(self) -> None:
        for observer in self._dragons_observers:
            observer.update_on_notify(self._dragons)

    def add_team_dragons_observer(self, observer: type[ObserverClass]) -> None:
        self._team_dragons_observers.append(observer)
        observer.update_on_notify(self._team_dragons)

    def notify_team_dragons_observers(self) -> None:
        for observer in self._team_dragons_observers:
            observer.update_on_notify(self._team_dragons)

    @property
    def dragons(self) -> list[Dragon]:
        return self._dragons

    @property
    def team_dragons(self) -> list[Dragon]:
        return self._team_dragons


user = User(
    [dragons.toothless, dragons.skyflame, dragons.prismscale, dragons.frostreaver, dragons.valentira, dragons.nyxar],
    [dragons.toothless, dragons.skyflame, dragons.frostreaver])
