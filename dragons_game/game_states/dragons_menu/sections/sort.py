from dragons_game.elements.button import Button
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.dragons import dragons_section
from dragons_game.game_states.dragons_menu.sections.page import page_section

sort_section = Section(
    (page_section.rect.left - dragons_section.rect.left - 4 * universal_sizes.LARGE, page_section.height), 'center',
    ((page_section.rect.left + dragons_section.rect.left) / 2, page_section.rect.centery))

_text = Text('dragons_game/fonts/pr_viking.ttf', sort_section.height / 1.5, 'Sorted by:', 'white', 'midleft', (0, 0), 3,
             'black')
sort_section.add_element('text', _text)

_key_button = Button('dragons_game/graphics/buttons/sort_key.png', (sort_section.width / 2.5, sort_section.height),
                     'midleft', (_text.width + universal_sizes.SMALL, 0))
sort_section.add_element('key', _key_button)

sort_section.add_element('reverse', Button('dragons_game/graphics/buttons/sort_reverse.png',
                                           (1.5 * sort_section.height, sort_section.height), 'midright', (0, 0)))
