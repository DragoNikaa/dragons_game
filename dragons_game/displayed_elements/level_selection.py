from dataclasses import dataclass

import pygame.sprite

from dragons_game import background
from dragons_game.button import Button
from dragons_game.configuration import LevelSelection


@dataclass
class Background:
    background_elements = background.Background(LevelSelection.BACKGROUNDS_DIR_PATH)


@dataclass
class LevelButtons:
    level_buttons_elements: 'pygame.sprite.Group[Button]' = pygame.sprite.Group()
    for button_number in range(LevelSelection.LEVEL_BUTTONS_NUMBER):
        button_dest = LevelSelection.LEVEL_BUTTONS_DEST[Background.background_elements.drawn_background_number][
            button_number]
        level_buttons_elements.add(Button(LevelSelection.LEVEL_BUTTON_WIDTH, LevelSelection.LEVEL_BUTTON_HEIGHT,
                                          LevelSelection.LEVEL_BUTTON_IMAGE, button_dest))


level_selection_elements = pygame.sprite.Group(Background.background_elements, LevelButtons.level_buttons_elements)
