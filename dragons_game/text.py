from math import sqrt
from typing import Union

import pygame

from dragons_game import configuration


class Text(pygame.sprite.Sprite):
    def __init__(self, font: pygame.font.Font, text: str, color: Union[str, tuple[int, int, int]],
                 dest: tuple[int, int], antialias: bool = True, position: str = 'center'):
        super().__init__()
        self.font = font
        self.text = text
        self.dest = dest
        self.antialias = antialias
        self.position = position
        self.image = font.render(text, antialias, color)
        self.rect = self.image.get_rect(**{position: dest})

    def add_text_border(self, color: Union[str, tuple[int, int, int]], thickness: int) -> None:
        added_width = configuration.General.SCREEN_WIDTH // 10
        added_height = configuration.General.SCREEN_HEIGHT // 10
        extended_image = pygame.surface.Surface(
            (self.image.get_width() + added_width, self.image.get_height() + added_height), pygame.SRCALPHA)
        extended_rect = extended_image.get_rect(center=self.rect.center)

        extended_image.blit(self.image, (added_width // 2, added_height // 2))

        text_border = extended_image.copy()
        text_border.fill(color, special_flags=pygame.BLEND_RGB_MULT)

        for offset in thickness, -thickness:
            text_border.blit(text_border, (offset, 0))
            text_border.blit(text_border, (0, offset))

        for offset in int(sqrt(thickness)), int(-sqrt(thickness)):
            text_border.blit(text_border, (offset, offset))
            text_border.blit(text_border, (offset, -offset))

        text_border.blit(extended_image, (0, 0))

        self.image = text_border
        self.rect = extended_rect
