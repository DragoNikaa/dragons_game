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
    NAME = "Dragons"
    # ICON = pygame.image.load('').convert_alpha()


pygame.display.set_caption(General.NAME)
# pygame.display.set_icon(General.ICON)


@dataclass
class StartScreen:
    BACKGROUNDS_DIR_PATH = "dragons_game/graphics/start_screen_backgrounds"

    NAME_FONT_PATH = "dragons_game/fonts/pr_viking.ttf"
    NAME_SIZE = int(General.SCREEN_HEIGHT / 3.5)
    NAME_COLOR = "white"
    NAME_DEST = (int(General.SCREEN_WIDTH / 2), int(General.SCREEN_HEIGHT / 3.5))
    NAME_ANTIALIAS = True

    NAME_BORDER_COLOR = "black"
    NAME_BORDER_THICKNESS = int(General.SCREEN_HEIGHT / 120)

    TEXT_BUTTON_TEXT_FONT_PATH = "dragons_game/fonts/rurik.ttf"
    TEXT_BUTTON_TEXT_SIZE = int(General.SCREEN_HEIGHT / 9)
    TEXT_BUTTON_TEXT_COLOR = "white"
    TEXT_BUTTON_TEXT_ANTIALIAS = True

    TEXT_BUTTON_TEXT_BORDER_COLOR = 'black'
    TEXT_BUTTON_TEXT_BORDER_THICKNESS = int(General.SCREEN_HEIGHT / 320)

    TEXT_BUTTON_WIDTH = int(General.SCREEN_WIDTH / 4)
    TEXT_BUTTON_HEIGHT = int(General.SCREEN_HEIGHT / 4)
    TEXT_BUTTON_IMAGE_PATH = "dragons_game/graphics/button_backgrounds/text_button.png"
    TEXT_BUTTON_Y_OFFSET = int(TEXT_BUTTON_HEIGHT / 6)

    START_BUTTON_TEXT = "START"
    START_BUTTON_DEST = (int(General.SCREEN_WIDTH / 2), int(General.SCREEN_HEIGHT / 1.5))


@dataclass
class LevelSelection:
    BACKGROUNDS_DIR_PATH = 'dragons_game/graphics/level_selection_backgrounds'

    LEVEL_BUTTONS_NUMBER = 4
    LEVEL_BUTTON_WIDTH = LEVEL_BUTTON_HEIGHT = int(General.SCREEN_HEIGHT / 8)
    LEVEL_BUTTON_IMAGE = 'dragons_game/graphics/button_backgrounds/level_button.png'
    LEVEL_BUTTONS_DEST = {1: ((int(General.SCREEN_WIDTH / 5.80), int(General.SCREEN_HEIGHT / 1.95)),
                              (int(General.SCREEN_WIDTH / 2.70), int(General.SCREEN_HEIGHT / 3.70)),
                              (int(General.SCREEN_WIDTH / 1.63), int(General.SCREEN_HEIGHT / 1.80)),
                              (int(General.SCREEN_WIDTH / 1.20), int(General.SCREEN_HEIGHT / 2.70)))}

    TOP_TILES_NUMBER = 4
    TOP_TILES_GAME_STATES = (GameStates.UNKNOWN, GameStates.UNKNOWN, GameStates.UNKNOWN, GameStates.UNKNOWN)
    TOP_TILE_WIDTH = int(General.SCREEN_WIDTH / TOP_TILES_NUMBER)
    TOP_TILE_HEIGHT = int(General.SCREEN_HEIGHT / 7)
    TOP_TILE_IMAGE = 'dragons_game/graphics/menu_elements/tile.png'
    TOP_TILES_DEST = [(x, 0) for x in range(0, General.SCREEN_WIDTH, int(General.SCREEN_WIDTH / TOP_TILES_NUMBER))]
