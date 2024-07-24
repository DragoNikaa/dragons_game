from typing import Any

import pygame

from dragons_game.game_states.common.manager import GameStateManager
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.start_screen.sections.start_screen import start_screen_section


class StartScreenManager(GameStateManager):
    _elements = pygame.sprite.Group(start_screen_section.elements)

    @staticmethod
    def handle_event(event: pygame.event.Event) -> Any:
        new_state = GameStateManager.handle_event(event)
        if new_state:
            return new_state

        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            return GameState.MAIN_MENU
