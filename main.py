from dragons_game.game.game import Game


def main() -> None:
    while Game.running:
        Game.update()


if __name__ == '__main__':
    main()
