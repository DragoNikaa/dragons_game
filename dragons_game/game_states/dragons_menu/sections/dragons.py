from dragons_game.dragons.dragon import Dragon
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.common.dragon_button import DragonButton
from dragons_game.game_states.dragons_menu.sections.team import team_section
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section
from dragons_game.user import user

dragons_section = Section(
    (GameConfig.WINDOW_WIDTH - team_section.width, GameConfig.WINDOW_HEIGHT - title_bar_section.height), 'topleft',
    (team_section.rect.right, title_bar_section.rect.bottom))

dragons_section.add_element('background',
                            Image('dragons_game/graphics/backgrounds/dragons_menu/dragons.png', dragons_section.size,
                                  'topleft', (0, 0)))


class _DragonButton(DragonButton):
    _WIDTH = (dragons_section.width - universal_sizes.LARGE) / 5 - universal_sizes.LARGE
    _HEIGHT = (dragons_section.height - 2 * universal_sizes.LARGE) / 2 - universal_sizes.LARGE
    _X_DESTINATIONS = [x for x in
                       range(universal_sizes.LARGE, dragons_section.width, round(_WIDTH) + universal_sizes.LARGE)]
    _ROW_1_Y_DESTINATION: float = universal_sizes.LARGE
    _ROW_2_Y_DESTINATION = 2 * universal_sizes.LARGE + _HEIGHT

    def __init__(self, dragon_index: int, dragon: Dragon):
        super().__init__(dragon, (self._WIDTH, self._HEIGHT), 'topleft', self._new_destination(dragon_index))

    @classmethod
    def update_on_notify(cls, dragons: list[Dragon], section: Section = dragons_section) -> None:
        super().update_on_notify(dragons, section)

    @classmethod
    def _new_destination(cls, dragon_index: int) -> tuple[int, int]:
        dragon_index %= 10

        x = cls._X_DESTINATIONS[dragon_index % 5]
        if dragon_index <= 4:
            y = cls._ROW_1_Y_DESTINATION
        else:
            y = cls._ROW_2_Y_DESTINATION

        return x, int(y)

    @classmethod
    def _create_instance(cls, dragon_index: int, dragon: Dragon) -> 'DragonButton':
        return cls(dragon_index, dragon)


user.add_dragons_observer(_DragonButton)
