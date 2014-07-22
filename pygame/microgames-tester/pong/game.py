import pygame, pygame.mixer
from pygame import Surface
from pygame.image import load
from pygame.locals import *
from pygame.mixer import music
from pygame.rect import Rect
from pygame.sprite import Group, Sprite

from random import randint, choice

import locals
from microgame import Microgame

##### GAME CONSTANTS ###########################################################

SPEED_BASE = 10
BAT_SPEED = 10
BALL_SPEED_BASE = 10
BALL_SPEED_RANGE = 10
AI_TRACKING_SLACK = 10
TIME_TO_WIN_AFTER_BOUNCE = 2000

##### LOADER-REQUIRED FUNCTIONS ################################################

def make_game():
    return PongMicrogame()

def title():
    return 'Pong'

def thumbnail():
    return 'games/pong/thumbnail.png'

def hint():
    return 'Return it!'

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

class Ball(Sprite):
    '''
    A ball in the Pong Microgame.

    Attributes:
    rect   - the bounding box encasing this ball
    image  - the rendering surface of this ball
    vx     - the x-component of the ball's velocity
    vy     - the y-component of the ball's velocity
    bat_sound  - the sound played when hitting a bat
    wall_sound - the sound played when hitting a wall
    area   - the bounding box of the game world
    game   - the PongMicrogame object that owns this Ball
    '''

    def __init__(self, game, x, y, vx, vy):
        Sprite.__init__(self)
        self.image, self.rect = _load_image('games/pong/ball.png', x, y)
        self.vx = vx
        self.vy = vy
        self.bat_sound  = pygame.mixer.Sound('games/pong/ping.wav')
        self.wall_sound = pygame.mixer.Sound('games/pong/pong.wav')
        self.area = game.rect
        self.game = game

    def update(self):
        # Store the future position of the ball (in rect), and ask...
        rect = self.rect.move(self.vx, self.vy)
        # Did the ball leave the playfield (i.e., hit a wall)?
        if not self.area.contains(self.rect):
            self.wall_sound.play()
            tl = not self.area.collidepoint(rect.topleft)
            tr = not self.area.collidepoint(rect.topright)
            bl = not self.area.collidepoint(rect.bottomleft)
            br = not self.area.collidepoint(rect.bottomright)
            if tl and tr or bl and br:
                self.vy = -self.vy
            if tl and bl:
                # Collision on the left-hand side --- win!
                self.vx = -self.vx
                self.game.win()
            if tr and br:
                # Collision on the right-hand side --- lose!
                self.vx = -self.vx
                self.game.lose()
            rect = self.rect.move(self.vx, self.vy)
        # Did the ball collide with the left bat?
        elif self.rect.colliderect(self.game.lbat.rect):
            self.bat_sound.play()
            self.vx = -self.vx
            rect.x = self.game.lbat.rect.x + self.game.lbat.rect.width + 1
        # Did the ball colilide with the right bat?
        elif self.rect.colliderect(self.game.rbat.rect):
            self.bat_sound.play()
            self.vx = -self.vx
            rect.x = self.game.rbat.rect.x - rect.width - 1
            self.game.start_win_countdown()
        # Commit the future position of the ball as its current position
        self.rect = rect

class Bat(Sprite):
    '''
    A Bat in the Pong Microgame

    Attributes:
    image     - the rendering surface of this bat
    rect      - the bounding box of the bat
    direction - direction of movement: -1 = up, 0 = not moving, 1 = down
    area      - the bounding box of the area enclosing the playfield
    ball      - the ball object that this bat will track (if ai is enabled)
    ai        - True if this bat is controlled by the ai, false otherwise
    '''

    def __init__(self, x, y, area, ball, ai=False):
        Sprite.__init__(self)
        self.direction = 0
        self.image, self.rect = _load_image('games/pong/bat.png', x, y)
        self.area = area
        self.ball = ball
        self.ai   = ai

    def _get_delta(self):
        if self.direction == -1:
            return -BAT_SPEED
        elif self.direction == 0:
            return 0
        else:
            return BAT_SPEED

    def update(self):
        # If the bat is AI controlled, determine its direction
        if self.ai:
            bat_midpoint  = self.rect.y + self.rect.height / 2
            ball_midpoint = self.ball.rect.y + self.ball.rect.height / 2
            if bat_midpoint > ball_midpoint + AI_TRACKING_SLACK:
                self.direction = -1
            elif bat_midpoint < ball_midpoint - AI_TRACKING_SLACK:
                self.direction = 1
        # Store the future position of the bat (in rect) and ask...
        rect = self.rect.move(0, self._get_delta())
        # Did the bat collide with the boundaries of the playfield?
        if not self.area.contains(self.rect):
            tl = not self.area.collidepoint(rect.topleft)
            tr = not self.area.collidepoint(rect.topright)
            bl = not self.area.collidepoint(rect.bottomleft)
            br = not self.area.collidepoint(rect.bottomright)
            if tl and tr:
                rect.y = 1
            elif bl and br:
                rect.y = self.area.height - rect.height - 1
        # Commit the finalized position of the bat
        self.rect = rect

class PongMicrogame(Microgame):
    '''
    Simple Pong Microgame.

    An example Microgame.  Single bounce Pong.

    Attributes:
    rect    - the bounding box of the playfield
    ball    - the ball of the microgame
    lbat    - the left-hand bat of this microgame, ai-controlled
    rbat    - the right-hand bat of this microgame, user-controlled
    sprites - the sprite group that contains the sprites of the game
    timeSinceWin - the time in (ms) when the player won the game, or 0 if the
                   game has not been won yet
    '''

    def __init__(self):
        Microgame.__init__(self)
        self.rect = Rect(0, 0, locals.WIDTH, locals.HEIGHT)
        speed = BALL_SPEED_BASE
        widthqrt  = self.rect.width / 4
        heightqrt = self.rect.height / 4

        self.ball = Ball(self, 150, randint(heightqrt, heightqrt * 3),  \
            randint(speed, speed + BALL_SPEED_RANGE),                   \
            choice([speed, -speed]))
        self.lbat = Bat(100, randint(heightqrt, heightqrt * 3),         \
                        self.rect, self.ball, True)
        self.rbat = Bat(self.rect.width - 150,                          \
                        randint(heightqrt, heightqrt * 3),              \
                        self.rect, self.ball)
        self.sprites = Group((self.ball, self.lbat, self.rbat))
        self.timeSinceWin = 0

    def start_win_countdown(self):
        '''
        Starts the successful hit countdown --- once this is up, the player wins
        the game.
        '''
        self.timeSinceWin = pygame.time.get_ticks()

    def start(self):
        music.load('games/pong/music.mp3')
        music.play(0, 0.5)

    def stop(self):
        music.stop()

    def update(self, events):
        time = pygame.time.get_ticks()
        if self.timeSinceWin > 0 and  \
           time > self.timeSinceWin + TIME_TO_WIN_AFTER_BOUNCE:
            self.win()
        self.sprites.update()
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.rbat.direction = -1
                elif event.key == K_DOWN:
                    self.rbat.direction = 1
            if event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    self.rbat.direction = 0

    def render(self, surface):
        surface.fill(Color(0, 0, 0))
        self.sprites.draw(surface)

    def get_timelimit(self):
        return 10
