from abc import abstractmethod
from typing import Any

import pygame

from dragons_game.utils import custom_events
from dragons_game.utils.class_without_instances import ClassWithoutInstances
from dragons_game.elements.elements_section import ElementsSection
from dragons_game.elements.text import Text


class GameStateManager(ClassWithoutInstances):
    _elements: 'pygame.sprite.Group[ElementsSection | Text]'

    @staticmethod
    @abstractmethod
    def handle_event(event: pygame.event.Event) -> Any:
        if event.type == custom_events.BUTTON_CLICK:
            if event.action == 'change_state':
                return event.next_state
            elif event.action == 'show_tooltip':
                event.tooltip()

    @classmethod
    def update(cls) -> None:
        cls._elements.update()

    @classmethod
    def draw(cls, screen: pygame.Surface) -> None:
        cls._elements.draw(screen)
