from typing import Iterable, TYPE_CHECKING

import pygame

from dragons_game.elements.custom_sprite import CustomSprite
from dragons_game.utils import custom_exceptions, custom_types

if TYPE_CHECKING:
    from dragons_game.elements.button import Button
    from dragons_game.elements.image import Image
    from dragons_game.elements.text import Text


class Section(CustomSprite):
    def __init__(self, size: tuple[float, float], position: custom_types.Position,
                 destination: tuple[float, float] = (0, 0), image: pygame.Surface | None = None):
        super().__init__(position, destination, image, size)

        self._elements: dict[str, CustomSprite] = {}

    def add_element(self, name: str, element: CustomSprite) -> None:
        if name in self._elements:
            raise custom_exceptions.ElementAlreadyInSectionError(name)

        self.upsert_element(name, element)

    def upsert_element(self, name: str, element: CustomSprite) -> None:
        if name in self._elements:
            self.remove_element(name)

        section_destination = getattr(self.rect, element.position)

        if isinstance(element, Section):
            for inner_element in element.all_elements:
                inner_element.rect.move_ip(section_destination)
        else:
            element.rect.move_ip(section_destination)

        self._elements[name] = element

    def remove_element(self, name: str) -> None:
        if name not in self._elements:
            raise custom_exceptions.ElementNotInSectionError(name)

        element = self._elements[name]

        if isinstance(element, Section):
            for inner_element in element.all_elements:
                setattr(inner_element.rect, inner_element.position, inner_element.destination)
        else:
            setattr(element.rect, element.position, element.destination)

        del self._elements[name]

    def remove_all_elements(self) -> None:
        element_names = list(self._elements.keys())
        for name in element_names:
            self.remove_element(name)

    def get_button(self, name: str) -> 'Button':
        from dragons_game.elements.button import Button

        element = self._get_element(name)
        if not isinstance(element, Button):
            raise custom_exceptions.IncorrectMethodError(name, self._get_expected_element_type(name, element))
        return element

    def get_image(self, name: str) -> 'Image':
        from dragons_game.elements.image import Image

        element = self._get_element(name)
        if not isinstance(element, Image):
            raise custom_exceptions.IncorrectMethodError(name, self._get_expected_element_type(name, element))
        return element

    def get_section(self, name: str) -> 'Section':
        from dragons_game.elements.button import Button

        element = self._get_element(name)
        if not isinstance(element, Section) or isinstance(element, Button):
            raise custom_exceptions.IncorrectMethodError(name, self._get_expected_element_type(name, element))
        return element

    def get_text(self, name: str) -> 'Text':
        from dragons_game.elements.text import Text

        element = self._get_element(name)
        if not isinstance(element, Text):
            raise custom_exceptions.IncorrectMethodError(name, self._get_expected_element_type(name, element))
        return element

    def _get_element(self, name: str) -> CustomSprite:
        if name not in self._elements:
            raise custom_exceptions.ElementNotInSectionError(name)

        return self._elements[name]

    @staticmethod
    def _get_expected_element_type(name: str, element: CustomSprite) -> type[CustomSprite]:
        from dragons_game.elements.button import Button
        from dragons_game.elements.image import Image
        from dragons_game.elements.text import Text

        element_type: type[CustomSprite] | None = type(element)
        expected_types = (Button, Image, Section, Text)

        while element_type not in expected_types:
            if element_type is None:
                raise custom_exceptions.ElementTypeError(name, expected_types)
            element_type = element_type.__base__

        return element_type

    @property
    def first_level_elements(self) -> Iterable[CustomSprite]:
        return self._elements.values()

    @property
    def all_elements(self) -> list[CustomSprite]:
        elements: list[CustomSprite] = [self]

        for element in self._elements.values():
            if isinstance(element, Section):
                elements += element.all_elements
            else:
                elements.append(element)

        return elements
