import pygame.sprite

from dragons_game.elements.abstract_configuration.button import ButtonConfig, ButtonImageConfig, ButtonTextConfig
from dragons_game.elements.abstract_configuration.text import TextBorderConfig
from dragons_game.elements.image import Image
from dragons_game.elements.text import Text
from dragons_game.event import BUTTON_CLICK


class Button(pygame.sprite.Sprite):
    def __init__(self, button_config: ButtonConfig, image_config: ButtonImageConfig | None = None,
                 text_config: ButtonTextConfig | None = None, text_border_config: TextBorderConfig | None = None):
        super().__init__()

        self._button_config = button_config
        self._image_config = image_config
        self._text_config = text_config
        self._text_border_config = text_border_config

        self.image = pygame.image.load(button_config.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (button_config.WIDTH, button_config.HEIGHT))
        self.rect = self.image.get_rect(**{button_config.POSITION.value: button_config.DESTINATION})

        self._current_brightness = 0
        self._brightness_step = 5
        self._max_brightness = 25

        if image_config:
            self._image = Image(image_config)
            self._add_image()

        if text_config:
            self._image_without_text = self.image.copy()
            self._text = Text(text_config, text_border_config=text_border_config)
            self._add_text()

        self._image_without_brightness = self.image.copy()

    def _add_image(self) -> None:
        if not self._image_config:
            return

        self._image.rect.center = (self._button_config.WIDTH // 2 + self._image_config.X_OFFSET,
                                   self._button_config.HEIGHT // 2 + self._image_config.Y_OFFSET)
        self.image.blit(self._image.image, self._image.rect)

    def _add_text(self) -> None:
        if not self._text_config:
            return

        self._text.rect.center = (self._button_config.WIDTH // 2 + self._text_config.X_OFFSET,
                                  self._button_config.HEIGHT // 2 + self._text_config.Y_OFFSET)
        self.image.blit(self._text.image, self._text.rect)

    def change_text(self, new_text: str) -> None:
        self.image = self._image_without_text.copy()
        self._text.change_text(new_text)
        self._add_text()
        self._image_without_brightness = self.image.copy()

    def _handle_hover(self) -> None:
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self._current_brightness < self._max_brightness:
                self._current_brightness += self._brightness_step
        elif self._current_brightness > 0:
            self._current_brightness -= self._brightness_step

        if self._current_brightness > 0:
            image_copy = self._image_without_brightness.copy()
            image_copy.fill((self._current_brightness, self._current_brightness, self._current_brightness),
                            special_flags=pygame.BLEND_RGB_ADD)
            self.image = image_copy

    def _handle_click(self) -> None:
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.event.post(pygame.event.Event(BUTTON_CLICK))

    def update(self) -> None:
        self._handle_hover()
        self._handle_click()
