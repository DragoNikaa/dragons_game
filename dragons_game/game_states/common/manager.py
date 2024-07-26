from abc import ABC, abstractmethod
from typing import Any

import pygame

from dragons_game.utils import custom_events
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text


class GameStateManager(ABC):
    def __init__(self, *sections: Section):
        self._elements = pygame.sprite.Group(*[section.elements for section in sections])
        self._tooltip: list[Section | Text] | None = None

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> Any:

        if event.type == custom_events.BUTTON_CLICK:
            if event.action == 'change_state':
                return event.next_state

        if event.type == custom_events.BUTTON_HOVER:
            if event.action == 'show_tooltip':
                if self._tooltip is None:
                    self._tooltip = event.tooltip.elements
                    self._elements.add(self._tooltip)

            elif event.action == 'end_hover':
                if self._tooltip:
                    self._elements.remove(self._tooltip)
                    self._tooltip = None

    def update(self) -> None:
        self._elements.update()

    def draw(self, screen: pygame.Surface) -> None:
        self._elements.draw(screen)
