import pygame
pygame.init()


WIDTH = 480
HEIGHT = 480
rows, cols = 8, 8
tile = 60

light = (240, 217, 181)
dark = (181, 136, 99)

screen = pygame.display.set_mode((WIDTH, HEIGHT))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for r in range(rows):
        for c in range(cols):
            if (r + c) % 2 == 0:
                color = light
            else:
                color =  dark
            pygame.draw.rect(screen, color, (c*tile, r*tile, tile, tile))
    pygame.display.update()