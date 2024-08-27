from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game.configuration import GameConfig
from dragons_game.utils import custom_types
from dragons_game.utils.image_proportions import proportional_width

top_buttons_section = Section((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT / 9), 'topleft', (0, 0))


class _TopButton(Button):
    _WIDTH = top_buttons_section.width / 4
    _X_DESTINATIONS = [x for x in range(top_buttons_section.rect.left, top_buttons_section.rect.right, round(_WIDTH))]

    def __init__(self, button_index: int, icon_image_path: str, amount: int,
                 click_action: custom_types.CustomEventDict | None = None,
                 hover_action: custom_types.CustomEventDict | None = None):
        super().__init__('dragons_game/graphics/buttons/top_and_bottom.png', (self._WIDTH, top_buttons_section.height),
                         'topleft', (self._X_DESTINATIONS[button_index], 0), click_action, hover_action)

        icon_height = self.height / 1.85
        icon_width = proportional_width(icon_image_path, icon_height)
        self.add_element('icon', Image(icon_image_path, (icon_width, icon_height), 'center', (-self._WIDTH / 3, 0)))

        self.add_element('amount',
                         Text('dragons_game/fonts/pr_viking.ttf', self.height / 2, str(amount), 'white', 'center',
                              (self._WIDTH / 10, 0), 3, 'black'))


top_buttons_section.add_element('trophies', _TopButton(0, 'dragons_game/graphics/icons/trophies.png', 21372))
top_buttons_section.add_element('eggs', _TopButton(1, 'dragons_game/graphics/icons/eggs.png', 42))
top_buttons_section.add_element('fish', _TopButton(2, 'dragons_game/graphics/icons/fish.png', 2137))
top_buttons_section.add_element('coins', _TopButton(3, 'dragons_game/graphics/icons/coins.png', 424242))
