from dragons_game.dragons.dragon import Dragon
from dragons_game.utils import custom_types
from dragons_game.utils.class_without_instances import ClassWithoutInstances
from dragons_game.utils.classproperty import classproperty
from dragons_game.utils.observers import ObserverClass


class User(ClassWithoutInstances):
    _dragons: list[Dragon] = []
    _dragons_sort_key = 'name'
    _dragons_sort_reverse = False

    _team_dragons: list[Dragon] = []

    _dragons_observers: list[type[ObserverClass]] = []
    _team_dragons_observers: list[type[ObserverClass]] = []

    @classmethod
    def add_dragon(cls, dragon: Dragon) -> None:
        if dragon not in cls._dragons:
            if cls._dragons_sort_key:
                if cls._dragons_sort_reverse:
                    dragon_lt_or_gt = getattr(dragon, cls._dragons_sort_key).__lt__
                else:
                    dragon_lt_or_gt = getattr(dragon, cls._dragons_sort_key).__gt__

                index = 0
                while index < len(cls._dragons) and dragon_lt_or_gt(
                        getattr(cls._dragons[index], cls._dragons_sort_key)):
                    index += 1

                cls._dragons.insert(index, dragon)
            else:
                cls._dragons.append(dragon)

            cls.notify_dragons_observers()

    @classmethod
    def add_team_dragon(cls, dragon_to_add: Dragon, dragon_to_remove_index: int = 2) -> None:
        if dragon_to_add in cls._dragons and dragon_to_add not in cls._team_dragons:
            if len(cls._team_dragons) < 3:
                cls._team_dragons.append(dragon_to_add)
            else:
                cls._team_dragons[dragon_to_remove_index] = dragon_to_add

            cls.notify_team_dragons_observers()

    @classmethod
    def sort_dragons(cls, key: custom_types.DragonsSortKey, reverse: bool = False) -> None:
        cls._dragons_sort_key = key
        cls._dragons_sort_reverse = reverse

        cls._dragons.sort(key=lambda dragon: getattr(dragon, key), reverse=reverse)
        cls.notify_dragons_observers()

    @classmethod
    def add_dragons_observer(cls, observer: type[ObserverClass]) -> None:
        cls._dragons_observers.append(observer)

    @classmethod
    def notify_dragons_observers(cls) -> None:
        for observer in cls._dragons_observers:
            observer.update_on_notify(cls._dragons)

    @classmethod
    def add_team_dragons_observer(cls, observer: type[ObserverClass]) -> None:
        cls._team_dragons_observers.append(observer)

    @classmethod
    def notify_team_dragons_observers(cls) -> None:
        for observer in cls._team_dragons_observers:
            observer.update_on_notify(cls._team_dragons)

    @classproperty
    def dragons(cls) -> list[Dragon]:
        return cls._dragons

    @classproperty
    def team_dragons(cls) -> list[Dragon]:
        return cls._team_dragons
