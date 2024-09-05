from typing import Any

import pygame

from dragons_game.game_states.battle.battle import battle
from dragons_game.game_states.battle.sections.battlefield import BattlefieldSection
from dragons_game.game_states.battle.sections.title_bar import title_bar_section
from dragons_game.game_states.battle.sections.top_menu import EnemyHealthBarsSection, PointsBar, UserHealthBarsSection, \
    attacks_section, top_menu_section
from dragons_game.game_states.common.manager import GameStateManager
from dragons_game.game_states.game_state import GameState
from dragons_game.utils import custom_events


class BattleManager(GameStateManager):
    def __init__(self) -> None:
        super().__init__(BattlefieldSection(), title_bar_section, top_menu_section, UserHealthBarsSection(),
                         EnemyHealthBarsSection(), attacks_section, PointsBar())

    def handle_event(self, event: pygame.event.Event) -> Any:
        new_state = super().handle_event(event)
        if new_state:
            return new_state

        elif event.type == custom_events.BATTLE:
            if event.action == 'change_state':
                return self._change_state(event.next_state)

            elif event.action == 'call':
                if hasattr(event, 'kwargs'):
                    event.callable(**event.kwargs)
                else:
                    event.callable()

        elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            return self._change_state(GameState.MAIN_MENU)

    def _change_state(self, next_state: GameState) -> GameState:
        battle.clean_up()
        return super()._change_state(next_state)
