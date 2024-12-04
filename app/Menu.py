import pygame
import os
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
        self.option_size = 22
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
        self.game.window.blit(self.game.background_left_blank, (0,0))
        self.game.window.blit(self.game.display1, (200, 0))
        # self.game.window.blit(self.game.display2, (700, 0))
        pygame.display.update()
        self.game.reset_keys()

    # def get_game_size(self):
    #     return self.game.SIZE


class button():
    def __init__(self, x, y, text, game):
        self.x = x
        self.y = y
        self.text = text
        self.game = game
        self.font = pygame.font.Font(game.font_name, 22)
        self.clicked = False

    def draw_button(self,display):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()
        # Calculate position within the surface
        # position of the surface display1 is (200, 0)
        display1_x = 200
        display1_y = 0
        surface_mouse_pos = (
            pos[0] - display1_x,
            pos[1] - display1_y
        )
        

        # create pygame Rect object for the button
        button_rect = pygame.Rect(self.x, self.y, BTN_WIDTH, BTN_HEIGHT)


        # check mouseover and clicked conditions
        text_color = BTN_COLOR_TEXT_COLOR  # Màu chữ khi hover
        if button_rect.collidepoint(surface_mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                # pygame.draw.rect(display, BTN_CLICKED, button_rect)
                text_color = BTN_CLICKED_TEXT_COLOR  # Màu chữ khi click
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
                action = True
            else:
                # pygame.draw.rect(display, BTN_HOVER, button_rect)
                text_color = BTN_HOVER_TEXT_COLOR  # Màu chữ khi hover
        else:
            # pygame.draw.rect(display, BTN_COLOR, button_rect)
            pass

        # add text to button
        text_img = self.font.render(self.text, True, text_color)
        text_len = text_img.get_width()
        display.blit(text_img, (self.x + int(BTN_WIDTH / 2) -
                                          int(text_len / 2), self.y + 25))

        return action

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

        # self.controller = controller
        self.onePlayer = button(
            self.mid_size - 100, self.mid_size - 100, '1 Player', game)
        self.twoPlayer = button(
            self.mid_size - 100, self.mid_size + -40, '2 Player', game)
        self.Quit = button(
            self.mid_size - 100, self.mid_size + 20, 'Quit', game)
        
        self.huyhoangx, self.huyhoangy = self.mid_size, self.mid_size + 150
        self.tintranx, self.tintrany = self.mid_size, self.mid_size + 200
        self.nhatanx, self.nhatany = self.mid_size, self.mid_size + 250
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running, self.game.playing = False, False
                    self.game.curr_menu.run_display = False
                    sys.exit()
                    
            self.game.display1.fill(WINDOW_COLOR)
            if self.onePlayer.draw_button(self.game.display1):
                self.play_sound(self.press_sound)
                Constants.twoPlayerOpt = False
                self.game.curr_menu = self.game.OnePlayerMenu
                self.run_display = False
                
            if self.twoPlayer.draw_button(self.game.display1):
                self.play_sound(self.press_sound)
                Constants.twoPlayerOpt = True
                self.game.curr_menu = self.game.TwoPlayerMenu_P1
                self.run_display = False
            
            if self.Quit.draw_button(self.game.display1):
                self.play_sound(self.press_sound)
                self.game.running, self.game.playing = False, False
                self.game.curr_menu.run_display = False
                sys.exit()
                
            self.game.draw_text(
                'SNAKE EATS BANANAS', size=self.title_size,
                x=self.game.SIZE/2, y=self.game.SIZE/2 - 2*(CELL_SIZE + NO_OF_CELLS)-50,
                color=TITLE_COLOR,
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
            
            
            self.blit_menu()
        self.reset()
        
    def reset(self):
        pass
                
class onePlayerMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'DFS'
        
        self.BFS = button(
            self.mid_size - 100, self.mid_size - 200, 'BFS', game)
        self.DFS = button(
            self.mid_size - 100, self.mid_size + -150, 'DFS', game)
        self.UCS = button(
            self.mid_size - 100, self.mid_size + -100, 'UCS', game)
        self.GREEDY = button(
            self.mid_size - 100, self.mid_size - 50, 'Greedy', game)
        self.ASTAR = button(
            self.mid_size - 100, self.mid_size + 0, 'A Star', game)
        self.HILLCLIMBING = button(
            self.mid_size - 100, self.mid_size + 50, 'Hill Climbing', game)
        self.BEAM = button(
            self.mid_size - 100, self.mid_size + 100, 'Beam search', game)
        self.Human = button(
            self.mid_size - 100, self.mid_size + 150, 'Human', game)
        self.Quit = button(
            self.mid_size - 100, self.mid_size + 200, 'Go Back to Main Menu', game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:

            self.game.display1.fill(WINDOW_COLOR)

            if self.BFS.draw_button(self.game.display1):
                self.state = 'BFS'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.playing = True
                
            if self.DFS.draw_button(self.game.display1):
                self.state = 'DFS'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.playing = True
            if self.UCS.draw_button(self.game.display1):
                self.state = 'UCS'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.playing = True
            if self.GREEDY.draw_button(self.game.display1):
                self.state = 'GREEDY'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.playing = True
            if self.ASTAR.draw_button(self.game.display1):
                self.state = 'ASTAR'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.playing = True
            if self.HILLCLIMBING.draw_button(self.game.display1):
                self.state = 'HILLCLIMBING'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.playing = True
            if self.BEAM.draw_button(self.game.display1):
                self.state = 'BEAM'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.playing = True
            if self.Human.draw_button(self.game.display1):
                self.state = 'HUMAN'    
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.playing = True   
            
            if self.Quit.draw_button(self.game.display1):
                self.play_sound(self.press_sound)
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

            self.game.event_handler()
            
            self.game.draw_text(
                'SNAKE EATS BANANAS', size=self.title_size,
                x=self.game.SIZE/2, y=self.game.SIZE/2 - 250,
                color=TITLE_COLOR
            )

            self.draw_cursor()
            self.blit_menu()

class twoPlayerMenu_P1(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'BFS'
        
        self.titlex, self.titley = self.mid_size, self.mid_size - 200
        self.BFS = button(
            self.mid_size - 100, self.mid_size - 200, 'BFS', game)
        self.DFS = button(
            self.mid_size - 100, self.mid_size + -150, 'DFS', game)
        self.UCS = button(
            self.mid_size - 100, self.mid_size + -100, 'UCS', game)
        self.GREEDY = button(
            self.mid_size - 100, self.mid_size - 50, 'Greedy', game)
        self.ASTAR = button(
            self.mid_size - 100, self.mid_size + 0, 'A Star', game)
        self.HILLCLIMBING = button(
            self.mid_size - 100, self.mid_size + 50, 'Hill Climbing', game)
        self.BEAM = button(
            self.mid_size - 100, self.mid_size + 100, 'Beam search', game)
        self.Human = button(
            self.mid_size - 100, self.mid_size + 150, 'Human', game)
        self.Quit = button(
            self.mid_size - 100, self.mid_size + 200, 'Go Back to Main Menu', game)
        
    def display_menu(self):
        self.run_display = True
        while self.run_display:

            self.game.display1.fill(WINDOW_COLOR)

            if self.BFS.draw_button(self.game.display1):
                self.state = 'BFS'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.curr_menu = self.game.TwoPlayerMenu_P2
                
            if self.DFS.draw_button(self.game.display1):
                self.state = 'DFS'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.curr_menu = self.game.TwoPlayerMenu_P2
            if self.UCS.draw_button(self.game.display1):
                self.state = 'UCS'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.curr_menu = self.game.TwoPlayerMenu_P2
            if self.GREEDY.draw_button(self.game.display1):
                self.state = 'GREEDY'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.curr_menu = self.game.TwoPlayerMenu_P2
            if self.ASTAR.draw_button(self.game.display1):
                self.state = 'ASTAR'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.curr_menu = self.game.TwoPlayerMenu_P2
            if self.HILLCLIMBING.draw_button(self.game.display1):
                self.state = 'HILLCLIMBING'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.curr_menu = self.game.TwoPlayerMenu_P2
            if self.BEAM.draw_button(self.game.display1):
                self.state = 'BEAM'
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.curr_menu = self.game.TwoPlayerMenu_P2
            if self.Human.draw_button(self.game.display1):
                self.state = 'HUMAN'    
                self.play_sound(self.press_sound)
                self.run_display = False
                self.game.curr_menu = self.game.TwoPlayerMenu_P2
            
            if self.Quit.draw_button(self.game.display1):
                self.play_sound(self.press_sound)
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

            self.game.event_handler()
            
            self.game.draw_text(
                'SNAKE EATS BANANAS', size=self.title_size,
                x=self.game.SIZE/2, y=self.game.SIZE/2 - 250,
                color=TITLE_COLOR
            )
            self.game.draw_text(
                'Choose Player 1 options: ', size=self.option_size,
                x=self.titlex,  y=self.titley,
                color=MENU_COLOR
            )

            self.draw_cursor()
            self.blit_menu()

class twoPlayerMenu_P2(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'BFS'
        
        self.titlex, self.titley = self.mid_size, self.mid_size - 200
        self.BFS = button(
            self.mid_size - 100, self.mid_size - 200, 'BFS', game)
        self.DFS = button(
            self.mid_size - 100, self.mid_size + -150, 'DFS', game)
        self.UCS = button(
            self.mid_size - 100, self.mid_size + -100, 'UCS', game)
        self.GREEDY = button(
            self.mid_size - 100, self.mid_size - 50, 'Greedy', game)
        self.ASTAR = button(
            self.mid_size - 100, self.mid_size + 0, 'A Star', game)
        self.HILLCLIMBING = button(
            self.mid_size - 100, self.mid_size + 50, 'Hill Climbing', game)
        self.BEAM = button(
            self.mid_size - 100, self.mid_size + 100, 'Beam search', game)
        self.Human = button(
            self.mid_size - 100, self.mid_size + 150, 'Human', game)
        self.Quit = button(
            self.mid_size - 100, self.mid_size + 200, 'Go Back to Main Menu', game)
        
    def display_menu(self):
        self.run_display = True
        while self.run_display:

            self.game.display1.fill(WINDOW_COLOR)

            if self.BFS.draw_button(self.game.display1):
                self.state = 'BFS'
                self.play_sound(self.press_sound)
                self.run_display = False
                os.environ['SDL_VIDEO_CENTERED'] = '1'
                self.game.window = pygame.display.set_mode((self.game.SIZE + 800, self.game.SIZE))
                self.game.playing = True
                
            if self.DFS.draw_button(self.game.display1):
                self.state = 'DFS'
                self.play_sound(self.press_sound)
                self.run_display = False
                os.environ['SDL_VIDEO_CENTERED'] = '1'
                self.game.window = pygame.display.set_mode((self.game.SIZE + 800, self.game.SIZE))
                self.game.playing = True
            if self.UCS.draw_button(self.game.display1):
                self.state = 'UCS'
                self.play_sound(self.press_sound)
                self.run_display = False
                os.environ['SDL_VIDEO_CENTERED'] = '1'
                self.game.window = pygame.display.set_mode((self.game.SIZE + 800, self.game.SIZE))
                self.game.playing = True
            if self.GREEDY.draw_button(self.game.display1):
                self.state = 'GREEDY'
                self.play_sound(self.press_sound)
                self.run_display = False
                os.environ['SDL_VIDEO_CENTERED'] = '1'
                self.game.window = pygame.display.set_mode((self.game.SIZE + 800, self.game.SIZE))
                self.game.playing = True
            if self.ASTAR.draw_button(self.game.display1):
                self.state = 'ASTAR'
                self.play_sound(self.press_sound)
                self.run_display = False
                os.environ['SDL_VIDEO_CENTERED'] = '1'
                self.game.window = pygame.display.set_mode((self.game.SIZE + 800, self.game.SIZE))
                self.game.playing = True
            if self.HILLCLIMBING.draw_button(self.game.display1):
                self.state = 'HILLCLIMBING'
                self.play_sound(self.press_sound)
                self.run_display = False
                os.environ['SDL_VIDEO_CENTERED'] = '1'
                self.game.window = pygame.display.set_mode((self.game.SIZE + 800, self.game.SIZE))
                self.game.playing = True
            if self.BEAM.draw_button(self.game.display1):
                self.state = 'BEAM'
                self.play_sound(self.press_sound)
                self.run_display = False
                os.environ['SDL_VIDEO_CENTERED'] = '1'
                self.game.window = pygame.display.set_mode((self.game.SIZE + 800, self.game.SIZE))
                self.game.playing = True
            if self.Human.draw_button(self.game.display1):
                self.state = 'HUMAN'    
                self.play_sound(self.press_sound)
                self.run_display = False
                os.environ['SDL_VIDEO_CENTERED'] = '1'
                self.game.window = pygame.display.set_mode((self.game.SIZE + 800, self.game.SIZE))
                self.game.playing = True
            
            if self.Quit.draw_button(self.game.display1):
                self.play_sound(self.press_sound)
                os.environ['SDL_VIDEO_CENTERED'] = '1'
                self.game.curr_menu = self.game.TwoPlayerMenu_P1
                self.run_display = False

            self.game.event_handler()
            
            self.game.draw_text(
                'SNAKE EATS BANANAS', size=self.title_size,
                x=self.game.SIZE/2, y=self.game.SIZE/2 - 250,
                color=TITLE_COLOR
            )
            self.game.draw_text(
                'Choose Player 2 options: ', size=self.option_size,
                x=self.titlex,  y=self.titley,
                color=MENU_COLOR
            )

            self.draw_cursor()
            self.blit_menu()
