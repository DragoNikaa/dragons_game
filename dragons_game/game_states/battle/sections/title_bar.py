from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.common.title_bar import TitleBar
from dragons_game.game_states.game_state import GameState

title_bar_section = TitleBar((GameConfig.WINDOW_WIDTH, universal_sizes.LARGE), 'topleft', (0, 0),
                             'dragons_game/graphics/icons/dragons.png', 'Battle',
                             {'action': 'change_state', 'next_state': GameState.MAIN_MENU})
