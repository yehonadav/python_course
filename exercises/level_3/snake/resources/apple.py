import pygame
import random


class Apple:
    def __init__(self, size):
        self.position = [random.randrange(10, 780, 10), random.randrange(10, 430, 10)]
        self.image = pygame.Surface((10 * size, 10 * size))
        self.image.fill((255, 0, 0))
