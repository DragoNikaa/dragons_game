from abc import ABC, abstractmethod
from typing import Any

import pygame

from dragons_game.elements.custom_sprite import CustomSprite
from dragons_game.elements.section import Section
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game_states.game_state import GameState
from dragons_game.utils import custom_events
from dragons_game.utils.observers import Observer


class GameStateManager(Observer, ABC):
    @abstractmethod
    def __init__(self, *sections: Section):
        super().__init__()

        self._elements: pygame.sprite.Group[CustomSprite] = pygame.sprite.Group()

        for section in sections:
            for element in section.elements:
                self._elements.add(element)

                if isinstance(element, Section):
                    element.add_observer(self)

        self._details: Section | None = None
        self._tooltip: Tooltip | None = None

        self._removed_elements: list[CustomSprite] = []

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> Any:
        if event.type == custom_events.BUTTON_CLICK:
            if event.action == 'change_state':
                return self._change_state(event.next_state)

            elif event.action == 'call':
                event.callable()

            elif event.action == 'open_details':
                self._upsert_details_window(event.details)

            elif event.action == 'close_details':
                self._remove_details_window()

        elif event.type == custom_events.BUTTON_HOVER:
            if event.action == 'show_tooltip':
                self._add_tooltip(event.tooltip)

            elif event.action == 'hide_tooltip':
                self._remove_tooltip()

    def update(self) -> None:
        self._elements.update()

    def draw(self, screen: pygame.Surface) -> None:
        self._elements.draw(screen)

    def update_on_notify(self, added_elements: list[CustomSprite] | None = None,
                         removed_elements: list[CustomSprite] | None = None) -> None:
        if added_elements:
            self._elements.add(*added_elements)
        if removed_elements:
            self._elements.remove(*removed_elements)

    def _change_state(self, next_state: GameState) -> GameState:
        self._remove_details_window()
        self._remove_tooltip()
        return next_state

    def _upsert_details_window(self, details: Section) -> None:
        self._remove_details_window()

        for element in self._elements:
            if element.rect.colliderect(details.rect):
                self._removed_elements.append(element)
                self._elements.remove(element)

        self._details = details
        self._elements.add(*details.elements)

    def _remove_details_window(self) -> None:
        if self._details:
            self._elements.remove(*self._details.elements)
            self._details = None

            if self._tooltip:
                self._elements.remove(*self._tooltip.elements)

            self._elements.add(*self._removed_elements)
            self._removed_elements.clear()

            if self._tooltip:
                self._elements.add(*self._tooltip.elements)

    def _add_tooltip(self, tooltip: Tooltip) -> None:
        self._tooltip = tooltip
        self._elements.add(*tooltip.elements)

    def _remove_tooltip(self) -> None:
        if self._tooltip:
            self._elements.remove(*self._tooltip.elements)
            self._tooltip = None
