import pygame

from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.dragons_menu.manager import DragonsMenuManager
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.main_menu.manager import MainMenuManager
from dragons_game.game_states.start_screen.manager import StartScreenManager
from dragons_game.utils.classproperty import classproperty


class Game(GameConfig):
    _running = True
    _STATE_TO_MANAGER = {GameState.START_SCREEN: StartScreenManager(), GameState.MAIN_MENU: MainMenuManager(),
                         GameState.DRAGONS_MENU: DragonsMenuManager()}
    _current_manager = _STATE_TO_MANAGER[GameState.START_SCREEN]

    @classmethod
    def update(cls) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cls._running = False
                pygame.quit()
                return

            new_state = cls._current_manager.handle_event(event)
            if new_state:
                cls._current_manager = cls._STATE_TO_MANAGER[new_state]
                return

        cls._current_manager.update()
        cls._current_manager.draw(cls.screen)

        pygame.display.update()
        cls.clock.tick(cls.FRAME_RATE)

    @classproperty
    def running(cls) -> bool:
        return cls._running
