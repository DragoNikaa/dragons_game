from typing import Any, Literal

Color = int | str | tuple[int, int, int]

Position = Literal[
    'topleft', 'bottomleft', 'topright', 'bottomright', 'midtop', 'midleft', 'midbottom', 'midright', 'center']

CustomEventDictKey = Literal['action', 'callable', 'details', 'kwargs', 'level', 'next_state', 'tooltip']
CustomEventDictValue = Literal[
    'battle', 'call', 'change_state', 'close_details', 'hide_tooltip', 'open_details', 'show_tooltip']
CustomEventDict = dict[CustomEventDictKey, CustomEventDictValue | Any]

DragonsSortKey = Literal['name', 'rarity', 'level', 'energy', 'health']
