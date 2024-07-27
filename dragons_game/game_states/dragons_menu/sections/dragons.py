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
    (team_section.rect.right, title_bar_section.rect.bottom),
    'dragons_game/graphics/backgrounds/dragons_menu/dragons.png')


class _DragonButton(Button):
    _WIDTH = (dragons_section.width - universal_sizes.LARGE) / 5 - universal_sizes.LARGE
    _HEIGHT = (dragons_section.height - 2 * universal_sizes.LARGE) / 2 - universal_sizes.LARGE
    _X_OFFSETS = [x for x in
                  range(int(universal_sizes.LARGE), int(dragons_section.width), int(_WIDTH + universal_sizes.LARGE))]
    _ROW_1_Y_OFFSET = universal_sizes.LARGE
    _ROW_2_Y_OFFSET = 2 * universal_sizes.LARGE + _HEIGHT

    def __init__(self, dragon_index: int, dragon: Dragon):
        dragon_index %= 10
        x_offset = self._X_OFFSETS[dragon_index % 5]
        if dragon_index <= 4:
            y_offset = self._ROW_1_Y_OFFSET
        else:
            y_offset = self._ROW_2_Y_OFFSET

        super().__init__(dragons_section, f'dragons_game/graphics/buttons/dragons/{dragon.dragon_class.value}.png',
                         (self._WIDTH, self._HEIGHT), 'topleft', (x_offset, y_offset))

        self._add_text('name', dragon.name, 'midtop', self._HEIGHT / 5.45)

        dragon_image_height = self._HEIGHT / 3.1
        dragon_image_width = calculate_proportional_width(dragon.image_path, dragon_image_height)
        self.add_image('dragon', Image(self, dragon.image_path, (dragon_image_width, dragon_image_height), 'center',
                                       (0, -self._HEIGHT / 50)))

        tooltip_transparency = 200
        health_bar = self._add_progress_bar('health', -self._HEIGHT / 7.4,
                                            'dragons_game/graphics/buttons/health_bar.png', dragon.current_health,
                                            dragon.max_health, (255, 0, 0, tooltip_transparency))
        energy_bar = self._add_progress_bar('energy', health_bar.y_offset - universal_sizes.SMALL,
                                            'dragons_game/graphics/buttons/energy_bar.png', dragon.current_energy,
                                            dragon.max_energy, (255, 255, 0, tooltip_transparency))
        experience_bar = self._add_progress_bar('experience', energy_bar.y_offset - universal_sizes.SMALL,
                                                'dragons_game/graphics/buttons/experience_bar.png',
                                                dragon.current_experience, dragon.experience_to_next_level,
                                                (0, 255, 0, tooltip_transparency))

        self._add_text('level', f'Level {dragon.level}', 'midbottom', experience_bar.y_offset - universal_sizes.SMALL)

    def _add_text(self, name: str, text: str, position: custom_types.Position, y_offset: float) -> None:
        self.add_text(name, Text(self, 'dragons_game/fonts/rurik.ttf', int(self._HEIGHT / 16), text, 'white', position,
                                 (0, y_offset), 1, 'black'))

    def _add_progress_bar(self, name: str, y_offset: float, current_image_path: str,
                          current_value: float, max_value: float, tooltip_fill_color: custom_types.Color) -> Button:
        tooltip = self._create_tooltip(name, current_value, max_value, tooltip_fill_color)
        progress_bar = Button(self, 'dragons_game/graphics/buttons/progress_bar.png',
                              (self._WIDTH / 2, self._HEIGHT / 30), 'midbottom', (0, y_offset),
                              hover_action={'action': 'show_tooltip', 'tooltip': tooltip})
        progress_bar.add_image('current', Image(progress_bar, current_image_path,
                                                (current_value / max_value * progress_bar.width, progress_bar.height),
                                                'midleft', (0, 0)))

        self.add_button(name, progress_bar)
        return progress_bar

    def _create_tooltip(self, name: str, current_value: float, max_value: float,
                        tooltip_fill_color: custom_types.Color) -> Tooltip:
        tooltip = Tooltip('bottomleft', fill_color=tooltip_fill_color)
        text = Text(tooltip, 'dragons_game/fonts/friz_quadrata.ttf', int(self._HEIGHT / 18),
                    f'{name.title()}: {current_value}/{max_value}', 'white', 'center', (0, 0), 1, 'black')
        tooltip.change_size((text.width + universal_sizes.SMALL, text.height + universal_sizes.SMALL))
        tooltip.add_text('text', text)
        return tooltip


user_dragons = [toothless for _ in range(10)]

for dragon_index, dragon in enumerate(user_dragons):
    dragons_section.add_button(f'dragon_{dragon_index}', _DragonButton(dragon_index, dragon))
