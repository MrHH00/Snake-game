
import pygame
from Snake import Snake

class HumanController:
    def __init__(self):
        self.snake = Snake()
        self.direction = pygame.K_RIGHT

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction = pygame.K_UP
        elif keys[pygame.K_DOWN]:
            self.direction = pygame.K_DOWN
        elif keys[pygame.K_LEFT]:
            self.direction = pygame.K_LEFT
        elif keys[pygame.K_RIGHT]:
            self.direction = pygame.K_RIGHT

    def move_snake(self):
        if self.direction == pygame.K_UP:
            self.snake.move_up()
        elif self.direction == pygame.K_DOWN:
            self.snake.move_down()
        elif self.direction == pygame.K_LEFT:
            self.snake.move_left()
        elif self.direction == pygame.K_RIGHT:
            self.snake.move_right()

    def update(self):
        self.handle_keys()
        self.move_snake()