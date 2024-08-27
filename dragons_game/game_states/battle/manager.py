from typing import Any

import pygame

from dragons_game.game_states.battle.sections.battle import BattleSection
from dragons_game.game_states.common.manager import GameStateManager
from dragons_game.game_states.game_state import GameState


class BattleManager(GameStateManager):
    def __init__(self) -> None:
        super().__init__(BattleSection())

    def handle_event(self, event: pygame.event.Event) -> Any:
        new_state = super().handle_event(event)
        if new_state:
            return new_state

        elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            return self._change_state(GameState.MAIN_MENU)
