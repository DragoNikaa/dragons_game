from abc import ABC

from dragons_game.elements.abstract_configuration.button import ButtonConfig
from dragons_game.elements.abstract_configuration.position import position
from dragons_game.user_event import user_event_dict_key, user_event_dict_value
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.main_menu.configuration.background import BackgroundConfig
from dragons_game.game_states.main_menu.configuration.top_and_bottom_buttons import _TopButtonConfig


class _LevelButtonConfig(ButtonConfig, ABC):
    WIDTH = HEIGHT = int(BackgroundConfig.HEIGHT / 6.5)
    IMAGE = 'dragons_game/graphics/buttons/level.png'
    POSITION = position.CENTER
    HOVER_ACTION = None


class Island1EasyLevelButtonConfig(_LevelButtonConfig):
    DESTINATION = (int(BackgroundConfig.WIDTH / 5.8), _TopButtonConfig.HEIGHT + int(BackgroundConfig.HEIGHT / 1.95))
    CLICK_ACTION = {user_event_dict_key.ACTION: user_event_dict_value.CHANGE_STATE,
                    user_event_dict_key.NEXT_STATE: GameState.UNKNOWN}


class Island1MediumLevelButtonConfig(_LevelButtonConfig):
    DESTINATION = (int(BackgroundConfig.WIDTH / 2.7), _TopButtonConfig.HEIGHT + int(BackgroundConfig.HEIGHT / 3.7))
    CLICK_ACTION = {user_event_dict_key.ACTION: user_event_dict_value.CHANGE_STATE,
                    user_event_dict_key.NEXT_STATE: GameState.UNKNOWN}


class Island1HardLevelButtonConfig(_LevelButtonConfig):
    DESTINATION = (int(BackgroundConfig.WIDTH / 1.63), _TopButtonConfig.HEIGHT + int(BackgroundConfig.HEIGHT / 1.8))
    CLICK_ACTION = {user_event_dict_key.ACTION: user_event_dict_value.CHANGE_STATE,
                    user_event_dict_key.NEXT_STATE: GameState.UNKNOWN}


class Island1FiendishLevelButtonConfig(_LevelButtonConfig):
    DESTINATION = (int(BackgroundConfig.WIDTH / 1.2), _TopButtonConfig.HEIGHT + int(BackgroundConfig.HEIGHT / 2.7))
    CLICK_ACTION = {user_event_dict_key.ACTION: user_event_dict_value.CHANGE_STATE,
                    user_event_dict_key.NEXT_STATE: GameState.UNKNOWN}
