from abc import ABC, abstractmethod
from typing import Any

import pygame

from dragons_game.utils import custom_events
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text


class GameStateManager(ABC):
    def __init__(self, *sections: Section):
        self._elements = pygame.sprite.Group(*[section.elements for section in sections])
        self._tooltip_elements: list[Section | Text] | None = None
        self._mouse_button_released = False

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> Any:
        if event.type == custom_events.BUTTON_PRESSED:
            if not pygame.mouse.get_pressed()[0]:
                self._mouse_button_released = True

            if self._mouse_button_released and event.action == 'change_state':
                self._clean_up()
                return event.next_state

        if event.type == custom_events.BUTTON_HOVERED_OVER:
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

    def _clean_up(self) -> None:
        self._remove_tooltip()
        self._mouse_button_released = False

    def _remove_tooltip(self) -> None:
        if self._tooltip_elements:
            self._elements.remove(*self._tooltip_elements)
            self._tooltip_elements = None
