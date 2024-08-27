from dragons_game.dragons.dragon import Dragon
from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.game.configuration import GameConfig
from dragons_game.user import user
from dragons_game.utils.image_proportions import calculate_proportional_height


class BattleSection(Section):
    def __init__(self) -> None:
        super().__init__((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT), 'topleft', (0, 0))

        self.add_element('background', Image(user.current_level.battle_image_path, self.size, 'topleft', (0, 0)))

        self._add_user_dragons()

    def _add_user_dragons(self) -> None:
        for dragon_index, dragon in enumerate(user.team_dragons):
            factors = user.current_level.dragons_factors[dragon_index]

            self.add_element(f'user_dragon_{dragon_index}',
                             Button(dragon.image_path, self._scaled_size(dragon), 'center',
                                    (self.width / factors[0], self.height / factors[1])))

    def _scaled_size(self, dragon: Dragon) -> tuple[float, float]:
        original_width = self.width / 8
        height = calculate_proportional_height(dragon.image_path, original_width)

        width = original_width * original_width / height

        if width > 1.1 * original_width:
            width = 1.1 * original_width
        elif width < 0.9 * original_width:
            width = 0.9 * original_width

        return width, calculate_proportional_height(dragon.image_path, width)
