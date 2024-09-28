from dragons_game.dragons.user_dragon import UserDragon
from dragons_game.elements.button import Button
from dragons_game.elements.image import Image
from dragons_game.elements.section import Section
from dragons_game.elements.text import Text
from dragons_game.game_states.common import universal_sizes
from dragons_game.user import user
from dragons_game.utils.observers import Observer


class _TeamSection(Section, Observer):
    def __init__(self, dragon: UserDragon, width: float, destination: tuple[float, float]):
        super().__init__((width, universal_sizes.LARGE), 'midbottom', destination)

        self._in_team_section = Section((self.width / 2.25, self.height), 'center', (0, 0))
        self._in_team_section.add_element('background', Image('dragons_game/graphics/buttons/sort_key.png',
                                                              self._in_team_section.size, 'center', (0, 0)))
        self._in_team_section.add_element('label', self._text('In team'))

        self._add_button = Button('dragons_game/graphics/buttons/sort_key.png', (self.width / 2.25, self.height),
                                  'center', (0, 0), {'action': 'call', 'callable': self._add_choose_section})
        self._add_button.add_element('label', self._text('Add to team'))

        self._choose_section = Section(self.size, 'center', (0, 0))
        self._choose_section.add_element('background',
                                         Image('dragons_game/graphics/buttons/sort_key.png', self._choose_section.size,
                                               'center', (0, 0)))
        self._choose_section.add_element('label', self._text('Choose team dragon to replace'))

        self._dragon = dragon
        dragon.add_in_team_observer(self)

    def _text(self, text: str) -> Text:
        return Text('dragons_game/fonts/rurik.ttf', self.height / 1.5, text, 'white', 'center', (0, self.height / 10),
                    2, 'black')

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
