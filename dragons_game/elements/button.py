from typing import Any

import pygame.sprite

from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.utils import custom_events, custom_types


class Button(Section):
    _BRIGHTNESS_STEP = 5
    _MAX_BRIGHTNESS = 25

    def __init__(self, image_path: str, size: tuple[float, float], position: custom_types.Position,
                 destination: tuple[float, float], click_action: custom_types.CustomEventDict | None = None,
                 hover_action: custom_types.CustomEventDict | None = None):
        image = pygame.image.load(image_path)
        super().__init__(size, position, destination, image)

        self._click_action = self._adjust_action(click_action)
        self._hover_action = self._adjust_action(hover_action)

        self._mouse_pressed_outside = self._mouse_pressed_inside = self._mouse_released = False
        self._hover_active = False

        self._current_brightness = 0

    def update(self) -> None:
        self._handle_click()
        self._handle_hover()

    def _handle_click(self) -> None:
        if self._click_action:
            mouse_pressed = pygame.mouse.get_pressed()[0]
            mouse_collision = self._check_mouse_collision()

            if mouse_pressed:
                if not mouse_collision:
                    self._mouse_pressed_outside = True
            else:
                self._mouse_pressed_outside = False

            if not self._mouse_pressed_outside:
                if mouse_collision:
                    if mouse_pressed:
                        self._mouse_pressed_inside = True
                    elif self._mouse_pressed_inside:
                        self._mouse_released = True

                    if self._mouse_released:
                        self._mouse_pressed_inside = self._mouse_released = False
                        pygame.event.post(pygame.event.Event(custom_events.BUTTON_CLICK, self._click_action))

                else:
                    self._mouse_pressed_inside = False

    def _handle_hover(self) -> None:
        self._highlight()

        if self._hover_action:
            if self._check_mouse_collision():
                self._hover_active = True
                pygame.event.post(pygame.event.Event(custom_events.BUTTON_HOVER, self._hover_action))

            elif self._hover_active:
                self._hover_active = False
                pygame.event.post(pygame.event.Event(custom_events.BUTTON_HOVER, {'action': 'end_hover'}))

    def _check_mouse_collision(self) -> bool:
        mouse_position = pygame.mouse.get_pos()

        if not self.rect.collidepoint(mouse_position):
            return False

        for element in self._elements.values():
            if isinstance(element, Button) and element.rect.collidepoint(mouse_position):
                return False
        return True

    def _highlight(self) -> None:
        if self._update_current_brightness():
            self._update_element_image(self)

            for element in self._elements.values():
                if isinstance(element, (Image, Text)):
                    self._update_element_image(element)

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

    @staticmethod
    def _adjust_action(action: custom_types.CustomEventDict | None) -> dict[str, Any] | None:
        if action is None:
            return None

        return {str(key): value for key, value in action.items()}
