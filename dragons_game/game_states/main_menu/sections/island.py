import pygame

from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.multiline_text import MultilineTextFixedTextSize
from dragons_game.elements.section import Section
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.main_menu.sections.bottom_buttons import bottom_buttons_section
from dragons_game.game_states.main_menu.sections.top_buttons import top_buttons_section
from dragons_game.islands.level import Level
from dragons_game.user import user
from dragons_game.utils import custom_events, custom_exceptions, custom_types


class _IslandSection(Section):
    def __init__(self) -> None:
        super().__init__((GameConfig.WINDOW_WIDTH,
                          GameConfig.WINDOW_HEIGHT - top_buttons_section.height - bottom_buttons_section.height),
                         'topleft', (0, top_buttons_section.rect.bottom))

        island = user.current_island

        self.add_element('background', Image(island.image_path, self.size, 'topleft', (0, 0)))

        self.add_element('easy', LevelButton(island.easy_level, self.size))
        self.add_element('medium', LevelButton(island.medium_level, self.size))
        self.add_element('hard', LevelButton(island.hard_level, self.size))
        self.add_element('fiendish', LevelButton(island.fiendish_level, self.size))


class LevelButton(Button):
    def __init__(self, level: Level, island_size: tuple[float, float]):
        super().__init__(level.button_image_path, (island_size[1] / 5, island_size[1] / 5), 'center',
                         (island_size[0] / level.button_factors[0], island_size[1] / level.button_factors[1]),
                         {'action': 'call', 'callable': self._manage_dragon_energy_and_start_battle},
                         {'action': 'show_tooltip', 'tooltip': level.tooltip})

        self._level = level

    def _manage_dragon_energy_and_start_battle(self) -> None:
        dragon_index = 0
        try:
            for dragon in user.team_dragons:
                dragon.remove_energy()
                dragon_index += 1
        except custom_exceptions.DragonEnergyError:
            for dragon in user.team_dragons[:dragon_index]:
                dragon.add_energy()

            self.add_onetime_hover_action({'action': 'show_tooltip', 'tooltip': self._tooltip(
                "Your dragons don't have enough energy to start this battle!", '#dc0000')})
            return

        pygame.event.post(pygame.event.Event(custom_events.BUTTON_CLICK, {'action': 'battle', 'level': self._level}))

    def handle_completed_level(self) -> None:
        new_image = pygame.image.load('dragons_game/graphics/buttons/levels/completed.png')
        new_image = pygame.transform.scale(new_image, self.size)
        self.set_image(new_image)

        self.set_click_action(None)
        self.set_hover_action({'action': 'show_tooltip', 'tooltip': self._tooltip('Level completed!', '#00da00')})

    @staticmethod
    def _tooltip(text: str, color: custom_types.Color) -> Tooltip:
        padding = 0.75 * universal_sizes.SMALL

        text_element = MultilineTextFixedTextSize(GameConfig.WINDOW_WIDTH / 3, 'center', (padding, padding),
                                                  'dragons_game/fonts/friz_quadrata.ttf', universal_sizes.MEDIUM, text,
                                                  'white', 1, 'black')

        tooltip = Tooltip('midbottom', (text_element.width + 2 * padding, text_element.height + 2 * padding), color, 3,
                          'black', 200)

        tooltip.add_element('text', text_element)
        return tooltip


island_section = _IslandSection()
