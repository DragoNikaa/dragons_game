from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.dragons import dragons_section
from dragons_game.game_states.dragons_menu.sections.page import page_section
from dragons_game.utils import custom_types
from dragons_game.utils.image_proportions import calculate_proportional_width


class _DragonClassButton(Button):
    def __init__(self, name: str, tooltip_color: custom_types.Color,
                 previous_button: '_DragonClassButton | None' = None):
        image_path = f'dragons_game/graphics/buttons/dragon_classes/{name}.png'

        height = page_section.height
        width = calculate_proportional_width(image_path, height)

        if previous_button is None:
            x = 0
            self._stars_number = 1
        else:
            x = previous_button.x_destination + previous_button.width + universal_sizes.MEDIUM
            self._stars_number = previous_button._stars_number + 1

        tooltip = self._create_tooltip(name, tooltip_color)

        super().__init__(image_path, (width, height), 'topleft', (x, 0),
                         hover_action={'action': 'show_tooltip', 'tooltip': tooltip})

    def _create_tooltip(self, name: str, color: custom_types.Color) -> Tooltip:
        stars = [self._create_star(star_number) for star_number in range(1, 7)]

        text = Text('dragons_game/fonts/friz_quadrata.ttf', universal_sizes.MEDIUM / 1.5, f'{name.title()}', 'white',
                    'midleft', (stars[5].rect.right + universal_sizes.SMALL / 2, 0), 1, 'black')

        tooltip = Tooltip('midbottom', (
            1.5 * universal_sizes.SMALL + 6 * stars[0].width + text.width, text.height + universal_sizes.SMALL), color,
                          3, 'black', 200)

        for star_index, star in enumerate(stars):
            tooltip.add_element(f'star_{star_index}', star)
        tooltip.add_element('text', text)

        return tooltip

    def _create_star(self, star_number: int) -> Image:
        if star_number <= self._stars_number:
            color = 'gold'
        else:
            color = 'grey'

        width = universal_sizes.MEDIUM / 1.75
        x = universal_sizes.SMALL / 2 + (star_number - 1) * width

        return Image(f'dragons_game/graphics/icons/{color}_star.png', (width, width), 'midleft', (x, 0))


_common = _DragonClassButton('common', '#985a1f')
_uncommon = _DragonClassButton('uncommon', '#08de31', _common)
_rare = _DragonClassButton('rare', '#016ece', _uncommon)
_epic = _DragonClassButton('epic', '#fdd53d', _rare)
_legendary = _DragonClassButton('legendary', '#f31e17', _epic)
_mythical = _DragonClassButton('mythical', '#d338de', _legendary)

section_width = sum([button.width + universal_sizes.MEDIUM for button in
                     (_common, _uncommon, _rare, _epic, _legendary, _mythical)]) - universal_sizes.MEDIUM
dragon_classes_section = Section((section_width, _common.height), 'center', (
    ((page_section.rect.right + dragons_section.rect.right) / 2, page_section.rect.centery)))

dragon_classes_section.add_element('common', _common)
dragon_classes_section.add_element('uncommon', _uncommon)
dragon_classes_section.add_element('rare', _rare)
dragon_classes_section.add_element('epic', _epic)
dragon_classes_section.add_element('legendary', _legendary)
dragon_classes_section.add_element('mythical', _mythical)
