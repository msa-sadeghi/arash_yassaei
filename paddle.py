import pygame
import random
pygame.init()
WIDTH = 1000
HEIGHT = 640
rect = pygame.Rect(0, 100, 25, 150)
rect1 = pygame.Rect(975, 100, 25, 150)
circle = pygame.Rect(470, 300, 50, 50)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()
# my_font = pygame.font.Font("GAMERIA.ttf", 24)
my_font = pygame.font.SysFont("arial", 24)
score = 0
score_text = my_font.render(f"score : {score}", True, "red")

ball_x = random.choice((-1,1))
ball_y = random.choice((-1,1))
ball_speed = 3
running = True
while running == True:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and rect1.top >= 0:
        rect1.y -= 10
    if keys[pygame.K_DOWN] and rect1.bottom <= HEIGHT:
        rect1.y += 10
        keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and rect.top >= 0:
        rect.y -= 10
    if keys[pygame.K_s] and rect.bottom <= HEIGHT:
        rect.y += 10

    circle.x += ball_x * ball_speed    
    circle.y += ball_y * ball_speed  
    if circle.bottom >= 640 or circle.top <= 0:
        ball_y *= -1  
    if circle.right >= 1000 or circle.left <= 0:
        ball_x *= -1  
    screen.fill((0, 0, 0))
    if rect.colliderect(circle):
        circle.x = random.randint(0, WIDTH - 50)
        circle.y = random.randint(0, HEIGHT - 50)
        score += 1
    if rect1.colliderect(circle):
        circle.x = random.randint(0, WIDTH - 50)
        circle.y = random.randint(0, HEIGHT - 50)
        score -= 1
    score_text = my_font.render(f"score : {score}", True, "red")
    screen.blit(score_text, (10,  10))
    pygame.draw.rect(screen, "white", rect)
    pygame.draw.rect(screen, "white", rect1)
    pygame.draw.ellipse(screen, "darkgreen", circle)
    pygame.draw.line(screen, "white", (500, 0), (500, 639), 1)
    pygame.display.update()