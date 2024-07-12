import pygame

from dragons_game.elements.abstract_configuration.position import POSITION
from dragons_game.elements.abstract_configuration.text import TextConfig, TextBorderConfig
from dragons_game.game.configuration import game_config


class NameConfig(TextConfig):
    FONT = pygame.font.Font('dragons_game/fonts/pr_viking.ttf', size=int(game_config.WINDOW_HEIGHT / 3.5))
    TEXT = game_config.NAME.upper()
    COLOR = 'white'
    POSITION = POSITION.CENTER
    DESTINATION = (int(game_config.WINDOW_WIDTH / 2), int(game_config.WINDOW_HEIGHT / 3.5))


class NameBorderConfig(TextBorderConfig):
    COLOR = 'black'
    THICKNESS = 10
