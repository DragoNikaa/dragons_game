import pygame

from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.text import Text
from dragons_game.game_states.dragons_menu.configuration.backgrounds import LeftBackgroundConfig, RightBackgroundConfig
# from dragons_game.game_states.dragons_menu.configuration.dragon_buttons import _Row1Dragon1ButtonConfig, \
#     _Row1Dragon2ButtonConfig, _Row1Dragon3ButtonConfig, _Row1Dragon4ButtonConfig
from dragons_game.game_states.dragons_menu.configuration.title_bar import TitleBarConfig, TitleBarImageConfig, \
    TitleBarTextConfig, TitleBarTextBorderConfig, TitleBarButtonConfig

_left_background = Image(LeftBackgroundConfig())
_right_background = Image(RightBackgroundConfig())

_title_bar = Image(TitleBarConfig())
_title_bar_image = Image(TitleBarImageConfig())
_title_bar_text = Text(TitleBarTextConfig(), text_border_config=TitleBarTextBorderConfig())
_title_bar_button = Button(TitleBarButtonConfig())

# _row_1_dragon_1_button = Button(_Row1Dragon1ButtonConfig())
# _row_1_dragon_2_button = Button(_Row1Dragon2ButtonConfig())
# _row_1_dragon_3_button = Button(_Row1Dragon3ButtonConfig())
# _row_1_dragon_4_button = Button(_Row1Dragon4ButtonConfig())
# _row_1_dragon_5_button = Button(_Row1Dragon5ButtonConfig())

dragons_menu_elements = pygame.sprite.Group(_left_background, _right_background, _title_bar, _title_bar_image,
                                            _title_bar_text, _title_bar_button)
                                            # , _row_1_dragon_1_button,
                                            # _row_1_dragon_2_button, _row_1_dragon_3_button, _row_1_dragon_4_button,
                                            # )
