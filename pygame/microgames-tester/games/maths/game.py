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
    return MATHS()
    pass

def title():
    return "Maths"
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
        self.num = 1
        imgpath = os.path.join("games","maths",str(str(self.num)+".png"))
        self.image, self.rect = _load_image(imgpath,300,100)
        self.rect.x, self.rect.y = int(x * locals.WIDTH), int(3.0 * locals.HEIGHT / 4)
        #bounding box
    def update(self):
        imgpath = os.path.join("games","maths",str(str(self.num)+".png"))
        self.image, self.rect = _load_image(imgpath,300,100)

class rotatingOperation(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        #randomly choose # btw 1-10
        self.operation = "1"
        imgpath = os.path.join("games","maths",self.operation + ".png")
        self.image, self.rect = _load_image(imgpath,300,100)
        #self.rect.x, self.rect.y = int(2.0 * locals.WIDTH / 3), s3.0 * locals.HEIGHT / 4
        #bounding box
    def update(self):
        self.image = os.path.join("games","maths",str(str(self.num)+".png")\)

##### MICROGAME CLASS #########################################################

# TODO: rename this class to your game's name
# (and change "MyMicrogame" instances throughout)
class MATHS(Microgame):
    def __init__(self):
        Microgame.__init__(self)
        self.numb1 = rotatingNumber(0.5)
        self.numb2 = rotatingNumber(5.0 / 6)
        self.op = rotatingOperation()
        self.sprites = Group(self.numb1,self.numb2,self.op)
        self.answer = 0
        self.time = 0

    def start(self):
        self.answer = randint(3, 9)
        self.numb2.num = randint(0, self.answer)
        self.numb1.num = self.answer - self.numb2.num
        print self.answer
        pass

    def stop(self):
        # TODO: Clean-up code here
        pass

    def update(self, events):
        self.time += 1
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key in (K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9):
                dictt = {K_0 : 0, K_1 : 1, K_2 : 2, K_3 : 3, K_4 : 4, K_5 : 5, K_6 : 6, K_7 : 7, K_8 : 8, K_9 : 9}
                if dictt[event.key] == self.answer:
                    if self.op.operation == "add":
                        print "You win"
                        self.op.operation = "sub"
                        self.numb1 = randint(3, 9)
                        self.numb2 = randint(0, self.numb1)
                        self.answer = self.numb2 - self.numb1
                    elif self.op.operation == "sub":
                        self.op.operation = "mod"
                        self.numb2 = randint(1, 4)
                        self.numb1 = randint(self.numb2 + 1, 9)
                        self.answer = self.numb1 % self.numb2
                    elif self.op.operation == "mod":
                        del self.numb1, self.numb2, self.op
                        self.time = -10
                else:
                    self.lose()
        if self.time >= 449:
            self.lose()

    def render(self, surface):
        surface.fill((0, 0, 0))
        self.sprites.draw(surface)

    def get_timelimit(self):
        return 15
