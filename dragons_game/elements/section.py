import pygame

from dragons_game.elements.custom_sprite import CustomSprite
from dragons_game.utils import custom_exceptions, custom_types
from dragons_game.utils.observers import Observer


class Section(CustomSprite):
    def __init__(self, size: tuple[float, float], position: custom_types.Position,
                 destination: tuple[float, float] = (0, 0), image: pygame.Surface | None = None):
        super().__init__(position, destination, image, size)

        self._elements: dict[str, CustomSprite] = {}

        self._observers: list[Observer] = []

    def add_element(self, name: str, element: CustomSprite) -> None:
        if name in self._elements:
            raise custom_exceptions.ElementAlreadyInSectionError(name)

        self.upsert_element(name, element)

    def upsert_element(self, name: str, element: CustomSprite) -> None:
        section_destination = getattr(self.rect, element.position)

        if isinstance(element, Section):
            for inner_element in element.elements:
                inner_element.rect.move_ip(section_destination)
        else:
            element.rect.move_ip(section_destination)

        self.notify_observers(added_element=element, removed_element=getattr(self._elements, name, None))
        self._elements[name] = element

    def remove_element(self, name: str) -> None:
        if name not in self._elements:
            raise custom_exceptions.ElementNotInSectionError(name)

        self.notify_observers(removed_element=self._elements[name])
        del self._elements[name]

    def get_element(self, name: str) -> CustomSprite:
        if name not in self._elements:
            raise custom_exceptions.ElementNotInSectionError(name)

        return self._elements[name]

    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify_observers(self, added_element: CustomSprite | None = None,
                         removed_element: CustomSprite | None = None) -> None:
        for observer in self._observers:
            observer.update_on_notify(self, added_element, removed_element)

    @property
    def elements(self) -> list[CustomSprite]:
        elements: list[CustomSprite] = [self]

        for element in self._elements.values():
            if isinstance(element, Section):
                elements += element.elements
            else:
                elements.append(element)

        return elements
