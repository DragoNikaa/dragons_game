from abc import ABC, abstractmethod

import pygame

from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.utils import custom_types
from dragons_game.utils.observers import Observer


class _MultilineText(Section, ABC):
    @abstractmethod
    def __init__(self, width: float, position: custom_types.Position, destination: tuple[float, float], font_path: str,
                 text: str, color: custom_types.Color, border_thickness: int, border_color: custom_types.Color,
                 alpha: int, height: float = 0, visible_lines: int = 0, text_size: float = 0):
        super().__init__((width, height), position, destination)

        self._font_path = font_path
        self._color = color
        self._border_thickness = border_thickness
        self._border_color = border_color
        self._alpha = alpha
        self._visible_lines = visible_lines
        self._words = text.split(' ')
        self._line_index = -1
        self._y_destinations = [0.0]
        self._spacing_percent = 0.2
        self._max_line_width = 0

        if not text_size:
            text_size = height / (visible_lines + (visible_lines - 1) * self._spacing_percent) - 2 * border_thickness
        self._text_size = text_size

    def _line(self) -> Text:
        self._line_index += 1
        start_index = 0
        end_index = 1
        text = ' '.join(self._words[start_index:end_index])
        line = previous_line = self._text(text)

        while line.width <= self.width and end_index <= len(self._words):
            previous_line = line
            end_index += 1
            text = ' '.join(self._words[start_index:end_index])
            line = self._text(text)

        if previous_line.width >= self._max_line_width:
            self._max_line_width = previous_line.width

        self._words = self._words[end_index - 1:]
        return previous_line

    def _text(self, text: str) -> Text:
        return Text(self._font_path, self._text_size, text, self._color, 'topleft',
                    (0, self._y_destination(self._line_index)), self._border_thickness, self._border_color, self._alpha)

    def _y_destination(self, line_index: int) -> float:
        if len(self._y_destinations) <= line_index:
            self._y_destinations.append(self._y_destinations[line_index - 1] + (
                    1 + self._spacing_percent) * self._text_size + self._border_thickness)

        return self._y_destinations[line_index]


class MultilineTextFixedTextSize(_MultilineText):
    def __init__(self, width: float, position: custom_types.Position, destination: tuple[float, float], font_path: str,
                 text_size: float, text: str, color: custom_types.Color, border_thickness: int = 0,
                 border_color: custom_types.Color = 0, alpha: int = 255):
        super().__init__(width, position, destination, font_path, text, color, border_thickness, border_color, alpha,
                         text_size=text_size)

        while self._words:
            self.add_element(f'line_{self._line_index + 1}', self._line())

        self.rect.size = self._max_line_width, self.get_text(
            f'line_{self._line_index}').rect.bottom - self.get_text('line_0').rect.top


class MultilineTextFixedSectionHeight(_MultilineText):
    def __init__(self, size: tuple[float, float], position: custom_types.Position, destination: tuple[float, float],
                 min_visible_lines: int, font_path: str, text: str, color: custom_types.Color,
                 border_thickness: int = 0, border_color: custom_types.Color = 0, alpha: int = 255):
        while True:
            super().__init__(size[0], position, destination, font_path, text, color, border_thickness, border_color,
                             alpha, height=size[1], visible_lines=min_visible_lines)

            while self._words:
                self.add_element(f'line_{self._line_index + 1}', self._line())

            if self.get_text(f'line_{self._line_index}').rect.bottom <= self.rect.bottom:
                self.rect.width = self._max_line_width
                return

            min_visible_lines += 1


class MultilineScrollText(_MultilineText, Observer):
    def __init__(self, size: tuple[float, float], position: custom_types.Position, destination: tuple[float, float],
                 visible_lines: int, font_path: str, text: str, color: custom_types.Color, border_thickness: int = 0,
                 border_color: custom_types.Color = 0, alpha: int = 255):
        super().__init__(size[0], position, destination, font_path, text, color, border_thickness, border_color, alpha,
                         height=size[1], visible_lines=visible_lines)

        self._first_visible_line = 0
        self._last_visible_line = visible_lines - 1
        self._lines = {}

        while self._words:
            line = self._line()
            self._lines[f'line_{self._line_index}'] = line

            if self._line_index < visible_lines:
                self.add_element(f'line_{self._line_index}', line)

        self.rect.width = self._max_line_width

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

        for line_index, y_destination in zip(range(self._visible_lines), self._y_destinations):
            line = self._lines[f'line_{line_index}']
            line.destination = line.x_destination, round(y_destination)
            self.add_element(f'line_{line_index}', line)

        self._first_visible_line = 0
        self._last_visible_line = self._visible_lines - 1
