from pygame.font import Font
from pygame.locals import *
from pygame.time import get_ticks
import pygame, pygame.image, pygame.mixer, pygame.time

from random import randint

from locals import *
from scene import Scene
from transition import Transition

FONT_SIZE = 36
TIMER_POS = (10, 10)
LIVES_POS = (20, HEIGHT - 70)
SCORE_POS = (WIDTH - 150, HEIGHT - 70)

class Engine(Scene):
    """
    Manages the playthrough of a collection of microgames.

    The engine is the main game scene.  It is responsible for managing the
    playthrough of a collection of microgames.  The player has a number of lives
    and must complete as many microgames as possible before they run out of
    lives.

    Attributes:
    game       - the Game object this engine operates under.
    screen     - the screen associated with the engine.
    lives      - the number of lives the player has left
    completed  - the number of games the player completed so far
    microgames - the list of microgame modules this engine randomly plays
    next_index - the index of the next game to play in the microgames list
    mg         - the current microgame this engine is playing
    randpick   - True if games are randomly picked, else they are rotated in-order
    in_transition - True if the engine is in transition mode
    base_time  - The base time when the last microgame was selected (in ms)

    """

    def _select_next_game(self):
        """ Updates next_index with the next microgame to play """
        if self.randpick:
            self.next_index = randint(0, len(self.microgames) - 1)
        else:
            self.next_index += 1
            if self.next_index >= len(self.microgames) - 1:
                self.lives = -1

    def _switch_to_transition(self):
        """ Switches to a transition screen """
        if self.mg:
            self.mg.stop()
        next_game = self.microgames[self.next_index]
        self.mg = Transition(next_game.hint(), next_game.thumbnail())
        self.mg.start()
        self.time_since_start = pygame.time.get_ticks()
        self.in_transition = True

    def _switch_to_microgame(self):
        """ Switches to the next microgame """
        if self.mg:
            self.mg.stop()
        self.mg = self.microgames[self.next_index].make_game()
        self.mg.start()
        self.time_since_start = pygame.time.get_ticks()
        self.in_transition = False

    def __init__(self, game, lives, microgames, prevscene, randpick = True):
        Scene.__init__(self, game)
        self.font = Font(GAME_FONT_FILENAME, FONT_SIZE)
        self.lives = lives
        self.completed = 0
        self.in_transition = False
        self.microgames = microgames
        self.prevscene = prevscene
        self.mg = None
        self.time_since_start = None
        self.randpick = randpick
        self.next_index = -1

    def start(self):
        self._select_next_game()
        self._switch_to_transition()

    def stop(self):
        # In addition to myself, unload my current microgame as well
        self.mg.stop()

    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == KEYUP and event.key == K_ESCAPE:
                self.game.change(self.prevscene)
        limit = self.mg.get_timelimit()
        if self.mg.finished:
            if self.in_transition:
                self._switch_to_microgame()
            else:
                if self.mg.winner:
                    self.completed += 1
                else:
                    self.lives -= 1
                if self.lives < 0:
                    self.game.change(self.prevscene)
                else:
                    self._select_next_game()
                    self._switch_to_transition()
        elif limit and pygame.time.get_ticks() - self.time_since_start > limit * 1000:
            self.mg.finished = True
        else:
            self.mg.update(events)

    def render(self, surface):
        self.mg.render(surface)
        surface.blit(self.font.render('Lives: {0}'.format(self.lives), True,
            C_WHITE), LIVES_POS)
        surface.blit(self.font.render('Score: {0}'.format(self.completed), True,
            C_WHITE), SCORE_POS)
        if not isinstance(self.mg, Transition):
            elapsed = self.mg.get_timelimit() -  \
                (pygame.time.get_ticks() - self.time_since_start) / 1000.0
            surface.blit(self.font.render('{0:.2f}'.format(elapsed), True,
                C_WHITE), TIMER_POS)
