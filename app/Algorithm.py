from abc import ABC, abstractmethod
from app.Constants import NO_OF_CELLS, BANNER_HEIGHT
from app.Utility import Node
import math


class Algorithm(ABC):

    def __init__(self, grid):
        self.grid = grid
        self.frontier = []
        self.explored_set = []
        self.path = []

    def get_initstate_and_goalstate(self, snake):
        return Node(snake.get_x(), snake.get_y()), Node(snake.get_fruit().x, snake.get_fruit().y)

    def manhattan_distance(self, nodeA, nodeB):
        distance_1 = abs(nodeA.x - nodeB.x)
        distance_2 = abs(nodeA.y - nodeB.y)
        return distance_1 + distance_2

    def euclidean_distance(self, nodeA, nodeB):
        distance_1 = nodeA.x - nodeB.x
        distance_2 = nodeA.y - nodeB.y
        return math.sqrt(distance_1**2 + distance_2**2)

    @abstractmethod
    def run_algorithm(self, snake):
        pass

    def get_path(self, node):
        if node.parent == None:
            return node

        while node.parent.parent != None:
            self.path.append(node)
            node = node.parent
        return node

    def inside_body(self, snake, node):
        for body in snake.body:
            if body.x == node.x and body.y == node.y:
                return True
        return False

    def outside_boundary(self, node):
        if not 0 <= node.x < NO_OF_CELLS:
            return True
        elif not BANNER_HEIGHT <= node.y < NO_OF_CELLS:
            return True
        return False

    def get_neighbors(self, node):
        i = int(node.x)
        j = int(node.y)

        neighbors = []
        # left [i-1, j]
        if i > 0:
            neighbors.append(self.grid[i-1][j])
        # right [i+1, j]
        if i < NO_OF_CELLS - 1:
            neighbors.append(self.grid[i+1][j])
        # top [i, j-1]
        if j > 0:
            neighbors.append(self.grid[i][j-1])

        # bottom [i, j+1]
        if j < NO_OF_CELLS - 1:
            neighbors.append(self.grid[i][j+1])

        return neighbors

    def keep_moving(self, snake):
        x = snake.body[0].x
        y = snake.body[0].y

        directions = [
            (x + 1, y),  # right
            (x - 1, y),  # left
            (x, y + 1),  # down
            (x, y - 1)   # up
        ]

        # Filter out invalid moves
        valid_moves = [
            (new_x, new_y) for new_x, new_y in directions
            if 0 <= new_x < NO_OF_CELLS and BANNER_HEIGHT <= new_y < NO_OF_CELLS and not any(body.x == new_x and body.y == new_y for body in snake.body)
        ]

        if valid_moves:
            # Choose the move that maximizes the distance from the snake's body
            max_distance = -1
            best_move = (x, y)
            for new_x, new_y in valid_moves:
                distance = min(abs(new_x - body.x) + abs(new_y - body.y) for body in snake.body)
                if distance > max_distance:
                    max_distance = distance
                    best_move = (new_x, new_y)
            return best_move
        else:
            # If no valid moves, stay in place
            return x, y
