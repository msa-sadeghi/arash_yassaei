import pygame
pygame.init()


WIDTH = 1000
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

circle_rect = pygame.Rect(10, 10, 50, 50)

NORMAL_SPEED = 5
BOOST_SPEED = 10
speed = NORMAL_SPEED
FPS = 60
CLOCK = pygame.time.Clock()
running = True
while running:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and keys[pygame.K_LEFT]:
        speed = BOOST_SPEED
        circle_rect.x -= speed
    elif (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and keys[pygame.K_RIGHT]:
        speed = BOOST_SPEED
        circle_rect.x += speed
    elif keys[pygame.K_LEFT]:
        speed = NORMAL_SPEED
        circle_rect.x -= speed
    elif keys[pygame.K_RIGHT]:
        speed = NORMAL_SPEED
        circle_rect.x += speed
    

    screen.fill("black")
    pygame.draw.ellipse(screen, "lightgreen", circle_rect)
    pygame.display.update()