from abc import ABC

import pygame

from dragons_game.configuration import General
from dragons_game.elements.abstract_configuration.button import ButtonConfig, ButtonTextConfig
from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.elements.abstract_configuration.text import TextBorderConfig
from dragons_game.game_states.game_state import GameState


class _ButtonConfig(ButtonConfig, ABC):
    WIDTH = int(General.WINDOW_WIDTH / 4)
    HEIGHT = int(General.WINDOW_HEIGHT / 4)
    IMAGE = 'dragons_game/graphics/buttons/start_screen.png'
    POSITION = Position.CENTER


class StartButtonConfig(_ButtonConfig):
    DESTINATION = (int(General.WINDOW_WIDTH / 2), int(General.WINDOW_HEIGHT / 1.5))
    AFTER_CLICK_STATE = GameState.MAIN_MENU


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
