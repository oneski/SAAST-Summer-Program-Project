# Pygame imports
import pygame, pygame.mixer
from pygame import Surface
from pygame.image import load
from pygame.locals import *
from pygame.mixer import music
from pygame.rect import Rect
from pygame.sprite import Group, Sprite, OrderedUpdates
from pygame.time import get_ticks

# Path imports
from os.path import join

# Random imports
from random import randint, choice

# Microgame-specific imports
import locals
from microgame import Microgame

##### LOADER-REQUIRED FUNCTIONS ################################################

def make_game():
    return Super_Saast_Bros()

def title():
    return 'SUPER SAAST BROS'

def thumbnail():
    return join('games', 'ssb', 'thumbnail.png')

def hint():
    return 'Don\'t get hit'

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

##### MODEL CLASSES ############################################################

##### CHARACTER SELECT #########################################################

class Player1_Selector(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'player1_selector.png')
        self.image, self.rect = _load_image(imgpath, 300, 600)
        self.lvelocity = 0
        self.rvelocity = 0
        self.uvelocity = 0
        self.dvelocity = 0

    def update(self):
        self.vvelocity = self.uvelocity + self.dvelocity
        self.hvelocity = self.lvelocity + self.rvelocity
        self.rect = self.rect.move(self.hvelocity, self.vvelocity)

class Player2_Selector(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'player2_selector.png')
        self.image, self.rect = _load_image(imgpath, 600, 600)
        self.lvelocity = 0
        self.rvelocity = 0
        self.uvelocity = 0
        self.dvelocity = 0

    def update(self):
        self.vvelocity = self.uvelocity + self.dvelocity
        self.hvelocity = self.lvelocity + self.rvelocity
        self.rect = self.rect.move(self.hvelocity, self.vvelocity)

class Falco_Selector(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'falco_selector.png')
        self.image, self.rect = _load_image(imgpath, 150, 100)

class Fox_Selector(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'fox_selector.png')
        self.image, self.rect = _load_image(imgpath, 350, 100)

class Samus_Selector(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'samus_selector.png')
        self.image, self.rect = _load_image(imgpath, 550, 100)

class Pit_Selector(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'pit_selector.png')
        self.image, self.rect = _load_image(imgpath, 750, 100)

class Snake_Selector(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'snake_selector.png')
        self.image, self.rect = _load_image(imgpath, 200, 500)

class Mewtwo_Selector(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'mewtwo_selector.png')
        self.image, self.rect = _load_image(imgpath, 450, 500)

class Zelda_Selector(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'zelda_selector.png')
        self.image, self.rect = _load_image(imgpath, 700, 500)


###### GAME ####################################################################

class Final_Destination(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'fd.png')
        self.image, self.rect = _load_image(imgpath, 100, 500)

