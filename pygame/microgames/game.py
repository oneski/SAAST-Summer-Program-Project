from locals import *
from menu import Menu
import loader

class Game():
    '''
    The Microgames game.

    Main model for the Microgames game.

    Attributes:
    finished   - True iff the Microgames game is over.
    scene      - The current scene this game is playing.
    microgames - The list of loaded microgame modules
    '''

    def __init__(self):
        ''' Initializes a new game to the start screen. '''
        self.finished = False
        self.scene = None
        self.microgames = loader.load(FAILFAST)
        self.change(Menu(self))

    def change(self, scene):
        ''' Changes the current scene to the given scene. '''
        if self.scene:
            self.scene.stop()
        self.scene = scene
        self.scene.start()

    def update(self):
        '''
        Updates the overall game by passing the request to the underlying
        scene.
        '''
        self.scene.update()

    def render(self, surface):
        '''
        Renders this game to the given by passing the request to the underying
        scene.
        '''
        self.scene.render(surface)
