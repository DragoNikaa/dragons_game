from collections.abc import Callable


class Attack:
    def __init__(self, name: str, description: str, action: Callable[[], None]):
        self._name = name
        self._description = description
        self._action = action

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def action(self) -> Callable[[], None]:
        return self._action
