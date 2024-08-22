from typing import Any

import pygame

from dragons_game.game_states.common.manager import GameStateManager
from dragons_game.game_states.loading_screen.sections.loading_screen import loading_screen_section


class LoadingScreenManager(GameStateManager):
    def __init__(self) -> None:
        super().__init__(loading_screen_section)

    def handle_event(self, event: pygame.event.Event) -> Any:
        pass
