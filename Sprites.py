# Sprite Classes for game.
import pygame as pg
from settings import *
vec = pg.math.Vector2

class SpriteSheet:

    # Utility class
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        # Grab an Image out of a larger spritesheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.center = (display_width / 2, display_height / 2)
        self.pos = vec(display_width / 2, display_height / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # Jump only if standing on Platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -player_jump

    def update(self):
        self.acc = vec(0, player_grav)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -player_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = player_ACC



        # Apply Friction
        self.acc.x += self.vel.x * player_Friction
        # Equation of Motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Makes sure Player in Screen
        if self.pos.x > display_width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = display_width


        self.rect.midbottom = self.pos


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):

        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

