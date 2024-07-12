from abc import ABC

import pygame

from dragons_game.elements.abstract_configuration.button import ButtonConfig, ButtonTextConfig
from dragons_game.elements.abstract_configuration.position import POSITION
from dragons_game.elements.abstract_configuration.text import TextBorderConfig
from dragons_game.user_event import USER_EVENT_DICT_KEY, USER_EVENT_DICT_VALUE
from dragons_game.game.configuration import game_config
from dragons_game.game_states.game_state import GameState


class _ButtonConfig(ButtonConfig, ABC):
    WIDTH = int(game_config.WINDOW_WIDTH / 4)
    HEIGHT = int(game_config.WINDOW_HEIGHT / 4)
    IMAGE = 'dragons_game/graphics/buttons/start_screen.png'
    POSITION = POSITION.CENTER
    HOVER_ACTION = None


class StartButtonConfig(_ButtonConfig):
    DESTINATION = (int(game_config.WINDOW_WIDTH / 2), int(game_config.WINDOW_HEIGHT / 1.5))
    CLICK_ACTION = {USER_EVENT_DICT_KEY.ACTION: USER_EVENT_DICT_VALUE.CHANGE_STATE,
                    USER_EVENT_DICT_KEY.NEXT_STATE: GameState.MAIN_MENU}


class _ButtonTextConfig(ButtonTextConfig, ABC):
    FONT = pygame.font.Font('dragons_game/fonts/rurik.ttf', size=int(_ButtonConfig.HEIGHT / 2.5))
    COLOR = 'white'
    X_OFFSET = 0
    Y_OFFSET = int(_ButtonConfig.HEIGHT / 6)


class StartButtonTextConfig(_ButtonTextConfig):
    TEXT = 'START'


class _ButtonTextBorderConfig(TextBorderConfig):
    COLOR = 'black'
    THICKNESS = 3


StartButtonTextBorderConfig = _ButtonTextBorderConfig
