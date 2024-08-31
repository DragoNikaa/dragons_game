import pygame

from dragons_game.dragons.attack import AttackType
from dragons_game.dragons.dragon import Dragon
from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.battle.sections.title_bar import title_bar_section
from dragons_game.game_states.common import universal_sizes
from dragons_game.user import user
from dragons_game.utils import custom_types

top_menu_section = Section((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT / 4.5), 'topleft',
                           (0, title_bar_section.rect.bottom))

_background = Image('dragons_game/graphics/backgrounds/dragons_menu/dragons.png', top_menu_section.size, 'topleft',
                    (0, 0))
_background.image.set_alpha(128)
top_menu_section.add_element('background', _background)

top_menu_section.add_element('border', Image('dragons_game/graphics/backgrounds/bottom_border.png',
                                             (top_menu_section.width, top_menu_section.height / 25), 'topleft',
                                             (0, top_menu_section.height)))


def _text(text: str, position: custom_types.Position, destination: tuple[float, float],
          size: float = top_menu_section.height / 8) -> Text:
    return Text('dragons_game/fonts/friz_quadrata.ttf', size, text, 'white', position, destination, 1, 'black')


class HealthBarsSection(Section):
    def __init__(self) -> None:
        super().__init__((GameConfig.WINDOW_WIDTH / 3.5, top_menu_section.height - 2 * universal_sizes.MEDIUM),
                         'topleft', (universal_sizes.MEDIUM, title_bar_section.rect.bottom + universal_sizes.MEDIUM))

        self._bar_height = (self.height - 2 * universal_sizes.SMALL) / 3

        for dragon_index, dragon in enumerate(user.team_dragons):
            y_destination = dragon_index * (self._bar_height + universal_sizes.SMALL)

            self.add_element(f'dragon_{dragon_index}_name', _text(f'{dragon.name}', 'topleft', (0, y_destination)))
            self._add_progress_bar(dragon_index, dragon, y_destination)

    def _add_progress_bar(self, dragon_index: int, dragon: Dragon, y_destination: float) -> None:
        progress_bar = Section((0.6 * self.width, self._bar_height), 'topright', (0, y_destination))

        progress_bar.add_element('background',
                                 Image('dragons_game/graphics/progress_bars/background.png', progress_bar.size,
                                       'topleft', (0, 0)))

        progress_bar.add_element(f'current', Image(f'dragons_game/graphics/progress_bars/health.png', (
            dragon.current_health / dragon.max_health * progress_bar.width, progress_bar.height), 'topleft', (0, 0)))

        progress_bar.add_element('numbers', _text(f'{dragon.current_health}/{dragon.max_health}', 'center', (0, 0),
                                                  0.8 * self._bar_height))

        self.add_element(f'dragon_{dragon_index}_health', progress_bar)


class AttacksSection(Section):
    def __init__(self) -> None:
        super().__init__((GameConfig.WINDOW_WIDTH / 3.5, 0.63 * (top_menu_section.height - 2 * universal_sizes.MEDIUM)),
                         'midtop',
                         (GameConfig.WINDOW_WIDTH / 2, title_bar_section.rect.bottom + universal_sizes.MEDIUM))

        icon_size = self.height, self.height

        special_attack = Button('dragons_game/graphics/icons/attacks/special.png', icon_size, 'topright', (0, 0),
                                {'action': 'call', 'callable': self._change_selected_attack,
                                 'kwargs': {'attack_type': AttackType.SPECIAL}})
        self.add_element('special_attack', special_attack)

        self.add_element('basic_attack', Button('dragons_game/graphics/icons/attacks/basic.png', icon_size, 'topright',
                                                (-special_attack.width - universal_sizes.SMALL, 0),
                                                {'action': 'call', 'callable': self._change_selected_attack,
                                                 'kwargs': {'attack_type': AttackType.BASIC}}))

        self._current_dragon = user.team_dragons[0]
        self._selected_attack = self._current_dragon.special_attack
        self._change_selected_attack(AttackType.BASIC)

    def _change_selected_attack(self, attack_type: AttackType) -> None:
        if attack_type is not self._selected_attack.type:
            unselected_button = self.get_button(f'{self._selected_attack.type.value}_attack')
            unselected_button.add_temporary_image(pygame.transform.grayscale(unselected_button.image_copy))

            selected_attack = f'{attack_type.value}_attack'
            self._selected_attack = getattr(self._current_dragon, selected_attack)
            self.get_button(selected_attack).remove_temporary_image()

            self._upsert_attack_details()

    def _upsert_attack_details(self) -> None:
        self.upsert_element('dragon_name', _text(self._current_dragon.name, 'topleft', (0, 0)))
        self.upsert_element('attack_name', _text(self._selected_attack.name, 'midleft', (0, 0)))
        self.upsert_element('cost', _text(f'Cost: {self._selected_attack.cost} points', 'bottomleft', (0, 0)))


class PointsBar(Section):
    def __init__(self) -> None:
        super().__init__((GameConfig.WINDOW_WIDTH / 5,
                          0.37 * (top_menu_section.height - 2 * universal_sizes.MEDIUM) - universal_sizes.SMALL),
                         'midbottom', (GameConfig.WINDOW_WIDTH / 2,
                                       title_bar_section.rect.bottom + top_menu_section.height - universal_sizes.MEDIUM))

        self.add_element('background',
                         Image('dragons_game/graphics/progress_bars/points//background.png', self.size, 'topleft',
                               (0, 0)))

        self._color_points = []
        x_destination = self.width / 20

        for point_index in range(5):
            args: tuple[tuple[float, float], custom_types.Position, tuple[float, float]] = (
                (self.width / 6.1, self.height / 2.1), 'midleft', (x_destination, 0))

            grey_point = Image('dragons_game/graphics/progress_bars/points/grey_point.png', *args)
            self.add_element(f'grey_point_{point_index}', grey_point)

            self._color_points.append(
                Image(f'dragons_game/graphics/progress_bars/points/color_points/{point_index}.png', *args))

            x_destination += grey_point.width + self.width / 50
