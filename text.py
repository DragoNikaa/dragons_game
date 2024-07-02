from typing import Union

import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, font: pygame.font.Font, text: str, color: Union[str, tuple[int, int, int]],
                 dest: Union[tuple[int, int], int], antialias: bool = True, position: str = 'center'):
        super().__init__()
        self.image = font.render(text, antialias, color)
        self.rect = self.image.get_rect(**{position: dest})
