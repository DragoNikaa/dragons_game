from typing import Any

import pygame.sprite

import dragons_game.game.game
from dragons_game.elements.image import Image
from dragons_game.elements.text import Text
from dragons_game.utils import custom_types, custom_events
from dragons_game.elements.elements_section import ElementsSection


class Button(ElementsSection):
    _BRIGHTNESS_STEP = 5
    _MAX_BRIGHTNESS = 25

    def __init__(self, outer_element: ElementsSection, image_path: str, size: tuple[float, float],
                 position: custom_types.Position, offset: tuple[float, float],
                 click_action: custom_types.CustomEventDict | None = None,
                 hover_action: custom_types.CustomEventDict | None = None):
        destination = outer_element.get_inner_element_destination(position, offset)
        super().__init__(size, position, destination, image_path)

        self._offset = offset

        self._click_action = self._adjust_action(click_action)
        self._hover_action = self._adjust_action(hover_action)

        self._current_brightness = 0

    def update(self) -> None:
        self._handle_click()
        self._handle_hover()

    def _handle_click(self) -> None:
        if self._click_action:
            Game = dragons_game.game.game.Game

            if Game.get_current_event_type() == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.event.post(pygame.event.Event(custom_events.BUTTON_CLICK, self._click_action))

    def _handle_hover(self) -> None:
        self._highlight()

    def _highlight(self) -> None:
        if self._update_current_brightness():
            self._update_element_image(self)
            for image in self._images.values():
                self._update_element_image(image)
            for text in self._texts.values():
                self._update_element_image(text)

    def _update_current_brightness(self) -> bool:
        if self._check_mouse_collision():
            if self._current_brightness < self._MAX_BRIGHTNESS:
                self._current_brightness += self._BRIGHTNESS_STEP
                return True

        elif self._current_brightness > 0:
            self._current_brightness -= self._BRIGHTNESS_STEP
            return True

        return False

    def _update_element_image(self, element: 'Button | Image | Text') -> None:
        image_copy = element.image_without_effects.copy()
        image_copy.fill((self._current_brightness, self._current_brightness, self._current_brightness),
                        special_flags=pygame.BLEND_RGB_ADD)
        element.image = image_copy

    def _check_mouse_collision(self) -> bool:
        mouse_position = pygame.mouse.get_pos()

        if not self.rect.collidepoint(mouse_position):
            return False

        for button in self._buttons.values():
            if button.rect.collidepoint(mouse_position):
                return False
        return True

    @staticmethod
    def _adjust_action(action: custom_types.CustomEventDict | None) -> dict[str, Any] | None:
        if action is None:
            return None

        return {str(key): value for key, value in action.items()}

    @property
    def x_offset(self) -> float:
        return self._offset[0]

    @property
    def y_offset(self) -> float:
        return self._offset[1]
