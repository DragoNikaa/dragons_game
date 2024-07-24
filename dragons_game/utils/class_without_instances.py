from typing import Any


class ClassWithoutInstances:
    def __new__(cls, *args: Any, **kwargs: Any) -> 'ClassWithoutInstances':
        raise TypeError(f"Instances of {cls.__name__} cannot be created")
