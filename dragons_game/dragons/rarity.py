from enum import IntEnum


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
    def color(self) -> str:
        if self is Rarity.COMMON:
            return '#985a1f'
        elif self is Rarity.UNCOMMON:
            return '#08de31'
        elif self is Rarity.RARE:
            return '#016ece'
        elif self is Rarity.EPIC:
            return '#fdd53d'
        elif self is Rarity.LEGENDARY:
            return '#f31e17'
        else:
            return '#d338de'
