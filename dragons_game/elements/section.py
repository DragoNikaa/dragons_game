from typing import TYPE_CHECKING

import pygame

from dragons_game.utils import custom_types

if TYPE_CHECKING:
    from dragons_game.elements.button import Button
    from dragons_game.elements.image import Image
    from dragons_game.elements.text import Text


class Section(pygame.sprite.Sprite):
    def __init__(self, size: tuple[float, float], position: custom_types.Position,
                 destination: tuple[float, float] = (0, 0), image_path: str = '', fill_color: custom_types.Color = 0):
        super().__init__()

        self._size = int(size[0]), int(size[1])
        self._position = str(position)

        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, size)
        else:
            self.image = pygame.Surface(size)
            self.image.fill(fill_color)
        self.image_without_effects = self.image

        self.rect = self.image.get_rect(**{self._position: destination})

        self._buttons: dict[str, 'Button'] = {}
        self._images: dict[str, 'Image'] = {}
        self._texts: dict[str, 'Text'] = {}

    def add_button(self, name: str, button: 'Button') -> None:
        self._buttons[name] = button

    def add_image(self, name: str, image: 'Image') -> None:
        self._images[name] = image

    def add_text(self, name: str, text: 'Text') -> None:
        self._texts[name] = text

    def get_inner_element_destination(self, position: custom_types.Position, offset: tuple[float, float]) -> tuple[
        float, float]:
        outer_element_position_destination = getattr(self.rect, position)
        return outer_element_position_destination[0] + offset[0], outer_element_position_destination[1] + offset[1]

    def get_button(self, name: str) -> 'Button':
        return self._buttons[name]

    def get_image(self, name: str) -> 'Image':
        return self._images[name]

    def get_text(self, name: str) -> 'Text':
        return self._texts[name]

    @property
    def elements(self) -> 'list[Section | Text]':
        elements: 'list[Section | Text]' = [self]
        for image_or_button in {**self._images, **self._buttons}.values():
            elements += image_or_button.elements
        elements += [*{**self._texts}.values()]
        return elements

    @property
    def width(self) -> int:
        return self._size[0]

    @property
    def height(self) -> int:
        return self._size[1]
