from typing import Any

import pygame

from dragons_game.game_states.dragons_menu.elements import dragons_menu_elements
from dragons_game.user_event import USER_EVENT, USER_EVENT_DICT_KEY, USER_EVENT_DICT_VALUE
from dragons_game.game_states.abstract_manager import GameStateManager
from dragons_game.game_states.game_state import GameState


class DragonsMenuManager(GameStateManager):
    def __init__(self) -> None:
        super().__init__(dragons_menu_elements)

    def handle_event(self, event: pygame.event.Event) -> Any:
        if event.type == USER_EVENT.BUTTON_CLICK:
            if getattr(event, USER_EVENT_DICT_KEY.ACTION) == USER_EVENT_DICT_VALUE.CHANGE_STATE:
                return getattr(event, USER_EVENT_DICT_KEY.NEXT_STATE)
            elif getattr(event, USER_EVENT_DICT_KEY.ACTION) == USER_EVENT_DICT_VALUE.SHOW_TOOLTIP:
                getattr(event, USER_EVENT_DICT_KEY.TOOLTIP)()

        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            return GameState.MAIN_MENU
