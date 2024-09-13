from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any

import pygame

from dragons_game.utils import custom_types


class CustomSprite(pygame.sprite.Sprite, ABC):
    @abstractmethod
    def __init__(self, position: custom_types.Position, destination: tuple[float, float],
                 image: pygame.Surface | None = None, size: tuple[float, float] | None = None):
        super().__init__()

        self._position = str(position)
        self._destination = round(destination[0]), round(destination[1])

        if size is None:
            size = (0, 0)
        else:
            size = round(size[0]), round(size[1])

        if image is None:
            image = pygame.Surface(size, flags=pygame.SRCALPHA)
        else:
            image = pygame.transform.scale(image, size)

        self.image = image.convert_alpha()
        self._original_image = self.image.copy()
        self._image_without_effects = self.image.copy()
        self.rect = self.image.get_rect(**{self._position: self._destination})

    def set_image(self, new_image: pygame.Surface) -> None:
        self.add_temporary_image(new_image)
        self._original_image = self.image.copy()

    def add_temporary_image(self, new_image: pygame.Surface) -> None:
        self.image = new_image.convert_alpha()
        self._image_without_effects = self.image.copy()

    def remove_temporary_image(self) -> None:
        self.image = self._original_image.copy()
        self._image_without_effects = self.image.copy()

    def transform_image(self, transform_callable: Callable[..., pygame.Surface], *callable_args: Any) -> None:
        self.image = transform_callable(self._image_without_effects, *callable_args).convert_alpha()
        self._image_without_effects = self.image.copy()

    @property
    def image_copy(self) -> pygame.Surface:
        return self._image_without_effects.copy()

    @property
    def size(self) -> tuple[int, int]:
        return self.rect.size

    @property
    def width(self) -> int:
        return self.rect.width

    @property
    def height(self) -> int:
        return self.rect.height

    @property
    def position(self) -> str:
        return self._position

    @property
    def destination(self) -> tuple[int, int]:
        return self._destination

    @destination.setter
    def destination(self, new_destination: tuple[int, int]) -> None:
        from dragons_game.elements.section import Section

        new_destination = round(new_destination[0]), round(new_destination[1])
        destination_difference = new_destination[0] - self.x_destination, new_destination[1] - self.y_destination

        if isinstance(self, Section):
            for element in self.all_elements:
                element.rect.move_ip(destination_difference)
        else:
            self.rect.move_ip(destination_difference)

        self._destination = new_destination

    @property
    def x_destination(self) -> int:
        return self._destination[0]

    @property
    def y_destination(self) -> int:
        return self._destination[1]
