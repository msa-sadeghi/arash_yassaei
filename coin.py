import pygame
import random
from pygame.sprite import Sprite
class Coin(Sprite):
    def __init__(self, image, x, y, speed, type):
        super().__init__()
        self.image = pygame.transform.scale_by(image, 0.3)
        self.speed = speed
        self.rect = self.image.get_rect(topleft=(x,y))
        self.type = type
        self.counter = 50
        self.sound = pygame.mixer.Sound("sound (3).wav")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        if self.type == "move_x":
            self.counter -= 1
            self.rect.x += self.speed
            if self.counter == 0:
                self.speed *= -1
                self.counter = 50
        elif self.type == "move_y":
            self.counter -= 1
            self.rect.y += self.speed
            if self.counter == 0:
                self.speed *= -1
                self.counter = 50


    def check_collision(self, player, score):
        if self.rect.colliderect(player.rect):
            self.kill()
            self.sound.play()
            score += 1
        return score