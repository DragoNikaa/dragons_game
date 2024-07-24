from dragons_game.utils import custom_types
from dragons_game.elements.elements_section import ElementsSection


class Image(ElementsSection):
    def __init__(self, outer_element: ElementsSection, image_path: str, size: tuple[float, float],
                 position: custom_types.Position, offset: tuple[float, float]):
        destination = outer_element.get_inner_element_destination(position, offset)
        super().__init__(size, position, destination, image_path)
