from dragons_game.utils import custom_types
from dragons_game.elements.button import Button
from dragons_game.elements.elements_section import ElementsSection
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.main_menu.sections.bottom_buttons import bottom_buttons_section
from dragons_game.game_states.main_menu.sections.top_buttons import top_buttons_section

island_section = ElementsSection(
    (GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT - top_buttons_section.height - bottom_buttons_section.height),
    'topleft', (0, top_buttons_section.rect.bottom), 'dragons_game/graphics/backgrounds/main_menu/1.png')


class _LevelButton(Button):
    def __init__(self, offset: tuple[float, float], click_action: custom_types.CustomEventDict | None = None,
                 hover_action: custom_types.CustomEventDict | None = None):
        super().__init__(island_section, 'dragons_game/graphics/buttons/level.png',
                         (island_section.height / 6.5, island_section.height / 6.5), 'topleft', offset, click_action,
                         hover_action)


island_section.add_button('easy', _LevelButton((island_section.width / 7, island_section.height / 2.25)))
island_section.add_button('medium', _LevelButton((island_section.width / 2.8, island_section.height / 4.7)))
island_section.add_button('hard', _LevelButton((island_section.width / 1.71, island_section.height / 2)))
island_section.add_button('fiendish', _LevelButton((island_section.width / 1.23, island_section.height / 3.4)))
