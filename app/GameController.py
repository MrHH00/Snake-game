from app.Snake import Snake
from app.Constants import NO_OF_CELLS, BANNER_HEIGHT
from app.Utility import Grid
from algorithms.DFS import DFS
from algorithms.BFS import BFS
from algorithms.UCS import UCS
from algorithms.GREEDY import GREEDY
from algorithms.A_STAR import A_STAR
from algorithms.HILL_CLIMBING import HILL_CLIMBING
from algorithms.BEAM import BEAM
from algorithms.HUMAN import HUMAN
from algorithms.BestFirstSearch import BestFirstSearch
from algorithms.UCS import UCS
from algorithms.BeamSearch import BeamSearch
import time


class GameController:

    def __init__(self):
        self.snake = None
        self.snakes = []
        self.score = 0
        self.end = False
        self.grid = Grid().grid
        self.algo = None
        self.model_loaded = False

    def reset(self):
        self.end = False
        if self.snake:
            self.snake.reset()
            self.snake = None

        self.algo = None
        self.snakes = []
        self.model_loaded = False

    def save_model(self):
        best_snake = self.algo.best_snake
        network = best_snake.network
        best_snake.save_model(network, 'saved_model')

    def load_model(self):
        self.snake = Snake()
        self.snake.load_model('saved_model')
        self.model_loaded = True

    def get_score(self):
        if self.snake:
            return self.snake.score
        else:
            return 0

    def ate_fruit(self):
        if self.snake.ate_fruit():
            self.snake.add_body_ai()
            self.change_fruit_location()
            self.snake.play_sound()

    def change_fruit_location(self):
        while True:
            self.snake.create_fruit()
            position = self.snake.get_fruit()
            inside_body = False
            for body in self.snake.body:
                if position == body:
                    inside_body = True

            if inside_body == False:
                break

    def died(self):
        current_x = self.snake.body[0].x
        current_y = self.snake.body[0].y

        if not 0 <= current_x < NO_OF_CELLS:
            self.end = True
        elif not BANNER_HEIGHT <= current_y < NO_OF_CELLS:
            self.end = True
        elif self.snake.ate_body():
            self.end = True

    def get_fruit_pos(self):
        return self.snake.get_fruit()

    def set_algorithm(self, algo_type):
        if self.algo != None:
            return

        if algo_type == 'BFS':
            self.algo = BFS(self.grid)
            self.snake = Snake()

        elif algo_type == 'DFS':
            self.algo = DFS(self.grid)
            self.snake = Snake()

        elif algo_type == 'GREEDY':
            self.algo = GREEDY(self.grid)
            self.snake = Snake()

        elif algo_type == 'ASTAR':
            self.algo = A_STAR(self.grid)
            self.snake = Snake()
            
        elif algo_type == 'UCS':
            self.algo = UCS(self.grid)
            self.snake = Snake()
            
        elif algo_type == 'HILLCLIMBING':
            self.algo = HILL_CLIMBING(self.grid)
            self.snake = Snake()
            
        elif algo_type == 'BEAM':
            self.algo = BEAM(self.grid)
            self.snake = Snake()
            
        elif algo_type == 'HUMAN':
            self.algo = HUMAN(self.grid)
            self.snake = Snake()

        elif algo_type == 'Best First Search':
            self.algo = BestFirstSearch(self.grid)
            self.snake = Snake()

        elif algo_type == 'UCS':
            self.algo = UCS(self.grid)
            self.snake = Snake()

        elif algo_type == 'Hill Climbing':
            self.algo = HILL_CLIMBING(self.grid)
            self.snake = Snake()

        elif algo_type == 'Beam Search':
            self.algo = BeamSearch(self.grid)
            self.snake = Snake()

    def ai_play(self, algorithm):
        self.set_algorithm(algorithm)

        if self.algo == None:
            return

        if isinstance(self.algo, HUMAN):
            self.update_human()
        else:
            start_time = time.time()  # Bắt đầu đo thời gian
            pos = self.algo.run_algorithm(self.snake)
            end_time = time.time()  # Kết thúc đo thời gian  
            self.snake.execution_time = (end_time - start_time) * 1000  # Tính thời gian thực thi
            self.update_path_finding_algo(pos)

    def keep_moving(self):
        x = self.snake.body[0].x
        y = self.snake.body[0].y

        directions = [
            (x + 1, y),  # right
            (x - 1, y),  # left
            (x, y + 1),  # down
            (x, y - 1)   # up
        ]

        # Filter out invalid moves
        valid_moves = [
            (new_x, new_y) for new_x, new_y in directions
            if 0 <= new_x < NO_OF_CELLS and BANNER_HEIGHT <= new_y < NO_OF_CELLS and not any(body.x == new_x and body.y == new_y for body in self.snake.body)
        ]

        if valid_moves:
            # Choose the move that maximizes the distance from the snake's body
            max_distance = -1
            best_move = (x, y)
            for new_x, new_y in valid_moves:
                distance = min(abs(new_x - body.x) + abs(new_y - body.y) for body in self.snake.body)
                if distance > max_distance:
                    max_distance = distance
                    best_move = (new_x, new_y)
            return best_move
        else:
            # If no valid moves, stay in place
            return x, y

    def update_path_finding_algo(self, pos):
        if pos == None:
            x, y = self.keep_moving()
        else:
            x = pos.x
            y = pos.y

        self.snake.move_ai(x, y)
        self.died()
        self.ate_fruit()

    def update_human(self):
        x, y = self.algo.run_algorithm(self.snake)
        self.snake.move_ai(x, y)
        self.died()
        self.ate_fruit()
