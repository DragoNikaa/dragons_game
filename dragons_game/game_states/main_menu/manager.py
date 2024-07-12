from typing import Any

import pygame

from dragons_game.user_event import user_event, user_event_dict_key, user_event_dict_value
from dragons_game.game_states.abstract_manager import GameStateManager
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.main_menu.elements import main_menu_elements


class MainMenuManager(GameStateManager):
    def __init__(self) -> None:
        super().__init__(main_menu_elements)

    def handle_event(self, event: pygame.event.Event) -> Any:
        if event.type == user_event.BUTTON_CLICK:
            if getattr(event, user_event_dict_key.ACTION) == user_event_dict_value.CHANGE_STATE:
                return getattr(event, user_event_dict_key.NEXT_STATE)
            elif getattr(event, user_event_dict_key.ACTION) == user_event_dict_value.SHOW_TOOLTIP:
                getattr(event, user_event_dict_key.TOOLTIP)()

        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            return GameState.UNKNOWN
