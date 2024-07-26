import pathlib
import random

from dragons_game.utils import custom_types
from dragons_game.elements.button import Button

from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.game_state import GameState


def _draw_background() -> str:
    backgrounds = [file for file in pathlib.Path('dragons_game/graphics/backgrounds/start_screen').iterdir() if
                   file.name != '__init__.py']
    return str(random.choice(backgrounds))


start_screen_section = Section((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT), 'topleft', (0, 0),
                               _draw_background())

start_screen_section.add_text('title', Text(start_screen_section, 'dragons_game/fonts/pr_viking.ttf',
                                            int(start_screen_section.height / 3.5), GameConfig.NAME.upper(), 'white',
                                            'center', (0, -start_screen_section.height / 4), 10, 'black'))


class _StartScreenButton(Button):
    def __init__(self, y_offset: float, click_action: custom_types.CustomEventDict, label: str):
        super().__init__(start_screen_section, 'dragons_game/graphics/buttons/start_screen.png',
                         (start_screen_section.width / 4, start_screen_section.height / 4), 'center', (0, y_offset),
                         click_action)

        self.add_text('label',
                      Text(self, 'dragons_game/fonts/rurik.ttf', int(self.height / 2.5), label, 'white', 'center',
                           (0, self.height / 6), 3, 'black'))


start_screen_section.add_button('start', _StartScreenButton(start_screen_section.height / 6, {'action': 'change_state',
                                                                                              'next_state': GameState.MAIN_MENU},
                                                            'Start'))
