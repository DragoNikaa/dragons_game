from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.dragons import dragons_section
from dragons_game.game_states.dragons_menu.sections.page import page_section
from dragons_game.game_states.dragons_menu.sections.sort import sort_section
from dragons_game.utils import custom_types
from dragons_game.utils.image_proportions import calculate_proportional_width

rarities_section = Section(sort_section.size, 'center',
                           ((page_section.rect.right + dragons_section.rect.right) / 2, page_section.rect.centery))

_text = Text('dragons_game/fonts/pr_viking.ttf', sort_section.height / 1.5, 'Rarities:', 'white', 'midleft', (0, 0), 3,
             'black')
rarities_section.add_element('text', _text)


class _RarityButton(Button):
    def __init__(self, name: str, tooltip_color: custom_types.Color, previous_button: '_RarityButton | None' = None):
        self._name = name
        image_path = f'dragons_game/graphics/buttons/rarities/{name}.png'

        height = rarities_section.height / 1.1
        width = calculate_proportional_width(image_path, height)

        if previous_button is None:
            x = _text.x_destination + _text.width + universal_sizes.SMALL
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
_space_between_buttons = (rarities_section.width - _text.width - universal_sizes.SMALL - _button_widths_sum) / (
        len(_all_buttons) - 1)

for button_index, button in enumerate(_all_buttons):
    button.destination = (round(button.x_destination + button_index * _space_between_buttons), button.y_destination)
    rarities_section.add_element(button.name, button)
