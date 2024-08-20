import pygame

from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.utils import custom_types
from dragons_game.utils.observers import Observer


class NewLineText(Section, Observer):
    def __init__(self, size: tuple[float, float], position: custom_types.Position, destination: tuple[float, float],
                 padding: float, font_path: str, text_size: float, text: str, color: custom_types.Color,
                 border_thickness: int = 0, border_color: custom_types.Color = 0, alpha: int = 255):
        super().__init__(size, position, destination)

        self._padding = padding
        self._font_path = font_path
        self._text_size = text_size
        self._color = color
        self._border_thickness = border_thickness
        self._border_color = border_color
        self._alpha = alpha

        self._first_visible_line = 0
        self._last_visible_line = 0
        self._y_destinations = []
        self._lines = {}

        words = text.split(' ')
        line_index = 0
        y_destination = padding

        while words:
            start_index = 0
            end_index = 1
            text = ' '.join(words[start_index:end_index])
            line = previous_line = self._line(text, y_destination)

            while line.width <= self.width - 2 * padding and end_index <= len(words):
                previous_line = line
                end_index += 1
                text = ' '.join(words[start_index:end_index])
                line = self._line(text, y_destination)

            if y_destination + previous_line.height <= self.height - padding:
                self.add_element(f'line_{line_index}', previous_line)
                self._y_destinations.append(y_destination)
                self._last_visible_line = line_index

            self._lines[f'line_{line_index}'] = previous_line
            line_index += 1
            words = words[end_index - 1:]
            y_destination += previous_line.height

    def _line(self, text: str, y_destination: float) -> Text:
        return Text(self._font_path, self._text_size, text, self._color, 'topleft', (self._padding, y_destination),
                    self._border_thickness, self._border_color, self._alpha)

    def update_on_notify(self, y: int) -> None:
        if self.rect.collidepoint(pygame.mouse.get_pos()) and (
                (y > 0 and self._first_visible_line > 0) or (y < 0 and self._last_visible_line + 1 < len(self._lines))):
            if y > 0:
                self._first_visible_line -= 1
                line_to_add = f'line_{self._first_visible_line}'
                line_to_remove = f'line_{self._last_visible_line}'
                self._last_visible_line -= 1
            else:
                self._last_visible_line += 1
                line_to_add = f'line_{self._last_visible_line}'
                line_to_remove = f'line_{self._first_visible_line}'
                self._first_visible_line += 1

            self.remove_element(line_to_remove)
            self.add_element(line_to_add, self._lines[line_to_add])

            for line_index in range(self._first_visible_line, self._last_visible_line + 1):
                line = self.get_text(f'line_{line_index}')
                line.destination = line.x_destination, round(
                    self._y_destinations[line_index - self._first_visible_line])

    def clean_up(self) -> None:
        for line_index in range(self._first_visible_line, self._last_visible_line + 1):
            self.remove_element(f'line_{line_index}')

        for line_index, y_destination in enumerate(self._y_destinations):
            line = self._lines[f'line_{line_index}']
            line.destination = line.x_destination, round(y_destination)
            self.add_element(f'line_{line_index}', line)

        self._first_visible_line = 0
        self._last_visible_line = len(self._y_destinations) - 1
