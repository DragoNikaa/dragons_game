import threading

import pygame

from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common.manager import GameStateManager
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.loading_screen.manager import LoadingScreenManager


class Game(GameConfig):
    def __init__(self) -> None:
        self._running = True
        self._initialized_managers: dict[GameState, GameStateManager] = {}
        self._loading_screen_manager = LoadingScreenManager()
        self._current_manager = self._get_manager(GameState.START_SCREEN)
        self._get_manager(GameState.MAIN_MENU)

    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                return

            new_state = self._current_manager.handle_event(event)
            if new_state:
                self._current_manager = self._get_manager(new_state)
                return

        self._current_manager.update()
        self._current_manager.draw(self.screen)

        pygame.display.update()
        self.clock.tick(self.FRAME_RATE)

    def _get_manager(self, new_state: GameState) -> GameStateManager:
        if new_state not in self._initialized_managers:
            loading_done_event = threading.Event()

            loading_screen_thread = threading.Thread(target=self._show_loading_screen, args=(loading_done_event,))
            loading_screen_thread.start()

            loading_manager_thread = threading.Thread(target=self._load_manager, args=(new_state, loading_done_event))
            loading_manager_thread.start()

            loading_manager_thread.join()
            loading_screen_thread.join()

        return self._initialized_managers[new_state]

    def _load_manager(self, new_state: GameState, loading_done_event: threading.Event) -> None:
        match new_state:
            case GameState.START_SCREEN:
                from dragons_game.game_states.start_screen.manager import StartScreenManager
                self._initialized_managers[new_state] = StartScreenManager()

            case GameState.MAIN_MENU:
                from dragons_game.game_states.main_menu.manager import MainMenuManager
                self._initialized_managers[new_state] = MainMenuManager()

            case GameState.DRAGONS_MENU:
                from dragons_game.game_states.dragons_menu.manager import DragonsMenuManager
                self._initialized_managers[new_state] = DragonsMenuManager()

        loading_done_event.set()

    def _show_loading_screen(self, loading_done_event: threading.Event) -> None:
        while not loading_done_event.is_set():
            self._loading_screen_manager.update()
            self._loading_screen_manager.draw(self.screen)

            pygame.display.update()
            self.clock.tick(self.FRAME_RATE)

    @property
    def running(self) -> bool:
        return self._running


game = Game()
