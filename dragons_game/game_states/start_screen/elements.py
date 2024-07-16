import pygame

from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.text import Text
from dragons_game.game_states.start_screen.configuration.background import BackgroundConfig
from dragons_game.game_states.start_screen.configuration.buttons import StartButtonConfig, \
    StartButtonTextConfig, StartButtonTextBorderConfig
from dragons_game.game_states.start_screen.configuration.title import TitleConfig, TitleBorderConfig

_background = Image(BackgroundConfig())

_title = Text(TitleConfig(), TitleBorderConfig())

_start_button = Button(StartButtonConfig())
_start_button_text = _start_button.add_text(StartButtonTextConfig(), StartButtonTextBorderConfig())

start_screen_elements = pygame.sprite.Group(_background, _title, _start_button, _start_button_text)
