from app.GameGUI import GameGUI
import pygame
from app.Constants import *

game = GameGUI()

while game.running:
    game.curr_menu.display_menu()
    game.game_loop()
