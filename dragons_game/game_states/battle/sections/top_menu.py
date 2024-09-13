from typing import Sequence

import pygame

from dragons_game.dragons.attack import Attack, AttackType
from dragons_game.dragons.dragon import Dragon
from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.multiline_text import MultilineTextFixedTextSize
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.battle.battle import battle
from dragons_game.game_states.battle.sections.title_bar import title_bar_section
from dragons_game.game_states.common import universal_sizes
from dragons_game.user import user
from dragons_game.utils import custom_types
from dragons_game.utils.observers import Observer

top_menu_section = Section((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT / 4.5), 'topleft',
                           (0, title_bar_section.rect.bottom))

_background = Image('dragons_game/graphics/backgrounds/dragons_menu/dragons.png', top_menu_section.size, 'topleft',
                    (0, 0))
_background.image.set_alpha(128)
top_menu_section.add_element('background', _background)

_border_size = top_menu_section.height / 25
top_menu_section.add_element('border', Image('dragons_game/graphics/backgrounds/bottom_border.png',
                                             (top_menu_section.width, _border_size), 'topleft',
                                             (0, top_menu_section.height)))

_section_width = GameConfig.WINDOW_WIDTH / 3.5


def _text(text: str, position: custom_types.Position, destination: tuple[float, float],
          size: float = top_menu_section.height / 8) -> Text:
    return Text('dragons_game/fonts/friz_quadrata.ttf', size, text, 'white', position, destination, 1, 'black')


class _HealthBarsSection(Section):
    def __init__(self, dragons: Sequence[Dragon], position: custom_types.Position, x_destination: float,
                 name_position: custom_types.Position, bar_position: custom_types.Position):
        super().__init__((_section_width, top_menu_section.height - 2 * universal_sizes.MEDIUM), position,
                         (x_destination, title_bar_section.rect.bottom + universal_sizes.MEDIUM))

        bar_height = (self.height - 2 * universal_sizes.SMALL) / 3

        for dragon_index, dragon in enumerate(dragons):
            y_destination = dragon_index * (bar_height + universal_sizes.SMALL)

            self.add_element(f'dragon_{dragon_index}_name', _text(f'{dragon.name}', name_position, (0, y_destination)))

            self.add_element(f'dragon_{dragon_index}_health',
                             _HealthBar(dragon, (0.6 * self.width, bar_height), bar_position, y_destination))


class _HealthBar(Section, Observer):
    def __init__(self, dragon: Dragon, size: tuple[float, float], position: custom_types.Position,
                 y_destination: float):
        super().__init__(size, position, (0, y_destination))

        self._dragon = dragon

        self.add_element('background',
                         Image('dragons_game/graphics/progress_bars/background.png', self.size, 'topleft', (0, 0)))

        dragon.add_health_observer(self)

    def update_on_notify(self) -> None:
        self.upsert_element('current', Image(f'dragons_game/graphics/progress_bars/health.png', (
            self._dragon.current_health / self._dragon.max_health * self.width, self.height), 'topleft', (0, 0)))

        self.upsert_element('numbers',
                            _text(f'{self._dragon.current_health}/{self._dragon.max_health}', 'center', (0, 0),
                                  0.8 * self.height))


class UserHealthBarsSection(_HealthBarsSection):
    X_DESTINATION = universal_sizes.MEDIUM

    def __init__(self) -> None:
        super().__init__(user.team_dragons, 'topleft', self.X_DESTINATION, 'topleft', 'topright')


class EnemyHealthBarsSection(_HealthBarsSection):
    def __init__(self) -> None:
        super().__init__(user.current_level.enemy_dragons, 'topright', GameConfig.WINDOW_WIDTH - universal_sizes.MEDIUM,
                         'topright', 'topleft')


