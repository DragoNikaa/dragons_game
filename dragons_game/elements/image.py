import pygame

from dragons_game.elements.custom_sprite import CustomSprite
from dragons_game.utils import custom_types


class Image(CustomSprite):
    def __init__(self, image_path: str, size: tuple[float, float], position: custom_types.Position,
                 destination: tuple[float, float]):
        image = pygame.image.load(image_path)
        super().__init__(position, destination, image, size)
