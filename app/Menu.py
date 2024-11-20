import pygame
from app.Constants import *
import app.Constants as Constants
import sys


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_size = self.game.SIZE/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -150
        self.title_size = 45
        self.option_size = 20
        self.press_sound = pygame.mixer.Sound('sounds/button.mp3')

    def play_sound(self,sound):
        pygame.mixer.Sound.play(sound)
    
    def draw_cursor(self):
        self.game.draw_text(
            '&', size=20,
            x=self.cursor_rect.x, y=self.cursor_rect.y,
            color=MENU_COLOR
        )

    def blit_menu(self):
        self.game.window.blit(self.game.display1, (350, 0))
        # self.game.window.blit(self.game.display2, (700, 0))
        pygame.display.update()
        self.game.reset_keys()

    # def get_game_size(self):
    #     return self.game.SIZE


class MainMenu(Menu): 
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = '1 Player'

        self.cursoronePlayer = MENU_COLOR
        self.cursortwoPlayer = WHITE
        self.cursorQuit = WHITE

        self.onePlayerx, self.onePlayery = self.mid_size, self.mid_size - 50
        self.twoPlayerx, self.twoPlayery = self.mid_size, self.mid_size + 0
        self.Quitx, self.Quity = self.mid_size, self.mid_size + 50
        self.huyhoangx, self.huyhoangy = self.mid_size, self.mid_size + 150
        self.tintranx, self.tintrany = self.mid_size, self.mid_size + 200
        self.nhatanx, self.nhatany = self.mid_size, self.mid_size + 250
        
        self.cursor_rect.midtop = (self.onePlayerx + self.offset, self.onePlayery)
        
    def  change_cursor_color(self):
        self.clear_cursor_color()
        if self.state == '1 Player':
            self.cursoronePlayer = MENU_COLOR
        elif self.state == '2 Player':
            self.cursortwoPlayer = MENU_COLOR
        elif self.state == 'QUIT':
            self.cursorQuit = MENU_COLOR
            
    def clear_cursor_color(self):
        self.cursoronePlayer = WHITE
        self.cursortwoPlayer = WHITE
        self.cursorQuit = WHITE
    
    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.game.event_handler()
            self.check_input()

            self.game.display1.fill(WINDOW_COLOR)

            self.game.draw_text(
                'SNAKE EATS BANANAS', size=self.title_size,
                x=self.game.SIZE/2, y=self.game.SIZE/2 - 2*(CELL_SIZE + NO_OF_CELLS),
                color=TITLE_COLOR,
            )

            self.game.draw_text(
                '1 Player', size=self.option_size,
                x=self.onePlayerx,  y=self.onePlayery,
                color=self.cursoronePlayer
            )
            self.game.draw_text(
                '2 Player', size=self.option_size,
                x=self.twoPlayerx,  y=self.twoPlayery,
                color=self.cursortwoPlayer
            )
            
            self.game.draw_text(
                'Quit', size=self.option_size,
                x=self.Quitx,  y=self.Quity,
                color=self.cursorQuit
            )
            
            self.game.draw_text(
                '22110028  -  Nguyen Mai Huy Hoang', size=self.option_size,
                x=self.huyhoangx,  y=self.huyhoangy,
                color=SNAKE_COLOR
            )
            
            self.game.draw_text(
                '22110076  -  Tran Trung Tin', size=self.option_size,
                x=self.tintranx,  y=self.tintrany,
                color=SNAKE_COLOR
            )
                        
            self.game.draw_text(
                '22110007  -  Nguyen Nhat An', size=self.option_size,
                x=self.nhatanx,  y=self.nhatany,
                color=SNAKE_COLOR
            )

            self.draw_cursor()
            self.change_cursor_color()
            self.blit_menu()
    
    def check_input(self):
        self.move_cursor()
        if self.game.START:
            self.play_sound(self.press_sound)
            if self.state == '1 Player':
                Constants.twoPlayerOpt = False
                self.game.curr_menu = self.game.OnePlayerMenu
            elif self.state == '2 Player':
                Constants.twoPlayerOpt = True
                self.game.curr_menu = self.game.TwoPlayerMenu_P1
            elif self.state == 'QUIT':
                pygame.quit()
                sys.exit()
                
            self.run_display = False
            
    def move_cursor(self):
            if self.game.DOWNKEY:
                if self.state == '1 Player':
                    self.cursor_rect.midtop = (
                        self.twoPlayerx + self.offset, self.twoPlayery)
                    self.state = '2 Player'

                elif self.state == '2 Player':
                    self.cursor_rect.midtop = (
                        self.Quitx + self.offset, self.Quity)
                    self.state = 'QUIT'
                    
                elif self.state == 'QUIT':
                    self.cursor_rect.midtop = (
                        self.onePlayerx + self.offset, self.onePlayery)
                    self.state = '1 Player' 
                

                
            if self.game.UPKEY:
                if self.state == '1 Player':
                    self.cursor_rect.midtop = (
                        self.Quity + self.offset, self.Quity)
                    self.state = 'QUIT'

                elif self.state == '2 Player':
                    self.cursor_rect.midtop = (
                        self.onePlayerx + self.offset, self.onePlayery)
                    self.state = '1 Player'
                
                elif self.state == 'QUIT':
                    self.cursor_rect.midtop = (
                        self.twoPlayerx + self.offset, self.twoPlayery)
                    self.state = '2 Player'

class onePlayerMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'DFS'

        self.cursorBFS = MENU_COLOR
        self.cursorDFS = WHITE
        self.cursorUCS = WHITE
        self.cursorGREEDY = WHITE
        self.cursorASTAR = WHITE
        self.cursorHILLCLIMBING = WHITE
        self.cursorBEAM = WHITE
        self.cursorHuman = WHITE
        self.cursorQuit = WHITE

        self.BFSx, self.BFSy = self.mid_size, self.mid_size - 200
        self.DFSx, self.DFSy = self.mid_size, self.mid_size - 150
        self.UCSx, self.UCSy = self.mid_size, self.mid_size - 100
        self.GREEDYx, self.GREEDYy = self.mid_size, self.mid_size - 50
        self.ASTARx, self.ASTARy = self.mid_size, self.mid_size + 0
        self.HILLCLIMBINGx, self.HILLCLIMBINGy = self.mid_size, self.mid_size + 50
        self.BEAMx, self.BEAMy = self.mid_size, self.mid_size + 100
        self.Humanx, self.Humany = self.mid_size, self.mid_size + 150
        self.Quitx, self.Quity = self.mid_size, self.mid_size + 200

        self.cursor_rect.midtop = (self.DFSx + self.offset, self.DFSy)

    def change_cursor_color(self):
        self.clear_cursor_color()
        if self.state == 'DFS':
            self.cursorDFS = MENU_COLOR
        elif self.state == 'BFS':
            self.cursorBFS = MENU_COLOR
        elif self.state == 'UCS':
            self.cursorUCS = MENU_COLOR
        elif self.state == 'GREEDY':
            self.cursorGREEDY = MENU_COLOR
        elif self.state == 'ASTAR':
            self.cursorASTAR = MENU_COLOR
        elif self.state == 'HILLCLIMBING':
            self.cursorHILLCLIMBING = MENU_COLOR
        elif self.state == 'BEAM':
            self.cursorBEAM = MENU_COLOR
        elif self.state == 'HUMAN':
            self.cursorHuman = MENU_COLOR
        elif self.state == 'QUIT':
            self.cursorQuit = MENU_COLOR

    def clear_cursor_color(self):
        self.cursorDFS = WHITE
        self.cursorBFS = WHITE
        self.cursorDFS = WHITE
        self.cursorUCS = WHITE
        self.cursorGREEDY = WHITE
        self.cursorASTAR = WHITE
        self.cursorHILLCLIMBING = WHITE
        self.cursorBEAM = WHITE
        self.cursorHuman = WHITE
        self.cursorQuit = WHITE

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            
            self.game.event_handler()
            self.check_input()

            self.game.display1.fill(WINDOW_COLOR)

            self.game.draw_text(
                'Ai Snake Game', size=self.title_size,
                x=self.game.SIZE/2, y=self.game.SIZE/2 - 250,
                color=TITLE_COLOR
            )

            self.game.draw_text(
                'DFS', size=self.option_size,
                x=self.DFSx,  y=self.DFSy,
                color=self.cursorDFS
            )
            self.game.draw_text(
                'BFS', size=self.option_size,
                x=self.BFSx,  y=self.BFSy,
                color=self.cursorBFS
            )
            self.game.draw_text(
                'DFS', size=self.option_size,
                x=self.DFSx,  y=self.DFSy,
                color=self.cursorDFS
            )
            
            self.game.draw_text(
                'UCS', size=self.option_size,
                x=self.UCSx,  y=self.UCSy,
                color=self.cursorUCS
            )
            
            self.game.draw_text(
                'GREEDY', size=self.option_size,
                x=self.GREEDYx,  y=self.GREEDYy,
                color=self.cursorGREEDY
            )

            self.game.draw_text(
                'AStar', size=self.option_size,
                x=self.ASTARx,  y=self.ASTARy,
                color=self.cursorASTAR
            )
            
            self.game.draw_text(
                'Hill Climbing', size=self.option_size,
                x=self.HILLCLIMBINGx,  y=self.HILLCLIMBINGy,
                color=self.cursorHILLCLIMBING
            )
            
            self.game.draw_text(
                'Beam Search', size=self.option_size,
                x=self.BEAMx,  y=self.BEAMy,
                color=self.cursorBEAM
            )
            
            self.game.draw_text(
                'Human', size=self.option_size,
                x=self.Humanx,  y=self.Humany,
                color=self.cursorHuman
            )
            
            self.game.draw_text(
                'Back to Main Menu', size=self.option_size,
                x=self.Quitx,  y=self.Quity,
                color=self.cursorQuit
            )

            self.draw_cursor()
            self.change_cursor_color()
            self.blit_menu()

    def check_input(self):
        self.move_cursor()

        if self.game.START:
            self.play_sound(self.press_sound)
            if self.state == 'QUIT':
                self.game.curr_menu = self.game.main_menu
            else:
                self.game.playing = True
            self.run_display = False

    def move_cursor(self):
        if self.game.DOWNKEY:
            if self.state == 'BFS':
                self.cursor_rect.midtop = (
                    self.DFSx + self.offset, self.DFSy)
                self.state = 'DFS'

            elif self.state == 'DFS':
                self.cursor_rect.midtop = (
                    self.UCSx + self.offset, self.UCSy)
                self.state = 'UCS'
                
            elif self.state == 'UCS':
                self.cursor_rect.midtop = (
                    self.GREEDYx + self.offset, self.GREEDYy)
                self.state = 'GREEDY'
                
            elif self.state == 'GREEDY':
                self.cursor_rect.midtop = (
                    self.ASTARx + self.offset, self.ASTARy)
                self.state = 'ASTAR'

            elif self.state == 'ASTAR':
                self.cursor_rect.midtop = (
                    self.HILLCLIMBINGx + self.offset, self.HILLCLIMBINGy)
                self.state = 'HILLCLIMBING'
                
            elif self.state == 'HILLCLIMBING':
                self.cursor_rect.midtop = (
                    self.BEAMx + self.offset, self.BEAMy)
                self.state = 'BEAM'

            elif self.state == 'BEAM':
                self.cursor_rect.midtop = (
                    self.Humanx + self.offset, self.Humany)
                self.state = 'HUMAN'
                
            elif self.state == 'HUMAN':
                self.cursor_rect.midtop = (
                    self.Quitx + self.offset, self.Quity)
                self.state = 'QUIT'
                
            elif self.state == 'QUIT':
                self.cursor_rect.midtop = (
                    self.BFSx + self.offset, self.BFSy)
                self.state = 'BFS'

        if self.game.UPKEY:
            if self.state == 'BFS':
                self.cursor_rect.midtop = (
                    self.Quitx + self.offset, self.Quity)
                self.state = 'QUIT'

            elif self.state == 'DFS':
                self.cursor_rect.midtop = (
                    self.BFSx + self.offset, self.BFSy)
                self.state = 'BFS'
                
            elif self.state == 'UCS':
                self.cursor_rect.midtop = (
                    self.DFSx + self.offset, self.DFSy)
                self.state = 'DFS'

            elif self.state == 'GREEDY':
                self.cursor_rect.midtop = (
                    self.UCSx + self.offset, self.UCSy)
                self.state = 'UCS'

            elif self.state == 'ASTAR':
                self.cursor_rect.midtop = (
                    self.GREEDYx + self.offset, self.GREEDYy)
                self.state = 'GREEDY'

            elif self.state == 'HILLCLIMBING':
                self.cursor_rect.midtop = (
                    self.ASTARx + self.offset, self.ASTARy)
                self.state = 'ASTAR'

            elif self.state == 'BEAM':
                self.cursor_rect.midtop = (
                    self.HILLCLIMBINGx + self.offset, self.HILLCLIMBINGy)
                self.state = 'HILLCLIMBING'

            elif self.state == 'HUMAN':
                self.cursor_rect.midtop = (
                    self.BEAMx + self.offset, self.BEAMy)
                self.state = 'BEAM'
            
            elif self.state == 'QUIT':
                self.cursor_rect.midtop = (
                    self.Humanx + self.offset, self.Humany)
                self.state = 'HUMAN'

