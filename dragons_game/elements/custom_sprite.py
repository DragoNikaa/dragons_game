import pygame

from dragons_game.utils import custom_types


class CustomSprite(pygame.sprite.Sprite):
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

        self.image = self.image_without_effects = image.convert_alpha()
        self.rect = self.image.get_rect(**{self._position: self._destination})

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
    def x_destination(self) -> int:
        return self._destination[0]

    @property
    def y_destination(self) -> int:
        return self._destination[1]
