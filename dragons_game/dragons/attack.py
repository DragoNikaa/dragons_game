from collections.abc import Callable
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dragons_game.dragons.dragon import Dragon


class AttackType(Enum):
    BASIC = 'basic'
    SPECIAL = 'special'

    @property
    def cost(self) -> int:
        if self is AttackType.BASIC:
            return 0
        return 3


class Attack:
    def __init__(self, attack_type: AttackType, name: str, description: str, action: Callable[['Dragon'], None]):
        self._attack_type = attack_type
        self._name = name
        self._description = description
        self._action = action

    @property
    def type(self) -> AttackType:
        return self._attack_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def action(self) -> Callable[['Dragon'], None]:
        return self._action

    @property
    def cost(self) -> int:
        return self._attack_type.cost