class twoPlayerMenu_P1(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'BFS'

        self.cursorBFS = MENU_COLOR
        self.cursorDFS = WHITE
        self.cursorUCS = WHITE
        self.cursorGREEDY = WHITE
        self.cursorASTAR = WHITE
        self.cursorHILLCLIMBING = WHITE
        self.cursorBEAM = WHITE
        self.cursorHuman = WHITE
        self.cursorQuit = WHITE

        self.titlex, self.titley = self.mid_size, self.mid_size - 200
        self.BFSx, self.BFSy = self.mid_size, self.mid_size - 150
        self.DFSx, self.DFSy = self.mid_size, self.mid_size - 100
        self.UCSx, self.UCSy = self.mid_size, self.mid_size - 50
        self.GREEDYx, self.GREEDYy = self.mid_size, self.mid_size + 0
        self.ASTARx, self.ASTARy = self.mid_size, self.mid_size + 50
        self.HILLCLIMBINGx, self.HILLCLIMBINGy = self.mid_size, self.mid_size + 100
        self.BEAMx, self.BEAMy = self.mid_size, self.mid_size + 150
        self.Humanx, self.Humany = self.mid_size, self.mid_size + 200
        self.Quitx, self.Quity = self.mid_size, self.mid_size + 250

        self.cursor_rect.midtop = (self.BFSx + self.offset, self.BFSy)

    def change_cursor_color(self):
        self.clear_cursor_color()
        if self.state == 'DFS':
            self.cursorDFS = MENU_COLOR
        elif self.state == 'BFS':
            self.cursorBFS = MENU_COLOR
        elif self.state == 'DFS':
            self.cursorDFS = MENU_COLOR
        elif self.state == 'UCS':
            self.cursorUCS = MENU_COLOR
        elif self.state == 'GREEDY':
            self.cursorGREEDY = MENU_COLOR
        elif self.state == 'ASTAR':
            self.cursorASTAR = MENU_COLOR
        elif self.state == 'HILLCLIMBING':
            self.cursorHILLCLIMBING = MENU_COLOR
        elif self.state == 'BEAM':
            self.cursorBEAM = MENU_COLOR
        elif self.state == 'HUMAN':
            self.cursorHuman = MENU_COLOR
        elif self.state == 'QUIT':
            self.cursorQuit = MENU_COLOR

    def clear_cursor_color(self):
        self.cursorDFS = WHITE
        self.cursorBFS = WHITE
        self.cursorDFS = WHITE
        self.cursorUCS = WHITE
        self.cursorGREEDY = WHITE
        self.cursorASTAR = WHITE
        self.cursorHILLCLIMBING = WHITE
        self.cursorBEAM = WHITE
        self.cursorHuman = WHITE
        self.cursorQuit = WHITE

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.game.event_handler()
            self.check_input()

            self.game.display1.fill(WINDOW_COLOR)

            self.game.draw_text(
                'Ai Snake Game', size=self.title_size,
                x=self.game.SIZE/2, y=self.game.SIZE/2 - 2*(CELL_SIZE + NO_OF_CELLS) - 150,
                color=TITLE_COLOR
            )
            
            self.game.draw_text(
                'Choose Player 1 options: ', size=self.option_size,
                x=self.titlex,  y=self.titley,
                color=MENU_COLOR
            )

            self.game.draw_text(
                'DFS', size=self.option_size,
                x=self.DFSx,  y=self.DFSy,
                color=self.cursorDFS
            )
            
            self.game.draw_text(
                'BFS', size=self.option_size,
                x=self.BFSx,  y=self.BFSy,
                color=self.cursorBFS
            )
            
            self.game.draw_text(
                'UCS', size=self.option_size,
                x=self.UCSx,  y=self.UCSy,
                color=self.cursorUCS
            )
            
            self.game.draw_text(
                'GREEDY', size=self.option_size,
                x=self.GREEDYx,  y=self.GREEDYy,
                color=self.cursorGREEDY
            )

            self.game.draw_text(
                'AStar', size=self.option_size,
                x=self.ASTARx,  y=self.ASTARy,
                color=self.cursorASTAR
            )
            
            self.game.draw_text(
                'Hill Climbing', size=self.option_size,
                x=self.HILLCLIMBINGx,  y=self.HILLCLIMBINGy,
                color=self.cursorHILLCLIMBING
            )
            
            self.game.draw_text(
                'Beam Search', size=self.option_size,
                x=self.BEAMx,  y=self.BEAMy,
                color=self.cursorBEAM
            )
            
            self.game.draw_text(
                'Human', size=self.option_size,
                x=self.Humanx,  y=self.Humany,
                color=self.cursorHuman
            )
            
            self.game.draw_text(
                'Back to Main Menu', size=self.option_size,
                x=self.Quitx,  y=self.Quity,
                color=self.cursorQuit
            )

            self.draw_cursor()
            self.change_cursor_color()
            self.blit_menu()

    def check_input(self):
        self.move_cursor()

        if self.game.START:
            self.play_sound(self.press_sound)
            if self.state == 'QUIT':
                self.game.curr_menu = self.game.main_menu
            else:
                self.game.curr_menu = self.game.TwoPlayerMenu_P2
            self.run_display = False

    def move_cursor(self):
        if self.game.DOWNKEY:
            if self.state == 'BFS':
                self.cursor_rect.midtop = (
                    self.DFSx + self.offset, self.DFSy)
                self.state = 'DFS'

            elif self.state == 'DFS':
                self.cursor_rect.midtop = (
                    self.UCSx + self.offset, self.UCSy)
                self.state = 'UCS'
                
            elif self.state == 'UCS':
                self.cursor_rect.midtop = (
                    self.GREEDYx + self.offset, self.GREEDYy)
                self.state = 'GREEDY'
                
            elif self.state == 'GREEDY':
                self.cursor_rect.midtop = (
                    self.ASTARx + self.offset, self.ASTARy)
                self.state = 'ASTAR'

            elif self.state == 'ASTAR':
                self.cursor_rect.midtop = (
                    self.HILLCLIMBINGx + self.offset, self.HILLCLIMBINGy)
                self.state = 'HILLCLIMBING'
                
            elif self.state == 'HILLCLIMBING':
                self.cursor_rect.midtop = (
                    self.BEAMx + self.offset, self.BEAMy)
                self.state = 'BEAM'

            elif self.state == 'BEAM':
                self.cursor_rect.midtop = (
                    self.Humanx + self.offset, self.Humany)
                self.state = 'HUMAN'
                
            elif self.state == 'HUMAN':
                self.cursor_rect.midtop = (
                    self.Quitx + self.offset, self.Quity)
                self.state = 'QUIT'
                
            elif self.state == 'QUIT':
                self.cursor_rect.midtop = (
                    self.BFSx + self.offset, self.BFSy)
                self.state = 'BFS'

        if self.game.UPKEY:
            if self.state == 'BFS':
                self.cursor_rect.midtop = (
                    self.Quitx + self.offset, self.Quity)
                self.state = 'QUIT'

            elif self.state == 'DFS':
                self.cursor_rect.midtop = (
                    self.BFSx + self.offset, self.BFSy)
                self.state = 'BFS'
                
            elif self.state == 'UCS':
                self.cursor_rect.midtop = (
                    self.DFSx + self.offset, self.DFSy)
                self.state = 'DFS'

            elif self.state == 'GREEDY':
                self.cursor_rect.midtop = (
                    self.UCSx + self.offset, self.UCSy)
                self.state = 'UCS'

            elif self.state == 'ASTAR':
                self.cursor_rect.midtop = (
                    self.GREEDYx + self.offset, self.GREEDYy)
                self.state = 'GREEDY'

            elif self.state == 'HILLCLIMBING':
                self.cursor_rect.midtop = (
                    self.ASTARx + self.offset, self.ASTARy)
                self.state = 'ASTAR'

            elif self.state == 'BEAM':
                self.cursor_rect.midtop = (
                    self.HILLCLIMBINGx + self.offset, self.HILLCLIMBINGy)
                self.state = 'HILLCLIMBING'

            elif self.state == 'HUMAN':
                self.cursor_rect.midtop = (
                    self.BEAMx + self.offset, self.BEAMy)
                self.state = 'BEAM'
            
            elif self.state == 'QUIT':
                self.cursor_rect.midtop = (
                    self.Humanx + self.offset, self.Humany)
                self.state = 'HUMAN'

class twoPlayerMenu_P2(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'BFS'

        self.cursorBFS = MENU_COLOR
        self.cursorDFS = WHITE
        self.cursorUCS = WHITE
        self.cursorGREEDY = WHITE
        self.cursorASTAR = WHITE
        self.cursorHILLCLIMBING = WHITE
        self.cursorBEAM = WHITE
        self.cursorQuit = WHITE

        self.titlex, self.titley = self.mid_size, self.mid_size - 200
        self.BFSx, self.BFSy = self.mid_size, self.mid_size - 150
        self.DFSx, self.DFSy = self.mid_size, self.mid_size - 100
        self.UCSx, self.UCSy = self.mid_size, self.mid_size - 50
        self.GREEDYx, self.GREEDYy = self.mid_size, self.mid_size + 0
        self.ASTARx, self.ASTARy = self.mid_size, self.mid_size + 50
        self.HILLCLIMBINGx, self.HILLCLIMBINGy = self.mid_size, self.mid_size + 100
        self.BEAMx, self.BEAMy = self.mid_size, self.mid_size + 150
        self.Quitx, self.Quity = self.mid_size, self.mid_size + 200

        self.cursor_rect.midtop = (self.BFSx + self.offset, self.BFSy)

    def change_cursor_color(self):
        self.clear_cursor_color()
        if self.state == 'DFS':
            self.cursorDFS = MENU_COLOR
        elif self.state == 'BFS':
            self.cursorBFS = MENU_COLOR
        elif self.state == 'DFS':
            self.cursorDFS = MENU_COLOR
        elif self.state == 'UCS':
            self.cursorUCS = MENU_COLOR
        elif self.state == 'GREEDY':
            self.cursorGREEDY = MENU_COLOR
        elif self.state == 'ASTAR':
            self.cursorASTAR = MENU_COLOR
        elif self.state == 'HILLCLIMBING':
            self.cursorHILLCLIMBING = MENU_COLOR
        elif self.state == 'BEAM':
            self.cursorBEAM = MENU_COLOR
        elif self.state == 'QUIT':
            self.cursorQuit = MENU_COLOR

    def clear_cursor_color(self):
        self.cursorDFS = WHITE
        self.cursorBFS = WHITE
        self.cursorDFS = WHITE
        self.cursorUCS = WHITE
        self.cursorGREEDY = WHITE
        self.cursorASTAR = WHITE
        self.cursorHILLCLIMBING = WHITE
        self.cursorBEAM = WHITE
        self.cursorQuit = WHITE

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.game.event_handler()
            self.check_input()

            self.game.display1.fill(WINDOW_COLOR)

            self.game.draw_text(
                'Ai Snake Game', size=self.title_size,
                x=self.game.SIZE/2, y=self.game.SIZE/2 - 2*(CELL_SIZE + NO_OF_CELLS) - 150,
                color=TITLE_COLOR
            )
            
            self.game.draw_text(
                'Choose Player 2 options: ', size=self.option_size,
                x=self.titlex,  y=self.titley,
                color=MENU_COLOR
            )

            self.game.draw_text(
                'DFS', size=self.option_size,
                x=self.DFSx,  y=self.DFSy,
                color=self.cursorDFS
            )
            
            self.game.draw_text(
                'BFS', size=self.option_size,
                x=self.BFSx,  y=self.BFSy,
                color=self.cursorBFS
            )
            
            self.game.draw_text(
                'UCS', size=self.option_size,
                x=self.UCSx,  y=self.UCSy,
                color=self.cursorUCS
            )
            
            self.game.draw_text(
                'GREEDY', size=self.option_size,
                x=self.GREEDYx,  y=self.GREEDYy,
                color=self.cursorGREEDY
            )

            self.game.draw_text(
                'AStar', size=self.option_size,
                x=self.ASTARx,  y=self.ASTARy,
                color=self.cursorASTAR
            )
            
            self.game.draw_text(
                'Hill Climbing', size=self.option_size,
                x=self.HILLCLIMBINGx,  y=self.HILLCLIMBINGy,
                color=self.cursorHILLCLIMBING
            )
            
            self.game.draw_text(
                'Beam Search', size=self.option_size,
                x=self.BEAMx,  y=self.BEAMy,
                color=self.cursorBEAM
            )
            
            self.game.draw_text(
                'Back to Player 1 Menu', size=self.option_size,
                x=self.Quitx,  y=self.Quity,
                color=self.cursorQuit
            )

            self.draw_cursor()
            self.change_cursor_color()
            self.blit_menu()

    def check_input(self):
        self.move_cursor()

        if self.game.START:
            self.play_sound(self.press_sound)
            if self.state == 'QUIT':
                self.game.curr_menu = self.game.TwoPlayerMenu_P1
            else:
                self.game.playing = True
            self.run_display = False

    def move_cursor(self):
        if self.game.DOWNKEY:
            if self.state == 'BFS':
                self.cursor_rect.midtop = (
                    self.DFSx + self.offset, self.DFSy)
                self.state = 'DFS'

            elif self.state == 'DFS':
                self.cursor_rect.midtop = (
                    self.UCSx + self.offset, self.UCSy)
                self.state = 'UCS'
                
            elif self.state == 'UCS':
                self.cursor_rect.midtop = (
                    self.GREEDYx + self.offset, self.GREEDYy)
                self.state = 'GREEDY'
                
            elif self.state == 'GREEDY':
                self.cursor_rect.midtop = (
                    self.ASTARx + self.offset, self.ASTARy)
                self.state = 'ASTAR'

            elif self.state == 'ASTAR':
                self.cursor_rect.midtop = (
                    self.HILLCLIMBINGx + self.offset, self.HILLCLIMBINGy)
                self.state = 'HILLCLIMBING'
                
            elif self.state == 'HILLCLIMBING':
                self.cursor_rect.midtop = (
                    self.BEAMx + self.offset, self.BEAMy)
                self.state = 'BEAM'
                
            elif self.state == 'BEAM':
                self.cursor_rect.midtop = (
                    self.Quitx + self.offset, self.Quity)
                self.state = 'QUIT'
                
            elif self.state == 'QUIT':
                self.cursor_rect.midtop = (
                    self.BFSx + self.offset, self.BFSy)
                self.state = 'BFS'

        if self.game.UPKEY:
            if self.state == 'BFS':
                self.cursor_rect.midtop = (
                    self.Quitx + self.offset, self.Quity)
                self.state = 'QUIT'

            elif self.state == 'DFS':
                self.cursor_rect.midtop = (
                    self.BFSx + self.offset, self.BFSy)
                self.state = 'BFS'
                
            elif self.state == 'UCS':
                self.cursor_rect.midtop = (
                    self.DFSx + self.offset, self.DFSy)
                self.state = 'DFS'

            elif self.state == 'GREEDY':
                self.cursor_rect.midtop = (
                    self.UCSx + self.offset, self.UCSy)
                self.state = 'UCS'

            elif self.state == 'ASTAR':
                self.cursor_rect.midtop = (
                    self.GREEDYx + self.offset, self.GREEDYy)
                self.state = 'GREEDY'

            elif self.state == 'HILLCLIMBING':
                self.cursor_rect.midtop = (
                    self.ASTARx + self.offset, self.ASTARy)
                self.state = 'ASTAR'

            elif self.state == 'BEAM':
                self.cursor_rect.midtop = (
                    self.HILLCLIMBINGx + self.offset, self.HILLCLIMBINGy)
                self.state = 'HILLCLIMBING'

            elif self.state == 'QUIT':
                self.cursor_rect.midtop = (
                    self.BEAMx + self.offset, self.BEAMy)
                self.state = 'BEAM'



class button():
    def __init__(self, x, y, text, game):
        self.x = x
        self.y = y
        self.text = text
        self.game = game
        self.font = pygame.font.Font(game.font_name, 30)
        self.clicked = False

    def draw_button(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = pygame.Rect(self.x, self.y, BTN_WIDTH, BTN_HEIGHT)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                pygame.draw.rect(self.game.display, BTN_CLICKED, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
                action = True
            else:
                pygame.draw.rect(self.game.display, BTN_HOVER, button_rect)
        else:
            pygame.draw.rect(self.game.display, BTN_COLOR, button_rect)

        # add text to button
        text_img = self.font.render(self.text, True, WHITE)
        text_len = text_img.get_width()
        self.game.display.blit(text_img, (self.x + int(BTN_WIDTH / 2) -
                                          int(text_len / 2), self.y + 25))

        return action


class TextBox:
    def __init__(self, x, y, game):
        self.font = pygame.font.Font(game.font_name, 20)
        self.input_rect = pygame.Rect(x, y, TXT_WIDTH, TXT_HEIGHT)
        self.input = ''
        self.game = game
        self.active = False

    def draw_input(self):
        # get mouse position
        pos = pygame.mouse.get_pos()

        if self.input_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.active = True

        elif pygame.mouse.get_pressed()[0] == 1:
            self.active = False

        if self.active:
            color = TXT_ACTIVE
        else:
            color = TXT_PASSIVE

        pygame.draw.rect(self.game.display, color, self.input_rect, 2)
        text_surface = self.font.render(self.input, False, WHITE)
        self.game.display.blit(
            text_surface, (self.input_rect.x + 15, self.input_rect.y + 1))
