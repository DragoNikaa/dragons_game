from dragons_game.game.update import game_update as game


def main() -> None:
    while game.running:
        game.update()


if __name__ == '__main__':
    main()
