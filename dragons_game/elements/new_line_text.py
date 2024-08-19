from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.utils import custom_types


class NewLineText(Section):
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

            self.add_element(f'line_{line_index}', previous_line)
            line_index += 1
            words = words[end_index - 1:]
            y_destination += previous_line.height

    def _line(self, text: str, y_destination: float) -> Text:
        return Text(self._font_path, self._text_size, text, self._color, 'topleft', (self._padding, y_destination),
                    self._border_thickness, self._border_color, self._alpha)
