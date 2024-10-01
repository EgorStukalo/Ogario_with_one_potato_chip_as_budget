import pygame
import pygame as pg
import SETTINGS as s
class Menu():
    def __init__(self,game):
        self.game = game
        self.Play_color = [0,255,0]
        self.Settings_color = [255, 255, 255]
        self.Quit_color = [255,255,255]

    def event(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.game.true_false = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if self.Play_color == [0,255,0]:
                        self.game.mode = 1
                        self.game.enemy_list = []
                        self.game.player.hitbox.width = 10
                        self.game.player.hitbox.height = 10
                    elif self.Settings_color == [0,255,0]:
                        print("sorry, this feature is still in development :(")
                    else:
                        self.game.true_false = False`
                if event.key == pg.K_DOWN:
                    if self.Play_color == [0,255,0]:
                        self.Play_color = [255, 255, 255]
                        self.Settings_color = [0, 255, 0]
                    elif self.Settings_color == [0,255,0]:
                        self.Settings_color = [255, 255, 255]
                        self.Quit_color = [0, 255, 0]
                if event.key == pg.K_UP:
                    if self.Quit_color == [0,255,0]:
                        self.Quit_color = [255, 255, 255]
                        self.Settings_color = [0, 255, 0]
                    elif self.Settings_color == [0,255,0]:
                        self.Settings_color = [255, 255, 255]
                        self.Play_color = [0, 255, 0]

    def drawing(self):
        self.game.window.fill([0,0,0])
        self.game.score_text.render_to(self.game.window, [20,0],"Agar.io",)
        self.game.score_text.render_to(self.game.window, [20, 150], "Play", self.Play_color)
        self.game.score_text.render_to(self.game.window, [20, 250], "Settings", self.Settings_color)
        self.game.score_text.render_to(self.game.window, [20, 350], "Quit", self.Quit_color)
        pg.display.update()
    def update(self):
        pass
