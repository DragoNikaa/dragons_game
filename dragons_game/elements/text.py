import pygame

from dragons_game.elements.custom_sprite import CustomSprite
from dragons_game.utils import custom_types


class Text(CustomSprite):
    def __init__(self, font_path: str, size: float, text: str, color: custom_types.Color,
                 position: custom_types.Position, destination: tuple[float, float], border_thickness: int = 0,
                 border_color: custom_types.Color = 0, alpha: int = 255):
        super().__init__(position, destination)

        self._font = pygame.font.Font(font_path, round(size))
        self._color = pygame.Color(color)
        self._border_thickness = border_thickness
        self._border_color = pygame.Color(border_color)
        self._alpha = alpha
        self.text = text

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text

        self.image = self._font.render(new_text, True, self._color)
        self.rect = self.image.get_rect(**{self._position: getattr(self.rect, self._position)})

        if self._border_thickness:
            self._add_text_border()

        self.image.set_alpha(self._alpha)
        self._image_without_effects = self.image.copy()

    def _add_text_border(self) -> None:
        added_size = 4 * self._border_thickness

        extended_image = pygame.surface.Surface((self.width + added_size, self.height + added_size),
                                                flags=pygame.SRCALPHA)
        pygame.mask.from_surface(self.image).to_surface(surface=extended_image, setcolor=self._border_color,
                                                        unsetcolor=None, dest=(added_size / 2, added_size / 2))

        for offset in (self._border_thickness, -self._border_thickness):
            extended_image.blit(extended_image, (offset, 0))
            extended_image.blit(extended_image, (0, offset))

        for offset in (self._border_thickness ** 0.5, -self._border_thickness ** 0.5):
            extended_image.blit(extended_image, (offset, offset))
            extended_image.blit(extended_image, (offset, -offset))

        extended_image.blit(self.image, (added_size / 2, added_size / 2))

        self.image = extended_image.convert_alpha()
        self.rect = self.image.get_rect(**{self._position: getattr(self.rect, self._position)})
