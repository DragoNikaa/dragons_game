from dragons_game.configuration import General
from dragons_game.elements.abstract_configuration.image import ImageConfig
from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.game_states.main_menu.configuration.top_and_bottom_buttons import _TopButtonConfig, \
    _BottomButtonConfig


class BackgroundConfig(ImageConfig):
    WIDTH = General.WINDOW_WIDTH
    HEIGHT = General.WINDOW_HEIGHT - _TopButtonConfig.HEIGHT - _BottomButtonConfig.HEIGHT
    IMAGE = 'dragons_game/graphics/backgrounds/main_menu/1.png'
    POSITION = Position.TOPLEFT
    DESTINATION = (0, _TopButtonConfig.HEIGHT)
