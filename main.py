import sys

import pygame

import configuration

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((configuration.General.SCREEN_WIDTH, configuration.General.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption(configuration.General.NAME)
    # pygame.display.set_icon(configuration.General.ICON)

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
            start_screen_elements.draw(screen)
            start_screen_elements.update()

        elif game_states.current_state == GameStates.LEVEL_SELECTION:
            level_selection_elements.draw(screen)
            level_selection_elements.update()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game_loop()
