import pathlib
from abc import ABC
import random

from dragons_game.elements.abstract_configuration.button import ButtonConfig
from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.game_states.dragons_menu.configuration.backgrounds import RightBackgroundConfig
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
