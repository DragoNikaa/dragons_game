from dataclasses import dataclass

import pygame


@dataclass(frozen=True)
class _UserEvent:
    BUTTON_CLICK = pygame.event.custom_type()
    BUTTON_HOVER = pygame.event.custom_type()


@dataclass(frozen=True)
class _UserEventDictKey:
    ACTION = 'action'
    NEXT_STATE = 'next_state'
    TOOLTIP = 'tooltip'


@dataclass(frozen=True)
class _UserEventDictValue:
    CHANGE_STATE = 'change_state'
    SHOW_TOOLTIP = 'show_tooltip'


USER_EVENT = _UserEvent()
USER_EVENT_DICT_KEY = _UserEventDictKey()
USER_EVENT_DICT_VALUE = _UserEventDictValue()
