import sys
from typing import Union

import pygame

import game_states
from button import Button
from game_states import GameStates
from text import Text, TextBorder, BorderPosition

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('Dragons')
# pygame.display.set_icon('')

background = pygame.image.load('graphics/start_screen_backgrounds/1.png').convert()
background = pygame.transform.scale(background, (1280, 720))

title_font = pygame.font.Font('fonts/pr_viking.ttf', 200)
title = Text(title_font, 'DRAGONS', 'white', (1280 // 2, 200))
title_border_left = TextBorder(title, 'black', 10, BorderPosition.LEFT)
title_border_right = TextBorder(title, 'black', 10, BorderPosition.RIGHT)
title_border_top = TextBorder(title, 'black', 10, BorderPosition.TOP)
title_border_bottom = TextBorder(title, 'black', 10, BorderPosition.BOTTOM)

start_button = Button(380, 180, 'graphics/button_backgrounds/start_game.png', (1280 // 2, 470))
start_button_text_font = pygame.font.Font('fonts/rurik.ttf', 80)
start_button_text = Text(start_button_text_font, "START", 'white',
                         (start_button.dest[0], start_button.dest[1] + start_button.height // 6), True,
                         start_button.position)
start_button_text_border_left = TextBorder(start_button_text, 'black', 4, BorderPosition.LEFT)
start_button_text_border_right = TextBorder(start_button_text, 'black', 4, BorderPosition.RIGHT)
start_button_text_border_top = TextBorder(start_button_text, 'black', 4, BorderPosition.TOP)
start_button_text_border_bottom = TextBorder(start_button_text, 'black', 4, BorderPosition.BOTTOM)

start_screen_elements = pygame.sprite.Group()  # type: pygame.sprite.Group[Union[Text, TextBorder, Button]]
start_screen_elements.add(title_border_left)
start_screen_elements.add(title_border_right)
start_screen_elements.add(title_border_top)
start_screen_elements.add(title_border_bottom)
start_screen_elements.add(title)
start_screen_elements.add(start_button)
start_screen_elements.add(start_button_text_border_left)
start_screen_elements.add(start_button_text_border_right)
start_screen_elements.add(start_button_text_border_top)
start_screen_elements.add(start_button_text_border_bottom)
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
