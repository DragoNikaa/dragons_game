from dragons_game.utils import custom_types
from dragons_game.game_states.common import universal_sizes
from dragons_game.elements.button import Button
from dragons_game.elements.elements_section import ElementsSection
from dragons_game.elements.text import Text
from dragons_game.game_states.dragons_menu.sections.dragons import dragons_section

page_section = ElementsSection((4 * universal_sizes.LARGE, universal_sizes.LARGE), 'center',
                               (dragons_section.rect.centerx, dragons_section.rect.bottom - universal_sizes.LARGE))

page_section.add_text('page_number',
                      Text(page_section, 'dragons_game/fonts/pr_viking.ttf', int(page_section.height), '1', 'white',
                           'center', (0, 0), 3, 'black'))


class _PageButton(Button):
    def __init__(self, image_path: str, position: custom_types.Position):
        super().__init__(page_section, image_path, (page_section.height, page_section.height), position, (0, 0))


page_section.add_button('left_page', _PageButton('dragons_game/graphics/buttons/left_page.png', 'topleft'))
page_section.add_button('right_page', _PageButton('dragons_game/graphics/buttons/right_page.png', 'topright'))
