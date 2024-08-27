from abc import ABC, abstractmethod

from dragons_game.dragons.dragon import Dragon
from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.text import Text
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.dragon_details import DragonDetails
from dragons_game.utils import custom_types
from dragons_game.utils.image_proportions import proportional_width
from dragons_game.utils.observers import ObserverClass


class DragonButton(Button, ObserverClass, ABC):
    @abstractmethod
    def __init__(self, dragon: Dragon, size: tuple[float, float], position: custom_types.Position,
                 destination: tuple[float, float]):
        super().__init__(f'dragons_game/graphics/buttons/dragons/{dragon.rarity}.png', size, position, destination,
                         {'action': 'open_details', 'details': DragonDetails(dragon)})

        self._add_text('name', dragon.name, 'midtop', self.height / 5.45)

        dragon_image_height = self.height / 3.1
        dragon_image_width = proportional_width(dragon.image_path, dragon_image_height)
        self.add_element('dragon', Image(dragon.image_path, (dragon_image_width, dragon_image_height), 'center',
                                         (0, -self.height / 50)))

        health_bar = self._add_progress_bar('health', -self.height / 7.4,
                                            'dragons_game/graphics/buttons/health_bar.png', dragon.current_health,
                                            dragon.max_health, '#dc0000')
        energy_bar = self._add_progress_bar('energy', health_bar.y_destination - self.height / 22.5,
                                            'dragons_game/graphics/buttons/energy_bar.png', dragon.current_energy,
                                            dragon.max_energy, '#eaea00')
        experience_bar = self._add_progress_bar('experience', energy_bar.y_destination - self.height / 22.5,
                                                'dragons_game/graphics/buttons/experience_bar.png',
                                                dragon.current_experience, dragon.experience_to_next_level, '#00da00')

        self._add_text('level', f'Level {dragon.level}', 'midbottom', experience_bar.y_destination - self.height / 22.5)

    def _add_text(self, name: str, text: str, position: custom_types.Position, y_destination: float) -> None:
        self.add_element(name, Text('dragons_game/fonts/rurik.ttf', self.height / 16, text, 'white', position,
                                    (0, y_destination), 1, 'black'))

    def _add_progress_bar(self, name: str, y_destination: float, current_image_path: str, current_value: float,
                          max_value: float, tooltip_color: custom_types.Color) -> Button:
        tooltip = self._tooltip(name, current_value, max_value, tooltip_color)

        progress_bar = Button('dragons_game/graphics/buttons/progress_bar.png', (self.width / 2, self.height / 30),
                              'midbottom', (0, y_destination),
                              hover_action={'action': 'show_tooltip', 'tooltip': tooltip})

        progress_bar.add_element('current', Image(current_image_path,
                                                  (current_value / max_value * progress_bar.width, progress_bar.height),
                                                  'midleft', (0, 0)))

        self.add_element(name, progress_bar)
        return progress_bar

    @staticmethod
    def _tooltip(name: str, current_value: float, max_value: float, color: custom_types.Color) -> Tooltip:
        text = Text('dragons_game/fonts/friz_quadrata.ttf', universal_sizes.MEDIUM / 1.5,
                    f'{name.title()}: {current_value}/{max_value}', 'white', 'center', (0, 0), 1, 'black')

        tooltip = Tooltip('bottomleft', (text.width + universal_sizes.SMALL, text.height + universal_sizes.SMALL),
                          color, 3, 'black', 200)

        tooltip.add_element('text', text)
        return tooltip
