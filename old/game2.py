import pygame
import random
pygame.init()
WIDTH = 1000
HEIGHT = 640
rect  = pygame.Rect(100, 100, 50, 50)
circle  = pygame.Rect(200, 300, 50, 50)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS  = 60
CLOCK = pygame.time.Clock()
my_font = pygame.font.Font("f.otf", 24)
score = 0
score_text =  my_font.render(f"score : {score}", True, "red")
running =  True
while running:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect.x -= 5
    if keys[pygame.K_RIGHT]:
        rect.x += 5
    if keys[pygame.K_UP]:
        rect.y -= 5
    if keys[pygame.K_DOWN]:
        rect.y += 5
    screen.fill((0,0,0))
    if rect.colliderect(circle):
        circle.x = random.randint(0, WIDTH - 50)
        circle.y = random.randint(0, HEIGHT - 50)
        score  += 1
    score_text =  my_font.render(f"score : {score}", True, "red")
    screen.blit(score_text, (10,  10))
    pygame.draw.rect(screen, "white",  rect)
    pygame.draw.ellipse(screen, "darkgreen",  circle)
    pygame.display.update()