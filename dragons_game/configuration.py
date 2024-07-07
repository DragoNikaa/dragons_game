from dataclasses import dataclass

import pygame

from dragons_game.game_states import GameStates

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()


@dataclass
class General:
    SCREEN_WIDTH = screen.get_width()
    SCREEN_HEIGHT = screen.get_height()
    NAME = 'Dragons'
    # ICON = pygame.image.load('').convert_alpha()


pygame.display.set_caption(General.NAME)
# pygame.display.set_icon(General.ICON)


@dataclass
class StartScreen:
    BACKGROUNDS_DIR_PATH = 'dragons_game/graphics/start_screen_backgrounds'

    NAME_FONT_PATH = 'dragons_game/fonts/pr_viking.ttf'
    NAME_SIZE = int(General.SCREEN_HEIGHT / 3.5)
    NAME_COLOR = 'white'
    NAME_DEST = (int(General.SCREEN_WIDTH / 2), int(General.SCREEN_HEIGHT / 3.5))
    NAME_ANTIALIAS = True

    NAME_BORDER_COLOR = 'black'
    NAME_BORDER_THICKNESS = int(General.SCREEN_HEIGHT / 120)

    TEXT_BUTTON_TEXT_FONT_PATH = 'dragons_game/fonts/rurik.ttf'
    TEXT_BUTTON_TEXT_SIZE = int(General.SCREEN_HEIGHT / 9)
    TEXT_BUTTON_TEXT_COLOR = 'white'
    TEXT_BUTTON_TEXT_ANTIALIAS = True

    TEXT_BUTTON_TEXT_BORDER_COLOR = 'black'
    TEXT_BUTTON_TEXT_BORDER_THICKNESS = int(TEXT_BUTTON_TEXT_SIZE / 40)

    TEXT_BUTTON_WIDTH = int(General.SCREEN_WIDTH / 4)
    TEXT_BUTTON_HEIGHT = int(General.SCREEN_HEIGHT / 4)
    TEXT_BUTTON_IMAGE_PATH = 'dragons_game/graphics/button_backgrounds/text_button.png'
    TEXT_BUTTON_Y_OFFSET = int(TEXT_BUTTON_HEIGHT / 6)

    START_BUTTON_TEXT = 'START'
    START_BUTTON_DEST = (int(General.SCREEN_WIDTH / 2), int(General.SCREEN_HEIGHT / 1.5))


