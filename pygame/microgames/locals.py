import pygame

# True if the game should failfast when it encounters a bad module.
FAILFAST = False

# The width of the screen
WIDTH = 1024

# The height of the screen
HEIGHT = 768

# The (fixed) frame rate of the game
FPS = 30

# The number of lives the player has
LIVES = 2

# The time in-between games
WAIT_PERIOD = 2

# The game-wide font to use
GAME_FONT_FILENAME = 'FrancoisOne.ttf'

# Common color constants
C_BLACK = pygame.Color(0, 0, 0)
C_WHITE = pygame.Color(255, 255, 255)
C_GOLD  = pygame.Color(255, 215, 0)

def load_image(name, x, y):
    """
    Loads an image file, returning the surface and rectangle corresponding to
    that image at the given location
    """
    try:
        image = pygame.image.load(name)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, msg:
        print 'Cannot load image: {}'.format(name)
        raise SystemExit, msg
    rect = image.get_rect().move(x, y)
    return image, rect
