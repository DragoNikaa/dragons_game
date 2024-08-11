from typing import Callable, Literal

import pygame

from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.dragons import dragons_section
from dragons_game.user import user
from dragons_game.utils import custom_types
from dragons_game.utils.image_proportions import calculate_proportional_width
from dragons_game.utils.observers import Observer

bottom_bar_section = Section((dragons_section.width - 4 * universal_sizes.LARGE, universal_sizes.LARGE), 'midbottom',
                             (dragons_section.rect.centerx, dragons_section.rect.bottom - universal_sizes.MEDIUM))
_section_height = bottom_bar_section.height


class _Text(Text):
    def __init__(self, height: float, text: str, position: custom_types.Position):
        super().__init__('dragons_game/fonts/pr_viking.ttf', height, text, 'white', position, (0, 0), 2, 'black')


_page_section = Section((4 * universal_sizes.LARGE, _section_height), 'center', (0, 0))
bottom_bar_section.add_element('page_section', _page_section)

_page_section.add_element('page_number', _Text(_section_height, '1', 'center'))


class _PageButton(Button):
    def __init__(self, image_path: str, position: custom_types.Position):
        super().__init__(image_path, (_section_height, _section_height), position, (0, 0))


_page_section.add_element('left_page', _PageButton('dragons_game/graphics/buttons/left_page.png', 'topleft'))
_page_section.add_element('right_page', _PageButton('dragons_game/graphics/buttons/right_page.png', 'topright'))

_sort_section = Section(
    ((bottom_bar_section.width - _page_section.width) / 2 - 2 * universal_sizes.LARGE, _section_height), 'topleft',
    (0, 0))
bottom_bar_section.add_element('sort_section', _sort_section)

_sort_text = _Text(_section_height / 1.5, 'Sorted by:', 'midleft')
_sort_section.add_element('text', _sort_text)


class _SortButton(Button, Observer):
    def __init__(self, key_or_reverse: Literal['key', 'reverse'], text: str, width: float,
                 position: custom_types.Position, x_destination: float, click_callable: Callable[[], None]):
        self._key_or_reverse = key_or_reverse

        super().__init__(f'dragons_game/graphics/buttons/sort_{key_or_reverse}.png', (width, _section_height), position,
                         (x_destination, 0), {'action': 'call', 'callable': click_callable})

        self._text = Text('dragons_game/fonts/rurik.ttf', _section_height / 1.5, text, 'white', 'center',
                          (0, self.height / 10), 2, 'black')
        self.add_element('label', self._text)

        if key_or_reverse == 'reverse':
            self._arrow_reverse = False
            self._rotate_reverse_arrow()

    def update_on_notify(self) -> None:
        if self._key_or_reverse == 'key':
            self._text.text = user.dragons_sort_key
        else:
            self._rotate_reverse_arrow()

    def _rotate_reverse_arrow(self) -> None:
        if self._arrow_reverse != user.dragons_sort_reverse:
            self._arrow_reverse = user.dragons_sort_reverse
            self._text.transform_image(pygame.transform.rotate, 180)

            if self._arrow_reverse:
                self._text.rect.move_ip(0, -self.height / 7)
            else:
                self._text.rect.move_ip(0, self.height / 7)


_key_button = _SortButton('key', user.dragons_sort_key, _sort_section.width / 2.5, 'midleft',
                          _sort_text.width + universal_sizes.SMALL, user.change_dragons_sort_key)
_reverse_button = _SortButton('reverse', 'T', 1.5 * _section_height, 'midright', 0, user.change_dragons_sort_reverse)

user.add_dragons_sort_key_observer(_key_button)
user.add_dragons_sort_reverse_observer(_reverse_button)

_sort_section.add_element('key', _key_button)
_sort_section.add_element('reverse', _reverse_button)

_rarities_section = Section(_sort_section.size, 'topright', (0, 0))
bottom_bar_section.add_element('rarities_section', _rarities_section)

_rarities_text = _Text(_section_height / 1.5, 'Rarities:', 'midleft')
_rarities_section.add_element('text', _rarities_text)


class _RarityButton(Button):
    def __init__(self, name: str, tooltip_color: custom_types.Color, previous_button: '_RarityButton | None' = None):
        self._name = name
        image_path = f'dragons_game/graphics/buttons/rarities/{name}.png'

        height = _section_height / 1.1
        width = calculate_proportional_width(image_path, height)

        if previous_button is None:
            x = _rarities_text.x_destination + _rarities_text.width + universal_sizes.SMALL
            self._stars_number = 1
        else:
            x = previous_button.x_destination + previous_button.width
            self._stars_number = previous_button._stars_number + 1

        tooltip = self._tooltip(name, tooltip_color)

        super().__init__(image_path, (width, height), 'midleft', (x, 0),
                         hover_action={'action': 'show_tooltip', 'tooltip': tooltip})

    def _tooltip(self, name: str, color: custom_types.Color) -> Tooltip:
        stars = [self._star(star_number) for star_number in range(1, 7)]

        text = Text('dragons_game/fonts/friz_quadrata.ttf', universal_sizes.MEDIUM / 1.5, f'{name.title()}', 'white',
                    'midleft', (stars[5].rect.right + universal_sizes.SMALL / 2, 0), 1, 'black')

        tooltip = Tooltip('midbottom', (
            1.5 * universal_sizes.SMALL + 6 * stars[0].width + text.width, text.height + universal_sizes.SMALL), color,
                          3, 'black', 200)

        for star_index, star in enumerate(stars):
            tooltip.add_element(f'star_{star_index}', star)
        tooltip.add_element('text', text)

        return tooltip

    def _star(self, star_number: int) -> Image:
        if star_number <= self._stars_number:
            color = 'gold'
        else:
            color = 'grey'

        width = universal_sizes.MEDIUM / 1.75
        x = universal_sizes.SMALL / 2 + (star_number - 1) * width

        return Image(f'dragons_game/graphics/icons/{color}_star.png', (width, width), 'midleft', (x, 0))

    @property
    def name(self) -> str:
        return self._name


_common = _RarityButton('common', '#985a1f')
_uncommon = _RarityButton('uncommon', '#08de31', _common)
_rare = _RarityButton('rare', '#016ece', _uncommon)
_epic = _RarityButton('epic', '#fdd53d', _rare)
_legendary = _RarityButton('legendary', '#f31e17', _epic)
_mythical = _RarityButton('mythical', '#d338de', _legendary)

_all_buttons = (_common, _uncommon, _rare, _epic, _legendary, _mythical)
_button_widths_sum = sum([button.width for button in _all_buttons])
_space_between_buttons = ((_rarities_section.width - _rarities_text.width - universal_sizes.SMALL - _button_widths_sum)
                          / (len(_all_buttons) - 1))

for button_index, button in enumerate(_all_buttons):
    button.destination = (round(button.x_destination + button_index * _space_between_buttons), button.y_destination)
    _rarities_section.add_element(button.name, button)