class Character(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.uvelocity = 0
        self.lvelocity = 0
        self.rvelocity = 0
        self.hvelocity = 0
        self.jumps = 2
        self.direct = 'right'
        self.no_projectile_time = 0
        self.percent = 0
        self.knockback = 0

    def update(self):
        self.uvelocity += GRAVITY
        if self.knockback > 0:
            self.knockback -= KNOCKBACK_RESISTANCE
        elif self.knockback < 0:
            self.knockback += KNOCKBACK_RESISTANCE
        self.hvelocity = self.lvelocity + self.rvelocity + self.knockback
        self.rect = self.rect.move(self.hvelocity, self.uvelocity)

    def knockback_calc(self, hitbox):
        if hitbox.velocity > 0:
            self.knockback = int(float(self.percent) / 5) * hitbox.damage
        elif hitbox.velocity < 0:
            self.knockback = (int(float(self.percent) / 5) * hitbox.damage) * -1
        
        if self.knockback > hitbox.max_knockback:
            self.knockback = hitbox.max_knockback
        elif self.knockback < (hitbox.max_knockback * -1):
            self.knockback = (hitbox.max_knockback * -1)

######## PROJECTILES ###########################################################

class Samus_Charge_Shot(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'samus', 'charge_shot.png')
        self.image, self.rect = _load_image(imgpath, x, y)
        self.velocity = 20
        self.damage = 5
        self.max_knockback = 130

    def update(self):
        self.rect = self.rect.move(self.velocity, 0)

class Fox_Laser(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'fox', 'laser.png')
        self.image, self.rect = _load_image(imgpath, x, y)
        self.velocity = 40
        self.damage = 3
        self.max_knockback = 100

    def update(self):
        self.rect = self.rect.move(self.velocity, 0)

class Falco_Laser(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'falco', 'laser.png')
        self.image, self.rect = _load_image(imgpath, x, y)
        self.velocity = 40
        self.damage = 5
        self.max_knockback = 100

    def update(self):
        self.rect = self.rect.move(self.velocity, 0)

class Mewtwo_Shadow_Ball(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'mewtwo', 'shadow_ball.png')
        self.image, self.rect = _load_image(imgpath, x, y)
        self.velocity = 20
        self.uvelocity = 20
        self.damage = 4
        self.y = y
        self.max_knockback = 120

    def update(self):
        if self.rect.topleft[1] > self.y:
            self.uvelocity -= 10
        elif self.rect.topleft[1] < self.y:
            self.uvelocity += 10
        self.rect = self.rect.move(self.velocity, self.uvelocity)

class Zelda_Fireball(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        imgpath = join('games', 'ssb', 'zelda', 'fireball.png')
        self.image, self.rect = _load_image(imgpath, x, y)
        self.velocity = 10
        self.damage = 5
        self.max_knockback = 80

    def update(self):
        self.rect = self.rect.move(self.velocity, 0)

class Pit_Arrow(Sprite):
    def __init__(self, x, y, direct):
        Sprite.__init__(self)
        if direct == 'right':
            imgpath = join('games', 'ssb', 'pit', 'arrowright.png')
        elif direct == 'left':
            imgpath = join('games', 'ssb', 'pit', 'arrowleft.png')
        self.image, self.rect = _load_image(imgpath, x, y)
        self.velocity = 60
        self.damage = 3
        self.max_knockback = 100

    def update(self):
        self.rect = self.rect.move(self.velocity, 0)

class Snake_Missile(Sprite):
    def __init__(self, x, y, direct):
        Sprite.__init__(self)
        if direct == 'right':
            imgpath = join('games', 'ssb', 'snake', 'missileright.png')
        if direct == 'left':
            imgpath = join('games', 'ssb', 'snake', 'missileleft.png')
        self.image, self.rect = _load_image(imgpath, x, y)
        self.velocity = 1
        self.damage = 4
        self.max_knockback = 200

    def update(self):
        self.velocity = self.velocity * 1.3
        self.rect = self.rect.move(self.velocity, 0)

##### CHARACTERS #################################################################

class Fox(Character):
    def __init__(self):
        Character.__init__(self)
        self.run = [join('games', 'ssb', 'fox', 'runright.png'), join('games', 'ssb', 'fox', 'runleft.png')]
        self.gun = [join('games', 'ssb', 'fox', 'gunright.png'), join('games', 'ssb', 'fox', 'gunleft.png')]
        self.idle = [join('games', 'ssb', 'fox', 'idleright.png'), join('games', 'ssb', 'fox', 'idleleft.png')]
        self.image, self.rect = _load_image(self.idle[0], 0, 0)
        self.reloadtime = 400
        self.projectilecount = 3
        self.projectilesound = pygame.mixer.Sound(join('games', 'ssb', 'fox', 'laser.ogg'))
        self.jumpsounds =  [pygame.mixer.Sound(join('games', 'ssb', 'fox', 'hah.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'fox', 'hah2.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'fox', 'hah3.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'fox', 'shooh.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'fox', 'shuh.ogg'))]

    def make_projectile(self, x, y, charac):
        if charac.direct == 'right':
            self.projectile = Fox_Laser(x, y + 24)
            self.projectile.velocity = charac.projectile.velocity
        elif charac.direct == 'left':
            self.projectile = Fox_Laser(x - 44, y + 24)
            self.projectile.velocity = charac.projectile.velocity * (-1)

    def projectile_logic(self):
        if (self.projectilecount == 0) and ((pygame.time.get_ticks() - self.no_projectile_time) >= self.reloadtime):
            self.projectilecount = 3

class Samus(Character):
    def __init__(self):
        Character.__init__(self)
        self.run = [join('games', 'ssb', 'samus', 'runright.png'), join('games', 'ssb', 'samus', 'runleft.png')]
        self.gun = [join('games', 'ssb', 'samus', 'gunright.png'), join('games', 'ssb', 'samus', 'gunleft.png')]
        self.idle = [join('games', 'ssb', 'samus', 'idleright.png'), join('games', 'ssb', 'samus', 'idleleft.png')]
        self.image, self.rect = _load_image(self.idle[0], 0, 0)
        self.reloadtime = 1200
        self.projectilecount = 1
        self.projectilesound = pygame.mixer.Sound(join('games', 'ssb', 'samus', 'charge_shot.ogg'))
        self.jumpsounds =  [pygame.mixer.Sound(join('games', 'ssb', 'samus', 'hah.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'samus', 'heh.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'samus', 'hoo.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'samus', 'huh.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'samus', 'tu.ogg'))]

    def make_projectile(self, x, y, charac):
        if charac.direct == 'right':
            self.projectile = Samus_Charge_Shot(x, y + 5)
            self.projectile.velocity = charac.projectile.velocity
        elif charac.direct == 'left':
            self.projectile = Samus_Charge_Shot(x - 50, y + 5)
            self.projectile.velocity = charac.projectile.velocity * (-1)

    def projectile_logic(self):
        if (self.projectilecount == 0) and ((pygame.time.get_ticks() - self.no_projectile_time) >= self.reloadtime):
            self.projectilecount = 1

class Falco(Character):
    def __init__(self):
        Character.__init__(self)
        self.run = [join('games', 'ssb', 'falco', 'runright.png'), join('games', 'ssb', 'falco', 'runleft.png')]
        self.gun = [join('games', 'ssb', 'falco', 'gunright.png'), join('games', 'ssb', 'falco', 'gunleft.png')]
        self.idle = [join('games', 'ssb', 'falco', 'idleright.png'), join('games', 'ssb', 'falco', 'idleleft.png')]
        self.image, self.rect = _load_image(self.idle[0], 0, 0)
        self.reloadtime = 500
        self.projectilecount = 1
        self.projectilesound = pygame.mixer.Sound(join('games', 'ssb', 'falco', 'laser.ogg'))
        self.jumpsounds =  [pygame.mixer.Sound(join('games', 'ssb', 'falco', 'huh.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'falco', 'hah.ogg'))]

    def make_projectile(self, x, y, charac):
        if charac.direct == 'right':
            self.projectile = Falco_Laser(x, y + 30)
            self.projectile.velocity = charac.projectile.velocity
        elif charac.direct == 'left':
            self.projectile = Falco_Laser(x - 50, y + 30)
            self.projectile.velocity = charac.projectile.velocity * (-1)

    def projectile_logic(self):
        if (self.projectilecount == 0) and ((pygame.time.get_ticks() - self.no_projectile_time) >= self.reloadtime):
            self.projectilecount = 1

class Mewtwo(Character):
    def __init__(self):
        Character.__init__(self)
        self.run = [join('games', 'ssb', 'mewtwo', 'runright.png'), join('games', 'ssb', 'mewtwo', 'runleft.png')]
        self.gun = [join('games', 'ssb', 'mewtwo', 'gunright.png'), join('games', 'ssb', 'mewtwo', 'gunleft.png')]
        self.idle = [join('games', 'ssb', 'mewtwo', 'idleright.png'), join('games', 'ssb', 'mewtwo', 'idleleft.png')]
        self.image, self.rect = _load_image(self.idle[0], 0, 0)
        self.reloadtime = 800
        self.projectilecount = 1
        self.projectilesound = pygame.mixer.Sound(join('games', 'ssb', 'mewtwo', 'shadow_ball.ogg'))
        self.jumpsounds =  [pygame.mixer.Sound(join('games', 'ssb', 'mewtwo', 'mewtwojump.ogg'))]

    def make_projectile(self, x, y, charac):
        if charac.direct == 'right':
            self.projectile = Mewtwo_Shadow_Ball(x, y)
            self.projectile.velocity = charac.projectile.velocity
        elif charac.direct == 'left':
            self.projectile = Mewtwo_Shadow_Ball(x, y)
            self.projectile.velocity = charac.projectile.velocity * (-1)

    def projectile_logic(self):
        if (self.projectilecount == 0) and ((pygame.time.get_ticks() - self.no_projectile_time) >= self.reloadtime):
            self.projectilecount = 1

class Zelda(Character):
    def __init__(self):
        Character.__init__(self)
        self.run = [join('games', 'ssb', 'zelda', 'runright.png'), join('games', 'ssb', 'zelda', 'runleft.png')]
        self.gun = [join('games', 'ssb', 'zelda', 'gunright.png'), join('games', 'ssb', 'zelda', 'gunleft.png')]
        self.idle = [join('games', 'ssb', 'zelda', 'idleright.png'), join('games', 'ssb', 'zelda', 'idleleft.png')]
        self.image, self.rect = _load_image(self.idle[0], 0, 0)
        self.reloadtime = 1800
        self.projectilecount = 2
        self.projectilesound = pygame.mixer.Sound(join('games', 'ssb', 'zelda', 'fireball.ogg'))
        self.jumpsounds =  [pygame.mixer.Sound(join('games', 'ssb', 'zelda', 'hap.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'zelda', 'hah.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'zelda', 'ha.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'zelda', 'hah.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'zelda', 'hut.ogg'))]

    def make_projectile(self, x, y, charac):
        if charac.direct == 'right':
            self.projectile = Zelda_Fireball(x, y)
            self.projectile.velocity = charac.projectile.velocity
        elif charac.direct == 'left':
            self.projectile = Zelda_Fireball(x, y)
            self.projectile.velocity = charac.projectile.velocity * (-1)

    def projectile_logic(self):
        if (self.projectilecount == 0) and ((pygame.time.get_ticks() - self.no_projectile_time) >= self.reloadtime):
            self.projectilecount = 2

class Pit(Character):
    def __init__(self):
        Character.__init__(self)
        self.run = [join('games', 'ssb', 'pit', 'runright.png'), join('games', 'ssb', 'pit', 'runleft.png')]
        self.gun = [join('games', 'ssb', 'pit', 'gunright.png'), join('games', 'ssb', 'pit', 'gunleft.png')]
        self.idle = [join('games', 'ssb', 'pit', 'idleright.png'), join('games', 'ssb', 'pit', 'idleleft.png')]
        self.image, self.rect = _load_image(self.idle[0], 0, 0)
        self.reloadtime = 1000
        self.projectilecount = 10
        self.projectilesound = pygame.mixer.Sound(join('games', 'ssb', 'pit', 'laser.ogg'))
        self.jumpsounds =  [pygame.mixer.Sound(join('games', 'ssb', 'pit', 'huh.ogg'))]
   

    def make_projectile(self, x, y, charac):
        if charac.direct == 'right':
            self.projectile = Pit_Arrow(x, y + 25, charac.direct)
            self.projectile.velocity = charac.projectile.velocity
        elif charac.direct == 'left':
            self.projectile = Pit_Arrow(x - 50, y + 25, charac.direct)
            self.projectile.velocity = charac.projectile.velocity * (-1)

    def projectile_logic(self):
        if (self.projectilecount == 0) and ((pygame.time.get_ticks() - self.no_projectile_time) >= self.reloadtime):
            self.projectilecount = 10

class Snake(Character):
    def __init__(self):
        Character.__init__(self)
        self.run = [join('games', 'ssb', 'snake', 'runright.png'), join('games', 'ssb', 'snake', 'runleft.png')]
        self.gun = [join('games', 'ssb', 'snake', 'gunright.png'), join('games', 'ssb', 'snake', 'gunleft.png')]
        self.idle = [join('games', 'ssb', 'snake', 'idleright.png'), join('games', 'ssb', 'snake', 'idleleft.png')]
        self.image, self.rect = _load_image(self.idle[0], 0, 0)
        self.reloadtime = 1300
        self.projectilecount = 2
        self.projectilesound = pygame.mixer.Sound(join('games', 'ssb', 'snake', 'gun.ogg'))
        self.jumpsounds =  [pygame.mixer.Sound(join('games', 'ssb', 'snake', 'huh.ogg')),
                            pygame.mixer.Sound(join('games', 'ssb', 'snake', 'hah.ogg'))]

    def make_projectile(self, x, y, charac):
        if charac.direct == 'right':
            self.projectile = Snake_Missile(x, y + 24, charac.direct)
            self.projectile.velocity = charac.projectile.velocity
        elif charac.direct == 'left':
            self.projectile = Snake_Missile(x - 44, y + 24, charac.direct)
            self.projectile.velocity = charac.projectile.velocity * (-1)

    def projectile_logic(self):
        if (self.projectilecount == 0) and ((pygame.time.get_ticks() - self.no_projectile_time) >= self.reloadtime):
            self.projectilecount = 2

##### MICROGAME CLASS ##########################################################

# TODO: rename this class to your game's name...

GRAVITY = 2
JUMP_BOOST = -25
AIR_JUMP_BOOST = -20
KNOCKBACK_RESISTANCE = 1

class Super_Saast_Bros(Microgame):
    def __init__(self):
        Microgame.__init__(self)
        self.character_select = True
        self.player1_selector = Player1_Selector()
        self.player2_selector = Player2_Selector()
        self.falco = Falco_Selector()
        self.fox = Fox_Selector()
        self.samus = Samus_Selector()
        self.snake = Snake_Selector()
        self.pit = Pit_Selector()
        self.mewtwo = Mewtwo_Selector()
        self.zelda = Zelda_Selector()
        self.character_possibilities = Group(self.falco, self.fox, self.samus, self.snake, self.pit, self.mewtwo, self.zelda)
        self.sprites = OrderedUpdates(self.falco, self.fox, self.samus, self.snake, self.pit, self.mewtwo, self.zelda, self.player1_selector, self.player2_selector)
        self.player1 = Fox()
        self.player2 = Falco()
        self.p1victory = pygame.image.load(join('games', 'ssb', 'p1_win.png'))
        self.p2victory = pygame.image.load(join('games', 'ssb', 'p2_win.png'))

        self.platform = Final_Destination()

        self.p1win = False
        self.p2win = False
        self.wincondition = False

        self.a_track = False
        self.d_track = False
        self.lshift_track = False
        self.quote_track = False
        self.l_track = False
        self.rshift_track = False

        self.playergroup = Group(self.player1, self.player2)
        self.player1_projectiles = Group()
        self.player2_projectiles = Group()

    def start(self):
        pygame.mixer.music.load(join('games', 'ssb', 'battlefield_melee.ogg'))
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def update(self, events):
        if self.wincondition == False:
            if self.character_select == True:
                player_1_character = self.detect_character(self.player1_selector, self.character_possibilities)
                player_2_character = self.detect_character(self.player2_selector, self.character_possibilities)
                if player_1_character == self.falco:
                    self.player1 = Falco()
                elif player_1_character == self.fox:
                    self.player1 = Fox()
                elif player_1_character == self.samus:
                    self.player1 = Samus()
                elif player_1_character == self.snake:
                    self.player1 = Snake()
                elif player_1_character == self.pit:
                    self.player1 = Pit()
                elif player_1_character == self.mewtwo:
                    self.player1 = Mewtwo()
                elif player_1_character == self.zelda:
                    self.player1 = Zelda()

                if player_2_character == self.falco:
                    self.player2 = Falco()
                elif player_2_character == self.fox:
                    self.player2 = Fox()
                elif player_2_character == self.samus:
                    self.player2 = Samus()
                elif player_2_character == self.snake:
                    self.player2 = Snake()
                elif player_2_character == self.pit:
                    self.player2 = Pit()
                elif player_2_character == self.mewtwo:
                    self.player2 = Mewtwo()
                elif player_2_character == self.zelda:
                    self.player2 = Zelda()

                for event in events:
                    self.player1_selector_logic(event, self.player1_selector)
                    self.player2_selector_logic(event, self.player2_selector)
                    self.character_select_logic(event)

                self.sprites.update()

            if self.character_select == False:
                self.detect_hit(self.player2, self.player1_projectiles)
                self.detect_hit(self.player1, self.player2_projectiles)

                self.remove_projectiles(self.player1_projectiles, self.sprites)
                self.remove_projectiles(self.player2_projectiles, self.sprites)

                self.sprites.update()

                self.detect_floor()
                
                for event in events:
                    self.char_logic1(event, self.player1)
                    self.char_logic2(event, self.player2)

                self.player1.projectile_logic()
                self.player2.projectile_logic()

                y1 = self.player1.rect.top
                y2 = self.player2.rect.top

                if (y1 > 1200) or (y2 > 1200):
                    if y1 > 1200:
                        self.p2win = True
                    if y2 > 1200:
                        self.p1win = True
                    self.sprites.remove(self.platform, self.player1, self.player2)
                    self.wincondition = True
                    self.win_time = pygame.time.get_ticks()

        elif self.wincondition == True:
            if pygame.time.get_ticks() - self.win_time >= 3000:
                self.win()

    def player1_selector_logic(self, event, player_selector):
        if event.type == KEYDOWN:
            if event.key == K_w:
                player_selector.uvelocity -= 15
            elif event.key == K_d:
                player_selector.rvelocity += 15
            elif event.key == K_s:
                player_selector.dvelocity += 15
            elif event.key == K_a:
                player_selector.lvelocity -= 15
        if event.type == KEYUP:
            if event.key == K_w:
                player_selector.uvelocity += 15
            elif event.key == K_d:
                player_selector.rvelocity -= 15
            elif event.key == K_s:
                player_selector.dvelocity -= 15
            elif event.key == K_a:
                player_selector.lvelocity += 15

    def player2_selector_logic(self, event, player_selector):
        if event.type == KEYDOWN:
            if event.key == K_p:
                player_selector.uvelocity -= 15
            elif event.key == K_QUOTE:
                player_selector.rvelocity += 15
            elif event.key == K_SEMICOLON:
                player_selector.dvelocity += 15
            elif event.key == K_l:
                player_selector.lvelocity -= 15
        if event.type == KEYUP:
            if event.key == K_p:
                player_selector.uvelocity += 15
            elif event.key == K_QUOTE:
                player_selector.rvelocity -= 15
            elif event.key == K_SEMICOLON:
                player_selector.dvelocity -= 15
            elif event.key == K_l:
                player_selector.lvelocity += 15

    def detect_character(self, player_selector, character_possibilities):
        for character in pygame.sprite.spritecollide(player_selector, character_possibilities, False):
            return character

    def character_select_logic(self, event):
        if event.type == KEYDOWN:
            if event.key == K_t:
                self.character_select = False
                self.player1.direct = 'right'
                self.player2.direct = 'left'
                self.player1.image, self.player1.rect = _load_image(self.player1.idle[0], 250, 350)
                self.player2.image, self.player2.rect = _load_image(self.player2.idle[1], 650, 350)
                self.sprites.remove(self.falco, self.fox, self.samus, self.snake, self.pit, self.mewtwo, self.zelda, self.player1_selector, self.player2_selector)
                self.sprites.add(self.platform, self.player1, self.player2)
                self.playergroup.add(self.player1, self.player2)


    def detect_floor(self):
        for char in pygame.sprite.spritecollide(self.platform, self.playergroup, False):
            char.rect.y = (self.platform.rect.topleft[1] - char.rect.height)
            char.uvelocity = 0
            char.jumps = 2

    def detect_hit(self, receiver, hitboxes):
        for hitbox in pygame.sprite.spritecollide(receiver, hitboxes, True):
            receiver.percent += hitbox.damage
            receiver.knockback_calc(hitbox)

    def remove_projectiles(self, projectilegroup, spritegroup):
        for projectile in projectilegroup:
            x_left, _ = projectile.rect.topleft
            x_right, _ = projectile.rect.bottomright
            if (x_left <= 0) or (x_right >= locals.WIDTH):
                spritegroup.remove(projectile)


    def render(self, surface):
        surface.fill(Color(0, 0, 0))
        self.sprites.draw(surface)

        if self.p1win == True:
            surface.blit(self.p1victory, (0, 0))
        elif self.p2win == True:
            surface.blit(self.p2victory, (0, 0))

    def get_timelimit(self):
        return 60

    def char_logic1(self, event, charac):
        x, y = charac.rect.topleft
        if event.type == KEYDOWN:
            if event.key == K_w:
                self.jump_logic(charac)
            elif event.key == K_a:
                self.a_track = True
                charac.image, charac.rect = _load_image(charac.run[1], x, y)
                charac.lvelocity -= 10
                charac.direct = 'left'
            elif event.key == K_d:
                self.d_track = True
                charac.rvelocity += 10
                charac.image, charac.rect = _load_image(charac.run[0], x, y)
                charac.direct = 'right'
            elif event.key == K_LSHIFT:
                if charac.projectilecount > 0:
                    charac.projectilesound.play()
                    self.lshift_track = True
                    if charac.direct == 'right':
                        charac.image, charac.rect = _load_image(charac.gun[0], x, y)
                        x, y = charac.rect.topright
                        charac.make_projectile(x, y, charac)
                    elif charac.direct == 'left':
                        charac.image, charac.rect = _load_image(charac.gun[1], x, y)
                        x, y = charac.rect.topleft
                        charac.make_projectile(x, y, charac)
                    self.sprites.add(charac.projectile)
                    self.player1_projectiles.add(charac.projectile)
                    charac.projectilecount -= 1
                    if charac.projectilecount == 0:
                        charac.no_projectile_time = pygame.time.get_ticks()
        elif event.type == KEYUP:
            if event.key == K_a:
                charac.lvelocity += 10
                self.a_track = False
                if self.d_track == False:
                    if self.lshift_track == False:
                        if charac.direct == 'right':
                            charac.image, charac.rect = _load_image(charac.idle[0], x, y - 10)
                        elif charac.direct == 'left':
                            charac.image, charac.rect = _load_image(charac.idle[1], x, y - 10)
                    elif self.lshift_track == True:
                        if charac.direct == 'right':
                            charac.image, charac.rect = _load_image(charac.gun[0], x, y - 5)
                        elif charac.direct == 'left':
                            charac.image, charac.rect = _load_image(charac.gun[1], x, y - 5)
                elif self.d_track == True:
                    if self.lshift_track == False:
                            charac.image, charac.rect = _load_image(charac.run[0], x, y)
                            charac.direct = 'right'
                    elif self.lshift_track == True:
                        charac.image, charac.rect = _load_image(charac.gun[0], x, y - 5)
            elif event.key == K_d:
                charac.rvelocity -= 10
                self.d_track = False
                if self.a_track == False:
                    if self.lshift_track == False:
                        if charac.direct == 'right':
                            charac.image, charac.rect = _load_image(charac.idle[0], x, y - 10)
                        elif charac.direct == 'left':    
                            charac.image, charac.rect = _load_image(charac.idle[1], x, y - 10)
                    elif self.lshift_track == True:
                        if charac.direct == 'right':
                            charac.image, charac.rect = _load_image(charac.gun[0], x, y - 5)
                        elif charac.direct == 'left':
                            charac.image, charac.rect = _load_image(charac.gun[1], x, y - 5)
                elif self.a_track == True:
                    if self.lshift_track == False:
                        charac.image, charac.rect = _load_image(charac.run[1], x, y)
                        charac.direct = 'left'
                    elif self.lshift_track == True:
                        charac.image, charac.rect = _load_image(charac.gun[1], x, y - 5)
            elif event.key == K_LSHIFT:
                self.lshift_track = False
                if (self.a_track == False) and (self.d_track == False):
                    if charac.direct == 'right':
                        charac.image, charac.rect = _load_image(charac.idle[0], x, y - 10)
                    elif charac.direct == 'left':    
                        charac.image, charac.rect = _load_image(charac.idle[1], x, y - 10)
                elif (self.a_track == False) and (self.d_track == True):
                    charac.image, charac.rect = _load_image(charac.run[0], x, y)
                    charac.direct = 'right'
                elif (self.a_track == True) and (self.d_track == False):
                    charac.image, charac.rect = _load_image(charac.run[1], x, y)
                    charac.direct = 'left'
                elif (self.a_track == True) and (self.d_track == False):
                    if charac.direct == 'right':
                        charac.image, charac.rect = _load_image(charac.gun[0], x, y)
                    elif charac.direct == 'left':
                        charac.image, charac.rect = _load_image(charac.gun[1], x, y)

    def char_logic2(self, event, charac):
        x, y = charac.rect.topleft
        if event.type == KEYDOWN:
            if event.key == K_p:
                self.jump_logic(charac)
            elif event.key == K_l:
                self.l_track = True
                charac.image, charac.rect = _load_image(charac.run[1], x, y)
                charac.lvelocity -= 10
                charac.direct = 'left'
            elif event.key == K_QUOTE:
                self.quote_track = True
                charac.rvelocity += 10
                charac.image, charac.rect = _load_image(charac.run[0], x, y)
                charac.direct = 'right'
            elif event.key == K_RSHIFT:
                if charac.projectilecount > 0:
                    charac.projectilesound.play()
                    self.rshift_track = True
                    if charac.direct == 'right':
                        charac.image, charac.rect = _load_image(charac.gun[0], x, y)
                        x, y = charac.rect.topright
                        charac.make_projectile(x, y, charac)
                    elif charac.direct == 'left':
                        charac.image, charac.rect = _load_image(charac.gun[1], x, y)
                        x, y = charac.rect.topleft
                        charac.make_projectile(x, y, charac)
                    self.sprites.add(charac.projectile)
                    self.player2_projectiles.add(charac.projectile)
                    charac.projectilecount -= 1
                    if charac.projectilecount == 0:
                        charac.no_projectile_time = pygame.time.get_ticks()
        elif event.type == KEYUP:
            if event.key == K_l:
                charac.lvelocity += 10
                self.l_track = False
                if self.quote_track == False:
                    if self.rshift_track == False:
                        if charac.direct == 'right':
                            charac.image, charac.rect = _load_image(charac.idle[0], x, y - 10)
                        elif charac.direct == 'left':
                            charac.image, charac.rect = _load_image(charac.idle[1], x, y - 10)
                    elif self.rshift_track == True:
                        if charac.direct == 'right':
                            charac.image, charac.rect = _load_image(charac.gun[0], x, y - 5)
                        elif charac.direct == 'left':
                            charac.image, charac.rect = _load_image(charac.gun[1], x, y - 5)
                elif self.quote_track == True:
                    if self.rshift_track == False:
                            charac.image, charac.rect = _load_image(charac.run[0], x, y)
                            charac.direct = 'right'
                    elif self.rshift_track == True:
                        charac.image, charac.rect = _load_image(charac.gun[0], x, y - 5)
            elif event.key == K_QUOTE:
                charac.rvelocity -= 10
                self.quote_track = False
                if self.l_track == False:
                    if self.rshift_track == False:
                        if charac.direct == 'right':
                            charac.image, charac.rect = _load_image(charac.idle[0], x, y - 10)
                        elif charac.direct == 'left':    
                            charac.image, charac.rect = _load_image(charac.idle[1], x, y - 10)
                    elif self.rshift_track == True:
                        if charac.direct == 'right':
                            charac.image, charac.rect = _load_image(charac.gun[0], x, y - 5)
                        elif charac.direct == 'left':
                            charac.image, charac.rect = _load_image(charac.gun[1], x, y - 5)
                elif self.l_track == True:
                    if self.rshift_track == False:
                        charac.image, charac.rect = _load_image(charac.run[1], x, y)
                        charac.direct = 'left'
                    elif self.rshift_track == True:
                        charac.image, charac.rect = _load_image(charac.gun[1], x, y - 5)
            elif event.key == K_RSHIFT:
                self.rshift_track = False
                if (self.l_track == False) and (self.quote_track == False):
                    if charac.direct == 'right':
                        charac.image, charac.rect = _load_image(charac.idle[0], x, y - 10)
                    elif charac.direct == 'left':    
                        charac.image, charac.rect = _load_image(charac.idle[1], x, y - 10)
                elif (self.l_track == False) and (self.quote_track == True):
                    charac.image, charac.rect = _load_image(charac.run[0], x, y)
                    charac.direct = 'right'
                elif (self.l_track == True) and (self.quote_track == False):
                    charac.image, charac.rect = _load_image(charac.run[1], x, y)
                    charac.direct = 'left'
                elif (self.l_track == True) and (self.quote_track == False):
                    if charac.direct == 'right':
                        charac.image, charac.rect = _load_image(charac.gun[0], x, y)
                    elif charac.direct == 'left':
                        charac.image, charac.rect = _load_image(charac.gun[1], x, y)

    def jump_logic(self, ch):
        if ch.jumps == 2:
            ch.uvelocity = JUMP_BOOST
            ch.jumpsounds[randint(0, len(ch.jumpsounds) - 1)].play()
        elif ch.jumps == 1:
            ch.uvelocity = AIR_JUMP_BOOST
            ch.jumpsounds[randint(0, len(ch.jumpsounds) - 1)].play()
        ch.jumps -= 1