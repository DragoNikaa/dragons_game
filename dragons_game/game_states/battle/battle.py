import random
import time

import pygame

from dragons_game.dragons.dragon import Dragon
from dragons_game.game_states.game_state import GameState
from dragons_game.user import user
from dragons_game.utils import custom_events, custom_exceptions
from dragons_game.utils.observers import Observer


class _Battle:
    def __init__(self) -> None:
        self._user_turn = True
        self._current_dragon_index = 0

        self._current_dragon_observers: list[Observer] = []

    def user_attack(self, dragon_index: int) -> None:
        if self._user_turn:
            from dragons_game.game_states.battle.sections.top_menu import attacks_section

            try:
                attacks_section.selected_attack.action(user.current_level.enemy_dragons[dragon_index])
            except custom_exceptions.DragonHealthError:
                pygame.event.post(
                    pygame.event.Event(custom_events.BATTLE, {'action': 'call', 'callable': self._user_win}))
                return

            self._change_turn()

    def enemy_attack(self) -> None:
        if not self._user_turn:
            time.sleep(2)

            try:
                user.current_level.enemy_dragons[self._current_dragon_index].basic_attack.action(
                    user.team_dragons[random.randint(0, 2)])
            except custom_exceptions.DragonHealthError:
                pygame.event.post(
                    pygame.event.Event(custom_events.BATTLE, {'action': 'call', 'callable': self._enemy_win}))
                return

            self._change_turn()

    def _change_turn(self) -> None:
        if self._user_turn:
            pygame.event.post(
                pygame.event.Event(custom_events.BATTLE, {'action': 'call', 'callable': self.enemy_attack}))
        else:
            self._current_dragon_index += 1
            if self._current_dragon_index > 2:
                self._current_dragon_index = 0

        self._user_turn = not self._user_turn
        self._notify_current_dragon_observers()

    def _user_win(self) -> None:
        print('Victory!')
        pygame.event.post(
            pygame.event.Event(custom_events.BATTLE, {'action': 'change_state', 'next_state': GameState.MAIN_MENU}))

    def _enemy_win(self) -> None:
        print('Defeat!')
        pygame.event.post(
            pygame.event.Event(custom_events.BATTLE, {'action': 'change_state', 'next_state': GameState.MAIN_MENU}))

    def clean_up(self) -> None:
        from dragons_game.game_states.battle.sections.top_menu import attacks_section

        self._user_turn = True
        self._current_dragon_index = 0

        for dragon in user.current_level.enemy_dragons:
            dragon.restore_health()

        attacks_section.clean_up()

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
        return user.team_dragons[self._current_dragon_index]


battle = _Battle()
