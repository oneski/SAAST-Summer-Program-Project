from pygame.locals import *
from locals import *
import sys, traceback, pygame
from game import Game

import loader

def main():
    """ Entry point of the microgames... game """
    pygame.init()
    try:
        surface = pygame.display.set_mode((WIDTH, HEIGHT))
        game = Game()
        pygame.display.set_caption('Microgames - SAAST Comp Sci 2013')
        clock = pygame.time.Clock()
        while not game.finished:
            clock.tick(FPS)
            game.update()
            game.render(surface)
            pygame.display.flip()
    except Exception as e:
        print 'An exception occurred.  Terminating the game!'
        ty, v, tb = sys.exc_info()
        print traceback.print_exception(ty, v, tb)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
