from math import sqrt

import pygame

from dragons_game.elements.abstract_configuration.button import ButtonTextConfig
from dragons_game.elements.abstract_configuration.text import TextConfig, TextBorderConfig


class Text(pygame.sprite.Sprite):
    def __init__(self, text_config: TextConfig | ButtonTextConfig, text_border_config: TextBorderConfig | None = None):
        super().__init__()

        self._text_config = text_config
        self._text_border_config = text_border_config

        self.image = text_config.FONT.render(text_config.TEXT, True, text_config.COLOR)
        self.rect = self._get_rect()

        if text_border_config:
            self._add_text_border()

    def _get_rect(self) -> pygame.Rect:
        if isinstance(self._text_config, TextConfig):
            return self.image.get_rect(**{self._text_config.POSITION: self._text_config.DESTINATION})

        return self.image.get_rect()

    def _add_text_border(self) -> None:
        if not self._text_border_config:
            return

        added_size = 4 * self._text_border_config.THICKNESS

        extended_image = pygame.surface.Surface(
            (self.image.get_width() + added_size, self.image.get_height() + added_size), flags=pygame.SRCALPHA)
        extended_image.blit(self.image, (added_size // 2, added_size // 2))
        extended_image.fill(self._text_border_config.COLOR, special_flags=pygame.BLEND_RGB_MULT)

        for offset in (self._text_border_config.THICKNESS, -self._text_border_config.THICKNESS):
            extended_image.blit(extended_image, (offset, 0))
            extended_image.blit(extended_image, (0, offset))

        for offset in (int(sqrt(self._text_border_config.THICKNESS)), -int(sqrt(self._text_border_config.THICKNESS))):
            extended_image.blit(extended_image, (offset, offset))
            extended_image.blit(extended_image, (offset, -offset))

        extended_image.blit(self.image, (added_size // 2, added_size // 2))
        self.image = extended_image
        self.rect = self._get_rect()

    def change_text(self, new_text: str) -> None:
        self.image = self._text_config.FONT.render(new_text, True, self._text_config.COLOR)
        self.rect = self._get_rect()

        if self._text_border_config:
            self._add_text_border()
