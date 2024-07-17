from abc import ABC, abstractmethod
from dataclasses import dataclass

import pygame

from dragons_game.elements.abstract_configuration.position import Position


@dataclass(frozen=True)
class TextConfig(ABC):
    @property
    @abstractmethod
    def FONT(self) -> pygame.font.Font:
        ...

    @property
    @abstractmethod
    def TEXT(self) -> str:
        ...

    @property
    @abstractmethod
    def COLOR(self) -> str | tuple[int, int, int]:
        ...

    @property
    @abstractmethod
    def POSITION(self) -> str:
        ...

    @property
    @abstractmethod
    def DESTINATION(self) -> tuple[int, int]:
        ...


@dataclass(frozen=True)
class TextBorderConfig(ABC):
    @property
    @abstractmethod
    def COLOR(self) -> str | tuple[int, int, int]:
        ...

    @property
    @abstractmethod
    def THICKNESS(self) -> int:
        ...


@dataclass
class ButtonTextConfig(ABC):
    POSITION: str = Position.CENTER
    DESTINATION: tuple[int, int] = (0, 0)

    @property
    @abstractmethod
    def FONT(self) -> pygame.font.Font:
        ...

    @property
    @abstractmethod
    def TEXT(self) -> str:
        ...

    @property
    @abstractmethod
    def COLOR(self) -> str | tuple[int, int, int]:
        ...

    @property
    @abstractmethod
    def OFFSET_FROM_CENTER(self) -> tuple[int, int]:
        ...
