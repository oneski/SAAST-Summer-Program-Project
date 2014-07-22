# Pygame imports
import os.path

import pygame, pygame.mixer
from pygame import Surface
from pygame.image import load
from pygame.locals import *
from pygame.mixer import music
from pygame.rect import Rect
from pygame.sprite import Group, Sprite

# Random imports
from random import randint, choice

# Microgame-specific imports
import locals
from microgame import Microgame

##### LOADER-REQUIRED FUNCTIONS ################################################

def make_game():
    return evade()
    pass

def title():
    return "Eskimo Game"
    pass

def thumbnail():
    return #Your mother
    pass

def hint():
    return "Evade the icicles!"
    pass

################################################################################

def _load_image(name, x, y):
    '''
    Loads an image file, returning the surface and rectangle corresponding to
    that image at the given location.
    '''
    try:
        image = load(name)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, msg:
        print 'Cannot load image: {}'.format(name)
        raise SystemExit, msg
    rect = image.get_rect().move(x, y)
    return image, rect

##### MODEL CLASSES ###########################################################

class e_icicle(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        #self.image = pygame.image.load('games/koala/koala.jpg').convert_alpha()
        self.rect  = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.left = randint(0, 330)
        self.velocity = 0.0

    def update(self):
        y += self.velocity
        self.rect.y = int(y)
        self.velocity += .3

class e_eskimo(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load('games/koala/koala.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        #2 lines above here might not work
        self.rect.bottom = 700
        self.rect.left = 120
        self.velocity = 0

    def update(self):
        self.rect.x += self.velocity 

##### MICROGAME CLASS #########################################################

class evade(Microgame):
    def __init__(self):
        Microgame.__init__(self)
        self.e_icicles = []
        self.e_eskimo = eskimo()
        self.sprites = Group(self.e_eskimo, self.)

    def start(self):
        # TODO: Startup code here

    def stop(self):
        # TODO: Clean-up code here

    def update(self, events):
        self.sprites.update()
        



    def render(self, surface):
        self.sprites.draw()

    def get_timelimit(self):
        return 15
