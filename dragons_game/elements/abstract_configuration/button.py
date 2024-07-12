from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

import pygame


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


@dataclass(frozen=True)
class ButtonImageConfig(ABC):
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
    def X_OFFSET(self) -> int:
        ...

    @property
    @abstractmethod
    def Y_OFFSET(self) -> int:
        ...


@dataclass(frozen=True)
class ButtonTextConfig(ABC):
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
    def X_OFFSET(self) -> int:
        ...

    @property
    @abstractmethod
    def Y_OFFSET(self) -> int:
        ...
