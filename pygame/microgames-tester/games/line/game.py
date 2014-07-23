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
    return "Ember Defense"
    pass

def thumbnail():
    return os.path.join("games", "line", "emberHD.png")
    pass

def hint():
    return "Don't let the ember get \n hit!"
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
        imgRand = randint(0,1)
        if(imgRand):
            imgpath = os.path.join("games", "line", "retro.png")
        else:
            imgpath = os.path.join("games","line","syspref.png")
        self.image, self.rect = _load_image(imgpath, 0, 0)
        #self.rect.bottom = y
        #self.rect.left = randint(0, locals.WIDTH / 3 - ICICLE_WIDTH)
        self.rect.left = 0
        posRand = randint(0,2)
        if posRand == 0:
            self.rect.centery = locals.HEIGHT/8
        elif posRand == 1:
            self.rect.centery = 2*locals.HEIGHT/8
        else:
            self.rect.centery = 3*locals.HEIGHT/8

        self.velocity = 1

    def update(self):
        #self.rect.y += self.velocity
        self.rect.x += self.velocity
        self.velocity += 1
        if self.rect.right > locals.WIDTH:
            asdf = randint(1, 20)
            if asdf == 1:
                #self.rect.top = 0
                #self.rect.left = randint(0, locals.WIDTH / 3 - ICICLE_WIDTH)
                imgRand = randint(0,1)
                if(imgRand):
                    imgpath = os.path.join("games", "line", "retro.png")
                else:
                    imgpath = os.path.join("games","line","syspref.png")
                self.image, self.rect = _load_image(imgpath, 0, 0)

                self.rect.left = 0
                posRand = randint(0,2)
                if posRand == 0:
                    self.rect.centery = locals.HEIGHT/8
                elif posRand == 1:
                    self.rect.centery = 2*locals.HEIGHT/8
                else:
                    self.rect.centery = 3*locals.HEIGHT/8
                self.velocity = 0

class eskimo(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = os.path.join("games", "line", "fireguy.png")
        self.image, self.rect = _load_image(imgpath, 60, 60)
        self.rect.centery = 2*(locals.HEIGHT/8)
        self.rect.left = 2*locals.WIDTH/3
        #self.velocity = 0

    def update(self):
        #self.rect.x += self.velocity
        pass

##### MICROGAME CLASS #########################################################

class evade(Microgame):
    def __init__(self):
        Microgame.__init__(self)
        self.e_icicles = [e_icicle(), e_icicle()]
        self.e_eskimo = eskimo()
        self.sprites = Group(self.e_eskimo, *self.e_icicles)

    def start(self):
        music.load(os.path.join("games", "line", "alt_song.wav"))
        music.play()

    def stop(self):
        music.stop()
        self.lose()

    def update(self, events):
        self.sprites.update()
        for event in events:
            if event.type == KEYUP and (event.key == K_UP or event.key == K_w) and (event.key == K_DOWN or event.key == K_s):
                pass
            elif event.type == KEYUP and event.key == K_q:
                self.win()
            elif event.type == KEYUP and (event.key == K_UP or event.key == K_w):
                if(self.e_eskimo.rect.centery == 2*locals.HEIGHT/8):
                    self.e_eskimo.rect.centery = locals.HEIGHT/8
                elif(self.e_eskimo.rect.centery == locals.HEIGHT/8):
                    self.e_eskimo.rect.centery = locals.HEIGHT/8
                elif(self.e_eskimo.rect.centery == 3*locals.HEIGHT/8):
                    self.e_eskimo.rect.centery = 2*locals.HEIGHT/8
            elif event.type == KEYUP and (event.key == K_DOWN or event.key == K_s):
                if(self.e_eskimo.rect.centery == 2*locals.HEIGHT/8):
                    self.e_eskimo.rect.centery = 3*locals.HEIGHT/8
                elif(self.e_eskimo.rect.centery == locals.HEIGHT/8):
                    self.e_eskimo.rect.centery = 2*locals.HEIGHT/8
                elif(self.e_eskimo.rect.centery == 3*locals.HEIGHT/8):
                    self.e_eskimo.rect.centery = 3*locals.HEIGHT/8
        """keys = pygame.key.get_pressed()
        if keys[K_q]:
            self.win()
        elif (keys[K_UP] or keys[K_w]) and (keys[K_DOWN] or keys[K_s]):
            pass
        elif keys[K_UP] or keys[K_w]:
            if(self.e_eskimo.rect.centery == 2*locals.HEIGHT/8):
                self.e_eskimo.rect.centery = locals.HEIGHT/8
            elif(self.e_eskimo.rect.centery == locals.HEIGHT/8):
                self.e_eskimo.rect.centery = locals.HEIGHT/8
            elif(self.e_eskimo.rect.centery == 3*locals.HEIGHT/8):
                self.e_eskimo.rect.centery = 2*locals.HEIGHT/8
        elif keys[K_DOWN] or keys[K_s]:
            if(self.e_eskimo.rect.centery == 2*locals.HEIGHT/8):
                self.e_eskimo.rect.centery = 3*locals.HEIGHT/8
            elif(self.e_eskimo.rect.centery == locals.HEIGHT/8):
                self.e_eskimo.rect.centery = 2*locals.HEIGHT/8
            elif(self.e_eskimo.rect.centery == 3*locals.HEIGHT/8):
                self.e_eskimo.rect.centery = 3*locals.HEIGHT/8
        """
        for icicle in self.e_icicles:
            if self.e_eskimo.rect.colliderect(icicle.rect):
                music.stop()
                self.lose()

    def render(self, surface):
        surface.fill((0, 0, 0))
        imgpathh = os.path.join("games", "line", "tile.png")
        test_image = pygame.image.load(imgpathh) 
        surface.blit(test_image,(0,0))
        imgpathhh = os.path.join("games", "line", "linesBG.png")
        test_imagee = pygame.image.load(imgpathhh)
        surface.blit(test_imagee,(377,0))
        self.sprites.draw(surface)

    def get_timelimit(self):
        return 15


