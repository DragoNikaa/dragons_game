from typing import Any

import pygame

from dragons_game.game_states.common.manager import GameStateManager
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.start_screen.sections.start_screen import start_screen_section


class StartScreenManager(GameStateManager):
    def __init__(self) -> None:
        super().__init__(start_screen_section)

    def handle_event(self, event: pygame.event.Event) -> Any:
        new_state = super().handle_event(event)
        if new_state:
            return new_state

        elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            return self._change_state(GameState.MAIN_MENU)
