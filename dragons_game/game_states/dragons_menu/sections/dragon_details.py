import pygame

from dragons_game.dragons.dragon import Dragon
from dragons_game.elements.section import Section
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section

test_background = pygame.Surface((1, 1))
test_background.fill('chocolate')


class DragonDetails(Section):
    def __init__(self, dragon: Dragon):
        super().__init__((GameConfig.WINDOW_WIDTH * 6 / 7, GameConfig.WINDOW_HEIGHT - title_bar_section.height),
                         'topleft', (GameConfig.WINDOW_WIDTH / 7, title_bar_section.rect.bottom), test_background)
