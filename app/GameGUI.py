import pygame
from app.Constants import *
import app.Constants as Constants
from app.Menu import *
from app.GameController import GameController
from pygame.math import Vector2
import sys


class GameGUI:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.SCREEN_UPDATE = pygame.USEREVENT

        self.speed = 110
        self.speed_up = 80

        pygame.time.set_timer(self.SCREEN_UPDATE, self.speed)

        # Khởi tạo hai GameController
        self.controller1 = GameController()
        self.controller2 = GameController()

        self.running, self.playing = True, False
        self.UPKEY, self.DOWNKEY, self.START, self.BACK = False, False, False, False

        self.SIZE = CELL_SIZE * NO_OF_CELLS
        self.display1 = pygame.Surface((self.SIZE, self.SIZE))
        self.display2 = pygame.Surface((self.SIZE, self.SIZE))
        self.background = pygame.Surface((self.SIZE, self.SIZE))
        self.background.fill(WINDOW_COLOR)
        self.window = pygame.display.set_mode((self.SIZE + 700, self.SIZE))
        self.window.fill(WINDOW_COLOR)

        self.font_name = 'Gameplay.ttf'

        # ---- all menus ----
        self.main_menu = MainMenu(self)
        # self.main_menu = onePlayerMenu(self)
        self.OnePlayerMenu = onePlayerMenu(self)
        self.TwoPlayerMenu_P1 = twoPlayerMenu_P1(self)
        self.TwoPlayerMenu_P2 = twoPlayerMenu_P2(self)
        self.curr_menu = self.main_menu

        self.load_model = False
        self.view_path = False
        self.view_explored = False
        
        self.banana = pygame.image.load('images/banana-30px.png').convert_alpha()

    def game_loop(self):
        while self.playing:
            self.event_handler()

            if self.BACK:
                self.playing = False

            self.display1.fill(WINDOW_COLOR)
            self.display2.fill(WINDOW_COLOR)
            if self.controller1.algo != None:
                self.draw_elements(self.controller1,self.display1)
            if self.controller2.algo != None:
                self.draw_elements(self.controller2,self.display2)
            
            if (Constants.twoPlayerOpt == False):
                self.window.blit(self.display2, (350, 0))
            else:
                self.window.blit(self.background, (350, 0))
                self.window.blit(self.display1, (0, 0))
                self.window.blit(self.display2, (700, 0))
            

            pygame.display.update()
            self.clock.tick(60)
            self.reset_keys()

    def draw_elements(self,controller,display):
        # draw banner and stats
        self.draw_grid(display)
        self.draw_banner(display)
        self.draw_game_stats(controller,display)

        fruit = controller.get_fruit_pos()
        snake = controller.snake

        
        self.draw_fruit(fruit, display)
        self.draw_snake(snake,display)
        self.draw_score(controller,display)

        if not controller.model_loaded:
            self.draw_path(controller,display)  # only path Ai has a path
            self.draw_explored(controller,display)  # only path Ai has explored set

    def draw_grid(self,display):
        grid_color = (209,74,54)
        for row in range(NO_OF_CELLS):
            if row % 2 == 0:
                for col in range(NO_OF_CELLS):
                    if col % 2 == 0:
                        grid_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(display, grid_color,grid_rect)
            else:
                for col in range(NO_OF_CELLS):
                    if col % 2 != 0:
                        grid_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(display, grid_color, grid_rect)                  

    def draw_game_stats(self, controller,display):
        if (Constants.twoPlayerOpt):
            if(self.TwoPlayerMenu_P1.state == 'HUMAN'):
                instruction1 = 'W to speed up, Q to go back'
                instruction2 = 'Space to view Ai path, W to speed up, Q to go back'
            else:
                instruction1 = 'Space to view Ai path, W to speed up, Q to go back'
                instruction2 = 'Space to view Ai path, W to speed up, Q to go back'
        elif (Constants.twoPlayerOpt == False):
            if self.curr_menu.state != 'HUMAN':  # path Ai algo
                instruction1 = 'Space to view Ai path, W to speed up, Q to go back'
            else:  # human
                instruction1 = 'W to speed up, Q to go back'
            
        if (Constants.twoPlayerOpt):
            self.draw_text_surface(
                instruction2, size=16,
                x=self.SIZE/2, y=(CELL_SIZE * NO_OF_CELLS) - NO_OF_CELLS,
                display=self.display2,
                color=WHITE
            )
            self.draw_text_surface(
                instruction1, size=16,
                x=self.SIZE/2, y=(CELL_SIZE * NO_OF_CELLS) - NO_OF_CELLS,
                display=self.display1,
                color=WHITE
            )
        else:
            self.draw_text_surface(
                instruction1, size=16,
                x=self.SIZE/2, y=(CELL_SIZE * NO_OF_CELLS) - NO_OF_CELLS,
                display=self.display2,
                color=WHITE
            )

        # current Algo Title
        if (Constants.twoPlayerOpt == False):
            self.draw_text_surface(
                self.OnePlayerMenu.state, size=30,
                x=self.SIZE/2, y=CELL_SIZE,
                display=display, color=WINDOW_COLOR
            )
        elif controller == self.controller1:
            self.draw_text_surface(
                self.TwoPlayerMenu_P1.state, size=30,
                x=self.SIZE/2, y=CELL_SIZE,
                display=display, color=WINDOW_COLOR
            )
        elif controller == self.controller2:
            self.draw_text_surface(
                self.TwoPlayerMenu_P2.state, size=30,
                x=self.SIZE/2, y=CELL_SIZE,
                display=display, color=WINDOW_COLOR
            )

    def draw_path(self,controller,display):
        if controller.algo != None and self.view_path:
            for path in controller.algo.path:  # for each {x,y} in path
                x = int(path.x * CELL_SIZE)
                y = int(path.y * CELL_SIZE)

                path_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

                shape_surf = pygame.Surface(path_rect.size, pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, PATHCOLOR, shape_surf.get_rect())

                pygame.draw.rect(display, BANNER_COLOR, path_rect, 1)
                display.blit(shape_surf, path_rect)

    def draw_explored(self,controller,display):
        if controller.algo != None and self.view_explored:
            for path in controller.algo.explored_set:
                x = int(path.x * CELL_SIZE)
                y = int(path.y * CELL_SIZE)

                path_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

                shape_surf = pygame.Surface(path_rect.size, pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, EXPLOREDCOLOR, shape_surf.get_rect())

                pygame.draw.rect(display, BANNER_COLOR, path_rect, 1)
                display.blit(shape_surf, path_rect)


    def draw_snake_head(self, snake,display):
        head = snake.body[0]
        self.draw_rect(head,display,color=SNAKE_HEAD_COLOR)

    def draw_snake_body(self, body,display):
        self.draw_rect(body,display, color=SNAKE_COLOR, border=True)

    def draw_rect(self, element,display, color, border=False):
        x = int(element.x * CELL_SIZE)
        y = int(element.y * CELL_SIZE)

        body_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(display, color, body_rect)

        if border:
            pygame.draw.rect(display, WINDOW_COLOR, body_rect, 3)

    def draw_snake(self, snake,display):
        # self.draw_snake_head(snake,display)  # draw head

        # for body in snake.body[1:]:
        #     self.draw_snake_body(body,display)  # draw body
        
        self.update_head_graphics(snake)
        self.update_tail_graphics(snake)
        # for block in self.body:
        #     #create a rectangle      pygame.Rect(x,y,width,height)
        #     block_rect = pygame.Rect(int(block.x*cell_size),int(block.y*cell_size),cell_size,cell_size)
        #     #draw the rectangle
        #     pygame.draw.rect(screen,(183,111,122),block_rect)
        
        # we 
        for index,block in enumerate(snake.body):
            #1. create a rectangle for positioning
            x_pos = int(block.x*CELL_SIZE)
            y_pos = int(block.y*CELL_SIZE)
            block_rect = pygame.Rect(x_pos,y_pos,CELL_SIZE,CELL_SIZE)
            #2. direction is the face heading
            #snake head direction update
            if index == 0:
                display.blit(snake.head,block_rect)
            #snake tail direction update
            elif index == len(snake.body)-1:
                display.blit(snake.tail,block_rect)
            #snake body direction update
            else: 
                previous_block = snake.body[index+1] - block
                next_block = snake.body[index-1] - block
                if previous_block.x == next_block.x:
                    display.blit(snake.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    display.blit(snake.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        display.blit(snake.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        display.blit(snake.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        display.blit(snake.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        display.blit(snake.body_br,block_rect)

    def update_head_graphics(self,snake):
        head_relation = snake.body[1] - snake.body[0]
        distance_to_fruit = (snake.body[0] - snake.get_fruit()).length()
        if distance_to_fruit <= 2:
            if head_relation == Vector2(1, 0): snake.head = snake.head_left_eating
            elif head_relation == Vector2(-1, 0): snake.head = snake.head_right_eating
            elif head_relation == Vector2(0, 1): snake.head = snake.head_up_eating
            elif head_relation == Vector2(0, -1): snake.head = snake.head_down_eating
        else:
            if head_relation == Vector2(1,0): snake.head = snake.head_left
            elif head_relation == Vector2(-1,0): snake.head = snake.head_right
            elif head_relation == Vector2(0,1): snake.head = snake.head_up
            elif head_relation == Vector2(0,-1): snake.head = snake.head_down
        
    def update_tail_graphics(self,snake):
        tail_relation = snake.body[-2] - snake.body[-1]
        if tail_relation == Vector2(1,0): snake.tail = snake.tail_left
        elif tail_relation == Vector2(-1,0): snake.tail = snake.tail_right
        elif tail_relation == Vector2(0,1): snake.tail = snake.tail_up
        elif tail_relation == Vector2(0,-1): snake.tail = snake.tail_down

    def draw_fruit(self, fruit, display):
        x = int(fruit.x * CELL_SIZE)
        y = int(fruit.y * CELL_SIZE)

        fruit_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        # pygame.draw.rect(display, FRUIT_COLOR, fruit_rect)
        display.blit(self.banana, fruit_rect)

    def draw_banner(self,display):
        banner = pygame.Rect(0, 0, self.SIZE, BANNER_HEIGHT * CELL_SIZE)
        pygame.draw.rect(display, BANNER_COLOR, banner)

    def draw_score(self,controller,display):
        score_text = 'Score: ' + str(controller.get_score()) 
        score_x = self.SIZE - (CELL_SIZE + 2*len(score_text)) - 20
        score_y = CELL_SIZE
        self.draw_text_surface(score_text, 20, score_x, score_y, display,WINDOW_COLOR)

    def game_over(self):
        again = False

        while not again:
            for event in pygame.event.get():
                if self.is_quit(event):
                    again = True
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        again = True
                        break
                    if event.key == pygame.K_s:
                        again = True
                        self.controller.save_model()
                        break

            self.display2.fill(WINDOW_COLOR)
            self.display1.fill(WINDOW_COLOR)

            if (Constants.twoPlayerOpt == False):
                high_score2 = f'{self.OnePlayerMenu.state} Score: {self.controller2.get_score()}'
            else:
                high_score1 = f'{self.TwoPlayerMenu_P1.state} Score: {self.controller1.get_score()}'
                high_score2 = f'{self.TwoPlayerMenu_P2.state} Score: {self.controller2.get_score()}'
            
            to_continue = 'Enter to Continue'

            if (Constants.twoPlayerOpt):
                self.draw_text_surface(
                    high_score1, size=30,
                    x=self.SIZE/2, y=self.SIZE/2,
                    display=self.display1, color=MENU_COLOR
                )
            
            self.draw_text_surface(
                high_score2, size=30,
                x=self.SIZE/2, y=self.SIZE/2,
                display=self.display2, color=MENU_COLOR
            )

            # self.draw_text(
            #     high_score1, size=35,
            #     x=self.SIZE/2, y=self.SIZE/2,
            # )
            
            # self.draw_text(
            #     high_score2, size=35,
            #     x=self.SIZE/2, y=self.SIZE/2,
            # )

            self.draw_text(
                to_continue, size=30,
                x=self.SIZE/2, y=self.SIZE/2 + 2*CELL_SIZE,
                color=WHITE
            )

            if (Constants.twoPlayerOpt == False):
                self.window.blit(self.display2, (350, 0))
            else:    
                self.window.blit(self.display2, (700, 0))
                self.window.blit(self.display1, (0, 0))
            pygame.display.update()
        self.controller1.reset()
        self.controller2.reset()

    def is_quit(self, event):
        # user presses exit icon
        if event.type == pygame.QUIT:
            self.running, self.playing = False, False
            self.curr_menu.run_display = False
            return True
        return False

    def event_handler(self):
        for event in pygame.event.get():
            if self.is_quit(event):
                pygame.quit()
                sys.exit()

            # user event that runs every self.speed milisec
            elif self.playing and event.type == pygame.USEREVENT:

                if self.load_model:  # user load model
                    self.controller1.load_model()
                    self.controller2.load_model()
                    self.load_model = False

                if (Constants.twoPlayerOpt == False):
                    self.controller2.ai_play(self.OnePlayerMenu.state)
                else:
                    self.controller1.ai_play(self.TwoPlayerMenu_P1.state)  # play
                    self.controller2.ai_play(self.TwoPlayerMenu_P2.state)  # play


                if self.controller1.end == True :  # Only path ai and trained model
                    self.playing = False
                    self.game_over()  # show game over stats
                    
                if self.controller2.end == True:  # Only path ai and trained model
                    self.playing = False
                    self.game_over()  # show game over stats

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:  # on Enter
                    self.START = True
                    self.view_path = False

                elif event.key == pygame.K_q:  # on q return
                    self.BACK = True
                    self.controller1.reset()
                    self.controller2.reset()
                    
                elif event.key == pygame.K_y:
                    self.view_explored = not self.view_explored

                elif event.key == pygame.K_SPACE:  # space view path or hide training snakes
                    self.view_path = not self.view_path

                elif event.key == pygame.K_DOWN:
                    self.DOWNKEY = True
                elif event.key == pygame.K_UP:
                    self.UPKEY = True

                elif event.key == pygame.K_w:  # speed up/down by self.speed_up
                    self.speed_up = -1 * self.speed_up
                    self.speed = self.speed + self.speed_up
                    pygame.time.set_timer(self.SCREEN_UPDATE, self.speed)

    def reset_keys(self):
        self.UPKEY, self.DOWNKEY, self.START, self.BACK = False, False, False, False

    def draw_text(self, text, size, x, y, color=WINDOW_COLOR):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display2.blit(text_surface, text_rect)
        self.display1.blit(text_surface, text_rect)
        
    def draw_text_surface(self, text, size, x, y, display,color=WINDOW_COLOR): 
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        display.blit(text_surface, text_rect)
