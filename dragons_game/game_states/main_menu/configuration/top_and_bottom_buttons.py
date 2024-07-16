from abc import ABC

import pygame.font

from dragons_game.elements.abstract_configuration.button import ButtonConfig, ButtonImageConfig, ButtonTextConfig
from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.elements.abstract_configuration.text import TextBorderConfig
from dragons_game.game.configuration import game_config
from dragons_game.game_states.general.configuration.icon_proportions import calculate_proportional_dimension
from dragons_game.game_states.general.game_state import GameState
from dragons_game.user_event import UserEventDictKey, UserEventDictValue


class _TopAndBottomButtonConfig(ButtonConfig, ABC):
    IMAGE = 'dragons_game/graphics/buttons/top_and_bottom.png'
    HOVER_ACTION = None


class _TopButtonConfig(_TopAndBottomButtonConfig, ABC):
    WIDTH = int(game_config.WINDOW_WIDTH / 4)
    HEIGHT = int(game_config.WINDOW_HEIGHT / 9)
    POSITION = Position.TOPLEFT


_TOP_BUTTONS_DESTINATIONS = [(x, 0) for x in range(0, game_config.WINDOW_WIDTH, _TopButtonConfig.WIDTH)]


class TrophiesButtonConfig(_TopButtonConfig):
    DESTINATION = _TOP_BUTTONS_DESTINATIONS[0]
    CLICK_ACTION = {UserEventDictKey.ACTION: UserEventDictValue.CHANGE_STATE,
                    UserEventDictKey.NEXT_STATE: GameState.UNKNOWN}


class EggsButtonConfig(_TopButtonConfig):
    DESTINATION = _TOP_BUTTONS_DESTINATIONS[1]
    CLICK_ACTION = {UserEventDictKey.ACTION: UserEventDictValue.CHANGE_STATE,
                    UserEventDictKey.NEXT_STATE: GameState.UNKNOWN}


class FishButtonConfig(_TopButtonConfig):
    DESTINATION = _TOP_BUTTONS_DESTINATIONS[2]
    CLICK_ACTION = {UserEventDictKey.ACTION: UserEventDictValue.CHANGE_STATE,
                    UserEventDictKey.NEXT_STATE: GameState.UNKNOWN}


class CoinsButtonConfig(_TopButtonConfig):
    DESTINATION = _TOP_BUTTONS_DESTINATIONS[3]
    CLICK_ACTION = {UserEventDictKey.ACTION: UserEventDictValue.CHANGE_STATE,
                    UserEventDictKey.NEXT_STATE: GameState.UNKNOWN}


class _BottomButtonConfig(_TopAndBottomButtonConfig, ABC):
    WIDTH = int(game_config.WINDOW_WIDTH / 5)
    HEIGHT = int(game_config.WINDOW_HEIGHT / 7)
    POSITION = Position.BOTTOMLEFT


_BOTTOM_BUTTONS_DESTINATIONS = [(x, game_config.WINDOW_HEIGHT) for x in
                                range(0, game_config.WINDOW_WIDTH, _BottomButtonConfig.WIDTH)]


class HatcheryButtonConfig(_BottomButtonConfig):
    DESTINATION = _BOTTOM_BUTTONS_DESTINATIONS[0]
    CLICK_ACTION = {UserEventDictKey.ACTION: UserEventDictValue.CHANGE_STATE,
                    UserEventDictKey.NEXT_STATE: GameState.UNKNOWN}


class DragonsButtonConfig(_BottomButtonConfig):
    DESTINATION = _BOTTOM_BUTTONS_DESTINATIONS[1]
    CLICK_ACTION = {UserEventDictKey.ACTION: UserEventDictValue.CHANGE_STATE,
                    UserEventDictKey.NEXT_STATE: GameState.DRAGONS_MENU}


class IslandsButtonConfig(_BottomButtonConfig):
    DESTINATION = _BOTTOM_BUTTONS_DESTINATIONS[2]
    CLICK_ACTION = {UserEventDictKey.ACTION: UserEventDictValue.CHANGE_STATE,
                    UserEventDictKey.NEXT_STATE: GameState.UNKNOWN}


class MarketButtonConfig(_BottomButtonConfig):
    DESTINATION = _BOTTOM_BUTTONS_DESTINATIONS[3]
    CLICK_ACTION = {UserEventDictKey.ACTION: UserEventDictValue.CHANGE_STATE,
                    UserEventDictKey.NEXT_STATE: GameState.UNKNOWN}


