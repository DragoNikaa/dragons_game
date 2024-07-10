from abc import ABC, abstractmethod
from dataclasses import dataclass

from pygame.font import Font

from dragons_game.elements.abstract_configuration.position import Position


@dataclass
class TextConfig(ABC):
    @property
    @abstractmethod
    def FONT(self) -> Font:
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
    def POSITION(self) -> Position:
        ...

    @property
    @abstractmethod
    def DESTINATION(self) -> tuple[int, int]:
        ...


@dataclass
class TextBorderConfig(ABC):
    @property
    @abstractmethod
    def COLOR(self) -> str | tuple[int, int, int]:
        ...

    @property
    @abstractmethod
    def THICKNESS(self) -> int:
        ...
