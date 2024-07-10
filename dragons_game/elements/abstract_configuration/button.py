from abc import ABC, abstractmethod
from dataclasses import dataclass

from pygame.font import Font

from dragons_game.elements.abstract_configuration.position import Position
from dragons_game.game_states.game_state import GameState


@dataclass
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
    def POSITION(self) -> Position:
        ...

    @property
    @abstractmethod
    def DESTINATION(self) -> tuple[int, int]:
        ...

    @property
    @abstractmethod
    def AFTER_CLICK_STATE(self) -> GameState:
        ...


@dataclass
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


@dataclass
class ButtonTextConfig(ABC):
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
    def X_OFFSET(self) -> int:
        ...

    @property
    @abstractmethod
    def Y_OFFSET(self) -> int:
        ...
