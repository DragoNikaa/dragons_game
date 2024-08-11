from typing import Any, Literal

Color = int | str | tuple[int, int, int]

Position = Literal[
    'topleft', 'bottomleft', 'topright', 'bottomright', 'midtop', 'midleft', 'midbottom', 'midright', 'center']

CustomEventDictKey = Literal['action', 'callable', 'next_state', 'tooltip']
CustomEventDictValue = Literal['call', 'change_state', 'show_tooltip']
CustomEventDict = dict[CustomEventDictKey, CustomEventDictValue | Any]

DragonsSortKey = Literal['name', 'rarity', 'level', 'energy', 'health']
