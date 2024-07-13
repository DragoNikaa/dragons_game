from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    TOPLEFT = 'topleft'
    BOTTOMLEFT = 'bottomleft'
    TOPRIGHT = 'topright'
    BOTTOMRIGHT = 'bottomright'
    MIDTOP = 'midtop'
    MIDLEFT = 'midleft'
    MIDBOTTOM = 'midbottom'
    MIDRIGHT = 'midright'
    CENTER = 'center'
