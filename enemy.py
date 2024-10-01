import random
import pygame
import SETTINGS

class Enemy:
    def __init__(self,window,side, path):
        if path == 0:
            #up
            self.hitbox = pygame.rect.Rect([random.randint(100,SETTINGS.WIDTH-2*side),0-side],[side, side])
            self.speedx = random.randint(-1, 1)
            self.speedy = random.randint(1, 3)
            #right
        if path == 1:
            self.hitbox = pygame.rect.Rect([SETTINGS.WIDTH+side, random.randint(100,SETTINGS.HEIGHT-2*side)], [side, side])
            self.speedx = random.randint(-3, -1)
            self.speedy = random.randint(-1, 1)
        self.window = window
            #down
        if path == 2:
            self.hitbox = pygame.rect.Rect([random.randint(100, SETTINGS.WIDTH - 2 * side), SETTINGS.HEIGHT + side], [side, side])
            self.speedx = random.randint(-1, 1)
            self.speedy = random.randint(-3, -1)
            #left
        if path == 3:
            self.hitbox = pygame.rect.Rect([0 - side, random.randint(100, SETTINGS.HEIGHT - 100)],[side, side])
            self.speedx = random.randint(1, 3)
            self.speedy = random.randint(-1, 1)


    def drawing(self):
        pygame.draw.ellipse(self.window,[255,255,255],self.hitbox)
    def moving(self):
        self.hitbox.x += self.speedx
        self.hitbox.y += self.speedy