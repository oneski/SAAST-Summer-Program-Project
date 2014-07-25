from chooser import Chooser
from engine import Engine
from locals import *

def _opt_Start_Game(menu):
    ''' Callback for the "Start Game" menu option '''
    games = [game for game,enabled in menu.game.microgames if enabled]
    if len(games) > 0:
        menu.game.change(Engine(menu.game, LIVES, games, menu))

def _opt_Tour(menu):
    ''' Callback for the "Tour" menu option '''
    games = [game for game,enabled in menu.game.microgames if enabled]
    menu.game.change(
        Engine(menu.game, 50, games, menu, False))

def _opt_Microgames(menu):
    menu.game.change(
        Chooser(menu.game, menu.game.microgames, menu))

def _opt_Quit(menu):
    ''' Callback for the "Quit" menu option '''
    menu.game.finished = True

def options():
    return [ ('Start Game', _opt_Start_Game)
           , ('Tour', _opt_Tour)
           , ('Microgames', _opt_Microgames)
           , ('Quit', _opt_Quit) ]
