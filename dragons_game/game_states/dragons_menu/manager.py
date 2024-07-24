from typing import Any

import pygame

from dragons_game.game_states.dragons_menu.sections.dragons import dragons_section
from dragons_game.game_states.dragons_menu.sections.page import page_section
from dragons_game.game_states.dragons_menu.sections.team import team_section
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section
from dragons_game.game_states.common.manager import GameStateManager
from dragons_game.game_states.game_state import GameState


class DragonsMenuManager(GameStateManager):
    _elements = pygame.sprite.Group(title_bar_section.elements, team_section.elements, dragons_section.elements,
                                    page_section.elements)

    @staticmethod
    def handle_event(event: pygame.event.Event) -> Any:
        new_state = GameStateManager.handle_event(event)
        if new_state:
            return new_state

        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            return GameState.MAIN_MENU
