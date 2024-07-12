import pygame

from dragons_game.game.configuration import game_config
from dragons_game.game_states.dragons_menu.manager import DragonsMenuManager
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.main_menu.manager import MainMenuManager
from dragons_game.game_states.start_screen.manager import StartScreenManager


class _GameUpdate:
    def __init__(self) -> None:
        self._running = True
        self._states = {GameState.START_SCREEN: StartScreenManager(), GameState.MAIN_MENU: MainMenuManager(),
                        GameState.DRAGONS_MENU: DragonsMenuManager()}
        self._current_state_manager = self._states[GameState.START_SCREEN]

        self._FRAME_RATE = game_config.FRAME_RATE
        self._screen = game_config._screen
        self._clock = game_config._clock

    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                return

            new_state = self._current_state_manager.handle_event(event)
            if new_state:
                self._current_state_manager = self._states[new_state]

        self._current_state_manager.update()
        self._current_state_manager.draw(self._screen)

        pygame.display.update()
        self._clock.tick(self._FRAME_RATE)

    @property
    def running(self) -> bool:
        return self._running


game_update = _GameUpdate()
