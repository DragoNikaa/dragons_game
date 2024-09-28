import pygame

from dragons_game.dragons.user_dragon import UserDragon
from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.multiline_text import MultilineScrollText, MultilineTextFixedSectionHeight
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.common.rarity_stars import rarity_stars
from dragons_game.game_states.dragons_menu.sections.dragon_details.bottom_bar import _TeamSection
from dragons_game.game_states.dragons_menu.sections.dragon_details.utils import _LevelText, _ProgressBar, _Text
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section
from dragons_game.game_states.game_state import GameState
from dragons_game.utils.image_proportions import proportional_height, proportional_width


class DragonDetails(Section):
    def __init__(self, dragon: UserDragon):
        super().__init__((GameConfig.WINDOW_WIDTH * 6 / 7, GameConfig.WINDOW_HEIGHT), 'topleft',
                         (GameConfig.WINDOW_WIDTH / 7, 0))

        self._dragon = dragon

        self.add_element('dragon_background',
                         Image('dragons_game/graphics/backgrounds/dragons_menu/dragon_details/dragon.png',
                               (self.width / 2, self.height), 'topleft', (0, 0)))

        name = Text('dragons_game/fonts/rurik.ttf', self.height / 9, dragon.name, dragon.rarity.color, 'midtop',
                    (-self.width / 4, 1.5 * universal_sizes.LARGE), 4, 'black')
        self.add_element('name', name)

        self._team_section = _TeamSection(dragon, self.width / 2.75, (name.x_destination, -universal_sizes.LARGE))
        self.add_element('team', self._team_section)

        self._add_dragon_image(name)

        self.add_element('right_background',
                         Image('dragons_game/graphics/backgrounds/dragons_menu/dragon_details/right.png',
                               (self.width / 2, self.height), 'topright', (0, 0)))

        self.add_element('close', Button('dragons_game/graphics/buttons/close.png',
                                         (title_bar_section.height, title_bar_section.height), 'topright', (0, 0),
                                         {'action': 'change_state', 'next_state': GameState.DRAGONS_MENU}))

        self._padding = self.width / 80

        self._add_rarity_section()
        self._add_description_section()
        self._add_stats_section()
        self._add_attacks_section()

    def _add_dragon_image(self, name: Text) -> None:
        dragon_image_width = self.width / 2.5
        dragon_image_height = proportional_height(self._dragon.image_path, dragon_image_width)

        max_height = (
                self.height - name.height - name.y_destination - self._team_section.height + self._team_section.y_destination - universal_sizes.LARGE)
        if dragon_image_height > max_height:
            dragon_image_height = max_height
            dragon_image_width = proportional_width(self._dragon.image_path, dragon_image_height)

        self.add_element('dragon', Image(self._dragon.image_path, (dragon_image_width, dragon_image_height), 'center',
                                         (name.x_destination, self.height / 28)))

    def _add_rarity_section(self) -> None:
        rarity_section = self._section(0.1, 'Rarity')

        for star_index, star in enumerate(rarity_stars(self._dragon.rarity, _Text.SIZE, self._padding)):
            rarity_section.add_element(f'star_{star_index}', star)
        last_star = rarity_section.get_image('star_5')

        rarity_section.add_element('text', _Text(f'{str(self._dragon.rarity).title()}', 'midleft',
                                                 (last_star.x_destination + last_star.width + self._padding, 0)))

        self.add_element('rarity', rarity_section)

    def _add_description_section(self) -> None:
        description_section = self._section(0.205, 'Description', self.get_section('rarity'))

        self.description_text = MultilineScrollText(
            (description_section.width - 2 * self._padding, description_section.height - 2 * self._padding), 'topleft',
            (self._padding, self._padding), 4, 'dragons_game/fonts/friz_quadrata.ttf', self._dragon.description,
            'white', 1, 'black')
        description_section.add_element('text', self.description_text)

        self.add_element('description', description_section)

    def _add_stats_section(self) -> None:
        stats_section = self._section(0.3, 'Statistics', self.get_section('description'))

        stats_section.add_element('level', _LevelText(self._dragon, (self._padding, self._padding)))

        progress_bar_size = (stats_section.width / 1.5, (stats_section.height - _Text.SIZE - 4 * self._padding) / 3)
        label_x_destination = progress_bar_size[0] + 2 * self._padding - stats_section.width

        health_bar = _ProgressBar('health', self._dragon, progress_bar_size, (-self._padding, -self._padding),
                                  label_x_destination)
        energy_bar = _ProgressBar('energy', self._dragon, progress_bar_size,
                                  (-self._padding, health_bar.y_destination - health_bar.height - self._padding / 2),
                                  label_x_destination)
        experience_bar = _ProgressBar('experience', self._dragon, progress_bar_size, (
            -self._padding, energy_bar.y_destination - health_bar.height - self._padding / 2), label_x_destination)

        stats_section.add_element('health', health_bar)
        stats_section.add_element('energy', energy_bar)
        stats_section.add_element('experience', experience_bar)

        self.add_element('stats', stats_section)

    def _add_attacks_section(self) -> None:
        attacks_section = self._section(0.395, 'Attacks', self.get_section('stats'))

        icon_size = (attacks_section.height - 2.5 * self._padding) / 2

        attacks_section.add_element('basic_icon',
                                    Image('dragons_game/graphics/icons/attacks/basic.png', (icon_size, icon_size),
                                          'topleft', (self._padding, self._padding)))
        attacks_section.add_element('special_icon',
                                    Image('dragons_game/graphics/icons/attacks/special.png', (icon_size, icon_size),
                                          'bottomleft', (self._padding, -self._padding)))

        basic_name = _Text(self._dragon.basic_attack.name, 'topleft', (icon_size + 2 * self._padding, self._padding))
        attacks_section.add_element('special_name', _Text(self._dragon.special_attack.name, 'topleft',
                                                          (basic_name.x_destination, icon_size + 1.5 * self._padding)))

        description_size = (
            attacks_section.width - icon_size - 3 * self._padding, icon_size - _Text.SIZE - self._padding / 2)

        basic_description = MultilineTextFixedSectionHeight(description_size, 'topleft', (
            basic_name.x_destination, _Text.SIZE + 1.5 * self._padding), 3, 'dragons_game/fonts/friz_quadrata.ttf',
                                                            self._dragon.basic_attack.description, 'white', 1, 'black')

        attacks_section.add_element('special_description', MultilineTextFixedSectionHeight(description_size, 'topleft',
                                                                                           (
                                                                                               basic_description.x_destination,
                                                                                               icon_size + _Text.SIZE + 2 * self._padding),
                                                                                           3,
                                                                                           'dragons_game/fonts/friz_quadrata.ttf',
                                                                                           self._dragon.special_attack.description,
                                                                                           'white', 1, 'black'))

        attacks_section.add_element('basic_name', basic_name)
        attacks_section.add_element('basic_description', basic_description)

        self.add_element('attacks', attacks_section)

    def _section(self, height_percentage: float, title: str, previous_section: Section | None = None) -> Section:
        total_height = self.height - 7 * universal_sizes.LARGE
        height = height_percentage * total_height

        if previous_section:
            y_destination = previous_section.y_destination + previous_section.height + 1.5 * universal_sizes.LARGE
        else:
            y_destination = 1.5 * universal_sizes.LARGE

        section = Section((self.width / 2 - 3 * universal_sizes.LARGE, height), 'topleft',
                          (self.width / 2 + 1.5 * universal_sizes.LARGE, y_destination))

        section.add_element('background',
                            Image('dragons_game/graphics/backgrounds/dragons_menu/dragon_details/text.png',
                                  section.size, 'topleft', (0, 0)))

        border_size = (section.width, self.height / 130)
        section.add_element('top_border',
                            Image('dragons_game/graphics/backgrounds/dragons_menu/dragon_details/text_top_border.png',
                                  border_size, 'topleft', (0, 0)))
        bottom_border = Image('dragons_game/graphics/backgrounds/dragons_menu/dragon_details/text_top_border.png',
                              border_size, 'bottomleft', (0, 0))
        bottom_border.transform_image(pygame.transform.rotate, 180)
        section.add_element('bottom_border', bottom_border)

        title_size = universal_sizes.LARGE
        section.add_element('title', Text('dragons_game/fonts/rurik.ttf', title_size, title, self._dragon.rarity.color,
                                          'topleft', (0, border_size[1] - title_size), 3, 'black'))

        return section

    def clean_up(self) -> None:
        self._team_section.clean_up()
        self._team_section.update_on_notify()
        self.description_text.clean_up()
