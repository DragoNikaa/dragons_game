import pygame

from dragons_game.background import Background
from dragons_game.button import Button
from dragons_game.configuration import StartScreen, General
from dragons_game.game_states import GameStates
from dragons_game.text import Text

text_button_text_font = pygame.font.Font(StartScreen.TEXT_BUTTON_TEXT_FONT_PATH, StartScreen.TEXT_BUTTON_TEXT_SIZE)

background = Background(StartScreen.BACKGROUNDS_DIR_PATH)

name_font = pygame.font.Font(StartScreen.NAME_FONT_PATH, StartScreen.NAME_SIZE)
name = Text(name_font, General.NAME.upper(), StartScreen.NAME_COLOR, StartScreen.NAME_DEST, StartScreen.NAME_ANTIALIAS)
name.add_text_border(StartScreen.NAME_BORDER_COLOR, StartScreen.NAME_BORDER_THICKNESS)

start_button = Button(StartScreen.TEXT_BUTTON_WIDTH, StartScreen.TEXT_BUTTON_HEIGHT, StartScreen.TEXT_BUTTON_IMAGE_PATH,
                      StartScreen.START_BUTTON_DEST, GameStates.LEVEL_SELECTION)
start_button.add_text(text_button_text_font, StartScreen.START_BUTTON_TEXT, StartScreen.TEXT_BUTTON_TEXT_COLOR,
                      StartScreen.TEXT_BUTTON_TEXT_ANTIALIAS, StartScreen.TEXT_BUTTON_Y_OFFSET)
start_button.add_text_border(StartScreen.TEXT_BUTTON_TEXT_BORDER_COLOR, StartScreen.TEXT_BUTTON_TEXT_BORDER_THICKNESS)

start_screen_elements: 'pygame.sprite.Group[Background | Text | Button]' = pygame.sprite.Group(background, name,
                                                                                               start_button)
