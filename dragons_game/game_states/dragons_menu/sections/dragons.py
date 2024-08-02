from dragons_game.elements.tooltip import Tooltip
from dragons_game.utils import custom_types
from dragons_game.game_states.common import universal_sizes
from dragons_game.dragons.database.dragons import toothless
from dragons_game.dragons.dragon import Dragon
from dragons_game.elements.button import Button
from dragons_game.elements.section import Section
from dragons_game.elements.image import Image
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.dragons_menu.sections.team import team_section
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section
from dragons_game.utils.image_proportions import calculate_proportional_width

dragons_section = Section(
    (GameConfig.WINDOW_WIDTH - team_section.width, GameConfig.WINDOW_HEIGHT - title_bar_section.height), 'topleft',
    (team_section.rect.right, title_bar_section.rect.bottom))

dragons_section.add_element('background',
                            Image('dragons_game/graphics/backgrounds/dragons_menu/dragons.png', dragons_section.size,
                                  'topleft', (0, 0)))


class _DragonButton(Button):
    _WIDTH = (dragons_section.width - universal_sizes.LARGE) / 5 - universal_sizes.LARGE
    _HEIGHT = (dragons_section.height - 2 * universal_sizes.LARGE) / 2 - universal_sizes.LARGE
    _X_DESTINATIONS = [x for x in range(int(universal_sizes.LARGE), int(dragons_section.width),
                                        int(_WIDTH + universal_sizes.LARGE))]
    _ROW_1_Y_DESTINATION = universal_sizes.LARGE
    _ROW_2_Y_DESTINATION = 2 * universal_sizes.LARGE + _HEIGHT

    def __init__(self, dragon_index: int, dragon: Dragon):
        dragon_index %= 10
        x_destination = self._X_DESTINATIONS[dragon_index % 5]
        if dragon_index <= 4:
            y_destination = self._ROW_1_Y_DESTINATION
        else:
            y_destination = self._ROW_2_Y_DESTINATION

        super().__init__(f'dragons_game/graphics/buttons/dragons/{dragon.dragon_class.value}.png',
                         (self._WIDTH, self._HEIGHT), 'topleft', (x_destination, y_destination))

        self._add_text('name', dragon.name, 'midtop', self._HEIGHT / 5.45)

        dragon_image_height = self._HEIGHT / 3.1
        dragon_image_width = calculate_proportional_width(dragon.image_path, dragon_image_height)
        self.add_element('dragon', Image(dragon.image_path, (dragon_image_width, dragon_image_height), 'center',
                                         (0, -self._HEIGHT / 50)))

        health_bar = self._add_progress_bar('health', -self._HEIGHT / 7.4,
                                            'dragons_game/graphics/buttons/health_bar.png', dragon.current_health,
                                            dragon.max_health, 'red')
        energy_bar = self._add_progress_bar('energy', health_bar.y_destination - universal_sizes.SMALL,
                                            'dragons_game/graphics/buttons/energy_bar.png', dragon.current_energy,
                                            dragon.max_energy, 'yellow')
        experience_bar = self._add_progress_bar('experience', energy_bar.y_destination - universal_sizes.SMALL,
                                                'dragons_game/graphics/buttons/experience_bar.png',
                                                dragon.current_experience, dragon.experience_to_next_level, 'green')

        self._add_text('level', f'Level {dragon.level}', 'midbottom',
                       experience_bar.y_destination - universal_sizes.SMALL)

    def _add_text(self, name: str, text: str, position: custom_types.Position, y_destination: float) -> None:
        self.add_element(name, Text('dragons_game/fonts/rurik.ttf', self._HEIGHT / 16, text, 'white', position,
                                    (0, y_destination), 1, 'black'))

    def _add_progress_bar(self, name: str, y_destination: float, current_image_path: str, current_value: float,
                          max_value: float, tooltip_color: custom_types.Color) -> Button:
        tooltip = self._create_tooltip(name, current_value, max_value, tooltip_color)

        progress_bar = Button('dragons_game/graphics/buttons/progress_bar.png', (self._WIDTH / 2, self._HEIGHT / 30),
                              'midbottom', (0, y_destination),
                              hover_action={'action': 'show_tooltip', 'tooltip': tooltip})

        progress_bar.add_element('current', Image(current_image_path,
                                                  (current_value / max_value * progress_bar.width, progress_bar.height),
                                                  'midleft', (0, 0)))

        self.add_element(name, progress_bar)
        return progress_bar

    def _create_tooltip(self, name: str, current_value: float, max_value: float, color: custom_types.Color) -> Tooltip:
        text = Text('dragons_game/fonts/friz_quadrata.ttf', self._HEIGHT / 18,
                    f'{name.title()}: {current_value}/{max_value}', 'white', 'center', (0, 0), 1, 'black')

        tooltip = Tooltip('bottomleft', (text.width + universal_sizes.SMALL, text.height + universal_sizes.SMALL),
                          color, 3, 'black', 200)

        tooltip.add_element('text', text)
        return tooltip


user_dragons = [toothless for _ in range(10)]

for dragon_index, dragon in enumerate(user_dragons):
    dragons_section.add_element(f'dragon_{dragon_index}', _DragonButton(dragon_index, dragon))
