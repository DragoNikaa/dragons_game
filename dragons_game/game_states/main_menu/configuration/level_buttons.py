from abc import ABC

from dragons_game.elements.abstract_configuration.button import ButtonConfig
from dragons_game.elements.abstract_configuration.position import POSITION
from dragons_game.user_event import USER_EVENT_DICT_KEY, USER_EVENT_DICT_VALUE
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.main_menu.configuration.background import BackgroundConfig
from dragons_game.game_states.main_menu.configuration.top_and_bottom_buttons import _TopButtonConfig


class _LevelButtonConfig(ButtonConfig, ABC):
    WIDTH = HEIGHT = int(BackgroundConfig.HEIGHT / 6.5)
    IMAGE = 'dragons_game/graphics/buttons/level.png'
    POSITION = POSITION.CENTER
    HOVER_ACTION = None


class Island1EasyLevelButtonConfig(_LevelButtonConfig):
    DESTINATION = (int(BackgroundConfig.WIDTH / 5.8), _TopButtonConfig.HEIGHT + int(BackgroundConfig.HEIGHT / 1.95))
    CLICK_ACTION = {USER_EVENT_DICT_KEY.ACTION: USER_EVENT_DICT_VALUE.CHANGE_STATE,
                    USER_EVENT_DICT_KEY.NEXT_STATE: GameState.UNKNOWN}


class Island1MediumLevelButtonConfig(_LevelButtonConfig):
    DESTINATION = (int(BackgroundConfig.WIDTH / 2.7), _TopButtonConfig.HEIGHT + int(BackgroundConfig.HEIGHT / 3.7))
    CLICK_ACTION = {USER_EVENT_DICT_KEY.ACTION: USER_EVENT_DICT_VALUE.CHANGE_STATE,
                    USER_EVENT_DICT_KEY.NEXT_STATE: GameState.UNKNOWN}


class Island1HardLevelButtonConfig(_LevelButtonConfig):
    DESTINATION = (int(BackgroundConfig.WIDTH / 1.63), _TopButtonConfig.HEIGHT + int(BackgroundConfig.HEIGHT / 1.8))
    CLICK_ACTION = {USER_EVENT_DICT_KEY.ACTION: USER_EVENT_DICT_VALUE.CHANGE_STATE,
                    USER_EVENT_DICT_KEY.NEXT_STATE: GameState.UNKNOWN}


class Island1FiendishLevelButtonConfig(_LevelButtonConfig):
    DESTINATION = (int(BackgroundConfig.WIDTH / 1.2), _TopButtonConfig.HEIGHT + int(BackgroundConfig.HEIGHT / 2.7))
    CLICK_ACTION = {USER_EVENT_DICT_KEY.ACTION: USER_EVENT_DICT_VALUE.CHANGE_STATE,
                    USER_EVENT_DICT_KEY.NEXT_STATE: GameState.UNKNOWN}
