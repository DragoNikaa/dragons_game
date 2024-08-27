from typing import Any

import pygame

from dragons_game.game_states.common.manager import GameStateManager
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.main_menu.sections.bottom_buttons import bottom_buttons_section
from dragons_game.game_states.main_menu.sections.island import island_section
from dragons_game.game_states.main_menu.sections.top_buttons import top_buttons_section
from dragons_game.user import user
from dragons_game.utils import custom_events


class MainMenuManager(GameStateManager):
    def __init__(self) -> None:
        super().__init__(top_buttons_section, bottom_buttons_section, island_section)

    def handle_event(self, event: pygame.event.Event) -> Any:
        new_state = super().handle_event(event)
        if new_state:
            return new_state

        elif event.type == custom_events.BUTTON_CLICK:
            if event.action == 'battle':
                user.current_level = event.level
                return self._change_state(GameState.BATTLE)

        elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            return self._change_state(GameState.UNKNOWN)
