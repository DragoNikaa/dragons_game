from enum import IntEnum


class DragonClass(IntEnum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5
    MYTHICAL = 6

    def __str__(self) -> str:
        return self.name.lower()
