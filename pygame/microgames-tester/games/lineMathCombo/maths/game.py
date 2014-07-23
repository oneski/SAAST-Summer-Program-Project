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
    def __init__(self, x, num):
        Sprite.__init__(self)
        self.num = num
        imgpath = os.path.join("games","maths",str(str(num)+".png"))
        self.image, self.rect = _load_image(imgpath,300,100)
        self.rect.centerx, self.rect.centery = int(x * locals.WIDTH), int(3.0 * locals.HEIGHT / 4)
    def update(self):
        pass

class rotatingOperation(Sprite):
    def __init__(self, x, operation):
        Sprite.__init__(self)
        self.operation = operation
        imgpath = os.path.join("games","maths",self.operation + ".png")
        self.image, self.rect = _load_image(imgpath,300,100)
        self.rect.centerx, self.rect.centery = x, int(3.0 * locals.HEIGHT / 4)
    def update(self):
        pass

##### MICROGAME CLASS #########################################################

# TODO: rename this class to your game's name
# (and change "MyMicrogame" instances throughout)
class MATHS(Microgame):
    def __init__(self):
        Microgame.__init__(self)
        self.addans = randint(3, 9)
        self.add1 = rotatingNumber(0.5, randint(0, self.addans))
        self.add2 = rotatingNumber(5.0 / 6.0, self.addans - self.add1.num)
        self.sub1 = rotatingNumber(0.5, randint(3, 9))
        self.sub2 = rotatingNumber(5.0 / 6.0, randint(0, self.sub1.num))
        self.subans = self.sub1.num - self.sub2.num
        self.mod2 = rotatingNumber(5.0 / 6.0, randint(2, 4))
        self.mod1 = rotatingNumber(0.5, randint(self.mod2.num + 1, 9))
        self.modans = self.mod1.num % self.mod2.num
        self.add = rotatingOperation(int(2.0 * locals.WIDTH / 3), "add")
        self.sub = rotatingOperation(int(2.0 * locals.WIDTH / 3), "sub")
        self.mod = rotatingOperation(int(2.0 * locals.WIDTH / 3), "mod")
        self.stage = 0
        self.sprites1 = Group(self.add1, self.add2, self.add)
        self.sprites2 = Group(self.sub1, self.sub2, self.sub)
        self.sprites3 = Group(self.mod1, self.mod2, self.mod)

    def start(self):
        self.answer = self.addans
        print self.answer, self.stage
        pass

    def stop(self):
        pass

    def update(self, events):
        for event in events:
            if event.type == KEYDOWN and event.key == K_q:
                self.lose()
            if event.type == KEYDOWN and event.key in (K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9):
                dictt = {K_0 : 0, K_1 : 1, K_2 : 2, K_3 : 3, K_4 : 4, K_5 : 5, K_6 : 6, K_7 : 7, K_8 : 8, K_9 : 9}
                if dictt[event.key] == self.answer:
                    if self.stage == 0:
                        self.answer = self.subans
                        self.stage = 1
                        print self.answer, self.stage
                    elif self.stage == 1:
                        self.answer = self.modans
                        self.stage = 2
                        print self.answer, self.stage
                    elif self.stage == 2:
                        self.stage = 3
                        self.answer = -1
                        time = -10
                else:
                    self.lose()


    def render(self, surface):
        surface.fill((0, 0, 0))
        imgpathhhh = os.path.join("games", "maths", "mathBG.png")
        test_imageee = pygame.image.load(imgpathhhh)
        surface.blit(test_imageee,(377,768 / 2))
        if self.stage == 0:
            self.sprites1.draw(surface)
        elif self.stage == 1:
            self.sprites2.draw(surface)
        elif self.stage == 2:
            self.sprites3.draw(surface)

    def get_timelimit(self):
        return 15