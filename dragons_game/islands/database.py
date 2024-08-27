from dragons_game.islands.island import Island
from dragons_game.islands.level import Level, LevelType

easy_1 = Level(LevelType.EASY, 'dragons_game/graphics/buttons/level.png', (-3.07, 60),
               'dragons_game/graphics/backgrounds/battle/island_1/easy.png', ((-3, 25), (-6, 5.5), (-3, 3.5)),
               ((10, 10), (10, 10), (10, 10)))
medium_1 = Level(LevelType.MEDIUM, 'dragons_game/graphics/buttons/level.png', (-8, -4.2),
                 'dragons_game/graphics/backgrounds/battle/island_1/medium.png', ((-6, 70), (-3, 6.5), (-6, 3.3)),
                 ((10, 10), (10, 10), (10, 10)))
hard_1 = Level(LevelType.HARD, 'dragons_game/graphics/buttons/level.png', (8, 12),
               'dragons_game/graphics/backgrounds/battle/island_1/hard.png', ((-6, 15), (-3, 5.5), (-6, 3.2)),
               ((10, 10), (10, 10), (10, 10)))
fiendish_1 = Level(LevelType.FIENDISH, 'dragons_game/graphics/buttons/level.png', (3, -7),
                   'dragons_game/graphics/backgrounds/battle/island_1/fiendish.png', ((-3.5, 20), (-7, 5.4), (-3, 3.5)),
                   ((10, 10), (10, 10), (10, 10)))

island_1 = Island('dragons_game/graphics/islands/1.png', easy_1, medium_1, hard_1, fiendish_1)
