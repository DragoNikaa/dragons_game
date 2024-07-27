import pygame

from dragons_game.elements.section import Section
from dragons_game.game.configuration import GameConfig
from dragons_game.utils import custom_types


class Tooltip(Section):
    def __init__(self, position: custom_types.Position, size: tuple[float, float] = (0, 0), image_path: str = '',
                 fill_color: custom_types.Color = 0):
        super().__init__(size, position, image_path=image_path, fill_color=fill_color)

    def change_size(self, new_size: tuple[float, float]) -> None:
        self._size = int(new_size[0]), int(new_size[1])
        self._set_image_and_rect()

    def update(self) -> None:
        destination = self._get_destination()
        setattr(self.rect, self._position, destination)

        for element in self.elements:
            x_offset = getattr(element, 'x_offset', 0)
            y_offset = getattr(element, 'y_offset', 0)

            tooltip_rect_position_destination = getattr(self.rect, element.position)
            element_rect_position_destination = (
                tooltip_rect_position_destination[0] + x_offset, tooltip_rect_position_destination[1] + y_offset)

            setattr(element.rect, element.position, element_rect_position_destination)

    def _get_destination(self) -> tuple[float, float]:
        x, y = pygame.mouse.get_pos()
        half_width, half_height = self.width // 2, self.height // 2

        if 'left' in self._position:
            if x + self.width > GameConfig.WINDOW_WIDTH:
                x = GameConfig.WINDOW_WIDTH - self.width
        elif 'right' in self._position:
            if x - self.width < 0:
                x = self.width

        if 'top' in self._position:
            if y + self.height > GameConfig.WINDOW_HEIGHT:
                y = GameConfig.WINDOW_HEIGHT - self.height
        elif 'bottom' in self._position:
            if y - self.height < 0:
                y = self.height

        if self._position in ('midtop', 'midbottom', 'center'):
            if x + half_width > GameConfig.WINDOW_WIDTH:
                x = GameConfig.WINDOW_WIDTH - half_width
            elif x - half_width < 0:
                x = half_width

        if self._position in ('midleft', 'midright', 'center'):
            if y + half_height > GameConfig.WINDOW_HEIGHT:
                y = GameConfig.WINDOW_HEIGHT - half_height
            elif y - half_height < 0:
                y = half_height // 2

        return x, y
