from abc import ABC, abstractmethod
from typing import Any

import pygame

from dragons_game.elements.custom_sprite import CustomSprite
from dragons_game.utils import custom_events
from dragons_game.elements.section import Section


class GameStateManager(ABC):
    def __init__(self, *sections: Section):
        super().__init__()

        self._elements = pygame.sprite.Group(*[section.elements for section in sections])
        self._tooltip_elements: list[CustomSprite] | None = None

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> Any:
        if event.type == custom_events.BUTTON_CLICK:
            if event.action == 'change_state':
                self._remove_tooltip()
                return event.next_state

        if event.type == custom_events.BUTTON_HOVER:
            if event.action == 'show_tooltip':
                if self._tooltip_elements is None:
                    self._tooltip_elements = event.tooltip.elements
                    self._elements.add(*self._tooltip_elements)

            elif event.action == 'end_hover':
                self._remove_tooltip()

    def update(self) -> None:
        self._elements.update()

    def draw(self, screen: pygame.Surface) -> None:
        self._elements.draw(screen)

    def _remove_tooltip(self) -> None:
        if self._tooltip_elements:
            self._elements.remove(*self._tooltip_elements)
            self._tooltip_elements = None
