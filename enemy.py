import random
import pygame
import SETTINGS

class Enemy:
    def __init__(self,window,side, path):
        if path == 0:
            self.hitbox = pygame.rect.Rect([random.randint(100,SETTINGS.WIDTH-2*side),0-side],[side, side])
            self.speedx = random.randint(-1, 1)
            self.speedy = random.randint(1, 3)
        else:
            self.hitbox = pygame.rect.Rect([SETTINGS.WIDTH+side, random.randint(100,SETTINGS.HEIGHT-2*side)], [side, side])
            self.speedx = random.randint(-3, -1)
            self.speedy = random.randint(-1, 1)
        self.window = window


    def drawing(self):
        pygame.draw.ellipse(self.window,[15,255,20],self.hitbox)
    def moving(self):
        self.hitbox.x += self.speedx
        self.hitbox.y += self.speedy