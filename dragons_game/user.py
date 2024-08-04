from dragons_game.dragons.database.dragons import toothless
from dragons_game.dragons.dragon import Dragon
from dragons_game.utils.class_without_instances import ClassWithoutInstances
from dragons_game.utils.classproperty import classproperty


class User(ClassWithoutInstances):
    _dragons: list[Dragon] = []
    _team_dragons: list[Dragon] = []

    @classmethod
    def add_dragon(cls, dragon: Dragon) -> None:
        if dragon not in cls._dragons:
            cls._dragons.append(dragon)

    @classmethod
    def add_team_dragon(cls, dragon_to_add: Dragon, dragon_to_remove_index: int = 2) -> None:
        if dragon_to_add in cls._dragons and dragon_to_add not in cls._team_dragons:
            if len(cls._team_dragons) < 3:
                cls._team_dragons.append(dragon_to_add)
            else:
                cls._team_dragons[dragon_to_remove_index] = dragon_to_add

    @classproperty
    def dragons(cls) -> list[Dragon]:
        return cls._dragons

    @classproperty
    def team_dragons(cls) -> list[Dragon]:
        return cls._team_dragons


User.add_dragon(toothless)
User.add_team_dragon(toothless)
