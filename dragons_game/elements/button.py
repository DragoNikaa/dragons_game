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

        self._BRIGHTNESS_STEP = 5
        self._MAX_BRIGHTNESS = 25

        self._current_brightness = 0
        self.image_without_brightness = self.image

        self._elements: list[Image | Text] = []

    def add_image(self, image_config: ButtonImageConfig) -> Image:
        image_config.DESTINATION = self._get_element_destination(image_config)
        image = Image(image_config)
        self._elements.append(image)
        return image

    def add_text(self, text_config: ButtonTextConfig, text_border_config: TextBorderConfig | None = None) -> Text:
        text_config.DESTINATION = self._get_element_destination(text_config)
        text = Text(text_config, text_border_config)
        self._elements.append(text)
        return text

    def update(self) -> None:
        self._handle_click()
        self._handle_hover()

    def _get_element_destination(self, element_config: ButtonImageConfig | ButtonTextConfig) -> tuple[int, int]:
        return (self.rect.centerx + element_config.OFFSET_FROM_CENTER[0],
                self.rect.centery + element_config.OFFSET_FROM_CENTER[1])

    def _handle_click(self) -> None:
        if self._button_config.CLICK_ACTION is None:
            return

        game = dragons_game.game.update.game_update

        if game.current_event_type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.event.post(pygame.event.Event(UserEvent.BUTTON_CLICK, self._button_config.CLICK_ACTION))

    def _handle_hover(self) -> None:
        self._highlight()

    def _highlight(self) -> None:
        if self._update_current_brightness():
            self._update_image(self)
            for element in self._elements:
                self._update_image(element)

    def _update_current_brightness(self) -> bool:
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self._current_brightness < self._MAX_BRIGHTNESS:
                self._current_brightness += self._BRIGHTNESS_STEP
                return True

        elif self._current_brightness > 0:
            self._current_brightness -= self._BRIGHTNESS_STEP
            return True

        return False

    def _update_image(self, element: 'Button | Image | Text') -> None:
        image_copy = element.image_without_brightness.copy()
        image_copy.fill((self._current_brightness, self._current_brightness, self._current_brightness),
                        special_flags=pygame.BLEND_RGB_ADD)
        element.image = image_copy
