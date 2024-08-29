from dragons_game.dragons.dragon import Dragon
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.game_states.battle.sections.title_bar import title_bar_section
from dragons_game.game_states.common import universal_sizes
from dragons_game.user import user
from dragons_game.utils import custom_types

top_menu_section = Section((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT / 4.5), 'topleft',
                           (0, title_bar_section.rect.bottom))

_background = Image('dragons_game/graphics/backgrounds/dragons_menu/dragons.png', top_menu_section.size, 'topleft',
                    (0, 0))
_background.image.set_alpha(128)
top_menu_section.add_element('background', _background)

top_menu_section.add_element('border', Image('dragons_game/graphics/backgrounds/bottom_border.png',
                                             (top_menu_section.width, top_menu_section.height / 25), 'topleft',
                                             (0, top_menu_section.height)))


class HealthBarsSection(Section):
    def __init__(self) -> None:
        super().__init__((GameConfig.WINDOW_WIDTH / 3, top_menu_section.height - 2 * universal_sizes.MEDIUM), 'topleft',
                         (universal_sizes.MEDIUM, title_bar_section.rect.bottom + universal_sizes.MEDIUM))

        self._bar_height = (self.height - 2 * universal_sizes.SMALL) / 3

        for dragon_index, dragon in enumerate(user.team_dragons):
            y_destination = dragon_index * (self._bar_height + universal_sizes.SMALL)

            self.add_element(f'dragon_{dragon_index}_name', self._text(f'{dragon.name}', 'topleft', y_destination))
            self._add_progress_bar(dragon_index, dragon, y_destination)

    def _add_progress_bar(self, dragon_index: int, dragon: Dragon, y_destination: float) -> None:
        progress_bar = Section((0.6 * self.width, self._bar_height), 'topright', (0, y_destination))

        progress_bar.add_element('background',
                                 Image('dragons_game/graphics/progress_bars/background.png', progress_bar.size,
                                       'topleft', (0, 0)))

        progress_bar.add_element(f'current', Image(f'dragons_game/graphics/progress_bars/health.png', (
            dragon.current_health / dragon.max_health * progress_bar.width, progress_bar.height), 'topleft', (0, 0)))

        progress_bar.add_element('numbers', self._text(f'{dragon.current_health}/{dragon.max_health}', 'center', 0))

        self.add_element(f'dragon_{dragon_index}_health', progress_bar)

    def _text(self, text: str, position: custom_types.Position, y_destination: float) -> Text:
        return Text('dragons_game/fonts/friz_quadrata.ttf', 0.8 * self._bar_height, text, 'white', position,
                    (0, y_destination), 1, 'black')
