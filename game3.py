import pygame
from player import Player
from coin  import Coin
from ground import Ground
pygame.init()
WIDTH = 1000
HEIGHT =  640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player1 = Player(100, 100, 10)
coin_image = pygame.image.load("coin.png")
coin_group = pygame.sprite.Group()
coin1 = Coin(coin_image, 450, 480, 5, "move_x")
coin2 = Coin(coin_image, 750, 280, 5, "move_y")
coin_group.add(coin1,coin2)
clicked = False
FPS = 60
CLOCK = pygame.time.Clock()
score = 0
myfont = pygame.font.Font("f.otf", 24)
score_text = myfont.render(f"Score: {score}", True, "darkblue")
ground = Ground(WIDTH, HEIGHT)
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
    score_text = myfont.render(f"Score: {score}", True, "darkblue")
    screen.fill("lightblue")
    screen.blit(score_text, (20, 20))
    coin_group.draw(screen)
    coin1.move()
    
    coin2.move()
    player1.draw(screen)
    player1.move()
    player1.jump()
    for coin in coin_group.sprites():
        score = coin.check_collision(player1, score)

    ground.draw(screen)
    pygame.display.update()