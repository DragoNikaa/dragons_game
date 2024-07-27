import pygame

from dragons_game.utils import custom_types
from dragons_game.elements.section import Section


class Text(pygame.sprite.Sprite):
    def __init__(self, outer_element: Section, font_path: str, size: int, text: str, color: custom_types.Color,
                 position: custom_types.Position, offset: tuple[float, float], border_thickness: int = 0,
                 border_color: custom_types.Color = 0):
        super().__init__()

        self._text = text
        self._color = color
        self._position = str(position)
        self._offset = offset
        self._border_thickness = border_thickness
        self._border_color = border_color

        self._font = pygame.font.Font(font_path, size)
        self._destination = outer_element.get_inner_element_destination(position, offset)

        self._set_image_and_rect()

    def change_text(self, new_text: str) -> None:
        self._text = new_text
        self._set_image_and_rect()

    def _set_image_and_rect(self) -> None:
        self.image = self._font.render(self._text, True, self._color)
        self.rect = self.image.get_rect(**{self._position: self._destination})

        if self._border_thickness:
            self._add_text_border()

        self.image_without_effects = self.image

    def _add_text_border(self) -> None:
        added_size = 4 * self._border_thickness

        extended_image = pygame.surface.Surface(
            (self.image.get_width() + added_size, self.image.get_height() + added_size), flags=pygame.SRCALPHA)
        extended_image.blit(self.image, (added_size / 2, added_size / 2))
        extended_image.fill(self._border_color, special_flags=pygame.BLEND_RGB_MULT)

        for offset in (self._border_thickness, -self._border_thickness):
            extended_image.blit(extended_image, (offset, 0))
            extended_image.blit(extended_image, (0, offset))

        for offset in (self._border_thickness ** 0.5, -self._border_thickness ** 0.5):
            extended_image.blit(extended_image, (offset, offset))
            extended_image.blit(extended_image, (offset, -offset))

        extended_image.blit(self.image, (added_size / 2, added_size / 2))
        self.image = extended_image
        self.rect = self.image.get_rect(**{self._position: self._destination})

    @property
    def width(self) -> int:
        return self.rect.width

    @property
    def height(self) -> int:
        return self.rect.height

    @property
    def position(self) -> str:
        return self._position

    @property
    def x_offset(self) -> float:
        return self._offset[0]

    @property
    def y_offset(self) -> float:
        return self._offset[1]
