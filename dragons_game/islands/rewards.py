from enum import Enum

from dragons_game.islands.level_type import LevelType


class Reward(Enum):
    TROPHIES = 1
    EGGS = 2
    FISH = 3
    COINS = 4
    MIN_EXPERIENCE = 5
    MAX_EXPERIENCE = 6
    LOST_BATTLE_EXPERIENCE = 7


LEVEL_TYPE_TO_REWARDS = {
    LevelType.EASY: {Reward.TROPHIES: 10, Reward.EGGS: 1, Reward.FISH: 50, Reward.COINS: 25, Reward.MIN_EXPERIENCE: 20,
                     Reward.MAX_EXPERIENCE: 30, Reward.LOST_BATTLE_EXPERIENCE: 5},
    LevelType.MEDIUM: {Reward.TROPHIES: 20, Reward.EGGS: 2, Reward.FISH: 80, Reward.COINS: 50,
                       Reward.MIN_EXPERIENCE: 50, Reward.MAX_EXPERIENCE: 70, Reward.LOST_BATTLE_EXPERIENCE: 5},
    LevelType.HARD: {Reward.TROPHIES: 30, Reward.EGGS: 3, Reward.FISH: 120, Reward.COINS: 80,
                     Reward.MIN_EXPERIENCE: 100, Reward.MAX_EXPERIENCE: 130, Reward.LOST_BATTLE_EXPERIENCE: 5},
    LevelType.FIENDISH: {Reward.TROPHIES: 40, Reward.EGGS: 4, Reward.FISH: 200, Reward.COINS: 150,
                         Reward.MIN_EXPERIENCE: 150, Reward.MAX_EXPERIENCE: 200, Reward.LOST_BATTLE_EXPERIENCE: 5}}
