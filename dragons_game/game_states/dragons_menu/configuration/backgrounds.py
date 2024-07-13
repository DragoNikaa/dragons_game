from dragons_game.elements.abstract_configuration.image import ImageConfig
from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.game.configuration import game_config
from dragons_game.game_states.dragons_menu.configuration.title_bar import TitleBarConfig


class LeftBackgroundConfig(ImageConfig):
    WIDTH = int(game_config.WINDOW_WIDTH / 6)
    HEIGHT = game_config.WINDOW_HEIGHT - TitleBarConfig.HEIGHT
    IMAGE = 'dragons_game/graphics/backgrounds/main_menu/1.png'
    POSITION = Position.TOPLEFT
    DESTINATION = (0, TitleBarConfig.HEIGHT)


class RightBackgroundConfig(ImageConfig):
    WIDTH = game_config.WINDOW_WIDTH - LeftBackgroundConfig.WIDTH
    HEIGHT = game_config.WINDOW_HEIGHT
    IMAGE = 'dragons_game/graphics/backgrounds/main_menu/1.png'
    POSITION = Position.TOPLEFT
    DESTINATION = (LeftBackgroundConfig.WIDTH, TitleBarConfig.HEIGHT)
