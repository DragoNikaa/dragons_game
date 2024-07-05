import pygame.sprite

from dragons_game import game_states
from dragons_game.game_states import GameStates
from dragons_game.text import Text


class Button(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, image_path: str, dest: tuple[int, int], state_after_click: GameStates,
                 position: str = 'center'):
        super().__init__()
        self.width = width
        self.height = height
        self.state_after_click = state_after_click
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image_shallow_copy = self.image
        self.rect = self.image.get_rect(**{position: dest})
        self.current_brightness = 0
        self.brightness_step = 5
        self.max_brightness = 25
        self.text: Text | None = None

    def add_text(self, font: pygame.font.Font, text: str, color: str | tuple[int, int, int], antialias: bool = True,
                 y_offset: int = 0) -> None:
        self.text = Text(font, text, color, (self.width // 2, self.height // 2 + y_offset), antialias)
        self.image.blit(self.text.image, self.text.rect)

    def add_text_border(self, color: str | tuple[int, int, int], thickness: int) -> None:
        if self.text is not None:
            self.text.add_text_border(color, thickness)
            self.image.blit(self.text.image, self.text.rect)

    def hover(self) -> None:
        if self.current_brightness < self.max_brightness and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.current_brightness += self.brightness_step
        elif self.current_brightness > 0:
            self.current_brightness -= self.brightness_step

        if self.current_brightness > 0:
            image_copy = self.image_shallow_copy.copy()
            image_copy.fill((self.current_brightness, self.current_brightness, self.current_brightness),
                            special_flags=pygame.BLEND_RGB_ADD)
            self.image = image_copy

    def click(self) -> None:
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            game_states.current_state = self.state_after_click

    def update(self) -> None:
        self.hover()
        self.click()
