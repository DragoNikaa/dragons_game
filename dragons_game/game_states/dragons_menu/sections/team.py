from dragons_game.dragons.dragon import Dragon
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.common.dragon_button import DragonButton
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section
from dragons_game.user import User

team_section = Section((GameConfig.WINDOW_WIDTH / 7, GameConfig.WINDOW_HEIGHT - title_bar_section.height), 'topleft',
                       (0, title_bar_section.rect.bottom))

team_section.add_element('background',
                         Image('dragons_game/graphics/backgrounds/dragons_menu/team.png', team_section.size, 'topleft',
                               (0, 0)))

title = Text('dragons_game/fonts/pr_viking.ttf', team_section.height / 20.5, 'My team', 'white', 'midtop',
             (0, universal_sizes.SMALL), 3, 'black')
team_section.add_element('title', title)


class _DragonButton(DragonButton):
    _WIDTH = team_section.width - 2 * universal_sizes.MEDIUM
    _HEIGHT = (team_section.height - title.height - 2 * universal_sizes.SMALL) / 3 - universal_sizes.SMALL
    _Y_DESTINATIONS = [y for y in range(title.height + 2 * universal_sizes.SMALL, team_section.height,
                                        round(_HEIGHT) + universal_sizes.SMALL)]

    def __init__(self, dragon_index: int, dragon: Dragon):
        super().__init__(dragon, (self._WIDTH, self._HEIGHT), 'midtop', self._new_destination(dragon_index))

    @classmethod
    def update_on_notify(cls, dragons: list[Dragon], section: Section = team_section) -> None:
        super().update_on_notify(dragons, section)

    @classmethod
    def _new_destination(cls, dragon_index: int) -> tuple[int, int]:
        return 0, cls._Y_DESTINATIONS[dragon_index]

    @classmethod
    def _create_instance(cls, dragon_index: int, dragon: Dragon) -> 'DragonButton':
        return cls(dragon_index, dragon)


User.add_team_dragons_observer(_DragonButton)
