from typing import Literal, Sequence

import pygame

from dragons_game.dragons.dragon import Dragon
from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.battle.battle import battle
from dragons_game.user import user
from dragons_game.utils import custom_types
from dragons_game.utils.image_proportions import proportional_height


class BattlefieldSection(Section):
    def __init__(self) -> None:
        super().__init__((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT), 'topleft', (0, 0))

        self.add_element('background', Image(user.current_level.battle_image_path, self.size, 'topleft', (0, 0)))

        self._add_dragons('user', user.team_dragons, 'left', user.current_level.user_dragons_factors)
        self._add_dragons('enemy', user.current_level.enemy_dragons, 'right', user.current_level.enemy_dragons_factors)

    def _add_dragons(self, dragon_type: Literal['user', 'enemy'], dragons: Sequence[Dragon],
                     facing_to_flip: custom_types.Facing, factors: custom_types.DragonsFactors) -> None:
        for dragon_index, dragon in enumerate(dragons):
            if dragon_type == 'enemy':
                click_action: custom_types.CustomEventDict | None = {'action': 'call', 'callable': battle.user_attack,
                                                                     'kwargs': {'dragon_index': dragon_index}}
            else:
                click_action = None

            dragon_button = Button(dragon.image_path, self._scaled_size(dragon), 'center',
                                   (self.width / factors[dragon_index][0], self.height / factors[dragon_index][1]),
                                   click_action)
            self.add_element(f'{dragon_type}_dragon_{dragon_index}', dragon_button)

            if dragon.facing == facing_to_flip:
                dragon_button.transform_image(pygame.transform.flip, 1, 0)

    def _scaled_size(self, dragon: Dragon) -> tuple[float, float]:
        original_width = self.width / 8
        height = proportional_height(dragon.image_path, original_width)

        width = original_width * original_width / height

        if width > 1.1 * original_width:
            width = 1.1 * original_width
        elif width < 0.9 * original_width:
            width = 0.9 * original_width

        return width, proportional_height(dragon.image_path, width)
