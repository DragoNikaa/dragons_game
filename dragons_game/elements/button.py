import pygame.sprite

import dragons_game.game.update
from dragons_game.elements.abstract_configuration.button import ButtonConfig, ButtonImageConfig, ButtonTextConfig
from dragons_game.elements.abstract_configuration.text import TextBorderConfig
from dragons_game.elements.image import Image
from dragons_game.elements.text import Text
from dragons_game.user_event import UserEvent


class Button(pygame.sprite.Sprite):
    def __init__(self, button_config: ButtonConfig):
        super().__init__()

        self._button_config = button_config

        self.image = pygame.image.load(button_config.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (button_config.WIDTH, button_config.HEIGHT))
        self.rect = self.image.get_rect(**{button_config.POSITION: button_config.DESTINATION})

        self._current_brightness = 0
        self._brightness_step = 5
        self._max_brightness = 25

        self._image_without_brightness = self.image.copy()

    def add_image(self, image_config: ButtonImageConfig) -> Image:
        image_config.DESTINATION = (
            self.rect.centerx + image_config.OFFSET_FROM_CENTER[0],
            self.rect.centery + image_config.OFFSET_FROM_CENTER[1])
        return Image(image_config)

    def add_text(self, text_config: ButtonTextConfig, text_border_config: TextBorderConfig | None = None) -> Text:
        text_config.DESTINATION = (
            self.rect.centerx + text_config.OFFSET_FROM_CENTER[0],
            self.rect.centery + text_config.OFFSET_FROM_CENTER[1])
        return Text(text_config, text_border_config)

    def _handle_click(self) -> None:
        if self._button_config.CLICK_ACTION is None:
            return

        game = dragons_game.game.update.game_update

        if game.current_event_type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.event.post(pygame.event.Event(UserEvent.BUTTON_CLICK, self._button_config.CLICK_ACTION))

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

    def update(self) -> None:
        self._handle_click()
        self._handle_hover()
