from abc import ABC, abstractmethod
from typing import Any

import pygame

from dragons_game.elements.section import Section
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game_states.game_state import GameState
from dragons_game.utils import custom_events


class GameStateManager(ABC):
    @abstractmethod
    def __init__(self, *sections: Section):
        super().__init__()

        self._sections = [*sections]
        self._active_sections = self._sections.copy()

        self._details: Section | None = None
        self._tooltip: Tooltip | None = None

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> Any:
        if event.type == custom_events.BUTTON_CLICK:
            if event.action == 'change_state':
                return self._change_state(event.next_state)

            elif event.action == 'call':
                if hasattr(event, 'kwargs'):
                    event.callable(**event.kwargs)
                else:
                    event.callable()

            elif event.action == 'open_details':
                self._upsert_details_window(event.details)

            elif event.action == 'close_details':
                self._remove_details_window()

        elif event.type == custom_events.BUTTON_HOVER:
            if event.action == 'show_tooltip':
                self._upsert_tooltip(event.tooltip)

            elif event.action == 'hide_tooltip':
                self._remove_tooltip()

    def update(self) -> None:
        for section in self._active_sections:
            pygame.sprite.Group(*section.all_elements).update()

    def draw(self, screen: pygame.Surface) -> None:
        for section in self._sections:
            pygame.sprite.Group(*section.all_elements).draw(screen)

    def _change_state(self, next_state: GameState) -> GameState:
        self._remove_details_window()
        self._remove_tooltip()
        return next_state

    def _upsert_details_window(self, details: Section) -> None:
        self._remove_details_window()

        for section in self._sections:
            if details.rect.colliderect(section.rect):
                self._active_sections.remove(section)

        self._details = details
        self._sections.append(details)
        self._active_sections.append(details)

    def _remove_details_window(self) -> None:
        if self._details:
            self._sections.remove(self._details)
            self._active_sections = self._sections.copy()
            self._details = None

    def _upsert_tooltip(self, tooltip: Tooltip) -> None:
        self._remove_tooltip()

        self._tooltip = tooltip
        self._sections.append(tooltip)
        self._active_sections.append(tooltip)

    def _remove_tooltip(self) -> None:
        if self._tooltip:
            self._sections.remove(self._tooltip)
            self._active_sections.remove(self._tooltip)
            self._tooltip = None
