from dataclasses import dataclass


@dataclass
class General:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    NAME = "Dragons"
    # ICON = pygame.image.load('').convert_alpha()


@dataclass
class StartScreen:
    BACKGROUNDS_DIR_PATH = "graphics/start_screen_backgrounds"

    NAME_FONT_PATH = "fonts/pr_viking.ttf"
    NAME_SIZE = 200
    NAME_COLOR = "white"
    NAME_DEST = (General.SCREEN_WIDTH // 2, 200)
    NAME_ANTIALIAS = True

    NAME_BORDER_COLOR = "black"
    NAME_BORDER_THICKNESS = 10

    TEXT_BUTTON_TEXT_FONT_PATH = "fonts/rurik.ttf"
    TEXT_BUTTON_TEXT_SIZE = 80
    TEXT_BUTTON_TEXT_COLOR = "white"
    TEXT_BUTTON_TEXT_ANTIALIAS = True

    TEXT_BUTTON_TEXT_BORDER_COLOR = 'black'
    TEXT_BUTTON_TEXT_BORDER_THICKNESS = 4

    TEXT_BUTTON_WIDTH = 380
    TEXT_BUTTON_HEIGHT = 180
    TEXT_BUTTON_IMAGE_PATH = "graphics/button_backgrounds/text_button.png"
    TEXT_BUTTON_Y_OFFSET = TEXT_BUTTON_HEIGHT // 6

    START_BUTTON_TEXT = "START"
    START_BUTTON_DEST = (General.SCREEN_WIDTH // 2, 470)


@dataclass
class LevelSelection:
    BACKGROUNDS_DIR_PATH = 'graphics/level_selection_backgrounds'

    LEVEL_BUTTON_WIDTH = LEVEL_BUTTON_HEIGHT = 100
    LEVEL_BUTTON_IMAGE = 'graphics/button_backgrounds/level_button.png'
    LEVEL_BUTTONS_NUMBER = 4
    LEVEL_BUTTONS_DEST = {1: ((General.SCREEN_WIDTH // 2.77, General.SCREEN_HEIGHT // 3.81),
                              (General.SCREEN_WIDTH // 6.08, General.SCREEN_HEIGHT // 1.89),
                              (General.SCREEN_WIDTH // 1.63, General.SCREEN_HEIGHT // 1.69),
                              (General.SCREEN_WIDTH // 1.19, General.SCREEN_HEIGHT // 2.72))}
