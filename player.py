import pygame.draw
import SETTINGS as s
import pygame
class Player:
    def __init__(self,side,window):
        self.hitbox = pygame.rect.Rect([450,400],[side,side])
        #side т.к. прямоугольник, в который вписана окружность- это квадрат
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
    def drawing(self):
        pygame.draw.ellipse(self.window,[255,255,255],self.hitbox)

