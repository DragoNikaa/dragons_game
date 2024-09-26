import random

from dragons_game.dragons.database import enemy_dragons
from dragons_game.dragons.enemy_dragon import EnemyDragon
from dragons_game.dragons.rarity import Rarity
from dragons_game.elements.image import Image
from dragons_game.elements.text import Text
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes
from dragons_game.islands.level_type import LevelType
from dragons_game.islands.rewards import LEVEL_TYPE_TO_REWARDS, Reward
from dragons_game.utils import custom_types
from dragons_game.utils.image_proportions import proportional_width


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
    def tooltip(self) -> Tooltip:
        return _Tooltip(self._level_type, self._rewards)

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


class _Tooltip(Tooltip):
    def __init__(self, level_type: LevelType, rewards: dict[Reward, int]):
        super().__init__('midbottom', (GameConfig.WINDOW_WIDTH / 4, 0), level_type.main_color, 5,
                         level_type.secondary_color, 200)

        self._level_type = level_type
        padding = universal_sizes.SMALL

        level = self._text(str(level_type).title(), 'midtop', (0, padding))
        self.add_element('level', level)

        self._icon_height = universal_sizes.LARGE
        column_1_x = 2 * padding
        column_2_x = 0.57 * self.width
        row_1_y = level.height + 2 * padding
        row_2_y = row_1_y + self._icon_height + padding

        self._add_reward('trophies', (column_1_x, row_1_y), str(rewards[Reward.TROPHIES]))
        self._add_reward('eggs', (column_2_x, row_1_y), str(rewards[Reward.EGGS]))
        self._add_reward('fish', (column_1_x, row_2_y), str(rewards[Reward.FISH]))
        self._add_reward('coins', (column_2_x, row_2_y), str(rewards[Reward.COINS]))

        dragon_icon_name = 'dragons'
        if level_type is LevelType.FIENDISH:
            dragon_icon_name += '_2'
        self._add_reward(dragon_icon_name, (column_1_x, row_2_y + self._icon_height + padding),
                         f'{rewards[Reward.MIN_EXPERIENCE]}-{rewards[Reward.MAX_EXPERIENCE]} exp')

        self.change_size((self.width, level.height + 3 * self._icon_height + 5 * padding))

    def _add_reward(self, name: str, destination: tuple[float, float], text: str) -> None:
        image_path = f'dragons_game/graphics/icons/{name}.png'
        width = proportional_width(image_path, self._icon_height)

        icon = Image(image_path, (width, self._icon_height), 'topleft', destination)
        self.add_element(f'{name}_icon', icon)

        self.add_element(f'{name}_text', self._text(text, 'topleft', (
            destination[0] + icon.width + universal_sizes.MEDIUM, destination[1])))

    def _text(self, text: str, position: custom_types.Position, destination: tuple[float, float]) -> Text:
        return Text('dragons_game/fonts/viking.ttf', universal_sizes.MEDIUM, text, self._level_type.secondary_color,
                    position, destination)
