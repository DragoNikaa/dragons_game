from abc import ABC, abstractmethod
from typing import Any

import pygame


class GameStateManager(ABC):
    def __init__(self, elements: 'pygame.sprite.Group[Any]') -> None:
        self._elements = elements

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> Any:
        ...

    def update(self) -> None:
        self._elements.update()

    def draw(self, screen: pygame.Surface) -> None:
        self._elements.draw(screen)
