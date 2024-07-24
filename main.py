from dragons_game.game.game import Game


def main() -> None:
    while Game.is_running():
        Game.update()


if __name__ == '__main__':
    main()
