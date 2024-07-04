import sys

import pygame

import configuration

import game_states
from displayed_elements.start_screen import start_screen_elements
from displayed_elements.level_selection import level_selection_elements
from game_states import GameStates


def game_loop() -> None:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_states.current_state == GameStates.START_SCREEN:
            start_screen_elements.draw(configuration.screen)
            start_screen_elements.update()

        elif game_states.current_state == GameStates.LEVEL_SELECTION:
            level_selection_elements.draw(configuration.screen)
            level_selection_elements.update()

        pygame.display.update()
        configuration.clock.tick(60)


if __name__ == '__main__':
    game_loop()
