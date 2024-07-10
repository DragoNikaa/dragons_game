import pygame

from dragons_game.configuration import General
from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.elements.abstract_configuration.text import TextConfig, TextBorderConfig


class NameConfig(TextConfig):
    FONT = pygame.font.Font('dragons_game/fonts/pr_viking.ttf', size=int(General.WINDOW_HEIGHT / 3.5))
    TEXT = General.NAME.upper()
    COLOR = 'white'
    POSITION = Position.CENTER
    DESTINATION = (int(General.WINDOW_WIDTH / 2), int(General.WINDOW_HEIGHT / 3.5))


class NameBorderConfig(TextBorderConfig):
    COLOR = 'black'
    THICKNESS = 10
