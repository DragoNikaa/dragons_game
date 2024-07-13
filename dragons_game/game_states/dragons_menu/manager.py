from typing import Any

import pygame

from dragons_game.game_states.dragons_menu.elements import dragons_menu_elements
from dragons_game.game_states.abstract_manager import GameStateManager
from dragons_game.game_states.game_state import GameState
from dragons_game.user_event import UserEvent, UserEventDictKey, UserEventDictValue


class DragonsMenuManager(GameStateManager):
    def __init__(self) -> None:
        super().__init__(dragons_menu_elements)

    def handle_event(self, event: pygame.event.Event) -> Any:
        if event.type == UserEvent.BUTTON_CLICK:
            if getattr(event, UserEventDictKey.ACTION) == UserEventDictValue.CHANGE_STATE:
                return getattr(event, UserEventDictKey.NEXT_STATE)
            elif getattr(event, UserEventDictKey.ACTION) == UserEventDictValue.SHOW_TOOLTIP:
                getattr(event, UserEventDictKey.TOOLTIP)()

        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            return GameState.MAIN_MENU
