from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

import pygame

from dragons_game.elements.abstract_configuration.position import Position


@dataclass(frozen=True)
class ButtonConfig(ABC):
    @property
    @abstractmethod
    def WIDTH(self) -> int:
        ...

    @property
    @abstractmethod
    def HEIGHT(self) -> int:
        ...

    @property
    @abstractmethod
    def IMAGE(self) -> str:
        ...

    @property
    @abstractmethod
    def POSITION(self) -> str:
        ...

    @property
    @abstractmethod
    def DESTINATION(self) -> tuple[int, int]:
        ...

    @property
    @abstractmethod
    def CLICK_ACTION(self) -> dict[str, Any] | None:
        ...

    @property
    @abstractmethod
    def HOVER_ACTION(self) -> dict[str, Any] | None:
        ...


@dataclass
class ButtonImageConfig(ABC):
    POSITION: str = Position.CENTER
    DESTINATION: tuple[int, int] = (0, 0)

    @property
    @abstractmethod
    def WIDTH(self) -> int:
        ...

    @property
    @abstractmethod
    def HEIGHT(self) -> int:
        ...

    @property
    @abstractmethod
    def IMAGE(self) -> str:
        ...

    @property
    @abstractmethod
    def OFFSET_FROM_CENTER(self) -> tuple[int, int]:
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
