from dragons_game.elements.button import Button
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.dragons import dragons_section
from dragons_game.utils import custom_types

page_section = Section((4 * universal_sizes.LARGE, universal_sizes.LARGE), 'midbottom',
                       (dragons_section.rect.centerx, dragons_section.rect.bottom - universal_sizes.MEDIUM))

page_section.add_element('page_number',
                         Text('dragons_game/fonts/pr_viking.ttf', page_section.height, '1', 'white', 'center', (0, 0),
                              3, 'black'))


class _PageButton(Button):
    def __init__(self, image_path: str, position: custom_types.Position):
        super().__init__(image_path, (page_section.height, page_section.height), position, (0, 0))


page_section.add_element('left_page', _PageButton('dragons_game/graphics/buttons/left_page.png', 'topleft'))
page_section.add_element('right_page', _PageButton('dragons_game/graphics/buttons/right_page.png', 'topright'))
