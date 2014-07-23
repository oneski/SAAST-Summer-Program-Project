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
    return "Ember Defense + Math"
    pass

def thumbnail():
    return os.path.join("games", "lineMathCombo", "logoHD.png")
    pass

def hint():
    return "Manage 3 games at once! (Don't DiE)"
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




#evade

ICICLE_WIDTH = 50

class ee_icicle(Sprite):
    def __init__(self, y):
        Sprite.__init__(self)
        imgpath = os.path.join("games", "lineMathCombo", "damage.png")
        self.image, self.rect = _load_image(imgpath, 0, 0)
        self.rect.bottom = y
        self.rect.left = randint(0, locals.WIDTH / 3 - ICICLE_WIDTH)
        self.velocity = 1

    def update(self):
        self.rect.y += self.velocity
        self.velocity += 2
        if self.rect.top > locals.HEIGHT:
            asdf = randint(1, 20)
            if asdf == 1:
                self.rect.top = 0
                self.rect.left = randint(0, locals.WIDTH / 3 - ICICLE_WIDTH)
                self.velocity = 0

class eeskimo(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = os.path.join("games", "lineMathCombo", "snowguy.png")
        self.image, self.rect = _load_image(imgpath, 60, 60)
        self.rect.bottom = 700
        self.rect.left = 120
        #self.velocity = 0

    def update(self):
        #self.rect.x += self.velocity
        pass








#line




class e_icicle(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgRand = randint(0,1)
        if(imgRand):
            imgpath = os.path.join("games", "lineMathCombo", "retro.png")
        else:
            imgpath = os.path.join("games","lineMathCombo","syspref.png")
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
                    imgpath = os.path.join("games", "lineMathCombo", "retro.png")
                else:
                    imgpath = os.path.join("games","lineMathCombo","syspref.png")
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
        imgpath = os.path.join("games", "lineMathCombo", "fireguy.png")
        self.image, self.rect = _load_image(imgpath, 60, 60)
        self.rect.centery = 2*(locals.HEIGHT/8)
        self.rect.left = 2*locals.WIDTH/3
        #self.velocity = 0

    def update(self):
        #self.rect.x += self.velocity
        pass

#maths
class rotatingNumber(Sprite):
    def __init__(self, x, num):
        Sprite.__init__(self)
        self.num = num
        imgpath = os.path.join("games","lineMathCombo",str(str(num)+".png"))
        self.image, self.rect = _load_image(imgpath,300,100)
        self.rect.centerx, self.rect.centery = int(x * locals.WIDTH), int(3.0 * locals.HEIGHT / 4)
    def update(self):
        pass

class rotatingOperation(Sprite):
    def __init__(self, x, operation):
        Sprite.__init__(self)
        self.operation = operation
        imgpath = os.path.join("games","lineMathCombo",self.operation + ".png")
        self.image, self.rect = _load_image(imgpath,300,100)
        self.rect.centerx, self.rect.centery = x, int(3.0 * locals.HEIGHT / 4)
    def update(self):
        pass

##### MICROGAME CLASS #########################################################

class evade(Microgame):
    def __init__(self):
        Microgame.__init__(self)
        #line
        self.e_icicles = [e_icicle(), e_icicle()]
        self.e_eskimo = eskimo()
        self.sprites = Group(self.e_eskimo, *self.e_icicles)

        #maths
        self.addans = randint(3, 9)
        self.add1 = rotatingNumber(0.5, randint(0, self.addans))
        self.add2 = rotatingNumber(5.0 / 6.0, self.addans - self.add1.num)
        self.sub1 = rotatingNumber(0.5, randint(3, 9))
        self.sub2 = rotatingNumber(5.0 / 6.0, randint(0, self.sub1.num))
        self.subans = self.sub1.num - self.sub2.num
        self.mod2 = rotatingNumber(5.0 / 6.0, randint(2, 4))
        self.mod1 = rotatingNumber(0.5, randint(self.mod2.num + 1, 9))
        self.modans = self.mod1.num % self.mod2.num
        self.mod_2 = rotatingNumber(5.0 / 6.0, randint(2, 4))
        self.mod_1 = rotatingNumber(0.5, randint(self.mod_2.num + 1, 9))
        self.mod_ans = self.mod_1.num % self.mod_2.num
        self.mod__2 = rotatingNumber(5.0 / 6.0, randint(2, 4))
        self.mod__1 = rotatingNumber(0.5, randint(self.mod_2.num + 1, 9))
        self.mod__ans = self.mod__1.num % self.mod__2.num
        self.add = rotatingOperation(int(2.0 * locals.WIDTH / 3), "add")
        self.sub = rotatingOperation(int(2.0 * locals.WIDTH / 3), "sub")
        self.mod = rotatingOperation(int(2.0 * locals.WIDTH / 3), "mod")
        self.stage = 0
        self.sprites1 = Group(self.add1, self.add2, self.add)
        self.sprites2 = Group(self.sub1, self.sub2, self.sub)
        self.sprites3 = Group(self.mod1, self.mod2, self.mod)
        self.sprites4 = Group(self.mod_1, self.mod_2, self.mod)
        self.sprites5 = Group(self.mod__1, self.mod__2, self.mod)
        self.losing = 0

        #evade

        self.ee_icicles = [ee_icicle(0) ,ee_icicle(locals.HEIGHT + 70), ee_icicle(100)]
        self.ee_eskimo = eeskimo()
        self.esprites = Group(self.ee_eskimo, *self.ee_icicles)






    def start(self):
        #line
        music.load(os.path.join("games", "lineMathCombo", "finalSound.wav"))
        music.play()
        #maths
        self.answer = self.addans
        self.winner = False

    def stop(self):
        #line
        music.stop()
 
    def update(self, events):
        
        #evade
        self.esprites.update()
        keys = pygame.key.get_pressed()
        if keys[K_q]:
            self.win()
        elif (keys[K_RIGHT] or keys[K_d]) and (keys[K_LEFT] or keys[K_a]):
            pass
        elif keys[K_LEFT] or keys[K_a]:
            self.ee_eskimo.rect.x = max(self.ee_eskimo.rect.x - 15, 0)
        elif keys[K_RIGHT] or keys[K_d]:
            self.ee_eskimo.rect.x = min((locals.WIDTH  / 3)-24, self.ee_eskimo.rect.x + 15)
        for icicle in self.ee_icicles:
            if self.ee_eskimo.rect.colliderect(icicle.rect):
                self.winner = False
                self.losing = 1

        #line
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

        for icicle in self.e_icicles:
            if self.e_eskimo.rect.colliderect(icicle.rect):
                self.winner = False
                self.losing = 2
            #maths
        for event in events:
            if event.type == KEYDOWN and event.key == K_q:
                self.lose()
            if event.type == KEYDOWN and event.key in (K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9):
                dictt = {K_0 : 0, K_1 : 1, K_2 : 2, K_3 : 3, K_4 : 4, K_5 : 5, K_6 : 6, K_7 : 7, K_8 : 8, K_9 : 9}
                if dictt[event.key] == self.answer:
                    if self.stage == 0:
                        self.answer = self.subans
                        self.stage = 1
                    elif self.stage == 1:
                        self.answer = self.modans
                        self.stage = 2
                    elif self.stage == 2:
                        self.stage = 3
                        self.answer = self.mod_ans
                    elif self.stage == 3:
                        self.stage = 4
                        self.answer = self.mod__ans
                    elif self.stage == 4:
                        self.stage = 5
                        self.winner = True                     
                else:
                    self.winner = False
                    self.losing = 3

    def render(self, surface):
        surface.fill((0, 0, 0))
        if self.losing == 1:
            #evade lose
            imgpathhhhhhh = os.path.join("games", "lineMathCombo", "retroFail.png")
            test_imageeeeee = pygame.image.load(imgpathhhhhhh) 
            surface.blit(test_imageeeeee,(locals.WIDTH / 2, locals.HEIGHT / 2))
            pass
        elif self.losing == 2:
            #line lose
            imgpathhhhhhhh = os.path.join("games", "lineMathCombo", "minimalistFail.png")
            test_imageeeeeee = pygame.image.load(imgpathhhhhhhh) 
            surface.blit(test_imageeeeeee,(locals.WIDTH / 2, locals.HEIGHT / 2))
            pass
        elif self.losing == 3:
            imgpathhhhhhhhh = os.path.join("games", "lineMathCombo", "mathFail.png")
            test_imageeeeeeee = pygame.image.load(imgpathhhhhhhhh) 
            surface.blit(test_imageeeeeeee,(locals.WIDTH / 2, locals.HEIGHT / 2))
            #maths lose
            pass
        else:
            #line
            imgpathh = os.path.join("games", "lineMathCombo", "tile.png")
            test_image = pygame.image.load(imgpathh) 
            surface.blit(test_image,(0,0))
            imgpathhh = os.path.join("games", "lineMathCombo", "linesBG.png")
            test_imagee = pygame.image.load(imgpathhh)
            surface.blit(test_imagee,(377,0))
            self.sprites.draw(surface)

            #maths
            imgpathhhh = os.path.join("games", "lineMathCombo", "mathBG.png")
            test_imageee = pygame.image.load(imgpathhhh)
            surface.blit(test_imageee,(377,768 / 2))
            if self.stage == 0:
                self.sprites1.draw(surface)
            elif self.stage == 1:
                self.sprites2.draw(surface)
            elif self.stage == 2:
                self.sprites3.draw(surface)
            elif self.stage == 3:
                self.sprites4.draw(surface)
            elif self.stage == 4:
                self.sprites5.draw(surface)
            elif self.stage == 5:
                imgpathhhhhh = os.path.join("games", "lineMathCombo", "finshed.png")
                test_imageeeee = pygame.image.load(imgpathhhhhh)
                surface.blit(test_imageeeee,(int(2.0 * locals.WIDTH / 3) - 213, int(3.0 * locals.HEIGHT / 4) - 27))

            #evade
            imgpathhhhh = os.path.join("games", "lineMathCombo", "tile.png")
            test_imageeee = pygame.image.load(imgpathhhhh) 
            surface.blit(test_imageeee,(0,0))
            self.esprites.draw(surface)



    def get_timelimit(self):
        return 15