from abc import ABC, abstractmethod
from typing import Any

import pygame

from dragons_game.elements.custom_sprite import CustomSprite
from dragons_game.elements.section import Section
from dragons_game.elements.tooltip import Tooltip
from dragons_game.utils import custom_events
from dragons_game.utils.observers import Observer


class GameStateManager(Observer, ABC):
    def __init__(self, *sections: Section):
        super().__init__()

        self._elements: pygame.sprite.Group[CustomSprite] = pygame.sprite.Group()

        for section in sections:
            for element in section.elements:
                self._elements.add(element)

                if isinstance(element, Section):
                    element.add_observer(self)

        self._tooltip: Tooltip | None = None

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> Any:
        if event.type == custom_events.BUTTON_CLICK:
            if event.action == 'change_state':
                self._remove_tooltip()
                return event.next_state

            elif event.action == 'call':
                event.callable()

        elif event.type == custom_events.BUTTON_HOVER:
            if event.action == 'show_tooltip':
                if self._tooltip is None:
                    self._tooltip = event.tooltip
                    self._elements.add(*self._tooltip.elements)

            elif event.action == 'end_hover':
                self._remove_tooltip()

    def update(self) -> None:
        self._elements.update()

    def draw(self, screen: pygame.Surface) -> None:
        self._elements.draw(screen)

    def update_on_notify(self, section: Section, added_elements: list[CustomSprite] | None = None,
                         removed_elements: list[CustomSprite] | None = None) -> None:
        if added_elements:
            self._elements.add(*added_elements)
        if removed_elements:
            self._elements.remove(*removed_elements)

    def _remove_tooltip(self) -> None:
        if self._tooltip:
            self._elements.remove(*self._tooltip.elements)
            self._tooltip = None
