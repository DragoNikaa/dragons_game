from abc import ABC, abstractmethod
from dataclasses import dataclass

from dragons_game.elements.abstract_configuration.position import Position


@dataclass(frozen=True)
class ImageConfig(ABC):
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
