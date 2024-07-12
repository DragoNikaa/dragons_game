import pygame

from dragons_game.elements.abstract_configuration.button import ButtonConfig, ButtonImageConfig
from dragons_game.elements.abstract_configuration.image import ImageConfig
from dragons_game.elements.abstract_configuration.position import POSITION
from dragons_game.elements.abstract_configuration.text import TextConfig, TextBorderConfig
from dragons_game.game.configuration import game_config
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.main_menu.configuration.top_and_bottom_buttons import DragonsButtonTextConfig
from dragons_game.user_event import USER_EVENT_DICT_KEY, USER_EVENT_DICT_VALUE


class TitleBarConfig(ImageConfig):
    WIDTH = game_config.WINDOW_WIDTH
    HEIGHT = int(game_config.WINDOW_HEIGHT / 20)
    IMAGE = 'dragons_game/graphics/backgrounds/main_menu/1.png'
    POSITION = POSITION.TOPLEFT
    DESTINATION = (0, 0)


class TitleBarImageConfig(ImageConfig):
    WIDTH = TitleBarConfig.WIDTH // 30
    HEIGHT = TitleBarConfig.HEIGHT
    IMAGE = 'dragons_game/graphics/backgrounds/main_menu/1.png'
    POSITION = POSITION.TOPLEFT
    DESTINATION = (int(game_config.WINDOW_WIDTH / 70), 0)


class TitleBarTextConfig(TextConfig):
    FONT = pygame.font.Font('dragons_game/fonts/pr_viking.ttf', size=int(TitleBarConfig.HEIGHT / 1.5))
    TEXT = DragonsButtonTextConfig.TEXT
    COLOR = 'white'
    POSITION = POSITION.MIDLEFT
    DESTINATION = (2 * TitleBarImageConfig.DESTINATION[0] + TitleBarImageConfig.WIDTH, int(TitleBarConfig.HEIGHT / 2))


class TitleBarTextBorderConfig(TextBorderConfig):
    COLOR = 'black'
    THICKNESS = 3


class TitleBarButtonConfig(ButtonConfig):
    HEIGHT = TitleBarConfig.HEIGHT
    WIDTH = HEIGHT
    IMAGE = 'dragons_game/graphics/backgrounds/main_menu/1.png'
    POSITION = POSITION.TOPRIGHT
    DESTINATION = (game_config.WINDOW_WIDTH, 0)
    CLICK_ACTION = {USER_EVENT_DICT_KEY.ACTION: USER_EVENT_DICT_VALUE.CHANGE_STATE,
                    USER_EVENT_DICT_KEY.NEXT_STATE: GameState.MAIN_MENU}
    HOVER_ACTION = None
