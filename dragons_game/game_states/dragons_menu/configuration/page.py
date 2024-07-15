from abc import ABC

import pygame

from dragons_game.elements.abstract_configuration.button import ButtonConfig
from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.elements.abstract_configuration.text import TextConfig, TextBorderConfig
from dragons_game.game_states.dragons_menu.configuration.backgrounds import RightBackgroundConfig
from dragons_game.game_states.general.configuration.title_bar import TitleBarConfig


class _PageButtonConfig(ButtonConfig, ABC):
    WIDTH = HEIGHT = TitleBarConfig.HEIGHT
    HOVER_ACTION = None
    CLICK_ACTION = None


class PageNumberConfig(TextConfig):
    FONT = pygame.font.Font('dragons_game/fonts/pr_viking.ttf', size=int(_PageButtonConfig.HEIGHT))
    TEXT = '1'
    COLOR = 'white'
    POSITION = Position.CENTER
    DESTINATION = (int(RightBackgroundConfig.DESTINATION[0] + RightBackgroundConfig.WIDTH / 2),
                   RightBackgroundConfig.DESTINATION[1] + RightBackgroundConfig.HEIGHT - TitleBarConfig.HEIGHT)


class PageNumberBorderConfig(TextBorderConfig):
    COLOR = 'black'
    THICKNESS = 3


class LeftPageButtonConfig(_PageButtonConfig):
    IMAGE = 'dragons_game/graphics/buttons/left_page.png'
    POSITION = Position.MIDRIGHT
    DESTINATION = (PageNumberConfig.DESTINATION[0] - TitleBarConfig.HEIGHT, PageNumberConfig.DESTINATION[1])


class RightPageButtonConfig(_PageButtonConfig):
    IMAGE = 'dragons_game/graphics/buttons/right_page.png'
    POSITION = Position.MIDLEFT
    DESTINATION = (PageNumberConfig.DESTINATION[0] + TitleBarConfig.HEIGHT, PageNumberConfig.DESTINATION[1])
