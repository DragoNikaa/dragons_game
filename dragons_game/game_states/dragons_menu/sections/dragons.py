from dragons_game.dragons.dragon import Dragon
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.common import DragonButton
from dragons_game.elements.section import Section
from dragons_game.elements.image import Image
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.dragons_menu.sections.team import team_section
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section
from dragons_game.user import User

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
        dragon_index %= 10
        x = self._X_DESTINATIONS[dragon_index % 5]
        if dragon_index <= 4:
            y = self._ROW_1_Y_DESTINATION
        else:
            y = self._ROW_2_Y_DESTINATION

        super().__init__(dragon, (self._WIDTH, self._HEIGHT), 'topleft', (x, y))


for dragon_index, dragon in enumerate(User.dragons):
    dragons_section.add_element(f'dragon_{dragon_index}', _DragonButton(dragon_index, dragon))
