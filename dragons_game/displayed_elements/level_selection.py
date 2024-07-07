import pygame.sprite

from dragons_game.background import Background
from dragons_game.button import Button
from dragons_game.configuration import LevelSelection
from dragons_game.game_states import GameStates

top_tile_text_font = pygame.font.Font(LevelSelection.TOP_TILE_TEXT_FONT_PATH, LevelSelection.TOP_TILE_TEXT_SIZE)

background = Background(LevelSelection.BACKGROUNDS_DIR_PATH)

level_buttons = []
for button_number in range(LevelSelection.LEVEL_BUTTONS_NUMBER):
    button_dest = LevelSelection.LEVEL_BUTTONS_DEST[background.drawn_background_number][button_number]
    level_buttons.append(
        Button(LevelSelection.LEVEL_BUTTON_WIDTH, LevelSelection.LEVEL_BUTTON_HEIGHT,
               LevelSelection.LEVEL_BUTTON_IMAGE_PATH, button_dest, GameStates.UNKNOWN))

top_tiles = []
for top_tile_number, (tile_dest, tile_game_state) in enumerate(
        zip(LevelSelection.TOP_TILES_DEST, LevelSelection.TOP_TILES_GAME_STATES)):
    top_tile = Button(LevelSelection.TOP_TILE_WIDTH, LevelSelection.TOP_TILE_HEIGHT, LevelSelection.TOP_TILE_IMAGE_PATH,
                      tile_dest, tile_game_state, 'topleft')
    top_tile.add_image(LevelSelection.TOP_TILES_IMAGE_WIDTHS[top_tile_number], LevelSelection.TOP_TILE_IMAGE_HEIGHT,
                       LevelSelection.TOP_TILES_IMAGE_PATHS[top_tile_number],
                       x_offset=LevelSelection.TOP_TILE_IMAGE_X_OFFSET)
    top_tile.add_text(top_tile_text_font, '2137', LevelSelection.TOP_TILE_TEXT_COLOR,
                      LevelSelection.TOP_TILE_TEXT_ANTIALIAS, x_offset=LevelSelection.TOP_TILE_TEXT_X_OFFSET)
    top_tile.add_text_border(LevelSelection.TOP_TILE_TEXT_BORDER_COLOR, LevelSelection.TOP_TILE_TEXT_BORDER_THICKNESS)
    top_tiles.append(top_tile)

level_selection_elements = pygame.sprite.Group(background, level_buttons, top_tiles)
