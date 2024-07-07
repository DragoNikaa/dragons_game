import pathlib
import random

import pygame.sprite

from dragons_game import configuration


class Background(pygame.sprite.Sprite):
    def __init__(self, backgrounds_dir_path: str, width: int = configuration.General.SCREEN_WIDTH,
                 height: int = configuration.General.SCREEN_HEIGHT, dest: tuple[int, int] = (0, 0)):
        super().__init__()
        self.height = height
        self.dest = dest
        background_paths = [background_path for background_path in pathlib.Path(backgrounds_dir_path).iterdir()]
        self.drawn_background_number = random.randint(1, len(background_paths))
        self.image = pygame.image.load(background_paths[self.drawn_background_number - 1]).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=dest)
