# Pygame imports
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
    pass

def title():
    # TODO: Return the title of the game.
    pass

def thumbnail():
    # TODO: Return a (relative path) to the thumbnail image file for your game.
    pass

def hint():
    # TODO: Return the hint string for your game.
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

# TODO: put your Sprite classes here

##### MICROGAME CLASS #########################################################

# TODO: rename this class to your game's name
# (and change "MyMicrogame" instances throughout)
class MyMicrogame(Microgame):
    def __init__(self):
        MyMicrogame.__init__(self)
        # TODO: Initialization code here

    def start(self):
        # TODO: Startup code here

    def stop(self):
        # TODO: Clean-up code here

    def update(self, events):
        # TODO: Update code here

    def render(self, surface):
        # TODO: Rendering code here

    def get_timelimit(self):
        # TODO: Return the time limit of this game (in seconds)
