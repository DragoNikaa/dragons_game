from dragons_game.utils import custom_types
from dragons_game.elements.section import Section


class Image(Section):
    def __init__(self, outer_element: Section, image_path: str, size: tuple[float, float],
                 position: custom_types.Position, offset: tuple[float, float]):
        destination = outer_element.get_inner_element_destination(position, offset)
        super().__init__(size, position, destination, image_path)

        self._offset = offset

    @property
    def x_offset(self) -> float:
        return self._offset[0]

    @property
    def y_offset(self) -> float:
        return self._offset[1]
