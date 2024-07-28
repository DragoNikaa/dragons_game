from typing import Literal, Any

import pygame

Color = int | str | tuple[int, int, int]

Position = Literal[
    'topleft', 'bottomleft', 'topright', 'bottomright', 'midtop', 'midleft', 'midbottom', 'midright', 'center']

CustomEventDictKey = Literal['action', 'next_state', 'tooltip']
CustomEventDictValue = Literal['change_state', 'show_tooltip']
CustomEventDict = dict[CustomEventDictKey, CustomEventDictValue | Any]
