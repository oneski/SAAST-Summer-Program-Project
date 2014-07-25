from pygame.font import Font
from pygame.locals import *
from pygame.time import get_ticks
import pygame, pygame.image, pygame.mixer, pygame.transform

from locals import *
from microgame import Microgame

FONT_SIZE = 56
Y_DIST = 60
THUMBNAIL_SIZE = (256, 256)

class Transition(Microgame):
    '''
    The transition scene

    The transition scene transitions between the various microgames displaying
    relevant information such as the player's score and their number of lives
    left.
    '''

    def __init__(self, hint, thumbnail):
        ''' Creates a transition with the given hint and next scene '''
        Microgame.__init__(self)
        font = Font(GAME_FONT_FILENAME, FONT_SIZE)

        self.thumbnail, _ = load_image(thumbnail, 0, 0)
        self.thumbnail    = pygame.transform.scale(self.thumbnail,
                                THUMBNAIL_SIZE)
        self.hint         = font.render(hint, True, C_WHITE)

        twidth, theight = self.thumbnail.get_size()
        hwidth, hheight = self.hint.get_size()
        self.thumbnail_rect = ( (WIDTH - twidth) / 2
                              , (HEIGHT - theight - hheight) / 2
                              , twidth
                              , theight )
        self.hint_rect      = ( (WIDTH - hwidth) / 2
                              , HEIGHT / 2 + hheight
                              , hwidth
                              , hheight )
    def _elapsed_time(self):
        return (get_ticks() - self.time) / 1000.0

    def start(self):
        self.time = get_ticks()
        pygame.mixer.music.load('transition.ogg')
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def update(self, events):
        if self._elapsed_time() > WAIT_PERIOD:
            self.win()

    def render(self, surface):
        surface.fill(C_BLACK)
        surface.blit(self.thumbnail, self.thumbnail_rect)
        surface.blit(self.hint, self.hint_rect)

    def get_timelimit(self):
        return 15
