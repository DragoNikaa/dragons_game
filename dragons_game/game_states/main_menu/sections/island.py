from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.main_menu.sections.bottom_buttons import bottom_buttons_section
from dragons_game.game_states.main_menu.sections.top_buttons import top_buttons_section
from dragons_game.islands.level import Level
from dragons_game.user import user


class _IslandSection(Section):
    def __init__(self) -> None:
        super().__init__((GameConfig.WINDOW_WIDTH,
                          GameConfig.WINDOW_HEIGHT - top_buttons_section.height - bottom_buttons_section.height),
                         'topleft', (0, top_buttons_section.rect.bottom))

        island = user.current_island

        self.add_element('background', Image(island.image_path, self.size, 'topleft', (0, 0)))

        self.add_element('easy', self._level_button(island.easy_level))
        self.add_element('medium', self._level_button(island.medium_level))
        self.add_element('hard', self._level_button(island.hard_level))
        self.add_element('fiendish', self._level_button(island.fiendish_level))

    def _level_button(self, level: Level) -> Button:
        return Button(level.button_image_path, (self.height / 5, self.height / 5), 'center',
                      (self.width / level.button_factors[0], self.height / level.button_factors[1]),
                      {'action': 'battle', 'level': level}, {'action': 'show_tooltip', 'tooltip': level.tooltip})


island_section = _IslandSection()
