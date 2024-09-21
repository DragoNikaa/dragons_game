from dragons_game.islands.island import Island
from dragons_game.islands.level import Level
from dragons_game.islands.level_type import LevelType

easy_1 = Level(1, LevelType.EASY, (-3.07, -200), ((-3, 25), (-6, 5.5), (-3, 3.5)), ((3.5, 12), (8.5, 5), (3.5, 3)))
medium_1 = Level(1, LevelType.MEDIUM, (-8, -4.2), ((-6, 70), (-3, 6.5), (-6, 3.3)), ((5.4, 70), (2.8, 6.5), (5.4, 3.3)))
hard_1 = Level(1, LevelType.HARD, (7.5, 12), ((-6, 15), (-3, 5.5), (-6, 3.2)), ((6.5, 15), (3.1, 5.5), (6.5, 3.2)))
fiendish_1 = Level(1, LevelType.FIENDISH, (3, -7), ((-3.5, 20), (-7, 5.4), (-3, 3.5)),
                   ((6.8, 20), (3.1, 5.4), (6.8, 3.2)))

island_1 = Island(1, easy_1, medium_1, hard_1, fiendish_1)