class _AttacksSection(Section, Observer):
    def __init__(self) -> None:
        super().__init__((_section_width, 0.48 * top_menu_section.height), 'midtop',
                         (GameConfig.WINDOW_WIDTH / 2, title_bar_section.rect.bottom + 1.5 * universal_sizes.SMALL))

        icon_size = self.height, self.height

        special_attack = Button('dragons_game/graphics/icons/attacks/special.png', icon_size, 'topright', (0, 0),
                                {'action': 'call', 'callable': self._change_selected_attack,
                                 'kwargs': {'attack_type': AttackType.SPECIAL}})
        self.add_element('special_attack', special_attack)

        self.add_element('basic_attack', Button('dragons_game/graphics/icons/attacks/basic.png', icon_size, 'topright',
                                                (-special_attack.width - universal_sizes.SMALL, 0),
                                                {'action': 'call', 'callable': self._change_selected_attack,
                                                 'kwargs': {'attack_type': AttackType.BASIC}}))

        self._attack_name = _text('', 'topleft', (0, 0))
        self._turn = _text('', 'midleft', (0, 0))
        self._cost = _text('', 'bottomleft', (0, 0))

        self.add_element('turn', self._turn)

        self._selected_attack = battle.current_user_dragon.special_attack
        self._change_selected_attack(AttackType.BASIC)

        battle.add_current_dragon_observer(self)

    def _change_selected_attack(self, attack_type: AttackType) -> None:
        if battle.user_turn and attack_type is not self._selected_attack.type:
            if attack_type is AttackType.SPECIAL and points_bar.points < attack_type.cost:
                self.get_button('special_attack').add_onetime_hover_action({'action': 'show_tooltip',
                                                                            'tooltip': self._tooltip(
                                                                                f'You need {attack_type.cost} points to use {attack_type.value} attack!',
                                                                                '#dc0000')})
                return

            unselected_button = self.get_button(f'{self._selected_attack.type.value}_attack')
            unselected_button.add_temporary_image(pygame.transform.grayscale(unselected_button.image_copy))

            selected_attack = f'{attack_type.value}_attack'
            self._selected_attack = getattr(battle.current_user_dragon, selected_attack)
            self.get_button(selected_attack).remove_temporary_image()

            self._update_attack_and_cost()

    @staticmethod
    def _tooltip(text: str, color: custom_types.Color) -> Tooltip:
        text_element = MultilineTextFixedTextSize(GameConfig.WINDOW_WIDTH / 4, 'topleft',
                                                  (0.75 * universal_sizes.SMALL, 0.75 * universal_sizes.SMALL),
                                                  'dragons_game/fonts/friz_quadrata.ttf', universal_sizes.MEDIUM / 1.5,
                                                  text, 'white', 1, 'black')

        tooltip = Tooltip('midbottom', (
            text_element.width + 1.5 * universal_sizes.SMALL, text_element.height + 1.5 * universal_sizes.SMALL), color,
                          3, 'black', 200)

        tooltip.add_element('text', text_element)
        return tooltip

    def _update_attack_and_cost(self) -> None:
        self._attack_name.text = self._selected_attack.name
        self._cost.text = f'Cost: {self._selected_attack.cost} points'

    def update_on_notify(self) -> None:
        if battle.user_turn:
            dragon = battle.current_user_dragon

            self._change_selected_attack(AttackType.BASIC)

            self._turn.text = f'Turn: {dragon.name}'
            self._update_attack_and_cost()

            self.upsert_element('attack_name', self._attack_name)
            self.upsert_element('cost', self._cost)

            self.get_button(f'{self._selected_attack.type.value}_attack').remove_temporary_image()

            self.get_button('basic_attack').set_hover_action(
                {'action': 'show_tooltip', 'tooltip': self._tooltip(dragon.basic_attack.description, '#976eec')})
            self.get_button('special_attack').set_hover_action(
                {'action': 'show_tooltip', 'tooltip': self._tooltip(dragon.special_attack.description, '#b581a3')})

        else:
            self._turn.text = f'Turn: Enemy'

            self.remove_element('attack_name')
            self.remove_element('cost')

            selected_button = self.get_button(f'{self._selected_attack.type.value}_attack')
            selected_button.add_temporary_image(pygame.transform.grayscale(selected_button.image_copy))

    def clean_up(self) -> None:
        self._change_selected_attack(AttackType.BASIC)
        self.update_on_notify()

    @property
    def selected_attack(self) -> Attack:
        return self._selected_attack


attacks_section = _AttacksSection()


class _PointsBar(Section):
    def __init__(self) -> None:
        super().__init__(
            (_section_width / 1.5, top_menu_section.height - attacks_section.height - 4.5 * universal_sizes.SMALL),
            'midbottom', (GameConfig.WINDOW_WIDTH / 2,
                          title_bar_section.rect.bottom + top_menu_section.height - 1.5 * universal_sizes.SMALL))

        self.add_element('background',
                         Image('dragons_game/graphics/progress_bars/points//background.png', self.size, 'topleft',
                               (0, 0)))

        self._color_points = []
        x_destination = self.width / 23

        for point_index in range(5):
            args: tuple[tuple[float, float], custom_types.Position, tuple[float, float]] = (
                (self.width / 5.95, self.height / 2.1), 'midleft', (x_destination, 0))

            grey_point = Image('dragons_game/graphics/progress_bars/points/grey_point.png', *args)
            self.add_element(f'grey_point_{point_index}', grey_point)

            self._color_points.append(
                Image(f'dragons_game/graphics/progress_bars/points/color_points/{point_index}.png', *args))

            x_destination += grey_point.width + self.width / 60

        self._points = 0
        self.add_point()

    def add_point(self) -> None:
        if self._points < 5:
            self.add_element(f'color_point_{self._points}', self._color_points[self._points])
            self._points += 1

    def remove_points(self, value: int) -> None:
        self._points -= value
        for point_index in range(self._points, self._points + value):
            self.remove_element(f'color_point_{point_index}')

    def clean_up(self) -> None:
        if self._points == 0:
            self.add_point()
            return

        for point_index in range(1, self._points):
            self.remove_element(f'color_point_{point_index}')
        self._points = 1

    @property
    def points(self) -> int:
        return self._points


points_bar = _PointsBar()

_divider_x_destination = ((GameConfig.WINDOW_WIDTH - _section_width) / 2 - UserHealthBarsSection.X_DESTINATION) / 2

for divider_side, x in zip(('left', 'right'), (-_divider_x_destination, _divider_x_destination)):
    top_menu_section.add_element(f'{divider_side}_divider', Image('dragons_game/graphics/backgrounds/side_border.png',
                                                                  (_border_size, top_menu_section.height), 'midtop',
                                                                  (x, 0)))
