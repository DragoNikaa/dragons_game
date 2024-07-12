from dataclasses import dataclass


@dataclass(frozen=True)
class _Position:
    TOPLEFT = 'topleft'
    BOTTOMLEFT = 'bottomleft'
    TOPRIGHT = 'topright'
    BOTTOMRIGHT = 'bottomright'
    MIDTOP = 'midtop'
    MIDLEFT = 'midleft'
    MIDBOTTOM = 'midbottom'
    MIDRIGHT = 'midright'
    CENTER = 'center'


position = _Position()
