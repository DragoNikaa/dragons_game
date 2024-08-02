import pathlib
import random

from dragons_game.elements.image import Image
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


start_screen_section = Section((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT), 'topleft', (0, 0))

start_screen_section.add_element('background', Image(_draw_background(), start_screen_section.size, 'topleft', (0, 0)))

start_screen_section.add_element('title', Text('dragons_game/fonts/pr_viking.ttf', start_screen_section.height / 3.5,
                                               GameConfig.NAME.upper(), 'white', 'center',
                                               (0, -start_screen_section.height / 4), 10, 'black'))


class _StartScreenButton(Button):
    def __init__(self, y_destination: float, click_action: custom_types.CustomEventDict, label: str):
        super().__init__('dragons_game/graphics/buttons/start_screen.png',
                         (start_screen_section.width / 4, start_screen_section.height / 4), 'center',
                         (0, y_destination), click_action)

        self.add_element('label', Text('dragons_game/fonts/rurik.ttf', self.height / 2.5, label, 'white', 'center',
                                       (0, self.height / 6), 3, 'black'))


start_screen_section.add_element('start', _StartScreenButton(start_screen_section.height / 6,
                                                             {'action': 'change_state',
                                                              'next_state': GameState.MAIN_MENU}, 'Start'))
