import pygame

from dragons_game.event import BUTTON_CLICK
from dragons_game.game.configuration import game_config
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.main_menu.elements import main_menu_elements
from dragons_game.game_states.start_screen.elements import start_screen_elements


class GameUpdate:
    def __init__(self) -> None:
        self._running = True
        self._current_state = GameState.START_SCREEN

        self._FRAME_RATE = game_config.FRAME_RATE
        self._screen = game_config._screen
        self._clock = game_config._clock

    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                return

            elif self._current_state is GameState.START_SCREEN:
                start_screen_elements.update()
                start_screen_elements.draw(self._screen)
                if event.type == BUTTON_CLICK:
                    self._current_state = GameState.MAIN_MENU

            elif self._current_state is GameState.MAIN_MENU:
                main_menu_elements.update()
                main_menu_elements.draw(self._screen)

        pygame.display.update()
        self._clock.tick(self._FRAME_RATE)

    @property
    def running(self) -> bool:
        return self._running


game_update = GameUpdate()
