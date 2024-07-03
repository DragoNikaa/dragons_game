from enum import Enum
from typing import Union

import pygame


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


class BorderPosition(Enum):
    LEFT = 1
    RIGHT = 2
    TOP = 3
    BOTTOM = 4


class TextBorder(pygame.sprite.Sprite):
    def __init__(self, text_object: Text, color: Union[str, tuple[int, int, int]], thickness: int,
                 border_position: BorderPosition):
        super().__init__()
        self.thickness = thickness
        self.border_position = border_position
        self.text_position = text_object.position
        self.image = text_object.font.render(text_object.text, text_object.antialias, color)
        self.x, self.y = text_object.dest
        self.rect = self.rect_with_offset()

    def rect_with_offset(self) -> pygame.Rect:
        if self.border_position is BorderPosition.LEFT:
            return self.image.get_rect(**{self.text_position: (self.x - self.thickness, self.y)})
        if self.border_position is BorderPosition.RIGHT:
            return self.image.get_rect(**{self.text_position: (self.x + self.thickness, self.y)})
        if self.border_position is BorderPosition.TOP:
            return self.image.get_rect(**{self.text_position: (self.x, self.y - self.thickness)})
        return self.image.get_rect(**{self.text_position: (self.x, self.y + self.thickness)})
