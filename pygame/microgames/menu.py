from pygame.font import Font
from pygame.locals import *

from locals import *
from menuopts import options
from scene import Scene

import pygame, pygame.event, pygame.mixer

OPTIONS_INIT_X    = 175
OPTIONS_INIT_Y    = 300
OPTIONS_FONT_SIZE = 48
OPTIONS_Y_DIST    = 67

class Menu(Scene):
    """
    The Menu scene

    The main menu of the Microgames game.  From here, you can start a new game,
    change various options, or quit.
    """

    def __init__(self, game):
        Scene.__init__(self, game)
        self.options = options()
        self.options_font = Font(GAME_FONT_FILENAME, OPTIONS_FONT_SIZE)
        self.background, self.rectbg = load_image('title.jpg', 0, 0)
        self.index = 0

    def start(self):
        self.index = 0
        pygame.mixer.music.load('theme.ogg')
        pygame.mixer.music.play(-1, 0)

    def stop(self):
        pygame.mixer.music.stop()
        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.options[self.index][1](self)
                elif event.key == K_UP:
                    self.index -= 0 if self.index == 0 else 1
                elif event.key == K_DOWN:
                    self.index += 0 if self.index == len(self.options)-1 else 1

    def _render_options(self, surface):
        surface.blit(self.options_font.render('>', True, C_WHITE),
                (OPTIONS_INIT_X, OPTIONS_INIT_Y + self.index * OPTIONS_Y_DIST))

    def render(self, surface):
        surface.fill(C_BLACK)
        surface.blit(self.background, (self.rectbg.x, self.rectbg.y))
        self._render_options(surface)
