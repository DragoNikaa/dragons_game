from abc import ABC

import pygame

from dragons_game.elements.abstract_configuration.button import ButtonConfig
from dragons_game.elements.abstract_configuration.image import ImageConfig
from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.elements.abstract_configuration.text import TextBorderConfig, TextConfig
from dragons_game.game.configuration import game_config
from dragons_game.game_states.general.configuration.icon_proportions import calculate_proportional_dimension
from dragons_game.game_states.general.game_state import GameState
from dragons_game.user_event import UserEventDictKey, UserEventDictValue


class TitleBarConfig(ImageConfig):
    HEIGHT = int(game_config.WINDOW_HEIGHT / 20)
    WIDTH = game_config.WINDOW_WIDTH - HEIGHT
    IMAGE = 'dragons_game/graphics/backgrounds/title_bar.png'
    POSITION = Position.TOPLEFT
    DESTINATION = (0, 0)


class GeneralTitleBarImageConfig(ImageConfig, ABC):
    WIDTH = int(TitleBarConfig.HEIGHT / 1.2)

    @property
    def HEIGHT(self) -> int:
        return calculate_proportional_dimension(self.IMAGE, self.WIDTH)

    POSITION = Position.MIDLEFT
    DESTINATION = (int(TitleBarConfig.HEIGHT / 2), int(TitleBarConfig.HEIGHT / 2))


class GeneralTitleBarTextConfig(TextConfig, ABC):
    FONT = pygame.font.Font('dragons_game/fonts/pr_viking.ttf', size=int(TitleBarConfig.HEIGHT / 1.5))
    COLOR = 'white'
    POSITION = Position.MIDLEFT
    DESTINATION = (
        2 * GeneralTitleBarImageConfig.DESTINATION[0] + GeneralTitleBarImageConfig.WIDTH,
        int(TitleBarConfig.HEIGHT / 2))


class TitleBarTextBorderConfig(TextBorderConfig):
    COLOR = 'black'
    THICKNESS = 3


class TitleBarButtonConfig(ButtonConfig):
    WIDTH = HEIGHT = TitleBarConfig.HEIGHT
    IMAGE = 'dragons_game/graphics/buttons/close.png'
    POSITION = Position.TOPRIGHT
    DESTINATION = (game_config.WINDOW_WIDTH, 0)
    CLICK_ACTION = {UserEventDictKey.ACTION: UserEventDictValue.CHANGE_STATE,
                    UserEventDictKey.NEXT_STATE: GameState.MAIN_MENU}
    HOVER_ACTION = None
