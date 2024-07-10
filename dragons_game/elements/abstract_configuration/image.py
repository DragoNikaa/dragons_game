from abc import ABC, abstractmethod
from dataclasses import dataclass

from dragons_game.elements.abstract_configuration.position import Position


@dataclass
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
    def POSITION(self) -> Position:
        ...

    @property
    @abstractmethod
    def DESTINATION(self) -> tuple[int, int]:
        ...
