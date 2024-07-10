from dataclasses import dataclass

import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()


@dataclass
class General:
    WINDOW_WIDTH = screen.get_width()
    WINDOW_HEIGHT = screen.get_height()
    NAME = 'Dragons'
    # ICON = pygame.image.load('').convert_alpha()
    FRAME_RATE = 60


pygame.display.set_caption(General.NAME)
# pygame.display.set_icon(General.ICON)
