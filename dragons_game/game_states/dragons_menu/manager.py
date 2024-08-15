from typing import Any

import pygame

from dragons_game.game_states.common.manager import GameStateManager
from dragons_game.game_states.dragons_menu.sections.bottom_bar import bottom_bar_section
from dragons_game.game_states.dragons_menu.sections.dragon_list import dragon_list_section
from dragons_game.game_states.dragons_menu.sections.team import team_section
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section
from dragons_game.game_states.game_state import GameState


class DragonsMenuManager(GameStateManager):
    def __init__(self) -> None:
        super().__init__(title_bar_section, team_section, dragon_list_section, bottom_bar_section)

    def handle_event(self, event: pygame.event.Event) -> Any:
        new_state = super().handle_event(event)
        if new_state:
            return new_state

        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            if self._details:
                self._remove_details_window()
            else:
                return self._change_state(GameState.MAIN_MENU)
