# Pygame imports
import pygame, pygame.mixer
from pygame import Surface
from pygame.image import load
from pygame.locals import *
from pygame.mixer import music
from pygame.rect import Rect
from pygame.sprite import Group, Sprite

# Path imports
from os.path import join

# Random imports
from random import randint, choice

# Microgame-specific imports
import locals
from microgame import Microgame

##### LOADER-REQUIRED FUNCTIONS ################################################

def make_game():
    return MomsSpaghettiGame()

def title():
    return "Mom's Spaghetti"

def thumbnail():
    return join('games', 'moms_spaghetti', 'thumbnail.jpg')

def hint():
    return "Feed Eminem"

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

INITIAL_X = 300
INITIAL_Y = 100

MIN_VELOCITY = -25
MAX_VELOCITY = 35
VELOCITY_INJ = 50
DECAY        = 2

class EminemSprite(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        imgpath = join('games', 'moms_spaghetti', 'flappy.png')
        self.image, self.rect = _load_image(imgpath, INITIAL_X, INITIAL_Y)
        self.velocity = MAX_VELOCITY / 2

    def _update_velocity(self):
        new_velocity = self.velocity + DECAY
        if new_velocity > MAX_VELOCITY:
            self.velocity = MAX_VELOCITY
        elif new_velocity < MIN_VELOCITY:
            self.velocity = MIN_VELOCITY
        else:
            self.velocity = new_velocity

    def update(self):
        # Update velocity
        self._update_velocity()

        # Updat
        self.rect = self.rect.move(0, self.velocity)

##### MICROGAME CLASS #########################################################

class MomsSpaghettiGame(Microgame):
    def __init__(self):
        Microgame.__init__(self)
        self.eminem  = EminemSprite()
        self.sprites = Group(self.eminem)

    def start(self):
        pass

    def stop(self):
        pass

    def update(self, events):
        # Update all our sprites
        self.sprites.update()

        # Check to see if we hit the bottom or top of the screen
        _, y_bot = self.eminem.rect.bottomleft
        if self.eminem.rect.y <= 0 or y_bot >= locals.HEIGHT:
            self.lose()

        # Process user input
        for event in events:
            if event.type == KEYUP and event.key == K_SPACE:
                self.eminem.velocity -= VELOCITY_INJ

    def render(self, surface):
        surface.fill(Color(0, 0, 0))
        self.sprites.draw(surface)

    def get_timelimit(self):
        return 10
