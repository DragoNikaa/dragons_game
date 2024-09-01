from dragons_game.dragons.attack import Attack
from dragons_game.dragons.dragon import Dragon
from dragons_game.dragons.rarity import Rarity
from dragons_game.utils import custom_types


class EnemyDragon(Dragon):
    rarity_to_dragons: dict[Rarity, list['EnemyDragon']] = {rarity: [] for rarity in Rarity}

    def __init__(self, name: str, rarity: Rarity, image_path: str, facing: custom_types.Facing, basic_attack: Attack,
                 special_attack: Attack):
        super().__init__(name, rarity, image_path, facing, basic_attack, special_attack)

        self.rarity_to_dragons[rarity].append(self)
