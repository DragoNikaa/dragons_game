from dragons_game.dragons.database import dragons
from dragons_game.game.game import Game
from dragons_game.user import User

User.add_dragon(dragons.toothless)
User.add_dragon(dragons.skyflame)
User.add_dragon(dragons.prismscale)
User.add_dragon(dragons.frostreaver)
User.add_dragon(dragons.valentira)
User.add_dragon(dragons.nyxar)

User.add_team_dragon(dragons.toothless)
User.add_team_dragon(dragons.skyflame)
User.add_team_dragon(dragons.frostreaver)


def main() -> None:
    while Game.running:
        Game.update()


if __name__ == '__main__':
    main()
