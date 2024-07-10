from enum import Enum


class GameState(Enum):
    START_SCREEN = 1
    MAIN_MENU = 2
    UNKNOWN = 42


current_state = GameState.START_SCREEN
