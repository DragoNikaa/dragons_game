from typing import Any

import pygame

from dragons_game.elements.section import Section
from dragons_game.game_states.common.manager import GameStateManager
from dragons_game.game_states.dragons_menu.sections.bottom_bar import bottom_bar_section
from dragons_game.game_states.dragons_menu.sections.dragon_details import DragonDetails
from dragons_game.game_states.dragons_menu.sections.dragon_list import dragon_list_section
from dragons_game.game_states.dragons_menu.sections.team import team_section
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section
from dragons_game.game_states.game_state import GameState
from dragons_game.utils.observers import Observer


class DragonsMenuManager(GameStateManager):
    def __init__(self) -> None:
        super().__init__(title_bar_section, team_section, dragon_list_section, bottom_bar_section)

        self._details: DragonDetails | None = None

        self._mouse_wheel_observers: list[Observer] = []

    def handle_event(self, event: pygame.event.Event) -> Any:
        new_state = super().handle_event(event)
        if new_state:
            return new_state

        elif event.type == pygame.MOUSEWHEEL:
            self._notify_mouse_wheel_observers(event.y)

        elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            if self._details:
                return self._change_state(GameState.DRAGONS_MENU)
            else:
                return self._change_state(GameState.MAIN_MENU)

    def _upsert_details_window(self, details: Section) -> None:
        if isinstance(details, DragonDetails):
            self._mouse_wheel_observers.append(details.description_text)
        super()._upsert_details_window(details)

    def _remove_details_window(self) -> None:
        if self._details:
            self._details.clean_up()
            self._mouse_wheel_observers.remove(self._details.description_text)
        super()._remove_details_window()

    def _notify_mouse_wheel_observers(self, y: int) -> None:
        for observer in self._mouse_wheel_observers:
            observer.update_on_notify(y)
