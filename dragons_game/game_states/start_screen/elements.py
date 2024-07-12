import pygame

from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.text import Text
from dragons_game.game_states.start_screen.configuration.background import BackgroundConfig
from dragons_game.game_states.start_screen.configuration.buttons import StartButtonConfig, \
    StartButtonTextConfig, StartButtonTextBorderConfig
from dragons_game.game_states.start_screen.configuration.name import NameConfig, NameBorderConfig

_background = Image(BackgroundConfig())

_name = Text(NameConfig(), text_border_config=NameBorderConfig())

_start_button = Button(StartButtonConfig(), text_config=StartButtonTextConfig(),
                       text_border_config=StartButtonTextBorderConfig())

start_screen_elements = pygame.sprite.Group(_background, _name, _start_button)
