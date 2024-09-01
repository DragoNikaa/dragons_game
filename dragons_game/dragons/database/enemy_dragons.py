from dragons_game.dragons.database.attacks import fancy_basic_attack, fancy_special_attack
from dragons_game.dragons.enemy_dragon import EnemyDragon
from dragons_game.dragons.rarity import Rarity

emberhorn = EnemyDragon('Emberhorn', Rarity.COMMON, 'dragons_game/graphics/dragons/enemy/emberhorn.png', 'left',
                        fancy_basic_attack, fancy_special_attack)
verdantail = EnemyDragon('Verdantail', Rarity.COMMON, 'dragons_game/graphics/dragons/enemy/verdantail.png', 'left',
                         fancy_basic_attack, fancy_special_attack)
duskspark = EnemyDragon('Duskspark', Rarity.UNCOMMON, 'dragons_game/graphics/dragons/enemy/duskspark.png', 'left',
                        fancy_basic_attack, fancy_special_attack)
