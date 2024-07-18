from typing import Callable


class Attack:
    def __init__(self, name: str, description: str, action: Callable[[], None]):
        self._name = name
        self._description = description
        self._action = action
