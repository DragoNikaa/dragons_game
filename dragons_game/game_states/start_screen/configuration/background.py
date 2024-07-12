import pathlib
import random

from dragons_game.elements.abstract_configuration.image import ImageConfig
from dragons_game.elements.abstract_configuration.position import position
from dragons_game.game.configuration import game_config


def draw_background(directory: str) -> str:
    backgrounds = [file for file in pathlib.Path(directory).iterdir() if file.name != '__init__.py']
    return str(random.choice(backgrounds))


class BackgroundConfig(ImageConfig):
    WIDTH = game_config.WINDOW_WIDTH
    HEIGHT = game_config.WINDOW_HEIGHT
    IMAGE = draw_background(directory='dragons_game/graphics/backgrounds/start_screen')
    POSITION = position.TOPLEFT
    DESTINATION = (0, 0)
