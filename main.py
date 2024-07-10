import sys

import pygame

from dragons_game import configuration
from dragons_game.game_states import game_state
from dragons_game.game_states.game_state import GameState
from dragons_game.game_states.main_menu.elements import main_menu_elements
from dragons_game.game_states.start_screen.elements import start_screen_elements


def game_loop() -> None:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_state.current_state == GameState.START_SCREEN:
            start_screen_elements.draw(configuration.screen)
            start_screen_elements.update()

        elif game_state.current_state == GameState.MAIN_MENU:
            main_menu_elements.draw(configuration.screen)
            main_menu_elements.update()

        pygame.display.update()
        configuration.clock.tick(configuration.General.FRAME_RATE)


if __name__ == '__main__':
    game_loop()
