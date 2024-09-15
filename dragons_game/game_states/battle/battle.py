import random
import time

import pygame

from dragons_game.dragons.dragon import Dragon
from dragons_game.dragons.enemy_dragon import EnemyDragon
from dragons_game.game_states.game_state import GameState
from dragons_game.user import user
from dragons_game.utils import custom_events, custom_exceptions
from dragons_game.utils.observers import Observer


class _Battle:
    def __init__(self) -> None:
        self._user_turn = True
        self._current_user_dragon_index = self._current_enemy_dragon_index = 0

        self._user_dragons = user.team_dragons.copy()
        self._enemy_dragons = user.current_level.enemy_dragons.copy()

        self._current_dragon_observers: list[Observer] = []

    def setup(self) -> None:
        from dragons_game.game_states.battle.sections.top_menu import attacks_section, points_bar

        self._user_turn = True
        self._current_user_dragon_index = self._current_enemy_dragon_index = 0

        self._user_dragons = user.team_dragons.copy()
        self._enemy_dragons = user.current_level.enemy_dragons.copy()

        for dragon in self._enemy_dragons:
            dragon.restore_health()

        attacks_section.clean_up()
        points_bar.clean_up()

    def user_attack(self, dragon: EnemyDragon) -> None:
        if self._user_turn:
            from dragons_game.game_states.battle.sections.top_menu import attacks_section, points_bar

            attack = attacks_section.selected_attack
            points_bar.remove_points(attack.cost)

            try:
                attack.action(dragon)
            except custom_exceptions.DragonHealthError:
                from dragons_game.game_states.battle.sections.battlefield import battlefield_section

                battlefield_section.remove_element(dragon.name)
                self._enemy_dragons.remove(dragon)

                if not self._enemy_dragons:
                    self._user_win()
                    return

            self._change_turn()

    def enemy_attack(self) -> None:
        if not self._user_turn:
            time.sleep(1)

            attack = self._enemy_dragons[self._current_enemy_dragon_index].basic_attack
            dragon = random.choice(self._user_dragons)

            try:
                attack.action(dragon)
            except custom_exceptions.DragonHealthError:
                from dragons_game.game_states.battle.sections.battlefield import battlefield_section

                battlefield_section.remove_element(dragon.name)
                self._user_dragons.remove(dragon)

                if not self._user_dragons:
                    self._enemy_win()
                    return

            self._change_turn()

    def _change_turn(self) -> None:
        self._user_turn = not self._user_turn

        if self._user_turn:
            from dragons_game.game_states.battle.sections.top_menu import points_bar

            points_bar.add_point()

            self._current_user_dragon_index += 1
            if self._current_user_dragon_index >= len(self._user_dragons):
                self._current_user_dragon_index = 0

        else:
            self._current_enemy_dragon_index += 1
            if self._current_enemy_dragon_index >= len(self._enemy_dragons):
                self._current_enemy_dragon_index = 0

            pygame.event.post(
                pygame.event.Event(custom_events.BATTLE, {'action': 'call', 'callable': self.enemy_attack}))

        self._notify_current_dragon_observers()

    def _user_win(self) -> None:
        print('Victory!')
        pygame.event.post(
            pygame.event.Event(custom_events.BATTLE, {'action': 'change_state', 'next_state': GameState.MAIN_MENU}))

    def _enemy_win(self) -> None:
        print('Defeat!')
        pygame.event.post(
            pygame.event.Event(custom_events.BATTLE, {'action': 'change_state', 'next_state': GameState.MAIN_MENU}))

    def add_current_dragon_observer(self, observer: Observer) -> None:
        self._current_dragon_observers.append(observer)
        observer.update_on_notify()

    def _notify_current_dragon_observers(self) -> None:
        for observer in self._current_dragon_observers:
            observer.update_on_notify()

    @property
    def user_turn(self) -> bool:
        return self._user_turn

    @property
    def current_user_dragon(self) -> Dragon:
        return self._user_dragons[self._current_user_dragon_index]


battle = _Battle()
