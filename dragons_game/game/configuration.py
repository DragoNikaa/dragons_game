import pygame


class GameConfig:
    NAME = 'Dragons'
    # ICON = pygame.image.load('').convert_alpha()
    FRAME_RATE = 60

    pygame.init()
    screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    pygame.display.set_caption(NAME)
    # pygame.display.set_icon(ICON)

    WINDOW_WIDTH = screen.get_width()
    WINDOW_HEIGHT = screen.get_height()
