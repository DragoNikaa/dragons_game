import random
import time

import pygame

from dragons_game.dragons.attack import Attack
from dragons_game.dragons.dragon import Dragon
from dragons_game.dragons.enemy_dragon import EnemyDragon
from dragons_game.dragons.user_dragon import UserDragon
from dragons_game.game_states.game_state import GameState
from dragons_game.user import user
from dragons_game.utils import custom_events, custom_exceptions
from dragons_game.utils.observers import Observer


class _Battle:
    def __init__(self) -> None:
        self._user_dragons = user.team_dragons.copy()
        self._enemy_dragons = user.current_level.enemy_dragons.copy()

        self._dragons_queue = [dragon for pair in zip(self._user_dragons, self._enemy_dragons) for dragon in pair]
        self._current_dragon_index = 0

        self._current_dragon_observers: list[Observer] = []

    def setup(self) -> None:
        from dragons_game.game_states.battle.sections.top_menu import attacks_section, points_bar

        self._user_dragons = user.team_dragons.copy()
        self._enemy_dragons = user.current_level.enemy_dragons.copy()

        self._dragons_queue = [dragon for pair in zip(self._user_dragons, self._enemy_dragons) for dragon in pair]
        self._current_dragon_index = 0

        for dragon in self._enemy_dragons:
            dragon.restore_health()

        attacks_section.clean_up()
        points_bar.clean_up()

    def user_attack(self, dragon: EnemyDragon) -> None:
        if self.user_turn:
            from dragons_game.game_states.battle.sections.top_menu import attacks_section, points_bar

            attack = attacks_section.selected_attack
            points_bar.remove_points(attack.cost)

            self._attack(attack, dragon)
            self._next_turn()

    def enemy_attack(self) -> None:
        if not self.user_turn:
            time.sleep(1)

            attack = self._dragons_queue[self._current_dragon_index].basic_attack
            dragon = random.choice(self._user_dragons)

            self._attack(attack, dragon)
            self._next_turn()

    def _attack(self, attack: Attack, dragon: Dragon) -> None:
        try:
            attack(dragon)
        except custom_exceptions.DragonHealthError:
            from dragons_game.game_states.battle.sections.battlefield import battlefield_section

            battlefield_section.remove_element(dragon.name)
            self._dragons_queue.remove(dragon)

            if isinstance(dragon, UserDragon):
                self._user_dragons.remove(dragon)
            elif isinstance(dragon, EnemyDragon):
                self._enemy_dragons.remove(dragon)

    def _next_turn(self) -> None:
        if not self._enemy_dragons:
            self._end(user_win=True)
            return

        elif not self._user_dragons:
            self._end(user_win=False)
            return

        self._current_dragon_index += 1
        if self._current_dragon_index >= len(self._dragons_queue):
            self._current_dragon_index = 0

        self._notify_current_dragon_observers()

        if self.user_turn:
            from dragons_game.game_states.battle.sections.top_menu import points_bar

            points_bar.add_point()
        else:
            pygame.event.post(
                pygame.event.Event(custom_events.BATTLE, {'action': 'call', 'callable': self.enemy_attack}))

    def _end(self, user_win: bool) -> None:
        if user_win:
            print('Victory!')

            for dragon in user.team_dragons:
                dragon.add_experience(100)

        else:
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
    def current_dragon(self) -> Dragon:
        return self._dragons_queue[self._current_dragon_index]

    @property
    def user_turn(self) -> bool:
        return isinstance(self.current_dragon, UserDragon)


battle = _Battle()
