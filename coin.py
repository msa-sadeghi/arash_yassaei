import pygame
import random
class Coin:
    def __init__(self, image, x, y, speed):
        self.image = pygame.transform.scale_by(image, 0.3)
        self.speed = speed
        self.rect = self.image.get_rect(topleft=(x,y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        if self.rect.bottom >= 1000:
            random_x = random.randint(50, 950)
            self.rect = self.image.get_rect(topleft=(random_x,0))

        self.rect.y += self.speed