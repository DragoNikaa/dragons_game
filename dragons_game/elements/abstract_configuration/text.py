from abc import ABC, abstractmethod
from dataclasses import dataclass

import pygame


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
