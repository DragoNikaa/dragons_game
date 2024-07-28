import pygame

from dragons_game.utils import custom_types
from dragons_game.elements.section import Section


class Text(pygame.sprite.Sprite):
    def __init__(self, outer_element: Section, font_path: str, size: int, text: str, color: custom_types.Color,
                 position: custom_types.Position, offset: tuple[float, float], border_thickness: int = 0,
                 border_color: custom_types.Color = 0, alpha: int = 255):
        super().__init__()

        self._text = text
        self._color = pygame.Color(color)
        self._position = str(position)
        self._offset = offset
        self._border_thickness = border_thickness
        self._border_color = pygame.Color(border_color)

        self._color.a = self._border_color.a = alpha

        self._font = pygame.font.Font(font_path, size)
        self._destination = outer_element.get_inner_element_destination(position, offset)

        self._set_image_and_rect()

    def change_text(self, new_text: str) -> None:
        self._text = new_text
        self._set_image_and_rect()

    def _set_image_and_rect(self) -> None:
        self.image = self._font.render(self._text, True, self._color)
        self.image = pygame.mask.from_surface(self.image).to_surface(setcolor=self._color, unsetcolor=None)
        self.rect = self.image.get_rect(**{self._position: self._destination})

        if self._border_thickness:
            self._add_text_border()

        self.image_without_effects = self.image

    def _add_text_border(self) -> None:
        added_size = 4 * self._border_thickness
        image_mask = pygame.mask.from_surface(self.image, 0)

        extended_surface = pygame.surface.Surface((self.width + added_size, self.height + added_size),
                                                  flags=pygame.SRCALPHA)
        extended_image_in_border_color = image_mask.to_surface(surface=extended_surface, setcolor=self._border_color,
                                                               unsetcolor=None, dest=(added_size / 2, added_size / 2))
        border = extended_image_in_border_color.copy()

        for offset in (self._border_thickness, -self._border_thickness):
            border.blit(border, (offset, 0), special_flags=pygame.BLEND_RGBA_MAX)
            border.blit(border, (0, offset), special_flags=pygame.BLEND_RGBA_MAX)

        for offset in (self._border_thickness ** 0.5, -self._border_thickness ** 0.5):
            border.blit(border, (offset, offset), special_flags=pygame.BLEND_RGBA_MAX)
            border.blit(border, (offset, -offset), special_flags=pygame.BLEND_RGBA_MAX)

        border.blit(extended_image_in_border_color, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

        self.image = image_mask.to_surface(surface=border, setcolor=self._color, unsetcolor=None,
                                           dest=(added_size / 2, added_size / 2))
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
