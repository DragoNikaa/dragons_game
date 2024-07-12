import pygame


class _GameConfig:
    def __init__(self) -> None:
        self._NAME = 'Dragons'
        # self._ICON = pygame.image.load('').convert_alpha()
        self._FRAME_RATE = 60

        pygame.init()
        self._screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
        self._clock = pygame.time.Clock()

        pygame.display.set_caption(self._NAME)
        # pygame.display.set_icon(self._ICON)

    @property
    def NAME(self) -> str:
        return self._NAME

    # @property
    # def ICON(self) -> pygame.Surface:
    #     return self._ICON

    @property
    def FRAME_RATE(self) -> int:
        return self._FRAME_RATE

    @property
    def WINDOW_WIDTH(self) -> int:
        return self._screen.get_width()

    @property
    def WINDOW_HEIGHT(self) -> int:
        return self._screen.get_height()


game_config = _GameConfig()
