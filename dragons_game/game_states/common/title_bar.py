from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.utils import custom_types
from dragons_game.utils.image_proportions import proportional_width


class TitleBar(Section):
    def __init__(self, size: tuple[float, float], position: custom_types.Position, destination: tuple[float, float],
                 icon_image_path: str, label: str, close_button_click_action: custom_types.CustomEventDict):
        super().__init__(size, position, destination)

        self.add_element('background', Image('dragons_game/graphics/backgrounds/title_bar.png',
                                             (self.width - self.height, self.height), 'topleft', (0, 0)))

        icon_height = self.height / 1.2
        icon_width = proportional_width(icon_image_path, icon_height)
        self.add_element('icon', Image(icon_image_path, (icon_width, icon_height), 'midleft', (self.height / 2, 0)))

        self.add_element('label', Text('dragons_game/fonts/pr_viking.ttf', self.height / 1.5, label, 'white', 'midleft',
                                       (self.height + icon_width, 0), 2, 'black'))

        self.add_element('close',
                         Button('dragons_game/graphics/buttons/close.png', (self.height, self.height), 'topright',
                                (0, 0), close_button_click_action))
