import pathlib
import random

from dragons_game.configuration import General
from dragons_game.elements.abstract_configuration.image import ImageConfig
from dragons_game.elements.abstract_configuration.position import Position


def draw_background(directory: str) -> str:
    backgrounds = [file for file in pathlib.Path(directory).iterdir() if file.name != '__init__.py']
    return str(random.choice(backgrounds))


class BackgroundConfig(ImageConfig):
    WIDTH = General.WINDOW_WIDTH
    HEIGHT = General.WINDOW_HEIGHT
    IMAGE = draw_background(directory='dragons_game/graphics/backgrounds/start_screen')
    POSITION = Position.TOPLEFT
    DESTINATION = (0, 0)
