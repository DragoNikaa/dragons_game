from dragons_game.islands.level import Level


class Island:
    def __init__(self, number: int, easy_level: Level, medium_level: Level, hard_level: Level, fiendish_level: Level):
        self._number = number
        self._easy_level = easy_level
        self._medium_level = medium_level
        self._hard_level = hard_level
        self._fiendish_level = fiendish_level

    @property
    def image_path(self) -> str:
        return f'dragons_game/graphics/islands/{self._number}.png'

    @property
    def easy_level(self) -> Level:
        return self._easy_level

    @property
    def medium_level(self) -> Level:
        return self._medium_level

    @property
    def hard_level(self) -> Level:
        return self._hard_level

    @property
    def fiendish_level(self) -> Level:
        return self._fiendish_level
