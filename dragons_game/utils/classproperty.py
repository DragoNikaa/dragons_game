from typing import Any


class classproperty(property):
    def __get__(self, instance: object, owner: type | None = None) -> Any:
        if self.fget is not None:
            return self.fget(owner)
