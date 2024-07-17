import pygame

from dragons_game.elements.abstract_configuration.button import ButtonImageConfig
from dragons_game.elements.abstract_configuration.image import ImageConfig


class Image(pygame.sprite.Sprite):
    def __init__(self, image_config: ImageConfig | ButtonImageConfig):
        super().__init__()

        self._image_config = image_config

        self.image = pygame.image.load(image_config.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (image_config.WIDTH, image_config.HEIGHT))
        self.rect = self.image.get_rect(**{self._image_config.POSITION: self._image_config.DESTINATION})

        self.image_without_brightness = self.image
