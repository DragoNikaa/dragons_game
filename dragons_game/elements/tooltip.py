import pygame

from dragons_game.elements.section import Section
from dragons_game.game.configuration import GameConfig
from dragons_game.utils import custom_types


class Tooltip(Section):
    def __init__(self, position: custom_types.Position, size: tuple[float, float], color: custom_types.Color,
                 border_thickness: int = 0, border_color: custom_types.Color = 0, alpha: int = 255):
        super().__init__(size, position)

        self._color = pygame.Color(color)
        self._border_thickness = border_thickness
        self._border_color = pygame.Color(border_color)
        self._alpha = alpha

        self._render_image()

    def change_size(self, size: tuple[float, float]) -> None:
        self.set_image(pygame.Surface(size, flags=pygame.SRCALPHA))
        self._render_image()

    def update(self) -> None:
        setattr(self.rect, self._position, self._dynamic_destination)

        for element in self.first_level_elements:
            if isinstance(element, Section):
                for inner_element in element.all_elements[1:]:
                    tooltip_destination = getattr(self.rect, inner_element.position)
                    inner_element_destination = (
                        tooltip_destination[0] + element.x_destination + inner_element.x_destination,
                        tooltip_destination[1] + element.y_destination + inner_element.y_destination)

                    setattr(inner_element.rect, inner_element.position, inner_element_destination)

            tooltip_destination = getattr(self.rect, element.position)
            element_destination = (
                tooltip_destination[0] + element.x_destination, tooltip_destination[1] + element.y_destination)

            setattr(element.rect, element.position, element_destination)

    def _render_image(self) -> None:
        self.image.fill(self._color)

        if self._border_thickness:
            self._add_border()

        self.image.set_alpha(self._alpha)

    def _add_border(self) -> None:
        border_image = self.image_copy
        border_image.fill(self._border_color)
        border_image.blit(self.image, (self._border_thickness, self._border_thickness),
                          pygame.Rect(0, 0, self.rect.width - 2 * self._border_thickness,
                                      self.rect.height - 2 * self._border_thickness))
        self.set_image(border_image)

    @property
    def _dynamic_destination(self) -> tuple[float, float]:
        x, y = pygame.mouse.get_pos()
        width, height = self.width, self.height
        half_width, half_height = width // 2, height // 2

        if 'left' in self._position:
            if x + width > GameConfig.WINDOW_WIDTH:
                x = GameConfig.WINDOW_WIDTH - width
        elif 'right' in self._position:
            if x - width < 0:
                x = width

        if 'top' in self._position:
            if y + height > GameConfig.WINDOW_HEIGHT:
                y = GameConfig.WINDOW_HEIGHT - height
        elif 'bottom' in self._position:
            if y - height < 0:
                y = height

        if self._position in ('midtop', 'midbottom', 'center'):
            if x + half_width > GameConfig.WINDOW_WIDTH:
                x = GameConfig.WINDOW_WIDTH - half_width
            elif x - half_width < 0:
                x = half_width

        if self._position in ('midleft', 'midright', 'center'):
            if y + half_height > GameConfig.WINDOW_HEIGHT:
                y = GameConfig.WINDOW_HEIGHT - half_height
            elif y - half_height < 0:
                y = half_height

        return x, y
