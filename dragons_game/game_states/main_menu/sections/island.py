from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.main_menu.sections.bottom_buttons import bottom_buttons_section
from dragons_game.game_states.main_menu.sections.top_buttons import top_buttons_section
from dragons_game.utils import custom_types

island_section = Section(
    (GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT - top_buttons_section.height - bottom_buttons_section.height),
    'topleft', (0, top_buttons_section.rect.bottom))

island_section.add_element('background',
                           Image('dragons_game/graphics/backgrounds/main_menu/1.png', island_section.size, 'topleft',
                                 (0, 0)))


class _LevelButton(Button):
    def __init__(self, destination: tuple[float, float], click_action: custom_types.CustomEventDict | None = None,
                 hover_action: custom_types.CustomEventDict | None = None):
        super().__init__('dragons_game/graphics/buttons/level.png',
                         (island_section.height / 6.5, island_section.height / 6.5), 'topleft', destination,
                         click_action, hover_action)


island_section.add_element('easy', _LevelButton((island_section.width / 7, island_section.height / 2.25)))
island_section.add_element('medium', _LevelButton((island_section.width / 2.8, island_section.height / 4.7)))
island_section.add_element('hard', _LevelButton((island_section.width / 1.71, island_section.height / 2)))
island_section.add_element('fiendish', _LevelButton((island_section.width / 1.23, island_section.height / 3.4)))
