from enum import Enum

from dragons_game.elements.text import Text
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes


class LevelType(Enum):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    FIENDISH = 'fiendish'


class Level:
    def __init__(self, level_type: LevelType, button_image_path: str, button_factors: tuple[float, float],
                 battle_image_path: str,
                 dragons_factors: tuple[tuple[float, float], tuple[float, float], tuple[float, float]],
                 enemies_factors: tuple[tuple[float, float], tuple[float, float], tuple[float, float]]):
        self._level_type = level_type
        self._button_image_path = button_image_path
        self._button_factors = button_factors
        self._battle_image_path = battle_image_path
        self._dragons_factors = dragons_factors
        self._enemies_factors = enemies_factors

    @property
    def tooltip(self) -> Tooltip:
        tooltip = Tooltip('midbottom', (GameConfig.WINDOW_WIDTH / 10, GameConfig.WINDOW_HEIGHT / 10), 'chocolate')
        tooltip.add_element('level', Text('dragons_game/fonts/friz_quadrata.ttf', universal_sizes.MEDIUM / 1.5,
                                          self._level_type.value.title(), 'white', 'center', (0, 0), 1, 'black'))
        return tooltip

    @property
    def button_image_path(self) -> str:
        return self._button_image_path

    @property
    def button_factors(self) -> tuple[float, float]:
        return self._button_factors

    @property
    def battle_image_path(self) -> str:
        return self._battle_image_path

    @property
    def dragons_factors(self) -> tuple[tuple[float, float], tuple[float, float], tuple[float, float]]:
        return self._dragons_factors

    @property
    def enemies_factors(self) -> tuple[tuple[float, float], tuple[float, float], tuple[float, float]]:
        return self._enemies_factors
