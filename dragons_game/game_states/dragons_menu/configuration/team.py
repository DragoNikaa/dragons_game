from abc import ABC

import pygame

from dragons_game.elements.abstract_configuration.button import ButtonConfig
from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.elements.abstract_configuration.text import TextConfig, TextBorderConfig
from dragons_game.game_states.dragons_menu.configuration.backgrounds import LeftBackgroundConfig
from dragons_game.game_states.dragons_menu.configuration.dragon_buttons import _DragonButtonConfig
from dragons_game.game_states.general.configuration.title_bar import TitleBarConfig

_SPACE_BETWEEN_ELEMENTS = int(TitleBarConfig.HEIGHT / 2)


class TeamTextConfig(TextConfig):
    FONT = pygame.font.Font('dragons_game/fonts/pr_viking.ttf', size=TitleBarConfig.HEIGHT)
    TEXT = 'My team'
    COLOR = 'white'
    POSITION = Position.MIDTOP
    DESTINATION = (int(LeftBackgroundConfig.WIDTH / 2), LeftBackgroundConfig.DESTINATION[1] + _SPACE_BETWEEN_ELEMENTS)


class TeamTextBorderConfig(TextBorderConfig):
    COLOR = 'black'
    THICKNESS = 3


class _TeamDragonButtonConfig(ButtonConfig, ABC):
    HEIGHT = int((LeftBackgroundConfig.HEIGHT - TeamTextConfig.FONT.get_height() - 5 * _SPACE_BETWEEN_ELEMENTS) / 3)
    WIDTH = int(HEIGHT * _DragonButtonConfig.WIDTH / _DragonButtonConfig.HEIGHT)
    IMAGE = 'dragons_game/graphics/backgrounds/main_menu/1.png'
    POSITION = Position.MIDTOP
    HOVER_ACTION = None
    CLICK_ACTION = None


_BUTTONS_DESTINATIONS = [(int(LeftBackgroundConfig.WIDTH / 2), y) for y in range(
    LeftBackgroundConfig.DESTINATION[1] + TeamTextConfig.FONT.get_height() + 2 * _SPACE_BETWEEN_ELEMENTS,
    LeftBackgroundConfig.DESTINATION[1] + LeftBackgroundConfig.HEIGHT,
    _TeamDragonButtonConfig.HEIGHT + _SPACE_BETWEEN_ELEMENTS)]


class TeamDragon1ButtonConfig(_TeamDragonButtonConfig):
    DESTINATION = _BUTTONS_DESTINATIONS[0]


class TeamDragon2ButtonConfig(_TeamDragonButtonConfig):
    DESTINATION = _BUTTONS_DESTINATIONS[1]


class TeamDragon3ButtonConfig(_TeamDragonButtonConfig):
    DESTINATION = _BUTTONS_DESTINATIONS[2]
