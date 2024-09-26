import random

from dragons_game.dragons.database import enemy_dragons
from dragons_game.dragons.enemy_dragon import EnemyDragon
from dragons_game.dragons.rarity import Rarity
from dragons_game.islands.level_type import LevelType
from dragons_game.islands.rewards import LEVEL_TYPE_TO_REWARDS, Reward
from dragons_game.utils import custom_types


class Level:
    def __init__(self, island_number: int, level_type: LevelType, button_factors: tuple[float, float],
                 user_dragons_factors: custom_types.DragonsFactors, enemy_dragons_factors: custom_types.DragonsFactors):
        self._island_number = island_number
        self._level_type = level_type
        self._button_factors = button_factors
        self._user_dragons_factors = user_dragons_factors
        self._enemy_dragons_factors = enemy_dragons_factors

        self._enemy_dragons = self._get_enemy_dragons()

        self._rewards = {reward: round((0.9 + island_number / 10) * value) for reward, value in
                         LEVEL_TYPE_TO_REWARDS[level_type].items()}

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
    def type(self) -> LevelType:
        return self._level_type

    @property
    def button_image_path(self) -> str:
        return f'dragons_game/graphics/buttons/levels/{self._level_type}.png'

    @property
    def button_factors(self) -> tuple[float, float]:
        return self._button_factors

    @property
    def battle_image_path(self) -> str:
        return f'dragons_game/graphics/backgrounds/battle/island_{self._island_number}/{self._level_type}.png'

    @property
    def user_dragons_factors(self) -> custom_types.DragonsFactors:
        return self._user_dragons_factors

    @property
    def enemy_dragons_factors(self) -> custom_types.DragonsFactors:
        return self._enemy_dragons_factors

    @property
    def enemy_dragons(self) -> list[EnemyDragon]:
        return self._enemy_dragons

    @property
    def rewards(self) -> dict[Reward, int]:
        return self._rewards
