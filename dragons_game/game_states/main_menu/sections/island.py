from abc import ABC, abstractmethod

import pygame

from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.multiline_text import MultilineTextFixedTextSize
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.main_menu.sections.bottom_buttons import bottom_buttons_section
from dragons_game.game_states.main_menu.sections.top_buttons import top_buttons_section
from dragons_game.islands.level import Level
from dragons_game.islands.level_type import LevelType
from dragons_game.islands.rewards import Reward
from dragons_game.user import user
from dragons_game.utils import custom_events, custom_exceptions, custom_types
from dragons_game.utils.image_proportions import proportional_width


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


class _LevelButtonTooltip(Tooltip, ABC):
    @abstractmethod
    def __init__(self, level_type: LevelType):
        super().__init__('midbottom', (GameConfig.WINDOW_WIDTH / 4, 0), level_type.main_color, 5,
                         level_type.secondary_color, 200)

        self._padding = universal_sizes.SMALL
        self._text_size = universal_sizes.MEDIUM
        self._text_color = level_type.secondary_color


class _RewardsTooltip(_LevelButtonTooltip):
    def __init__(self, level_type: LevelType, rewards: dict[Reward, int]):
        super().__init__(level_type)

        level = self._text(str(level_type).title(), 'midtop', (0, self._padding))
        self.add_element('level', level)

        self._icon_height = universal_sizes.LARGE
        column_1_x = 2 * self._padding
        column_2_x = 0.57 * self.width
        row_1_y = level.height + 2 * self._padding
        row_2_y = row_1_y + self._icon_height + self._padding

        self._add_reward('trophies', (column_1_x, row_1_y), str(rewards[Reward.TROPHIES]))
        self._add_reward('eggs', (column_2_x, row_1_y), str(rewards[Reward.EGGS]))
        self._add_reward('fish', (column_1_x, row_2_y), str(rewards[Reward.FISH]))
        self._add_reward('coins', (column_2_x, row_2_y), str(rewards[Reward.COINS]))

        dragon_icon_name = 'dragons'
        if level_type is LevelType.FIENDISH:
            dragon_icon_name += '_2'
        self._add_reward(dragon_icon_name, (column_1_x, row_2_y + self._icon_height + self._padding),
                         f'{rewards[Reward.MIN_EXPERIENCE]}-{rewards[Reward.MAX_EXPERIENCE]} exp')

        self.change_size((self.width, level.height + 3 * self._icon_height + 5 * self._padding))

    def _add_reward(self, name: str, destination: tuple[float, float], text: str) -> None:
        image_path = f'dragons_game/graphics/icons/{name}.png'
        width = proportional_width(image_path, self._icon_height)

        icon = Image(image_path, (width, self._icon_height), 'topleft', destination)
        self.add_element(f'{name}_icon', icon)

        self.add_element(f'{name}_text', self._text(text, 'topleft', (
            destination[0] + icon.width + universal_sizes.MEDIUM, destination[1])))

    def _text(self, text: str, position: custom_types.Position, destination: tuple[float, float]) -> Text:
        return Text('dragons_game/fonts/viking.ttf', self._text_size, text, self._text_color, position, destination)


class _TextTooltip(_LevelButtonTooltip):
    def __init__(self, level_type: LevelType, text: str):
        super().__init__(level_type)

        text_element = MultilineTextFixedTextSize(GameConfig.WINDOW_WIDTH / 3, 'center', (self._padding, self._padding),
                                                  'dragons_game/fonts/friz_quadrata.ttf', self._text_size, text,
                                                  self._text_color)
        self.add_element('text', text_element)

        self.change_size((text_element.width + 2 * self._padding, text_element.height + 2 * self._padding))


class LevelButton(Button):
    def __init__(self, level: Level, island_size: tuple[float, float]):
        super().__init__(level.button_image_path, (island_size[1] / 5, island_size[1] / 5), 'center',
                         (island_size[0] / level.button_factors[0], island_size[1] / level.button_factors[1]),
                         {'action': 'call', 'callable': self._manage_dragon_energy_and_start_battle},
                         {'action': 'show_tooltip', 'tooltip': _RewardsTooltip(level.type, level.rewards)})

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

            self.add_onetime_hover_action({'action': 'show_tooltip', 'tooltip': _TextTooltip(self._level.type,
                                                                                             "Your dragons don't have enough energy to start this battle!")})
            return

        pygame.event.post(pygame.event.Event(custom_events.BUTTON_CLICK, {'action': 'battle', 'level': self._level}))

    def handle_completed_level(self) -> None:
        new_image = pygame.image.load('dragons_game/graphics/buttons/levels/completed.png')
        new_image = pygame.transform.scale(new_image, self.size)
        self.set_image(new_image)

        self.set_click_action(None)
        self.set_hover_action({'action': 'show_tooltip', 'tooltip': _TextTooltip(self._level.type, 'Level completed!')})


island_section = _IslandSection()
