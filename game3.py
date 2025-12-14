import pygame
from player import Player
from coin  import Coin
pygame.init()

WIDTH = 1000
HEIGHT =  640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
player1 = Player(100, 100, 10)
coin_image = pygame.image.load("coin.png")

coin1 = Coin(coin_image, 0, 50, 5)

clicked = False
FPS = 60
CLOCK = pygame.time.Clock()

circle_color = "red"
running = True
while running:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            circle_color = "blue"
        else:
            circle_color = "red"

    
    screen.fill("lightblue")
    # coin1.draw(screen)
    # coin1.move()
    player1.draw(screen)
    player1.move()
    pygame.display.update()