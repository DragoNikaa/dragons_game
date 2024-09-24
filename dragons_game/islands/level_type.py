from enum import Enum

from dragons_game.utils import custom_types


class LevelType(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    FIENDISH = 4

    def __str__(self) -> str:
        return self.name.lower()

    @property
    def main_color(self) -> custom_types.Color:
        match self:
            case LevelType.EASY:
                return '#3e1e18'
            case LevelType.MEDIUM:
                return '#265115'
            case LevelType.HARD:
                return '#500e68'
            case LevelType.FIENDISH:
                return '#8a150c'

    @property
    def secondary_color(self) -> custom_types.Color:
        match self:
            case LevelType.EASY | LevelType.MEDIUM | LevelType.HARD:
                return '#cfcfcf'
            case LevelType.FIENDISH:
                return '#f1ab2a'
