from typing import Any

import pygame

from dragons_game.game_states.common.manager import GameStateManager
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.main_menu.sections.bottom_buttons import bottom_buttons_section
from dragons_game.game_states.main_menu.sections.island import island_section
from dragons_game.game_states.main_menu.sections.top_buttons import top_buttons_section


class MainMenuManager(GameStateManager):
    _elements = pygame.sprite.Group(top_buttons_section.elements, bottom_buttons_section.elements,
                                    island_section.elements)

    @staticmethod
    def handle_event(event: pygame.event.Event) -> Any:
        new_state = GameStateManager.handle_event(event)
        if new_state:
            return new_state

        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            return GameState.UNKNOWN
