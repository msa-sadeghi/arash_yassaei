import pygame
class Player:
    def __init__(self, image, x, y, speed):
        self.image = pygame.transform.scale_by(image, 0.3)
        self.speed = speed
        self.rect = self.image.get_rect(topleft=(x,y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 1000:
            self.rect.x += self.speed