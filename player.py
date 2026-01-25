import pygame
import os
class Player:
    def __init__(self, x, y, speed):
        self.animation_types = ("Idle", "Walk","Run", "Jump", "Dead")
        self.all_images = {}
        for animation in self.animation_types:
            img_list = []
            n_of_frames = len(os.listdir(f"png/{animation}"))
            for i in range(1, n_of_frames + 1):
                img = pygame.image.load(f"png/{animation}/{animation} ({i}).png")
                img = pygame.transform.scale_by(img, 0.3)
                img_list.append(img)
            self.all_images[animation] = img_list
        self.current_animation = "Idle"
        self.image = self.all_images[self.current_animation][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed
        self.rect = self.image.get_rect(topleft=(x,y))
        
        self.frame_index = 0
        self.animated_time = 0
        self.direction = 1
        self.yspeed = 0
        self.is_grounded = True

    def draw(self, screen):
        img = pygame.transform.flip(self.image,  self.direction == -1, False)
        screen.blit(img, self.rect)
        self.animation()
        pygame.draw.lines(self.image, "red",True, self.mask.outline())

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.change_animation("Walk")
            self.direction = -1
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 1000:
            self.change_animation("Walk")
            self.direction = 1
            self.rect.x += self.speed
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.change_animation("Idle")

    def jump(self):
        dy = 0
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE] and self.is_grounded:
            self.yspeed = -12
            self.is_grounded = False
        dy += self.yspeed
        self.yspeed += 1
        if self.rect.bottom + dy >= 640:
            self.yspeed = 0
            dy = 0
            self.is_grounded = True
      
        self.rect.y += dy
    
    def animation(self):
        if pygame.time.get_ticks() - self.animated_time >= 100:
            self.animated_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.all_images):
            self.frame_index = 0
        self.image =  self.all_images[self.current_animation][self.frame_index]

    def change_animation(self, new_animation):
        if new_animation != self.current_animation:
            self.current_animation = new_animation
            self.frame_index = 0
            self.animated_time = pygame.time.get_ticks()