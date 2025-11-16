import pygame
import random
pygame.init()
WIDTH = 800
HEIGHT = 640
r = 0
g = 0
b = 0
color = (r, g, b)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player_image_right = pygame.image.load("player.png")
player_image_right = pygame.transform.scale_by(player_image_right, 0.5)
player_rect = player_image_right.get_rect(center=(WIDTH//2, HEIGHT//2))

player_image_left = pygame.transform.flip(player_image_right, True, False)
player_image = player_image_right
FPS = 60
CLOCK = pygame.time.Clock()
running = True
while running == True:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_rect.left >= 0:
        player_image = player_image_left
        player_rect.x -= 5
    if keys[pygame.K_d] and player_rect.right <= WIDTH:
        player_image = player_image_right
        player_rect.x += 5
    if keys[pygame.K_w] and player_rect.top >= 0:
        player_rect.y -= 5
    if keys[pygame.K_s] and player_rect.bottom <= HEIGHT:
        player_rect.y += 5
    color = (r, g, b)
    screen.fill(color)
    screen.blit(player_image, player_rect)
    pygame.display.update()