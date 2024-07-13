import pygame


def calculate_proportional_dimension(image: str, input_dimension: int) -> int:
    image_surf = pygame.image.load(image)
    width_to_height_proportion = image_surf.get_width() / image_surf.get_height()
    return int(width_to_height_proportion * input_dimension)
