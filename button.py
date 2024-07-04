from typing import Union

import pygame.sprite

import game_states
from game_states import GameStates
from text import Text


class Button(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, image_path: str, dest: tuple[int, int], position: str = 'center'):
        super().__init__()
        self.height = height
        self.dest = dest
        self.position = position
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image_copy = self.image.copy()
        self.rect = self.image.get_rect(**{position: dest})
        self.current_brightness = 0
        self.brightness_step = 5
        self.max_brightness = 25

    def add_text(self, font: pygame.font.Font, text: str, color: Union[str, tuple[int, int, int]],
                 antialias: bool = True, y_offset: int = 0) -> Text:
        text_dest = (self.dest[0], self.dest[1] + y_offset)
        return Text(font, text, color, text_dest, antialias, self.position)

    def hover(self) -> None:
        mouse_position = pygame.mouse.get_pos()
        if self.current_brightness < self.max_brightness and self.rect.collidepoint(mouse_position):
            self.current_brightness += self.brightness_step
        elif self.current_brightness > 0:
            self.current_brightness -= self.brightness_step

        image_copy = self.image_copy.copy()
        image_copy.fill((self.current_brightness, self.current_brightness, self.current_brightness),
                        special_flags=pygame.BLEND_RGB_ADD)
        self.image = image_copy

    def click(self) -> None:
        mouse_position = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(mouse_position):
            game_states.current_state = GameStates.LEVEL_SELECTION

    def update(self) -> None:
        self.hover()
        self.click()
