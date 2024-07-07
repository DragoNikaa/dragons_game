import pygame.sprite

from dragons_game.background import Background
from dragons_game.button import Button
from dragons_game.configuration import LevelSelection
from dragons_game.game_states import GameStates

top_tile_text_font = pygame.font.Font(LevelSelection.TOP_TILE_TEXT_FONT_PATH, LevelSelection.TOP_TILE_TEXT_SIZE)
bottom_tile_text_font = pygame.font.Font(LevelSelection.BOTTOM_TILE_TEXT_FONT_PATH,
                                         LevelSelection.BOTTOM_TILE_TEXT_SIZE)

background = Background(LevelSelection.BACKGROUNDS_DIR_PATH, height=LevelSelection.BACKGROUND_HEIGHT,
                        dest=LevelSelection.BACKGROUND_DEST)

level_buttons = []
for button_number in range(LevelSelection.LEVEL_BUTTONS_NUMBER):
    button_dest = LevelSelection.LEVEL_BUTTONS_DEST[background.drawn_background_number][button_number]
    level_buttons.append(
        Button(LevelSelection.LEVEL_BUTTON_WIDTH, LevelSelection.LEVEL_BUTTON_HEIGHT,
               LevelSelection.LEVEL_BUTTON_IMAGE_PATH, button_dest, GameStates.UNKNOWN))

top_tiles = []
for tile_number, (tile_dest, tile_game_state) in enumerate(
        zip(LevelSelection.TOP_TILES_DEST, LevelSelection.TOP_TILES_GAME_STATES)):
    bottom_tile = Button(LevelSelection.TOP_TILE_WIDTH, LevelSelection.TOP_TILE_HEIGHT,
                         LevelSelection.TILE_BACKGROUND_IMAGE_PATH,
                         tile_dest, tile_game_state, LevelSelection.TOP_TILE_POSITION)
    bottom_tile.add_image(LevelSelection.TOP_TILES_IMAGE_WIDTHS[tile_number], LevelSelection.TOP_TILE_IMAGE_HEIGHT,
                          LevelSelection.TOP_TILES_IMAGE_PATHS[tile_number],
                          x_offset=LevelSelection.TOP_TILE_IMAGE_X_OFFSET)
    bottom_tile.add_text(top_tile_text_font, '2137', LevelSelection.TOP_TILE_TEXT_COLOR,
                         LevelSelection.TOP_TILE_TEXT_ANTIALIAS, x_offset=LevelSelection.TOP_TILE_TEXT_X_OFFSET)
    bottom_tile.add_text_border(LevelSelection.TOP_TILE_TEXT_BORDER_COLOR,
                                LevelSelection.TOP_TILE_TEXT_BORDER_THICKNESS)
    top_tiles.append(bottom_tile)

bottom_tiles = []
for tile_number, (tile_dest, tile_game_state, tile_text) in enumerate(
        zip(LevelSelection.BOTTOM_TILES_DEST, LevelSelection.BOTTOM_TILES_GAME_STATES,
            LevelSelection.BOTTOM_TILES_TEXTS)):
    bottom_tile = Button(LevelSelection.BOTTOM_TILE_WIDTH, LevelSelection.BOTTOM_TILE_HEIGHT,
                         LevelSelection.TILE_BACKGROUND_IMAGE_PATH,
                         tile_dest, tile_game_state, LevelSelection.BOTTOM_TILE_POSITION)
    bottom_tile.add_image(LevelSelection.BOTTOM_TILES_IMAGE_WIDTHS[tile_number],
                          LevelSelection.BOTTOM_TILE_IMAGE_HEIGHT,
                          LevelSelection.BOTTOM_TILES_IMAGE_PATHS[tile_number],
                          x_offset=LevelSelection.BOTTOM_TILE_IMAGE_X_OFFSET)
    bottom_tile.add_text(bottom_tile_text_font, tile_text, LevelSelection.BOTTOM_TILE_TEXT_COLOR,
                         LevelSelection.BOTTOM_TILE_TEXT_ANTIALIAS, x_offset=LevelSelection.BOTTOM_TILE_TEXT_X_OFFSET)
    bottom_tile.add_text_border(LevelSelection.BOTTOM_TILE_TEXT_BORDER_COLOR,
                                LevelSelection.BOTTOM_TILE_TEXT_BORDER_THICKNESS)
    bottom_tiles.append(bottom_tile)

level_selection_elements = pygame.sprite.Group(background, level_buttons, top_tiles, bottom_tiles)
