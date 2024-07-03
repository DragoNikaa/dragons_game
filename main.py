import sys
from typing import Union

import pygame

import game_states
from button import Button
from game_states import GameStates
from text import Text

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('Dragons')
# pygame.display.set_icon('')

background = pygame.image.load('graphics/start_screen_backgrounds/1.png').convert()
background = pygame.transform.scale(background, (1280, 720))

title_font = pygame.font.Font('fonts/pr_viking.ttf', 200)
title = Text(title_font, 'DRAGONS', 'white', (1280 // 2, 200))

start_button = Button(380, 180, 'graphics/button_backgrounds/start_game.png', (1280 // 2, 470))
start_button_text_font = pygame.font.Font('fonts/rurik.ttf', 80)
start_button_text = Text(start_button_text_font, "START", 'white',
                         (start_button.dest[0], start_button.dest[1] + start_button.height // 6), True,
                         start_button.position)

start_screen_elements = pygame.sprite.Group()  # type: pygame.sprite.Group[Union[Text, Button]]
start_screen_elements.add(title)
start_screen_elements.add(start_button)
start_screen_elements.add(start_button_text)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_states.current_state == GameStates.START_SCREEN:
        screen.blit(background, (0, 0))
        start_screen_elements.draw(screen)
        start_button.update()

    elif game_states.current_state == GameStates.LEVEL_SELECTION:
        screen.fill('black')

    pygame.display.update()
    clock.tick(60)
