from abc import ABC, abstractmethod
from typing import Any


class ObserverClass(ABC):
    @classmethod
    @abstractmethod
    def update_on_notify(cls, *args: Any, **kwargs: Any) -> None:
        ...


class Observer(ABC):
    @abstractmethod
    def update_on_notify(self, *args: Any, **kwargs: Any) -> None:
        ...
