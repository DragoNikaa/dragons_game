from dragons_game.utils import custom_types
from dragons_game.elements.button import Button
from dragons_game.elements.elements_section import ElementsSection
from dragons_game.elements.image import Image
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.utils.image_proportions import calculate_proportional_width
from dragons_game.game_states.game_state import GameState

bottom_buttons_section = ElementsSection((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT / 7), 'bottomleft',
                                         (0, GameConfig.WINDOW_HEIGHT))


class _BottomButton(Button):
    _WIDTH = bottom_buttons_section.width / 5
    _X_OFFSETS = [x_offset for x_offset in
                  range(bottom_buttons_section.rect.left, bottom_buttons_section.rect.right, int(_WIDTH))]

    def __init__(self, button_index: int, icon_image_path: str, label: str,
                 click_action: custom_types.CustomEventDict | None = None,
                 hover_action: custom_types.CustomEventDict | None = None):
        super().__init__(bottom_buttons_section, 'dragons_game/graphics/buttons/top_and_bottom.png',
                         (self._WIDTH, bottom_buttons_section.height), 'topleft', (self._X_OFFSETS[button_index], 0),
                         click_action, hover_action)

        icon_height = self.height / 1.85
        icon_width = calculate_proportional_width(icon_image_path, icon_height)
        self.add_image('icon',
                       Image(self, icon_image_path, (icon_width, icon_height), 'center', (-self._WIDTH / 3.15, 0)))

        self.add_text('label',
                      Text(self, 'dragons_game/fonts/pr_viking.ttf', int(self.height / 2.8), label, 'white', 'center',
                           (self._WIDTH / 7.7, 0), 3, 'black'))


bottom_buttons_section.add_button('hatchery', _BottomButton(0, 'dragons_game/graphics/icons/hatchery.png', 'Hatchery'))
bottom_buttons_section.add_button('dragons', _BottomButton(1, 'dragons_game/graphics/icons/dragons.png', 'Dragons',
                                                           {'action': 'change_state',
                                                            'next_state': GameState.DRAGONS_MENU}))
bottom_buttons_section.add_button('islands', _BottomButton(2, 'dragons_game/graphics/icons/islands.png', 'Islands'))
bottom_buttons_section.add_button('market', _BottomButton(3, 'dragons_game/graphics/icons/market.png', 'Market'))
bottom_buttons_section.add_button('settings', _BottomButton(4, 'dragons_game/graphics/icons/settings.png', 'Settings'))
