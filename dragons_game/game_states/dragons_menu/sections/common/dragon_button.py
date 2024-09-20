from abc import ABC, abstractmethod

from dragons_game.dragons.dragon import Dragon
from dragons_game.dragons.user_dragon import UserDragon
from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.text import Text
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.dragon_details import DragonDetails
from dragons_game.utils import custom_types
from dragons_game.utils.image_proportions import proportional_width
from dragons_game.utils.observers import Observer, ObserverClass


class DragonButton(Button, ObserverClass, ABC):
    @abstractmethod
    def __init__(self, dragon: UserDragon, size: tuple[float, float], position: custom_types.Position,
                 destination: tuple[float, float]):
        super().__init__(f'dragons_game/graphics/buttons/dragons/{dragon.rarity}.png', size, position, destination,
                         {'action': 'open_details', 'details': DragonDetails(dragon)})

        text_size = self.height / 16
        self.add_element('name', _Text(text_size, dragon.name, 'midtop', self.height / 5.45))

        dragon_image_height = self.height / 3.1
        dragon_image_width = proportional_width(dragon.image_path, dragon_image_height)
        self.add_element('dragon', Image(dragon.image_path, (dragon_image_width, dragon_image_height), 'center',
                                         (0, -self.height / 50)))

        progress_bar_size = (self.width / 2, self.height / 30)

        health_bar = _ProgressBar('health', dragon, progress_bar_size, -self.height / 7.4, '#dc0000')
        energy_bar = _ProgressBar('energy', dragon, progress_bar_size, health_bar.y_destination - self.height / 22.5,
                                  '#eaea00')
        experience_bar = _ProgressBar('experience', dragon, progress_bar_size,
                                      energy_bar.y_destination - self.height / 22.5, '#00da00')

        self.add_element('health', health_bar)
        self.add_element('energy', energy_bar)
        self.add_element('experience', experience_bar)

        self.add_element('level', _LevelText(dragon, text_size, experience_bar.y_destination - self.height / 22.5))


class _Text(Text):
    def __init__(self, size: float, text: str, position: custom_types.Position, y_destination: float):
        super().__init__('dragons_game/fonts/rurik.ttf', size, text, 'white', position, (0, y_destination), 1, 'black')


class _LevelText(_Text, Observer):
    def __init__(self, dragon: UserDragon, size: float, y_destination: float):
        super().__init__(size, '', 'midbottom', y_destination)

        self._dragon = dragon
        dragon.add_level_observer(self)

    def update_on_notify(self) -> None:
        self.text = f'Level {self._dragon.level}'


class _ProgressBar(Button, Observer):
    def __init__(self, name: str, dragon: Dragon, size: tuple[float, float], y_destination: float,
                 tooltip_color: custom_types.Color):
        tooltip = _ProgressTooltip(name, dragon, tooltip_color)

        super().__init__('dragons_game/graphics/progress_bars/background.png', size, 'midbottom', (0, y_destination),
                         hover_action={'action': 'show_tooltip', 'tooltip': tooltip})

        self._name = name
        self._dragon = dragon

        getattr(dragon, f"add_{name}_observer")(self)

    def update_on_notify(self) -> None:
        current_value = getattr(self._dragon, f'current_{self._name}')
        max_value = getattr(self._dragon, f'max_{self._name}')

        self.upsert_element('current', Image(f'dragons_game/graphics/progress_bars/{self._name}.png',
                                             (current_value / max_value * self.width, self.height), 'midleft', (0, 0)))


class _ProgressTooltip(Tooltip, Observer):
    def __init__(self, name: str, dragon: Dragon, color: custom_types.Color):
        super().__init__('bottomleft', (0, 0), color, 3, 'black', 200)

        self._name = name
        self._dragon = dragon

        self._text = Text('dragons_game/fonts/friz_quadrata.ttf', universal_sizes.MEDIUM / 1.5, '', 'white', 'center',
                          (0, 0), 1, 'black')
        self.add_element('text', self._text)

        getattr(dragon, f"add_{name}_observer")(self)

    def update_on_notify(self) -> None:
        current_value = getattr(self._dragon, f'current_{self._name}')
        max_value = getattr(self._dragon, f'max_{self._name}')

        self._text.text = f'{self._name.title()}: {current_value}/{max_value}'

        self.change_size(
            (self._text.width + 1.25 * universal_sizes.SMALL, self._text.height + 1.25 * universal_sizes.SMALL))
