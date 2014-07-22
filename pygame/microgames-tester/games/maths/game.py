# Pygame imports
import pygame, pygame.mixer
from pygame import Surface
from pygame.image import load
from pygame.locals import *
from pygame.mixer import music
from pygame.rect import Rect
from pygame.sprite import Group, Sprite

#os import
import os
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
    return os.path.join("games","maths","thumbnail.png")
    # TODO: Return a(relative path) to the thumbnail image file for your game.
    

def hint():
    return "Solve the problems"
    # TODO: Return the hint string for your game.
    

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

class rotatingNumber(Sprite):
    def __init__(self, x):
        Sprite.__init__(self)
        #randomly choose # btw 1-10
        self.num = 0
        imgpath = os.path.join("games","maths",str(str(self.num)+".png"))
        self.image, self.rect = _load_image(imgpath,300,100)
        self.rect.x, self.rect.y = int(x * locals.WIDTH), int(3.0 * locals.HEIGHT / 4)
        #bounding box
    def update(self):
        pass

class rotatingOperation(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        #randomly choose # btw 1-10
        self.operation = "add"
        imgpath = os.path.join("games","maths",self.operation + ".png"))
        self.image, self.rect = _load_image(imgpath,300,100)
        self.rect.x, self.rect.y = int(2.0 * locals.WIDTH / 3), s3.0 * locals.HEIGHT / 4
        #bounding box
    def update(self):
        pass

##### MICROGAME CLASS #########################################################

# TODO: rename this class to your game's name
# (and change "MyMicrogame" instances throughout)
class MATHS(Microgame):
    def __init__(self):
        Microgame.__init__(self)
        # TODO: Initialization code here

        self.numb1 = rotatingNumber()
        self.numb2 = rotatingNumber()
        self.op = rotatingOperation()
        self.sprites = Group(self.numb1,self.numb2,self.op)

    def start(self):
        # TODO: Startup code here
        pass
    def stop(self):
        # TODO: Clean-up code here
        pass
    def update(self, events):
        # TODO: Update code here
        pass
    def render(self, surface):
        # TODO: Rendering code here
        pass
    def get_timelimit(self):
        # TODO: Return the time limit of this game (in seconds)
        pass
