from enum import Enum, auto


class GameState(Enum):
    START_SCREEN = auto()
    MAIN_MENU = auto()
    BATTLE = auto()
    DRAGONS_MENU = auto()
    UNKNOWN = 42
