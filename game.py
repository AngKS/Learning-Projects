

import pygame as pg
import random
from settings import *
from Sprites import *
import pickle

pg.init()

class Game:
    def __init__(self):
        #initialize game Window
        self.running = True
        self.gameDisplay = pg.display.set_mode((display_width, display_height))
        pg.display.set_caption(Title)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(Font_name)
        self.highscore = 0




        # Reset
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in plat_list:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.run()

    def run(self):
        #Gameloop
        running = True
        while running:
            self.playing = True
            while self.playing:
                self.clock.tick(FPS)
                self.events()
                self.update()
                self.draw()

    def update(self):
        # Game Loop update
        self.all_sprites.update()
        # Check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        # Check if die
        if self.player.rect.bottom > display_height:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
                self.playing = False



        # Check if Player reaches top 1/4 of the screen
        if self.player.rect.top <= display_height / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= display_height:
                    plat.kill()
                    self.score += 5

        # Spawn new platforms
        while len(self.platforms) < 5:
            width = random.randint(50, 100)
            p = Platform(random.randrange(0, display_width - width),
                         random.randrange(-75, -30),
                         width,
                         20)
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        self.gameDisplay.fill(blue)
        self.all_sprites.draw(self.gameDisplay)
        self.drawTXT(str(self.score), 22, orange, display_width / 2, 50)

        pg.display.update()

    def drawTXT(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.gameDisplay.blit(text_surface, text_rect)

    def show_start_screen(self):

        pass

    def show_go_screen(self):
        pass


g = Game()
g.show_start_screen()

while g.running:
    g.new()

    g.show_go_screen()


pg.quit()