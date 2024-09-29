from dragons_game.dragons.user_dragon import UserDragon
from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.elements.tooltip import Tooltip
from dragons_game.game_states.common import universal_sizes
from dragons_game.user import user
from dragons_game.utils import custom_exceptions, custom_types
from dragons_game.utils.image_proportions import proportional_width
from dragons_game.utils.observers import Observer


class ButtonSection(Section):
    def __init__(self, dragon: UserDragon, width: float, destination: tuple[float, float]):
        super().__init__((width, 2.25 * universal_sizes.LARGE), 'midbottom', destination)

        self.add_element('feed', _FeedButton(dragon))
        self.add_element('team', _TeamSection(dragon, self.width))

    @staticmethod
    def text(text: str, position: custom_types.Position, x_destination: float) -> Text:
        return Text('dragons_game/fonts/rurik.ttf', universal_sizes.LARGE / 1.5, text, 'white', position,
                    (x_destination, universal_sizes.LARGE / 10), 2, 'black')

    @staticmethod
    def tooltip(text: str) -> Tooltip:
        text_element = Text('dragons_game/fonts/friz_quadrata.ttf', universal_sizes.MEDIUM / 1.5, text, 'white',
                            'center', (0, 0), 1, 'black')

        tooltip = Tooltip('midbottom', (
            text_element.width + 1.25 * universal_sizes.SMALL, text_element.height + 1.25 * universal_sizes.SMALL),
                          '#dc0000', 3, 'black', 200)

        tooltip.add_element('text', text_element)
        return tooltip


class _FeedButton(Button):
    def __init__(self, dragon: UserDragon):
        self._dragon = dragon
        self._fish = 20
        self._health = 30

        height = universal_sizes.LARGE
        padding = universal_sizes.MEDIUM

        text = ButtonSection.text(f'Feed: {self._fish}', 'midleft', padding)

        icon_height = height / 1.5
        icon_width = proportional_width('dragons_game/graphics/icons/fish.png', icon_height)
        icon = Image('dragons_game/graphics/icons/fish.png', (icon_width, icon_height), 'midright', (-padding, 0))

        super().__init__('dragons_game/graphics/buttons/sort_key.png',
                         (text.width + icon_width + 2.1 * padding, height), 'topleft', (0, 0),
                         {'action': 'call', 'callable': self._feed_dragon})

        self.add_element('text', text)
        self.add_element('icon', icon)

    def _feed_dragon(self) -> None:
        if self._dragon.current_health >= self._dragon.max_health:
            self.add_onetime_hover_action(
                {'action': 'show_tooltip', 'tooltip': ButtonSection.tooltip('Your dragon has maximum health!')})
            return

        try:
            user.fish -= self._fish
        except custom_exceptions.NotEnoughFishError:
            self.add_onetime_hover_action(
                {'action': 'show_tooltip', 'tooltip': ButtonSection.tooltip("You don't have enough fish!")})
        else:
            self._dragon.add_health(self._health)


class _TeamSection(Section, Observer):
    def __init__(self, dragon: UserDragon, max_width: float):
        super().__init__((max_width, universal_sizes.LARGE), 'midbottom', (0, 0))

        self._in_team_section = Section((max_width / 2.5, self.height), 'center', (0, 0))
        self._in_team_section.add_element('background', Image('dragons_game/graphics/buttons/sort_key.png',
                                                              self._in_team_section.size, 'center', (0, 0)))
        self._in_team_section.add_element('label', ButtonSection.text('In team', 'center', 0))

        self._add_button = Button('dragons_game/graphics/buttons/sort_key.png', (max_width / 2.5, self.height),
                                  'center', (0, 0), {'action': 'call', 'callable': self._add_choose_section})
        self._add_button.add_element('label', ButtonSection.text('Add to team', 'center', 0))

        self._choose_section = Section(self.size, 'center', (0, 0))
        self._choose_section.add_element('background',
                                         Image('dragons_game/graphics/buttons/sort_key.png', self._choose_section.size,
                                               'center', (0, 0)))
        self._choose_section.add_element('label', ButtonSection.text('Choose team dragon to replace', 'center', 0))

        self._dragon = dragon
        dragon.add_in_team_observer(self)

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
