import pygame as pg
import pygame.freetype
import SETTINGS as s
import enemy as e
import player as p
import menu
import random
pg.init()

class Game_is_game:
    def __init__(self):
        self.window = pg.display.set_mode([s.WIDTH,s.HEIGHT])
        self.true_false = True
        self.fps = pygame.time.Clock()
        self.enemy_creation = pygame.USEREVENT
        pygame.time.set_timer(self.enemy_creation, 300)
        self.enemy_list = []
        self.enemy_number = 0
        self.score_text = pg.freetype.Font("BodoniFLF-Roman.ttf", 30)
        self.score = 0
        self.player = p.Player(10,self.window)
        self.menu = menu.Menu(self)
        self.mode = 1

    def event(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.true_false = False
            if event.type == self.enemy_creation:
                random_path = random.randint(0, 3)
                self.enemy_side = random.randint(self.player.hitbox.width-4,self.player.hitbox.width+15)
                self.enemy = e.Enemy(self.window,self.enemy_side,random_path)
                self.enemy_number += 1
                self.enemy_list.append(self.enemy)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.mode == 3:
                        self.mode = 2




    def drawing(self):
        self.window.fill([0,0,0])
        self.player.drawing()
        for enemy in self.enemy_list:
            enemy.drawing()
        if self.mode == 3:
            self.score_text.render_to(self.window, [400, 350], "GG (get good)",(255,255,255))

        pygame.display.update()

    def update(self):
        for enemy in self.enemy_list:
            if self.player.hitbox.colliderect(enemy.hitbox) == True:
                if self.player.hitbox.w >= enemy.hitbox.w:
                    self.player.hitbox.w += 3
                    self.player.hitbox.h += 3
                    self.enemy_list.remove(enemy)
                else:
                    self.mode = 3
        self.player.moving()
        for enemy in self.enemy_list:
            enemy.moving()

    def start(self):
        while self.true_false:
            if self.mode == 1:
                self.event()
                self.drawing()
                self.update()
            elif self.mode == 2:
                self.menu.event()
                self.menu.drawing()
                self.menu.update()
            elif self.mode == 3:
                self.event()
                self.drawing()
            self.fps.tick(100)


game = Game_is_game()
game.start()
