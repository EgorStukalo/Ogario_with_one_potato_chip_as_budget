import pygame.draw
import SETTINGS as s
import pygame
class Player:
    def __init__(self,side,window):
        self.hitbox_pos = [400,450]
        self.hitbox = pygame.rect.Rect(self.hitbox_pos,[side,side])
        #side т.к. прямоугольник, в который вписана окружность- это квадрат +
        self.window = window
    def moving(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.hitbox.y += -3
        if pressed[pygame.K_s]:
            self.hitbox.y += 3
        if pressed[pygame.K_a]:
            self.hitbox.x += -3
        if pressed[pygame.K_d]:
            self.hitbox.x += 3
        self.hitbox.center = pygame.mouse.get_pos()
    def drawing(self):
        pygame.draw.ellipse(self.window,[0,255,0],self.hitbox)