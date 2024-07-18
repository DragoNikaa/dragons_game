import pygame


def calculate_proportional_width(image: str, input_height: int) -> int:
    image_surf = pygame.image.load(image)
    width_to_height_proportion = image_surf.get_width() / image_surf.get_height()
    return int(width_to_height_proportion * input_height)


def calculate_proportional_height(image: str, input_width: int) -> int:
    image_surf = pygame.image.load(image)
    height_to_width_proportion = image_surf.get_height() / image_surf.get_width()
    return int(height_to_width_proportion * input_width)
