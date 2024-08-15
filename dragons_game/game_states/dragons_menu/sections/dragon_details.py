import pygame

from dragons_game.dragons.dragon import Dragon
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section
from dragons_game.utils.image_proportions import calculate_proportional_height, calculate_proportional_width

test_background = pygame.Surface((1, 1))
test_background.fill('chocolate')


class DragonDetails(Section):
    def __init__(self, dragon: Dragon):
        super().__init__((GameConfig.WINDOW_WIDTH * 6 / 7, GameConfig.WINDOW_HEIGHT - title_bar_section.height),
                         'topleft', (GameConfig.WINDOW_WIDTH / 7, title_bar_section.rect.bottom), test_background)

        self.add_element('dragon_background',
                         Image('dragons_game/graphics/backgrounds/dragons_menu/dragon_details/dragon_background.png',
                               (self.width / 2, self.height), 'topleft', (0, 0)))

        name = Text('dragons_game/fonts/rurik.ttf', self.height / 9, dragon.name, dragon.rarity.color, 'midtop',
                    (-self.width / 4, 1.5 * universal_sizes.LARGE), 4, 'black')
        self.add_element('name', name)

        dragon_image_width = self.width / 2.6
        dragon_image_height = calculate_proportional_height(dragon.image_path, dragon_image_width)

        max_height = self.height - name.height - 3.5 * universal_sizes.LARGE
        if dragon_image_height > max_height:
            dragon_image_height = max_height
            dragon_image_width = calculate_proportional_width(dragon.image_path, dragon_image_height)

        self.add_element('dragon', Image(dragon.image_path, (dragon_image_width, dragon_image_height), 'center',
                                         (name.x_destination, self.height / 13)))
