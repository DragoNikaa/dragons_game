import pathlib
import random

import pygame.sprite

import configuration


class Background(pygame.sprite.Sprite):
    def __init__(self, backgrounds_dir_path: str):
        super().__init__()
        self.backgrounds_dir_path = backgrounds_dir_path
        self.image = pygame.image.load(self.draw_background()).convert()
        self.image = pygame.transform.scale(self.image,
                                            (configuration.General.SCREEN_WIDTH, configuration.General.SCREEN_HEIGHT))
        self.rect = self.image.get_rect()

    def draw_background(self) -> pathlib.Path:
        backgrounds_dir_path = pathlib.Path(self.backgrounds_dir_path)
        background_paths = [background_path for background_path in backgrounds_dir_path.iterdir()]
        return random.choice(background_paths)
