from dragons_game.elements.image import Image


def _star(star_number: int, stars_number: int, size: float, x_destination: float) -> Image:
    if star_number <= stars_number:
        color = 'gold'
    else:
        color = 'grey'

    return Image(f'dragons_game/graphics/icons/stars/{color}.png', (size, size), 'midleft',
                 (x_destination + (star_number - 1) * size, 0))


def rarity_stars(stars_number: int, size: float, x_destination: float) -> list[Image]:
    return [_star(star_number, stars_number, size, x_destination) for star_number in range(1, 7)]
