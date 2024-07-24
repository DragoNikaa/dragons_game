from dragons_game.dragons.database.attacks import fancy_attack
from dragons_game.dragons.dragon import Dragon
from dragons_game.dragons.dragon_class import DragonClass

toothless = Dragon('Toothless', DragonClass.MYTHICAL,
                   'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                   'dragons_game/graphics/dragons/toothless.png', fancy_attack, fancy_attack)

toothless.add_experience(450)
toothless._current_energy = 4
toothless._current_health = 200
