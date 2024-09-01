from dragons_game.dragons.database.attacks import fancy_basic_attack, fancy_special_attack
from dragons_game.dragons.rarity import Rarity
from dragons_game.dragons.user_dragon import UserDragon

toothless = UserDragon('Toothless', Rarity.MYTHICAL,
                       'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                       'dragons_game/graphics/dragons/user/toothless.png', 'left', fancy_basic_attack,
                       fancy_special_attack)
skyflame = UserDragon('Skyflame', Rarity.RARE,
                      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                      'dragons_game/graphics/dragons/user/skyflame.png', 'right', fancy_basic_attack,
                      fancy_special_attack)
prismscale = UserDragon('Prismscale', Rarity.EPIC,
                        'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                        'dragons_game/graphics/dragons/user/prismscale.png', 'left', fancy_basic_attack,
                        fancy_special_attack)
frostreaver = UserDragon('Frostreaver', Rarity.UNCOMMON,
                         'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                         'dragons_game/graphics/dragons/user/frostreaver.png', 'left', fancy_basic_attack,
                         fancy_special_attack)
valentira = UserDragon('Valentira', Rarity.COMMON,
                       'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                       'dragons_game/graphics/dragons/user/valentira.png', 'left', fancy_basic_attack,
                       fancy_special_attack)
nyxar = UserDragon('Nyxar', Rarity.LEGENDARY,
                   'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                   'dragons_game/graphics/dragons/user/nyxar.png', 'right', fancy_basic_attack, fancy_special_attack)

toothless.add_experience(450)
toothless._current_energy = 4
toothless._current_health = 200
