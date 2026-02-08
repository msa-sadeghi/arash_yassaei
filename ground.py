import pygame

class Ground:
    def __init__(self, width, height):
        self.rect = pygame.Rect(0, height - 40, width, 40)

    def draw(self, screen):
        pygame.draw.rect(screen,"green", self.rect)
