class Scene(object):
    '''
    Base class for all scenes.

    A scene is an abstract game component run by the top-level Game.  Scenes
    include the menu and the microgame engine.

    Attributes:
    game     - the Game object this scene operates under.
    finished - True iff this scene has completed
    '''

    def __init__(self, game):
        self.game = game
        self.finished = False

    def start(self):
        '''
        Initializes this scene.

        init is called precisely when the scene begins.  In contrast, the
        constructor (__init__) may be called to construct a scene, but the game
        itself may not be start until some time after.
        '''
        raise NotImplementedError('Scene.start')

    def stop(self):
        '''
        Stops this scene.

        stop is called when the scene is over.  If this scene requires any
        cleanup, it should be done here.
        '''
        raise NotImplementedError('Scene.stop')

    def update(self):
        '''
        Updates this scene.

        update is called on every game tick in main and should handle all user
        input for that tick as well as update the scene's own model.
        '''
        raise NotImplementedError('Scene.update')

    def render(self, surface):
        '''
        Renders this scene to the given surface.

        render is called on every game tick in main and should handle all
        rendering of this scene to the given surface.
        '''
        raise NotImplementedError('Scene.render')
