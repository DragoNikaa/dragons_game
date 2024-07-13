from dragons_game.elements.abstract_configuration.image import ImageConfig
from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.game.configuration import game_config
from dragons_game.game_states.main_menu.configuration.top_and_bottom_buttons import _TopButtonConfig, \
    _BottomButtonConfig


class BackgroundConfig(ImageConfig):
    WIDTH = game_config.WINDOW_WIDTH
    HEIGHT = game_config.WINDOW_HEIGHT - _TopButtonConfig.HEIGHT - _BottomButtonConfig.HEIGHT
    IMAGE = 'dragons_game/graphics/backgrounds/main_menu/1.png'
    POSITION = Position.TOPLEFT
    DESTINATION = (0, _TopButtonConfig.HEIGHT)
