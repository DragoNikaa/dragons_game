from enum import Enum


class GameStates(Enum):
    START_SCREEN = 1
    LEVEL_SELECTION = 2


current_state = GameStates.START_SCREEN
