from dragons_game.dragons.attack import Attack, AttackType


def fancy_action() -> None:
    pass


fancy_basic_attack = Attack(AttackType.BASIC, 'Fancy basic attack',
                            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                            fancy_action)
fancy_special_attack = Attack(AttackType.SPECIAL, 'Fancy special attack',
                              'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                              fancy_action)
