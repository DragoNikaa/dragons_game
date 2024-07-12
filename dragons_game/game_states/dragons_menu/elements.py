import pygame

from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.text import Text
from dragons_game.game_states.dragons_menu.configuration.backgrounds import LeftBackgroundConfig, RightBackgroundConfig
from dragons_game.game_states.dragons_menu.configuration.title_bar import TitleBarConfig, TitleBarImageConfig, \
    TitleBarTextConfig, TitleBarTextBorderConfig, TitleBarButtonConfig

_left_background = Image(LeftBackgroundConfig())
_right_background = Image(RightBackgroundConfig())

_title_bar = Image(TitleBarConfig())
_title_bar_image = Image(TitleBarImageConfig())
_title_bar_text = Text(TitleBarTextConfig(), text_border_config=TitleBarTextBorderConfig())
_title_bar_button = Button(TitleBarButtonConfig())

dragons_menu_elements = pygame.sprite.Group(_left_background, _right_background, _title_bar, _title_bar_image,
                                            _title_bar_text, _title_bar_button)
