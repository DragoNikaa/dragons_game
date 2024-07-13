from dragons_game.game_states.general.configuration.title_bar import GeneralTitleBarImageConfig, GeneralTitleBarTextConfig
from dragons_game.game_states.main_menu.configuration.top_and_bottom_buttons import DragonsButtonTextConfig


class TitleBarImageConfig(GeneralTitleBarImageConfig):
    IMAGE = 'dragons_game/graphics/backgrounds/main_menu/1.png'


class TitleBarTextConfig(GeneralTitleBarTextConfig):
    TEXT = DragonsButtonTextConfig.TEXT