class SettingsButtonConfig(_BottomButtonConfig):
    DESTINATION = _BOTTOM_BUTTONS_DESTINATIONS[4]
    CLICK_ACTION = {UserEventDictKey.ACTION: UserEventDictValue.CHANGE_STATE,
                    UserEventDictKey.NEXT_STATE: GameState.UNKNOWN}


class _TopAndBottomImageConfig(ButtonImageConfig, ABC):
    @property
    def WIDTH(self) -> int:
        return calculate_proportional_dimension(self.IMAGE, self.HEIGHT)


class _TopButtonImageConfig(_TopAndBottomImageConfig, ABC):
    HEIGHT = int(_TopButtonConfig.HEIGHT / 1.85)
    OFFSET_FROM_CENTER = (-int(_TopButtonConfig.WIDTH / 3), 0)


class TrophiesButtonImageConfig(_TopButtonImageConfig):
    IMAGE = 'dragons_game/graphics/icons/trophies.png'


class EggsButtonImageConfig(_TopButtonImageConfig):
    IMAGE = 'dragons_game/graphics/icons/eggs.png'


class FishButtonImageConfig(_TopButtonImageConfig):
    IMAGE = 'dragons_game/graphics/icons/fish.png'


class CoinsButtonImageConfig(_TopButtonImageConfig):
    IMAGE = 'dragons_game/graphics/icons/coins.png'


class _BottomButtonImageConfig(_TopAndBottomImageConfig, ABC):
    HEIGHT = int(_BottomButtonConfig.HEIGHT / 1.85)
    OFFSET_FROM_CENTER = (-int(_BottomButtonConfig.WIDTH / 3.15), 0)


class HatcheryButtonImageConfig(_BottomButtonImageConfig):
    IMAGE = 'dragons_game/graphics/icons/hatchery.png'


class DragonsButtonImageConfig(_BottomButtonImageConfig):
    IMAGE = 'dragons_game/graphics/icons/dragons.png'


class IslandsButtonImageConfig(_BottomButtonImageConfig):
    IMAGE = 'dragons_game/graphics/icons/islands.png'


class MarketButtonImageConfig(_BottomButtonImageConfig):
    IMAGE = 'dragons_game/graphics/icons/market.png'


class SettingsButtonImageConfig(_BottomButtonImageConfig):
    IMAGE = 'dragons_game/graphics/icons/settings.png'


class _TopAndBottomButtonTextConfig(ButtonTextConfig, ABC):
    COLOR = 'white'


class _TopButtonTextConfig(_TopAndBottomButtonTextConfig, ABC):
    FONT = pygame.font.Font('dragons_game/fonts/pr_viking.ttf', size=int(_TopButtonConfig.HEIGHT / 2))
    OFFSET_FROM_CENTER = (int(_TopButtonConfig.WIDTH / 10), 0)


class TrophiesButtonTextConfig(_TopButtonTextConfig):
    TEXT = '2137'


class EggsButtonTextConfig(_TopButtonTextConfig):
    TEXT = '42'


class FishButtonTextConfig(_TopButtonTextConfig):
    TEXT = '2137'


class CoinsButtonTextConfig(_TopButtonTextConfig):
    TEXT = '2137'


class _BottomButtonTextConfig(_TopAndBottomButtonTextConfig, ABC):
    FONT = pygame.font.Font('dragons_game/fonts/pr_viking.ttf', size=int(_BottomButtonConfig.HEIGHT / 2.8))
    OFFSET_FROM_CENTER = (int(_BottomButtonConfig.WIDTH / 7.7), 0)


class HatcheryButtonTextConfig(_BottomButtonTextConfig):
    TEXT = 'Hatchery'


class DragonsButtonTextConfig(_BottomButtonTextConfig):
    TEXT = 'Dragons'


class IslandsButtonTextConfig(_BottomButtonTextConfig):
    TEXT = 'Islands'


class MarketButtonTextConfig(_BottomButtonTextConfig):
    TEXT = 'Market'


class SettingsButtonTextConfig(_BottomButtonTextConfig):
    TEXT = 'Settings'


class _TopAndBottomButtonTextBorderConfig(TextBorderConfig):
    COLOR = 'black'
    THICKNESS = 3


TrophiesButtonTextBorderConfig = EggsButtonTextBorderConfig = FishButtonTextBorderConfig = CoinsButtonTextBorderConfig \
    = HatcheryButtonTextBorderConfig = DragonsButtonTextBorderConfig = IslandsButtonTextBorderConfig \
    = MarketButtonTextBorderConfig = SettingsButtonTextBorderConfig = _TopAndBottomButtonTextBorderConfig
