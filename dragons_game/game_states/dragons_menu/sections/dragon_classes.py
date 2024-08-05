from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.game_states.common import universal_sizes
from dragons_game.game_states.dragons_menu.sections.dragons import dragons_section
from dragons_game.game_states.dragons_menu.sections.page import page_section
from dragons_game.utils.image_proportions import calculate_proportional_width


class _DragonClassButton(Button):
    def __init__(self, image_path: str, previous_button: '_DragonClassButton | None' = None):
        height = page_section.height
        width = calculate_proportional_width(image_path, height)

        if previous_button is None:
            x = 0
        else:
            x = previous_button.x_destination + previous_button.width + universal_sizes.MEDIUM

        super().__init__(image_path, (width, height), 'topleft', (x, 0))


_common = _DragonClassButton('dragons_game/graphics/buttons/dragon_classes/common.png')
_uncommon = _DragonClassButton('dragons_game/graphics/buttons/dragon_classes/uncommon.png', _common)
_rare = _DragonClassButton('dragons_game/graphics/buttons/dragon_classes/rare.png', _uncommon)
_epic = _DragonClassButton('dragons_game/graphics/buttons/dragon_classes/epic.png', _rare)
_legendary = _DragonClassButton('dragons_game/graphics/buttons/dragon_classes/legendary.png', _epic)
_mythical = _DragonClassButton('dragons_game/graphics/buttons/dragon_classes/mythical.png', _legendary)

section_width = sum([button.width + universal_sizes.MEDIUM for button in
                     (_common, _uncommon, _rare, _epic, _legendary, _mythical)]) - universal_sizes.MEDIUM
dragon_classes_section = Section((section_width, page_section.height), 'center', (
    ((page_section.rect.right + dragons_section.rect.right) / 2, page_section.rect.centery)))

dragon_classes_section.add_element('common', _common)
dragon_classes_section.add_element('uncommon', _uncommon)
dragon_classes_section.add_element('rare', _rare)
dragon_classes_section.add_element('epic', _epic)
dragon_classes_section.add_element('legendary', _legendary)
dragon_classes_section.add_element('mythical', _mythical)
