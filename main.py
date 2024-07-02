import sys

import pygame

from text import Text

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('Dragons')
# pygame.display.set_icon('')
start_screen = True

background = pygame.image.load('graphics/start_screen_backgrounds/1.png').convert()
background = pygame.transform.scale(background, (1280, 720))

title_font = pygame.font.Font('fonts/friz_quadrata.ttf', 100)
title = pygame.sprite.GroupSingle()  # type: pygame.sprite.GroupSingle[Text]
title.add(Text(title_font, 'DRAGONS', 'white', (1280 // 2, 100)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if start_screen:
        screen.blit(background, (0, 0))
        title.draw(screen)

    pygame.display.update()
    clock.tick(60)
