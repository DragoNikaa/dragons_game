from dragons_game.dragons.database.attacks import some_fancy_attack
from dragons_game.dragons.dragon import Dragon
from dragons_game.dragons.dragon_class import DragonClass

toothless = Dragon('Toothless',
                   'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                   DragonClass.MYTHICAL, 'dragons_game/graphics/dragons/toothless.png', some_fancy_attack,
                   some_fancy_attack)
