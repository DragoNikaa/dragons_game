import pygame.sprite

from dragons_game.background import Background
from dragons_game.button import Button
from dragons_game.configuration import LevelSelection
from dragons_game.game_states import GameStates

background = Background(LevelSelection.BACKGROUNDS_DIR_PATH)

level_buttons: 'pygame.sprite.Group[Button]' = pygame.sprite.Group()
for button_number in range(LevelSelection.LEVEL_BUTTONS_NUMBER):
    button_dest = LevelSelection.LEVEL_BUTTONS_DEST[background.drawn_background_number][button_number]
    level_buttons.add(
        Button(LevelSelection.LEVEL_BUTTON_WIDTH, LevelSelection.LEVEL_BUTTON_HEIGHT, LevelSelection.LEVEL_BUTTON_IMAGE,
               button_dest, GameStates.UNKNOWN))

top_tiles = pygame.sprite.Group()
for tile_dest, tile_game_state in zip(LevelSelection.TOP_TILES_DEST, LevelSelection.TOP_TILES_GAME_STATES):
    top_tiles.add(
        Button(LevelSelection.TOP_TILE_WIDTH, LevelSelection.TOP_TILE_HEIGHT, LevelSelection.TOP_TILE_IMAGE, tile_dest,
               tile_game_state, 'topleft'))

level_selection_elements = pygame.sprite.Group(background, level_buttons, top_tiles)
