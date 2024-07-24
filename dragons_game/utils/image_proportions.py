import pygame


def calculate_proportional_width(image_path: str, height: float) -> float:
    image = pygame.image.load(image_path)
    width_to_height_proportion = image.get_width() / image.get_height()
    return width_to_height_proportion * height


def calculate_proportional_height(image_path: str, width: float) -> float:
    image = pygame.image.load(image_path)
    height_to_width_proportion = image.get_height() / image.get_width()
    return height_to_width_proportion * width
