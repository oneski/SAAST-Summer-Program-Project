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
    return os.path.join("games", "evade", "snowguy.png")
    pass

def hint():
    return "Evade the icicles (mini)!"
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

ICICLE_WIDTH = 50

class e_icicle(Sprite):
    def __init__(self, y):
        Sprite.__init__(self)
        imgpath = os.path.join("games", "evade", "damage.png")
        self.image, self.rect = _load_image(imgpath, 0, 0)
        self.rect.bottom = y
        self.rect.left = randint(0, locals.WIDTH / 3 - ICICLE_WIDTH)
        self.velocity = 1

    def update(self):
        self.rect.y += self.velocity
        self.velocity += 1
        if self.rect.top > locals.HEIGHT:
            asdf = randint(1, 20)
            if asdf == 1:
                self.rect.top = 0
                self.rect.left = randint(0, locals.WIDTH / 3 - ICICLE_WIDTH)
                self.velocity = 0

class eskimo(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = os.path.join("games", "evade", "snowguy.png")
        self.image, self.rect = _load_image(imgpath, 60, 60)
        self.rect.bottom = 700
        self.rect.left = 120
        #self.velocity = 0

    def update(self):
        #self.rect.x += self.velocity
        pass

##### MICROGAME CLASS #########################################################

class evade(Microgame):
    def __init__(self):
        Microgame.__init__(self)
        self.e_icicles = [e_icicle(0), e_icicle(locals.HEIGHT + 70)]
        self.e_eskimo = eskimo()
        self.sprites = Group(self.e_eskimo, *self.e_icicles)

    def start(self):
        music.load(os.path.join("games", "evade", "alt_song.wav"))
        music.play()

    def stop(self):
        music.stop()
        self.lose()

    def update(self, events):
        self.sprites.update()
        keys = pygame.key.get_pressed()
        if keys[K_q]:
            self.win()
        elif (keys[K_RIGHT] or keys[K_d]) and (keys[K_LEFT] or keys[K_a]):
            pass
        elif keys[K_LEFT] or keys[K_a]:
            self.e_eskimo.rect.x = max(self.e_eskimo.rect.x - 15, 0)
        elif keys[K_RIGHT] or keys[K_d]:
            self.e_eskimo.rect.x = min((locals.WIDTH  / 3)-24, self.e_eskimo.rect.x + 15)
        for icicle in self.e_icicles:
            if self.e_eskimo.rect.colliderect(icicle.rect):
                music.stop()
                self.lose()

    def render(self, surface):
        surface.fill((0, 0, 0))
        imgpathh = os.path.join("games", "evade", "tile.png")
        test_image = pygame.image.load(imgpathh) 
        surface.blit(test_image,(0,0))
        self.sprites.draw(surface)

    def get_timelimit(self):
        return 15