@dataclass
class LevelSelection:
    TOP_TILES_NUMBER = 4
    TOP_TILE_WIDTH = int(General.SCREEN_WIDTH / TOP_TILES_NUMBER)
    TOP_TILE_HEIGHT = int(General.SCREEN_HEIGHT / 9)
    TILE_BACKGROUND_IMAGE_PATH = 'dragons_game/graphics/menu_elements/tile.png'
    TOP_TILES_DEST = [(x, 0) for x in range(0, General.SCREEN_WIDTH, int(General.SCREEN_WIDTH / TOP_TILES_NUMBER))]
    TOP_TILE_POSITION = 'topleft'
    TOP_TILES_GAME_STATES = (GameStates.UNKNOWN, GameStates.UNKNOWN, GameStates.UNKNOWN, GameStates.UNKNOWN)

    TOP_TILES_IMAGE_WIDTHS = (
        int(TOP_TILE_HEIGHT / 1.6), int(TOP_TILE_HEIGHT / 2.1), int(TOP_TILE_HEIGHT / 1.5), int(TOP_TILE_HEIGHT / 1.85))
    TOP_TILE_IMAGE_HEIGHT = int(TOP_TILE_HEIGHT / 1.85)
    TOP_TILES_IMAGE_PATHS = (
        'dragons_game/graphics/menu_elements/trophy.png', 'dragons_game/graphics/menu_elements/dragon_egg.png',
        'dragons_game/graphics/menu_elements/fish.png', 'dragons_game/graphics/menu_elements/coin.png')
    TOP_TILE_IMAGE_X_OFFSET = -int(TOP_TILE_WIDTH / 3.05)

    TOP_TILE_TEXT_FONT_PATH = 'dragons_game/fonts/pr_viking.ttf'
    TOP_TILE_TEXT_SIZE = int(TOP_TILE_HEIGHT / 2)
    TOP_TILE_TEXT_COLOR = 'white'
    TOP_TILE_TEXT_ANTIALIAS = True
    TOP_TILE_TEXT_X_OFFSET = int(TOP_TILE_WIDTH / 9)

    TOP_TILE_TEXT_BORDER_COLOR = 'black'
    TOP_TILE_TEXT_BORDER_THICKNESS = int(TOP_TILE_TEXT_SIZE / 30)

    BOTTOM_TILES_NUMBER = 5
    BOTTOM_TILE_WIDTH = int(General.SCREEN_WIDTH / BOTTOM_TILES_NUMBER)
    BOTTOM_TILE_HEIGHT = int(General.SCREEN_HEIGHT / 7)
    BOTTOM_TILES_DEST = [(x, General.SCREEN_HEIGHT) for x in
                         range(0, General.SCREEN_WIDTH, int(General.SCREEN_WIDTH / BOTTOM_TILES_NUMBER))]
    BOTTOM_TILE_POSITION = 'bottomleft'
    BOTTOM_TILES_GAME_STATES = (
        GameStates.UNKNOWN, GameStates.UNKNOWN, GameStates.UNKNOWN, GameStates.UNKNOWN, GameStates.UNKNOWN)

    BOTTOM_TILES_IMAGE_WIDTHS = (
        int(BOTTOM_TILE_HEIGHT / 1.85), int(BOTTOM_TILE_HEIGHT / 1.85), int(BOTTOM_TILE_HEIGHT / 1.85),
        int(BOTTOM_TILE_HEIGHT / 1.85), int(BOTTOM_TILE_HEIGHT / 1.85))
    BOTTOM_TILE_IMAGE_HEIGHT = int(BOTTOM_TILE_HEIGHT / 1.85)
    BOTTOM_TILES_IMAGE_PATHS = (
        'dragons_game/graphics/menu_elements/coin.png', 'dragons_game/graphics/menu_elements/coin.png',
        'dragons_game/graphics/menu_elements/map.png', 'dragons_game/graphics/menu_elements/coin.png',
        'dragons_game/graphics/menu_elements/coin.png')
    BOTTOM_TILE_IMAGE_X_OFFSET = -int(BOTTOM_TILE_WIDTH / 3.3)

    BOTTOM_TILE_TEXT_FONT_PATH = 'dragons_game/fonts/pr_viking.ttf'
    BOTTOM_TILE_TEXT_SIZE = int(BOTTOM_TILE_HEIGHT / 3)
    BOTTOM_TILES_TEXTS = ('Hatchery', 'Dragons', 'Islands', 'Market', 'Settings')
    BOTTOM_TILE_TEXT_COLOR = 'white'
    BOTTOM_TILE_TEXT_ANTIALIAS = True
    BOTTOM_TILE_TEXT_X_OFFSET = int(BOTTOM_TILE_WIDTH / 8)

    BOTTOM_TILE_TEXT_BORDER_COLOR = 'black'
    BOTTOM_TILE_TEXT_BORDER_THICKNESS = TOP_TILE_TEXT_BORDER_THICKNESS

    BACKGROUNDS_DIR_PATH = 'dragons_game/graphics/level_selection_backgrounds'
    BACKGROUND_HEIGHT = General.SCREEN_HEIGHT - TOP_TILE_HEIGHT - BOTTOM_TILE_HEIGHT
    BACKGROUND_DEST = (0, TOP_TILE_HEIGHT)

    LEVEL_BUTTONS_NUMBER = 4
    LEVEL_BUTTON_WIDTH = LEVEL_BUTTON_HEIGHT = int(BACKGROUND_HEIGHT / 6.5)
    LEVEL_BUTTON_IMAGE_PATH = 'dragons_game/graphics/button_backgrounds/level_button.png'
    LEVEL_BUTTONS_DEST = {
        1: (
            (int(General.SCREEN_WIDTH / 5.80), TOP_TILE_HEIGHT + int(BACKGROUND_HEIGHT / 1.95)),
            (int(General.SCREEN_WIDTH / 2.70), TOP_TILE_HEIGHT + int(BACKGROUND_HEIGHT / 3.70)),
            (int(General.SCREEN_WIDTH / 1.63), TOP_TILE_HEIGHT + int(BACKGROUND_HEIGHT / 1.80)),
            (int(General.SCREEN_WIDTH / 1.20), TOP_TILE_HEIGHT + int(BACKGROUND_HEIGHT / 2.70)),
        )
    }
