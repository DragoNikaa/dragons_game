from enum import IntEnum

from dragons_game.utils import custom_types


class Rarity(IntEnum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5
    MYTHICAL = 6

    def __str__(self) -> str:
        return self.name.lower()

    @property
    def color(self) -> custom_types.Color:
        match self:
            case Rarity.COMMON:
                return '#b67630'
            case Rarity.UNCOMMON:
                return '#08de31'
            case Rarity.RARE:
                return '#1279d7'
            case Rarity.EPIC:
                return '#f4bb15'
            case Rarity.LEGENDARY:
                return '#f31e17'
            case Rarity.MYTHICAL:
                return '#d338de'
