import pygame

from dragons_game.dragons.user_dragon import UserDragon
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.common.dragon_button import DragonButton
from dragons_game.game_states.dragons_menu.sections.team import team_section
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section
from dragons_game.user import user
from dragons_game.utils import custom_exceptions

dragon_list_section = Section(
    (GameConfig.WINDOW_WIDTH - team_section.width, GameConfig.WINDOW_HEIGHT - title_bar_section.height), 'topleft',
    (team_section.rect.right, title_bar_section.rect.bottom))

dragon_list_section.add_element('background', Image('dragons_game/graphics/backgrounds/dragons_menu/dragons.png',
                                                    dragon_list_section.size, 'topleft', (0, 0)))


class _DragonButton(DragonButton):
    _WIDTH = (dragon_list_section.width - universal_sizes.LARGE) / 5 - universal_sizes.LARGE
    _HEIGHT = ((dragon_list_section.height - 2 * universal_sizes.MEDIUM - universal_sizes.LARGE) / 2
               - universal_sizes.MEDIUM)
    _X_DESTINATIONS = [x for x in
                       range(universal_sizes.LARGE, dragon_list_section.width, round(_WIDTH) + universal_sizes.LARGE)]
    _ROW_1_Y_DESTINATION: float = universal_sizes.MEDIUM
    _ROW_2_Y_DESTINATION = 2 * universal_sizes.MEDIUM + _HEIGHT

    def __init__(self, dragon_index: int, dragon: UserDragon):
        super().__init__(dragon, (self._WIDTH, self._HEIGHT), 'topleft', self._new_destination(dragon_index))

    @classmethod
    def update_on_notify(cls, dragons: list[UserDragon] | None = None, added_team_dragon: UserDragon | None = None,
                         removed_team_dragon: UserDragon | None = None) -> None:
        if dragons:
            for dragon_index, dragon in enumerate(dragons):
                try:
                    dragon_button = dragon_list_section.get_button(dragon.name)
                    dragon_button.destination = cls._new_destination(dragon_index)
                except custom_exceptions.ElementNotInSectionError:
                    dragon_list_section.add_element(dragon.name, cls(dragon_index, dragon))

        if added_team_dragon:
            dragon_button = dragon_list_section.get_button(added_team_dragon.name)

            team_mark = Text('dragons_game/fonts/pr_viking.ttf', dragon_button.height / 10, 'In team', 'white',
                             'center', (0, -dragon_button.height / 40), 2, 'black')
            team_mark.transform_image(pygame.transform.rotate, 45)
            dragon_button.add_element('team_mark', team_mark)

            dragon_image = dragon_button.get_image('dragon').image_copy
            dragon_image.fill((0, 0, 0, 128), special_flags=pygame.BLEND_RGBA_SUB)
            dragon_button.get_image('dragon').add_temporary_image(dragon_image)

        if removed_team_dragon:
            dragon_button = dragon_list_section.get_button(removed_team_dragon.name)
            dragon_button.remove_element('team_mark')
            dragon_button.get_image('dragon').remove_temporary_image()

    @classmethod
    def _new_destination(cls, dragon_index: int) -> tuple[int, int]:
        dragon_index %= 10

        x = cls._X_DESTINATIONS[dragon_index % 5]
        if dragon_index <= 4:
            y = cls._ROW_1_Y_DESTINATION
        else:
            y = cls._ROW_2_Y_DESTINATION

        return x, round(y)


user.add_dragons_observer(_DragonButton)
