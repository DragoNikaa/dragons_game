import pygame

from dragons_game.elements.abstract_configuration.button import ButtonConfig
from dragons_game.elements.abstract_configuration.image import ImageConfig
from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.elements.abstract_configuration.text import TextConfig, TextBorderConfig
from dragons_game.game.configuration import game_config
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.main_menu.configuration.top_and_bottom_buttons import DragonsButtonTextConfig
from dragons_game.user_event import UserEventDictKey, UserEventDictValue


class TitleBarConfig(ImageConfig):
    WIDTH = game_config.WINDOW_WIDTH
    HEIGHT = int(game_config.WINDOW_HEIGHT / 20)
    IMAGE = 'dragons_game/graphics/backgrounds/main_menu/1.png'
    POSITION = Position.TOPLEFT
    DESTINATION = (0, 0)


class TitleBarImageConfig(ImageConfig):
    WIDTH = TitleBarConfig.WIDTH // 30
    HEIGHT = TitleBarConfig.HEIGHT
    IMAGE = 'dragons_game/graphics/backgrounds/main_menu/1.png'
    POSITION = Position.TOPLEFT
    DESTINATION = (int(game_config.WINDOW_WIDTH / 70), 0)


class TitleBarTextConfig(TextConfig):
    FONT = pygame.font.Font('dragons_game/fonts/pr_viking.ttf', size=int(TitleBarConfig.HEIGHT / 1.5))
    TEXT = DragonsButtonTextConfig.TEXT
    COLOR = 'white'
    POSITION = Position.MIDLEFT
    DESTINATION = (2 * TitleBarImageConfig.DESTINATION[0] + TitleBarImageConfig.WIDTH, int(TitleBarConfig.HEIGHT / 2))


class TitleBarTextBorderConfig(TextBorderConfig):
    COLOR = 'black'
    THICKNESS = 3


class TitleBarButtonConfig(ButtonConfig):
    HEIGHT = TitleBarConfig.HEIGHT
    WIDTH = HEIGHT
    IMAGE = 'dragons_game/graphics/backgrounds/main_menu/1.png'
    POSITION = Position.TOPRIGHT
    DESTINATION = (game_config.WINDOW_WIDTH, 0)
    CLICK_ACTION = {UserEventDictKey.ACTION: UserEventDictValue.CHANGE_STATE,
                    UserEventDictKey.NEXT_STATE: GameState.MAIN_MENU}
    HOVER_ACTION = None
