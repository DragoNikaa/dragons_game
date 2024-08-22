from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes


class _LoadingSection(Section):
    def __init__(self) -> None:
        super().__init__((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT), 'topleft', (0, 0))

        self.add_element('background',
                         Image('dragons_game/graphics/backgrounds/loading_screen.png', self.size, 'topleft', (0, 0)))
        text = self._text('Loading', -GameConfig.WINDOW_WIDTH / 4.5)
        self.add_element('text', text)

        dot_0 = self._dot(text)
        dot_1 = self._dot(dot_0)
        dot_2 = self._dot(dot_1)

        self.add_element('dot_1', dot_1)
        self.add_element('dot_2', dot_2)

        self._dots = [dot_0, dot_1, dot_2]
        self._invisible_dot = 0
        self._counter = 0

    def _text(self, text: str, x_destination: float) -> Text:
        return Text('dragons_game/fonts/pr_viking.ttf', self.height / 7, text, 'white', 'bottomright',
                    (x_destination, -GameConfig.WINDOW_HEIGHT / 6), 5, 'black')

    def _dot(self, previous_text: Text) -> Text:
        return self._text('.', previous_text.x_destination + universal_sizes.LARGE)

    def update(self) -> None:
        self._counter += 1

        if self._counter >= 30:
            self.add_element(f'dot_{self._invisible_dot}', self._dots[self._invisible_dot])

            if self._invisible_dot < 2:
                self._invisible_dot += 1
            else:
                self._invisible_dot = 0

            self.remove_element(f'dot_{self._invisible_dot}')
            self._counter = 0


loading_screen_section = _LoadingSection()
