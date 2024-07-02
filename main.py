import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('Dragons')
# pygame.display.set_icon('')
start_screen = True

background = pygame.image.load('graphics/start_screen_backgrounds/1.png').convert()
background = pygame.transform.scale(background, (1280, 720))

title_font = pygame.font.Font('fonts/friz_quadrata.ttf', 100)
title_surf = title_font.render("DRAGONS", True, 'white')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if start_screen:
        screen.blit(background, (0, 0))
        screen.blit(title_surf, (400, 100))

    pygame.display.update()
    clock.tick(60)
