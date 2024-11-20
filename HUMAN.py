import pygame
from Utility import Node
from Algorithm import Algorithm

class HUMAN(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)
        self.grid = grid
        self.direction = pygame.K_RIGHT

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.direction != pygame.K_DOWN:
            self.direction = pygame.K_UP
        elif keys[pygame.K_DOWN] and self.direction != pygame.K_UP:
            self.direction = pygame.K_DOWN
        elif keys[pygame.K_LEFT] and self.direction != pygame.K_RIGHT:
            self.direction = pygame.K_LEFT
        elif keys[pygame.K_RIGHT] and self.direction != pygame.K_LEFT:
            self.direction = pygame.K_RIGHT

    def run_algorithm(self, snake):
        self.handle_keys()
        if self.direction == pygame.K_UP:
            return snake.body[0].x, snake.body[0].y - 1
        elif self.direction == pygame.K_DOWN:
            return snake.body[0].x, snake.body[0].y + 1
        elif self.direction == pygame.K_LEFT:
            return snake.body[0].x - 1, snake.body[0].y
        elif self.direction == pygame.K_RIGHT:
            return snake.body[0].x + 1, snake.body[0].y

