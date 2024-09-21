from enum import Enum


class LevelType(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    FIENDISH = 4

    def __str__(self) -> str:
        return self.name.lower()
