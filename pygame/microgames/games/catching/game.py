# Created by Nathan Yang of Computer Science at SAAST 2014

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
    # TODO: Return a new instance of your Microgame class.
    return CollectCoinMicrogame()

def title():
    # TODO: Return the title of the game.
    return "Coin Collection"

def thumbnail():
    # TODO: Return a (relative path) to the thumbnail image file for your game.
    return os.path.join('games', 'catching', '8bitironman_edit.png')

def hint():
    # TODO: Return the hint string for your game.
    return "Collect all the coins!"

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

COIN_WIDTH = 30

class coin(Sprite):
    def __init__(self, y):
        Sprite.__init__(self)
        imgpath = os.path.join("games", "catching", "8bitcoin_trans.png")
        self.image, self.rect = _load_image(imgpath, 0, 0)
        self.rect.bottom = y
        self.rect.left = randint(0, locals.WIDTH - COIN_WIDTH)
        self.velocity = 1

    def update(self):
        self.rect.y += self.velocity
        self.velocity += 1
        # if self.rect.top > locals.HEIGHT:
            # rand_chance = randint(1, 20)
            # if rand_chance == 1:
                # self.rect.top = 0
                # self.rect.left = randint(0, locals.WIDTH - COIN_WIDTH)
                # self.velocity = 0


class ironman(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = os.path.join("games", "catching", "8bitironman_trans.png")
        self.image, self.rect = _load_image(imgpath, 60, 60)
        self.rect.bottom = 700
        self.rect.left = 120

    def update(self):
        pass


##### MICROGAME CLASS #########################################################

# TODO: rename this class to your game's name
# "Hi guyth" -Alan Yao
# (and change "MyMicrogame" instances throughout)
class CollectCoinMicrogame(Microgame):
    def __init__(self):
        # TODO: Initialization code here
        Microgame.__init__(self)
        self.coins = coin(0) #coin(locals.HEIGHT + 70)]
        self.ironman = ironman()
        self.sprites = Group(self.ironman, self.coins)
        self.time = pygame.time.get_ticks()

    def start(self):
        # TODO: Startup code here
        music.load(os.path.join("games", "catching", "super_mario_levels.wav"))
        music.play()

    def stop(self):
        # TODO: Clean-up code here
        music.stop()
        self.lose()

    def update(self, events):
        # TODO: Update code here
        self.sprites.update()
        ctrls = pygame.key.get_pressed()
        if ctrls[K_q]:
            self.win()
        elif ctrls[K_a] or ctrls[K_LEFT]:
            self.ironman.rect.x = max(self.ironman.rect.x - 30, 0)
        elif ctrls[K_d] or ctrls[K_RIGHT]:
            self.ironman.rect.x = min(locals.WIDTH - 68, self.ironman.rect.x + 30)
        if self.coins.rect.colliderect(self.ironman):
            # self.time = pygame.time.get_ticks()
            # self.sprites.remove(self.coins)
            # print str(self.time) + " " + str(pygame.time.get_ticks())
            # if self.time + 3000 <= pygame.time.get_ticks():
            # self.coins = coin(0)
                # self.sprites.add(self.coins)
            self.coins.rect.y = 0
            self.coins.velocity = 0
            self.coins.rect.left = randint(0, locals.WIDTH - COIN_WIDTH)
                # self.sprites.update()
        elif self.coins.rect.top > locals.HEIGHT:
            self.lose()

    def render(self, surface):
        # TODO: Rendering code here
        surface.fill(Color(0, 0, 0))
        imgpath = os.path.join("games", "catching", "8bitsky.jpg")
        test_image = pygame.image.load(imgpath)
        surface.blit(test_image,(0,0))
        self.sprites.draw(surface)

    def get_timelimit(self ):
        # TODO: Return the time limit of this game (in seconds)
        return 15