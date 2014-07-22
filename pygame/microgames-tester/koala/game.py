import pygame, sys, os
from os.path import join
from pygame.locals import *
from pygame.color import Color
from pygame.sprite import Sprite, Group
from pygame.surface import Surface
from pygame.rect import Rect

import locals
from microgame import Microgame

##### LOADER-REQUIRED FUNCTIONS ################################################

def make_game():
    return KoalaGame()

def title():
    return 'Koala'

def thumbnail():
    return 'games/koala/koala.jpg'

def hint():
    return 'Eat stuff!'

################################################################################

class Koala(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load('games/koala/koala.jpg').convert_alpha()
        self.rect  = self.image.get_rect()
        self.velocity = (0, 0)

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

class KoalaGame(Microgame):
    def __init__(self):
        Microgame.__init__(self)
        self.koala = Koala()
        self.entities = Group([self.koala])

    def start(self):
        pass

    def stop(self):
        pass

    def update(self, events):
        self.entities.update()
        for event in events:
            if event.type == KEYUP and event.key == K_q:
                self.lose()
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                self.koala.velocity = (5, 0)
            elif event.type == KEYUP and event.key == K_RIGHT:
                self.koala.velocity = (0, 0)
            elif event.type == KEYDOWN and event.key == K_UP:
                self.koala.velocity = (0, -5)
            elif event.type == KEYUP and event.key == K_UP:
                self.koala.velocity = (0, 0)
            elif event.type == KEYDOWN and event.key == K_DOWN:
                self.koala.velocity = (0, 5)
            elif event.type == KEYUP and event.key == K_DOWN:
                self.koala.velocity = (0, 0)
            elif event.type == KEYDOWN and event.key == K_LEFT:
                self.koala.velocity = (-5, 0)
            elif event.type == KEYUP and event.key == K_LEFT:
                self.koala.velocity = (0, 0)

    def render(self, surface):
        surface.fill(Color(0, 0, 0))
        self.entities.draw(surface)

    def get_timelimit():
        return 5
