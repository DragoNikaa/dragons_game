import pathlib
from abc import ABC
import random

import pygame

from dragons_game.elements.abstract_configuration.button import ButtonConfig, ButtonInsideButtonConfig
from dragons_game.elements.abstract_configuration.image import ButtonImageConfig
from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.elements.abstract_configuration.text import ButtonTextConfig, TextBorderConfig
from dragons_game.game_states.dragons_menu.configuration.backgrounds import RightBackgroundConfig
from dragons_game.game_states.general.configuration.icon_proportions import calculate_proportional_width
from dragons_game.game_states.general.configuration.title_bar import TitleBarConfig

_SPACE_BETWEEN_ELEMENTS = TitleBarConfig.HEIGHT


class _DragonButtonConfig(ButtonConfig, ABC):
    WIDTH = int((RightBackgroundConfig.WIDTH - _SPACE_BETWEEN_ELEMENTS) / 5 - _SPACE_BETWEEN_ELEMENTS)
    HEIGHT = int((RightBackgroundConfig.HEIGHT - 2 * _SPACE_BETWEEN_ELEMENTS) / 2 - _SPACE_BETWEEN_ELEMENTS)

    @property
    def IMAGE(self) -> str:
        return str(random.choice([file for file in pathlib.Path('dragons_game/graphics/buttons/dragons').iterdir() if
                                  file.name != '__init__.py']))

    POSITION = Position.TOPLEFT
    HOVER_ACTION = None
    CLICK_ACTION = None


_BUTTONS_X_DESTINATIONS = [x for x in range(RightBackgroundConfig.DESTINATION[0] + _SPACE_BETWEEN_ELEMENTS,
                                            RightBackgroundConfig.DESTINATION[0] + RightBackgroundConfig.WIDTH,
                                            _DragonButtonConfig.WIDTH + _SPACE_BETWEEN_ELEMENTS)]
_ROW_1_BUTTONS_Y_DESTINATION = RightBackgroundConfig.DESTINATION[1] + _SPACE_BETWEEN_ELEMENTS


class Row1Dragon1ButtonConfig(_DragonButtonConfig):
    DESTINATION = (_BUTTONS_X_DESTINATIONS[0], _ROW_1_BUTTONS_Y_DESTINATION)


class Row1Dragon2ButtonConfig(_DragonButtonConfig):
    DESTINATION = (_BUTTONS_X_DESTINATIONS[1], _ROW_1_BUTTONS_Y_DESTINATION)


class Row1Dragon3ButtonConfig(_DragonButtonConfig):
    DESTINATION = (_BUTTONS_X_DESTINATIONS[2], _ROW_1_BUTTONS_Y_DESTINATION)


class Row1Dragon4ButtonConfig(_DragonButtonConfig):
    DESTINATION = (_BUTTONS_X_DESTINATIONS[3], _ROW_1_BUTTONS_Y_DESTINATION)


class Row1Dragon5ButtonConfig(_DragonButtonConfig):
    DESTINATION = (_BUTTONS_X_DESTINATIONS[4], _ROW_1_BUTTONS_Y_DESTINATION)


_ROW_2_BUTTONS_Y_DESTINATION = _ROW_1_BUTTONS_Y_DESTINATION + _DragonButtonConfig.HEIGHT + _SPACE_BETWEEN_ELEMENTS


class Row2Dragon1ButtonConfig(_DragonButtonConfig):
    DESTINATION = (_BUTTONS_X_DESTINATIONS[0], _ROW_2_BUTTONS_Y_DESTINATION)


class Row2Dragon2ButtonConfig(_DragonButtonConfig):
    DESTINATION = (_BUTTONS_X_DESTINATIONS[1], _ROW_2_BUTTONS_Y_DESTINATION)


class Row2Dragon3ButtonConfig(_DragonButtonConfig):
    DESTINATION = (_BUTTONS_X_DESTINATIONS[2], _ROW_2_BUTTONS_Y_DESTINATION)


class Row2Dragon4ButtonConfig(_DragonButtonConfig):
    DESTINATION = (_BUTTONS_X_DESTINATIONS[3], _ROW_2_BUTTONS_Y_DESTINATION)


class Row2Dragon5ButtonConfig(_DragonButtonConfig):
    DESTINATION = (_BUTTONS_X_DESTINATIONS[4], _ROW_2_BUTTONS_Y_DESTINATION)


class _DragonButtonTextConfig(ButtonTextConfig, ABC):
    FONT = pygame.font.Font('dragons_game/fonts/rurik.ttf', size=int(_SPACE_BETWEEN_ELEMENTS / 2.1))
    COLOR = 'white'


class DragonNameConfig(_DragonButtonTextConfig):
    @property
    def TEXT(self) -> str:
        return 'Dragon Name'

    OFFSET_FROM_CENTER = (0, -int(_DragonButtonConfig.HEIGHT / 3.55))


class DragonLevelConfig(_DragonButtonTextConfig):
    @property
    def TEXT(self) -> str:
        return f'Level {random.randint(1, 99)}'

    OFFSET_FROM_CENTER = (0, int(_DragonButtonConfig.HEIGHT / 5.1))


class DragonButtonTextBorderConfig(TextBorderConfig):
    COLOR = 'black'
    THICKNESS = 1


class DragonButtonImageConfig(ButtonImageConfig):
    HEIGHT = int(_DragonButtonConfig.HEIGHT / 3.1)
    IMAGE = 'dragons_game/graphics/dragons/toothless.png'
    WIDTH = calculate_proportional_width(IMAGE, HEIGHT)
    OFFSET_FROM_CENTER = (0, -int(_DragonButtonConfig.HEIGHT / 50))


class _ProgressBarButtonConfig(ButtonInsideButtonConfig, ABC):
    WIDTH = int(_DragonButtonConfig.WIDTH / 2)
    HEIGHT = int(_DragonButtonConfig.HEIGHT / 30)
    IMAGE = 'dragons_game/graphics/buttons/progress_bar.png'
    HOVER_ACTION = None
    CLICK_ACTION = None


class ExperienceBarButtonConfig(_ProgressBarButtonConfig):
    OFFSET_FROM_CENTER = (0, int(_DragonButtonConfig.HEIGHT / 2.9))


class EnergyBarButtonConfig(_ProgressBarButtonConfig):
    OFFSET_FROM_CENTER = (0, int(_DragonButtonConfig.HEIGHT / 2.9) - int(_SPACE_BETWEEN_ELEMENTS / 3))


class HealthBarButtonConfig(_ProgressBarButtonConfig):
    OFFSET_FROM_CENTER = (0, int(_DragonButtonConfig.HEIGHT / 2.9) - int(_SPACE_BETWEEN_ELEMENTS / 1.5))

# class ExperienceBarButtonImageConfig(ButtonImageConfig):
