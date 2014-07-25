import math

from pygame.font import Font
from pygame.locals import *

from locals import *
from scene import Scene

import pygame, pygame.draw, pygame.event, pygame.mixer

GAME_FONT_SIZE = 32
GAMES_PER_PAGE = 5
PADDING_X = 250
PADDING_Y = 20
TITLE_FIXUP = 4
BORDER_OFFSET = 7
THUMBNAIL_WIDTH = 128
THUMBNAIL_HEIGHT = 128

def _is_numeric(k):
    return k == K_0 or k == K_1 or k == K_2 or k == K_3 or k == K_4  \
        or k == K_5 or k == K_6 or k == K_7 or k == K_8 or k == K_9

def _get_numeric_value(k):
    if   k == K_0: return 0
    elif k == K_1: return 1
    elif k == K_2: return 2
    elif k == K_3: return 3
    elif k == K_4: return 4
    elif k == K_5: return 5
    elif k == K_6: return 6
    elif k == K_7: return 7
    elif k == K_8: return 8
    elif k == K_9: return 9
    else: return None

class Chooser(Scene):
    """
    Microgame chooser.

    The microgame choosers allows the user to preview and select which
    microgames are active.

    Attributes
    microgames - the game's list of pairs of microgame modules and booleans
                 that determine if they are enabled
    nextscene  - the next scene object that should play after this chooser is
                 done
    index      - the current multiple (of NUM_GAMES_PER_PAGE) that we are
                 currently viewing
    """

    def __init__(self, game, microgames, nextscene):
        Scene.__init__(self, game)
        self.game_font = Font(GAME_FONT_FILENAME, GAME_FONT_SIZE)
        self.microgames = microgames
        self.nextscene = nextscene
        self.index = 0

    def start(self):
        pygame.mixer.music.load('chooser.ogg')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1, 0)

    def stop(self):
        pygame.mixer.music.stop()

    def update(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.game.change(self.nextscene)
                elif event.key == K_LEFT:
                    self.index -= 1
                    if self.index < 0:
                        self.index = 0
                elif event.key == K_RIGHT:
                    if (self.index + 1) * GAMES_PER_PAGE < len(self.microgames):
                        self.index += 1
                elif _is_numeric(event.key):
                    value = _get_numeric_value(event.key)
                    if 1 <= value <= GAMES_PER_PAGE:
                        index = self.index * GAMES_PER_PAGE + value - 1
                        if index < len(self.microgames):
                            self.microgames[index] =  \
                                (self.microgames[index][0],
                                 not self.microgames[index][1])

    def render(self, surface):
        surface.fill(C_BLACK)
        y = PADDING_Y
        offset = 0
        start_index = self.index * GAMES_PER_PAGE
        end_index = start_index + GAMES_PER_PAGE
        surface.blit(
            self.game_font.render('Page {0}/{1}'.format(self.index+1,
                int(math.ceil(len(self.microgames) / float(GAMES_PER_PAGE)))),
                True, C_WHITE), (10, 0))
        for game, enabled in self.microgames[start_index:end_index]:
            title = game.title()
            filename = game.thumbnail()
            filename = filename if filename else 'default.png'
            image, irect = load_image(filename, 0, 0)
            image = pygame.transform.scale(image, (128, 128))
            irect.width, irect.height = (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT)
            text_height = y + 0.25 * THUMBNAIL_HEIGHT + TITLE_FIXUP
            surface.blit(
                self.game_font.render('({0})'.format(offset+1), True, C_WHITE),
                (PADDING_X, text_height))
            surface.blit(
                self.game_font.render(title, True, C_WHITE),
                (PADDING_X + GAME_FONT_SIZE + 10, text_height))
            if enabled:
                surface.fill(
                    C_GOLD,
                    Rect(WIDTH - PADDING_X - THUMBNAIL_WIDTH - BORDER_OFFSET,
                         y - BORDER_OFFSET,
                         THUMBNAIL_WIDTH + BORDER_OFFSET * 2,
                         THUMBNAIL_WIDTH + BORDER_OFFSET * 2))
            surface.blit(image, (WIDTH - PADDING_X - THUMBNAIL_WIDTH, y))
            y += PADDING_Y + THUMBNAIL_HEIGHT
            offset += 1
