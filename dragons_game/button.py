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
        self.image_without_text = self.image.copy()
        self.image_without_brightness = self.image
        self.rect = self.image.get_rect(**{position: dest})
        self.current_brightness = 0
        self.brightness_step = 5
        self.max_brightness = 25
        self.text: Text | None = None

    def add_image(self, width: int, height: int, image_path: str, x_offset: int = 0, y_offset: int = 0) -> None:
        if self.text:
            raise Exception('Image must be added before text!')
        image_surf = pygame.image.load(image_path).convert_alpha()
        image_surf = pygame.transform.scale(image_surf, (width, height))
        image_rect = image_surf.get_rect(center=(self.width // 2 + x_offset, self.height // 2 + y_offset))
        self.image.blit(image_surf, image_rect)
        self.image_without_text = self.image.copy()

    def add_text(self, font: pygame.font.Font, text: str, color: str | tuple[int, int, int], antialias: bool = True,
                 x_offset: int = 0, y_offset: int = 0) -> None:
        if self.text:
            self.image = self.image_without_brightness = self.image_without_text.copy()
        self.text = Text(font, text, color, (self.width // 2 + x_offset, self.height // 2 + y_offset), antialias)
        self.image.blit(self.text.image, self.text.rect)

    def modify_text(self, text: str) -> None:
        if not self.text:
            raise Exception('There is no self.text, use add_text instead!')
        x_offset = self.text.dest[0] - self.width // 2
        y_offset = self.text.dest[1] - self.height // 2
        self.add_text(self.text.font, text, self.text.color, self.text.antialias, x_offset, y_offset)

    def add_text_border(self, color: str | tuple[int, int, int], thickness: int) -> None:
        if self.text:
            self.text.add_text_border(color, thickness)
            self.image.blit(self.text.image, self.text.rect)

    def hover(self) -> None:
        if self.current_brightness < self.max_brightness and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.current_brightness += self.brightness_step
        elif self.current_brightness > 0:
            self.current_brightness -= self.brightness_step

        if self.current_brightness > 0:
            image_copy = self.image_without_brightness.copy()
            image_copy.fill((self.current_brightness, self.current_brightness, self.current_brightness),
                            special_flags=pygame.BLEND_RGB_ADD)
            self.image = image_copy

    def click(self) -> None:
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            game_states.current_state = self.state_after_click

    def update(self) -> None:
        self.hover()
        self.click()
