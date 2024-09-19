import pygame

from dragons_game.dragons.dragon import Dragon
from dragons_game.dragons.user_dragon import UserDragon
from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.multiline_text import MultilineScrollText, MultilineTextFixedSectionHeight
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.common.rarity_stars import rarity_stars
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section
from dragons_game.game_states.game_state import GameState
from dragons_game.user import user
from dragons_game.utils import custom_types
from dragons_game.utils.image_proportions import proportional_height, proportional_width
from dragons_game.utils.observers import Observer


class DragonDetails(Section):
    _TEXT_SIZE = GameConfig.WINDOW_HEIGHT / 38

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

        dragon_image_width = self.width / 2.5
        dragon_image_height = proportional_height(dragon.image_path, dragon_image_width)

        max_height = (self.height - name.height - name.y_destination - self._team_section.height
                      + self._team_section.y_destination - universal_sizes.LARGE)
        if dragon_image_height > max_height:
            dragon_image_height = max_height
            dragon_image_width = proportional_width(dragon.image_path, dragon_image_height)

        self.add_element('dragon', Image(dragon.image_path, (dragon_image_width, dragon_image_height), 'center',
                                         (name.x_destination, self.height / 28)))

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

    def _add_rarity_section(self) -> None:
        rarity_section = self._section(0.1, 'Rarity')

        for star_index, star in enumerate(rarity_stars(self._dragon.rarity, self._TEXT_SIZE, self._padding)):
            rarity_section.add_element(f'star_{star_index}', star)
        last_star = rarity_section.get_image('star_5')

        rarity_section.add_element('text', self.text(f'{str(self._dragon.rarity).title()}', 'midleft',
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

        stats_section.add_element('level',
                                  self.text(f'Level {self._dragon.level}', 'midtop', (self._padding, self._padding)))

        progress_bar_size = (
            stats_section.width / 1.5, (stats_section.height - self._TEXT_SIZE - 4 * self._padding) / 3)
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

        basic_name = self.text(self._dragon.basic_attack.name, 'topleft',
                               (icon_size + 2 * self._padding, self._padding))
        attacks_section.add_element('special_name', self.text(self._dragon.special_attack.name, 'topleft', (
            basic_name.x_destination, icon_size + 1.5 * self._padding)))

        description_size = (
            attacks_section.width - icon_size - 3 * self._padding, icon_size - self._TEXT_SIZE - self._padding / 2)

        basic_description = MultilineTextFixedSectionHeight(description_size, 'topleft', (
            basic_name.x_destination, self._TEXT_SIZE + 1.5 * self._padding), 3, 'dragons_game/fonts/friz_quadrata.ttf',
                                                            self._dragon.basic_attack.description, 'white', 1, 'black')

        attacks_section.add_element('special_description', MultilineTextFixedSectionHeight(description_size, 'topleft',
                                                                                           (
                                                                                               basic_description.x_destination,
                                                                                               icon_size + self._TEXT_SIZE + 2 * self._padding),
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

    @classmethod
    def text(cls, text: str, position: custom_types.Position, destination: tuple[float, float]) -> Text:
        return Text('dragons_game/fonts/friz_quadrata.ttf', cls._TEXT_SIZE, text, 'white', position, destination, 1,
                    'black')

    def clean_up(self) -> None:
        self._team_section.clean_up()
        self._team_section.update_on_notify()
        self.description_text.clean_up()


class _TeamSection(Section, Observer):
    def __init__(self, dragon: UserDragon, width: float, destination: tuple[float, float]):
        super().__init__((width, universal_sizes.LARGE), 'midbottom', destination)

        self._in_team_section = Section((self.width / 2.25, self.height), 'center', (0, 0))
        self._in_team_section.add_element('background', Image('dragons_game/graphics/buttons/sort_key.png',
                                                              self._in_team_section.size, 'center', (0, 0)))
        self._in_team_section.add_element('label', self._text('In team'))

        self._add_button = Button('dragons_game/graphics/buttons/sort_key.png', (self.width / 2.25, self.height),
                                  'center', (0, 0), {'action': 'call', 'callable': self._add_choose_section})
        self._add_button.add_element('label', self._text('Add to team'))

        self._choose_section = Section(self.size, 'center', (0, 0))
        self._choose_section.add_element('background',
                                         Image('dragons_game/graphics/buttons/sort_key.png', self._choose_section.size,
                                               'center', (0, 0)))
        self._choose_section.add_element('label', self._text('Choose team dragon to replace'))

        self._dragon = dragon
        dragon.add_in_team_observer(self)

    def _text(self, text: str) -> Text:
        return Text('dragons_game/fonts/rurik.ttf', self.height / 1.5, text, 'white', 'center', (0, self.height / 10),
                    2, 'black')

    def _add_choose_section(self) -> None:
        from dragons_game.game_states.dragons_menu.sections.team import team_section

        self.upsert_element('team_status', self._choose_section)

        for dragon_index in range(3):
            team_section.get_button(f'team_dragon_{dragon_index}').add_temporary_click_action(
                {'action': 'call', 'callable': user.add_team_dragon,
                 'kwargs': {'dragon': self._dragon, 'dragon_index': dragon_index}})

    def update_on_notify(self) -> None:
        if self._dragon.in_team:
            self.upsert_element('team_status', self._in_team_section)
        else:
            self.upsert_element('team_status', self._add_button)
            self.clean_up()

    @staticmethod
    def clean_up() -> None:
        from dragons_game.game_states.dragons_menu.sections.team import team_section

        for dragon_index in range(3):
            team_section.get_button(f'team_dragon_{dragon_index}').remove_temporary_click_action()


class _ProgressBar(Section, Observer):
    def __init__(self, name: str, dragon: Dragon, size: tuple[float, float], destination: tuple[float, float],
                 label_x_destination: float):
        super().__init__(size, 'bottomright', destination)

        self._name = name
        self._dragon = dragon

        self.add_element('background',
                         Image(f'dragons_game/graphics/progress_bars/background.png', size, 'topleft', (0, 0)))

        self.add_element('label', DragonDetails.text(name.title(), 'midleft', (label_x_destination, 0)))

        getattr(dragon, f"add_{self._name}_observer")(self)

    def update_on_notify(self) -> None:
        current_value = getattr(self._dragon, f'current_{self._name}')
        max_value = getattr(self._dragon, f'max_{self._name}')

        self.upsert_element('current', Image(f'dragons_game/graphics/progress_bars/{self._name}.png',
                                             (current_value / max_value * self.width, self.height), 'midleft', (0, 0)))

        self.upsert_element('numbers', DragonDetails.text(f'{current_value}/{max_value}', 'center', (0, 0)))
