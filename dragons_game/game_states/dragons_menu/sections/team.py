from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section
from dragons_game.game_states.common import universal_sizes

team_section = Section((GameConfig.WINDOW_WIDTH / 7, GameConfig.WINDOW_HEIGHT - title_bar_section.height), 'topleft',
                       (0, title_bar_section.rect.bottom), 'dragons_game/graphics/backgrounds/dragons_menu/team.png')

team_section.add_text('title',
                      Text(team_section, 'dragons_game/fonts/pr_viking.ttf', int(team_section.height / 20.5), 'My team',
                           'white', 'midtop', (0, universal_sizes.SMALL), 3, 'black'))
