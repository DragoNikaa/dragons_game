from dragons_game.game.game import game


def main() -> None:
    while game.running:
        game.update()


if __name__ == '__main__':
    main()
