from dragons_game.dragons.dragon import Dragon
from dragons_game.dragons.user_dragon import UserDragon
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.utils import custom_types
from dragons_game.utils.observers import Observer


class _Text(Text):
    SIZE = GameConfig.WINDOW_HEIGHT / 38

    def __init__(self, text: str, position: custom_types.Position, destination: tuple[float, float]):
        super().__init__('dragons_game/fonts/friz_quadrata.ttf', self.SIZE, text, 'white', position, destination, 1,
                         'black')


class _LevelText(_Text, Observer):
    def __init__(self, dragon: UserDragon, destination: tuple[float, float]):
        super().__init__('', 'midtop', destination)

        self._dragon = dragon
        dragon.add_level_observer(self)

    def update_on_notify(self) -> None:
        self.text = f'Level {self._dragon.level}'


class _ProgressBar(Section, Observer):
    def __init__(self, name: str, dragon: Dragon, size: tuple[float, float], destination: tuple[float, float],
                 label_x_destination: float):
        super().__init__(size, 'bottomright', destination)

        self._name = name
        self._dragon = dragon

        self.add_element('background',
                         Image(f'dragons_game/graphics/progress_bars/background.png', size, 'topleft', (0, 0)))

        self.add_element('label', _Text(name.title(), 'midleft', (label_x_destination, 0)))

        getattr(dragon, f"add_{self._name}_observer")(self)

    def update_on_notify(self) -> None:
        current_value = getattr(self._dragon, f'current_{self._name}')
        max_value = getattr(self._dragon, f'max_{self._name}')

        self.upsert_element('current', Image(f'dragons_game/graphics/progress_bars/{self._name}.png',
                                             (current_value / max_value * self.width, self.height), 'midleft', (0, 0)))

        self.upsert_element('numbers', _Text(f'{current_value}/{max_value}', 'center', (0, 0)))
