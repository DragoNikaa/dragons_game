from abc import ABC, abstractmethod
from typing import Any

import pygame

from dragons_game.elements.section import Section
from dragons_game.elements.tooltip import Tooltip
from dragons_game.utils import custom_events
from dragons_game.utils.observers import Observer


class GameStateManager(Observer, ABC):
    def __init__(self, *sections: Section):
        super().__init__()

        for section in sections:
            section.add_observer(self)

        self._section_to_elements = {section: pygame.sprite.Group(*section.elements) for section in sections}
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
                    self._section_to_elements[self._tooltip] = pygame.sprite.Group(*self._tooltip.elements)

            elif event.action == 'end_hover':
                self._remove_tooltip()

    def update(self) -> None:
        for elements in self._section_to_elements.values():
            elements.update()

    def draw(self, screen: pygame.Surface) -> None:
        for elements in self._section_to_elements.values():
            elements.draw(screen)

    def update_on_notify(self, section: Section) -> None:
        self._section_to_elements[section] = pygame.sprite.Group(*section.elements)

    def _remove_tooltip(self) -> None:
        if self._tooltip:
            del self._section_to_elements[self._tooltip]
            self._tooltip = None
