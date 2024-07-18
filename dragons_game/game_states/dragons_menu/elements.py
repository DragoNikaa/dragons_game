import pygame

from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.text import Text
from dragons_game.game_states.dragons_menu.configuration.backgrounds import LeftBackgroundConfig, RightBackgroundConfig
from dragons_game.game_states.dragons_menu.configuration.page import PageNumberConfig, PageNumberBorderConfig, \
    LeftPageButtonConfig, RightPageButtonConfig
from dragons_game.game_states.dragons_menu.configuration.dragon_buttons import Row1Dragon1ButtonConfig, \
    Row1Dragon2ButtonConfig, Row1Dragon3ButtonConfig, Row1Dragon4ButtonConfig, Row1Dragon5ButtonConfig, \
    Row2Dragon1ButtonConfig, Row2Dragon2ButtonConfig, Row2Dragon3ButtonConfig, Row2Dragon4ButtonConfig, \
    Row2Dragon5ButtonConfig, ExperienceBarButtonConfig, EnergyBarButtonConfig, HealthBarButtonConfig, DragonNameConfig, \
    DragonButtonTextBorderConfig, DragonLevelConfig, DragonButtonImageConfig
from dragons_game.game_states.dragons_menu.configuration.team import TeamTextConfig, TeamTextBorderConfig, \
    TeamDragon1ButtonConfig, TeamDragon2ButtonConfig, TeamDragon3ButtonConfig
from dragons_game.game_states.dragons_menu.configuration.title_bar import TitleBarImageConfig, TitleBarTextConfig
from dragons_game.game_states.general.configuration.title_bar import TitleBarConfig, TitleBarTextBorderConfig, \
    TitleBarButtonConfig

_title_bar = Image(TitleBarConfig())
_title_bar_image = Image(TitleBarImageConfig())
_title_bar_text = Text(TitleBarTextConfig(), TitleBarTextBorderConfig())
_title_bar_button = Button(TitleBarButtonConfig())

_left_background = Image(LeftBackgroundConfig())
_right_background = Image(RightBackgroundConfig())

_team_text = Text(TeamTextConfig(), TeamTextBorderConfig())
_team_dragon_buttons = (
    Button(TeamDragon1ButtonConfig()), Button(TeamDragon2ButtonConfig()), Button(TeamDragon3ButtonConfig()))

_dragon_buttons = (
    Button(Row1Dragon1ButtonConfig()), Button(Row1Dragon2ButtonConfig()), Button(Row1Dragon3ButtonConfig()),
    Button(Row1Dragon4ButtonConfig()), Button(Row1Dragon5ButtonConfig()), Button(Row2Dragon1ButtonConfig()),
    Button(Row2Dragon2ButtonConfig()), Button(Row2Dragon3ButtonConfig()), Button(Row2Dragon4ButtonConfig()),
    Button(Row2Dragon5ButtonConfig()))

_dragon_names = []
_dragon_levels = []
_dragon_images = []
_progress_bar_buttons = []
for button in _dragon_buttons:
    _dragon_names.append(button.add_text(DragonNameConfig(), DragonButtonTextBorderConfig()))
    _dragon_levels.append(button.add_text(DragonLevelConfig(), DragonButtonTextBorderConfig()))
    _dragon_images.append(button.add_image(DragonButtonImageConfig()))
    _progress_bar_buttons.append(button.add_inside_button(ExperienceBarButtonConfig()))
    _progress_bar_buttons.append(button.add_inside_button(EnergyBarButtonConfig()))
    _progress_bar_buttons.append(button.add_inside_button(HealthBarButtonConfig()))

_page_number = Text(PageNumberConfig(), PageNumberBorderConfig())
_page_buttons = (Button(LeftPageButtonConfig()), Button(RightPageButtonConfig()))

dragons_menu_elements = pygame.sprite.Group(_title_bar, _title_bar_image, _title_bar_text, _title_bar_button,
                                            _left_background, _right_background, _team_text, _team_dragon_buttons,
                                            _dragon_buttons, _dragon_names, _dragon_levels, _dragon_images,
                                            _progress_bar_buttons, _page_number, _page_buttons)
