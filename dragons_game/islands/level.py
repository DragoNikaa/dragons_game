import random
from enum import Enum

from dragons_game.dragons.database import enemy_dragons
from dragons_game.dragons.enemy_dragon import EnemyDragon
from dragons_game.dragons.rarity import Rarity
from dragons_game.elements.text import Text
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes
from dragons_game.utils import custom_types


class LevelType(Enum):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    FIENDISH = 'fiendish'


class Level:
    def __init__(self, level_type: LevelType, button_factors: tuple[float, float], battle_image_path: str,
                 user_dragons_factors: custom_types.DragonsFactors, enemy_dragons_factors: custom_types.DragonsFactors):
        self._level_type = level_type
        self._button_factors = button_factors
        self._battle_image_path = battle_image_path
        self._user_dragons_factors = user_dragons_factors
        self._enemy_dragons_factors = enemy_dragons_factors

        self._enemy_dragons = self._get_enemy_dragons()

    def _get_enemy_dragons(self) -> list[EnemyDragon]:
        # match self._level_type:
        #     case LevelType.EASY:
        #         possible_rarities = Rarity.COMMON, Rarity.UNCOMMON
        #     case LevelType.MEDIUM:
        #         possible_rarities = Rarity.UNCOMMON, Rarity.RARE
        #     case LevelType.HARD:
        #         possible_rarities = Rarity.EPIC, Rarity.LEGENDARY
        #     case _:
        #         possible_rarities = Rarity.LEGENDARY, Rarity.MYTHICAL
        #
        # rarities = [random.choice(possible_rarities) for _ in range(3)]

        rarities = Rarity.COMMON, Rarity.UNCOMMON, Rarity.COMMON
        dragons = []

        for rarity in rarities:
            dragon = random.choice(EnemyDragon.rarity_to_dragons[rarity])
            while dragon in dragons:
                dragon = random.choice(EnemyDragon.rarity_to_dragons[rarity])
            dragons.append(dragon)

        return dragons

    @property
    def tooltip(self) -> Tooltip:
        tooltip = Tooltip('midbottom', (GameConfig.WINDOW_WIDTH / 10, GameConfig.WINDOW_HEIGHT / 10), 'chocolate')
        tooltip.add_element('level', Text('dragons_game/fonts/friz_quadrata.ttf', universal_sizes.MEDIUM / 1.5,
                                          self._level_type.value.title(), 'white', 'center', (0, 0), 1, 'black'))
        return tooltip

    @property
    def button_image_path(self) -> str:
        return f'dragons_game/graphics/buttons/levels/{self._level_type.value}.png'

    @property
    def button_factors(self) -> tuple[float, float]:
        return self._button_factors

    @property
    def battle_image_path(self) -> str:
        return self._battle_image_path

    @property
    def user_dragons_factors(self) -> custom_types.DragonsFactors:
        return self._user_dragons_factors

    @property
    def enemy_dragons_factors(self) -> custom_types.DragonsFactors:
        return self._enemy_dragons_factors

    @property
    def enemy_dragons(self) -> list[EnemyDragon]:
        return self._enemy_dragons
