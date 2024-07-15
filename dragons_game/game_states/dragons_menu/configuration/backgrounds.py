from dragons_game.elements.abstract_configuration.image import ImageConfig
from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.game.configuration import game_config
from dragons_game.game_states.general.configuration.title_bar import TitleBarConfig


class LeftBackgroundConfig(ImageConfig):
    WIDTH = int(game_config.WINDOW_WIDTH / 7)
    HEIGHT = game_config.WINDOW_HEIGHT - TitleBarConfig.HEIGHT
    IMAGE = 'dragons_game/graphics/backgrounds/dragons_menu/left.png'
    POSITION = Position.TOPLEFT
    DESTINATION = (0, TitleBarConfig.HEIGHT)


class RightBackgroundConfig(ImageConfig):
    WIDTH = game_config.WINDOW_WIDTH - LeftBackgroundConfig.WIDTH
    HEIGHT = LeftBackgroundConfig.HEIGHT
    IMAGE = 'dragons_game/graphics/backgrounds/dragons_menu/right.png'
    POSITION = Position.TOPLEFT
    DESTINATION = (LeftBackgroundConfig.WIDTH, TitleBarConfig.HEIGHT)
