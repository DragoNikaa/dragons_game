from dataclasses import dataclass

import pygame


@dataclass(frozen=True)
class UserEvent:
    BUTTON_CLICK = pygame.event.custom_type()
    BUTTON_HOVER = pygame.event.custom_type()


@dataclass(frozen=True)
class UserEventDictKey:
    ACTION = 'action'
    NEXT_STATE = 'next_state'
    TOOLTIP = 'tooltip'


@dataclass(frozen=True)
class UserEventDictValue:
    CHANGE_STATE = 'change_state'
    SHOW_TOOLTIP = 'show_tooltip'
