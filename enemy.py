import random
import pygame
import SETTINGS

class Enemy:
    def __init__(self,window,side):
        self.hitbox = pygame.rect.Rect([random.randint(0,SETTINGS.WIDTH-side),random.randint(0, SETTINGS.HEIGHT-side)],[side, side])
        self.speedx = random.randint(-4, -1)
        self.speedy = random.randint(-1, 1)
        self.window = window

    def drawing(self):
        pygame.draw.ellipse(self.window,[15,255,20],self.hitbox)
    def moving(self):
        self.hitbox.x += self.speedx
        self.hitbox.y += self.speedy