import pygame

from dragons_game.dragons.dragon import Dragon
from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.new_line_text import NewLineText
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.title_bar import title_bar_section
from dragons_game.game_states.game_state import GameState
from dragons_game.user import user
from dragons_game.utils.image_proportions import calculate_proportional_height, calculate_proportional_width
from dragons_game.utils.observers import Observer


class DragonDetails(Section):
    def __init__(self, dragon: Dragon):
        super().__init__((GameConfig.WINDOW_WIDTH * 6 / 7, GameConfig.WINDOW_HEIGHT), 'topleft',
                         (GameConfig.WINDOW_WIDTH / 7, 0))

        self._dragon = dragon

        self.add_element('dragon_background',
                         Image('dragons_game/graphics/backgrounds/dragons_menu/dragon_details/dragon_background.png',
                               (self.width / 2, self.height), 'topleft', (0, 0)))

        name = Text('dragons_game/fonts/rurik.ttf', self.height / 9, dragon.name, dragon.rarity.color, 'midtop',
                    (-self.width / 4, 1.5 * universal_sizes.LARGE), 4, 'black')
        self.add_element('name', name)

        dragon_image_width = self.width / 2.5
        dragon_image_height = calculate_proportional_height(dragon.image_path, dragon_image_width)

        max_height = self.height - name.height - 3.5 * universal_sizes.LARGE
        if dragon_image_height > max_height:
            dragon_image_height = max_height
            dragon_image_width = calculate_proportional_width(dragon.image_path, dragon_image_height)

        self.add_element('dragon', Image(dragon.image_path, (dragon_image_width, dragon_image_height), 'center',
                                         (name.x_destination, self.height / 13.5)))

        self.add_element('right_background',
                         Image('dragons_game/graphics/backgrounds/dragons_menu/dragon_details/right_background.png',
                               (self.width / 2, self.height), 'topright', (0, 0)))

        self.add_element('close', Button('dragons_game/graphics/buttons/close.png',
                                         (title_bar_section.height, title_bar_section.height), 'topright', (0, 0),
                                         {'action': 'change_state', 'next_state': GameState.DRAGONS_MENU}))

        rarity_section = self._section(0.1, 'Rarity')

        description_section = self._section(0.3, 'Description', rarity_section)
        self.description_text = NewLineText(description_section.size, 'topleft', (0, 0),
                                            description_section.height / 10, 'dragons_game/fonts/friz_quadrata.ttf',
                                            description_section.height / 7.3, dragon.description, 'white', 1, 'black')
        description_section.add_element('text', self.description_text)

        stats_section = self._section(0.4, 'Statistics', description_section)
        attacks_section = self._section(0.2, 'Attacks', stats_section)

        self.add_element('rarity_section', rarity_section)
        self.add_element('description_section', description_section)
        self.add_element('stats_section', stats_section)
        self.add_element('attacks_section', attacks_section)

        self._team_section = _TeamSection(dragon, self.width)
        self.add_element('team', self._team_section)

    def _section(self, height_percentage: float, title: str, previous_section: Section | None = None) -> Section:
        total_height = self.height - 8.5 * universal_sizes.LARGE
        height = height_percentage * total_height

        if previous_section:
            y_destination = previous_section.y_destination + previous_section.height + 1.5 * universal_sizes.LARGE
        else:
            y_destination = 1.5 * universal_sizes.LARGE

        section = Section((self.width / 2 - 3 * universal_sizes.LARGE, height), 'topleft',
                          (self.width / 2 + 1.5 * universal_sizes.LARGE, y_destination))

        section.add_element('background',
                            Image('dragons_game/graphics/backgrounds/dragons_menu/dragon_details/text_background.png',
                                  section.size, 'topleft', (0, 0)))

        border_size = (section.width, self.height / 130)
        section.add_element('top_border', Image(
            'dragons_game/graphics/backgrounds/dragons_menu/dragon_details/text_background_top_border.png', border_size,
            'topleft', (0, 0)))
        bottom_border = Image(
            'dragons_game/graphics/backgrounds/dragons_menu/dragon_details/text_background_top_border.png', border_size,
            'bottomleft', (0, 0))
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


class _TeamSection(Section, Observer):
    def __init__(self, dragon: Dragon, section_width: float):
        super().__init__((section_width / 2.75, universal_sizes.LARGE), 'midbottom',
                         (section_width / 4, -universal_sizes.LARGE / 1.5))

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
