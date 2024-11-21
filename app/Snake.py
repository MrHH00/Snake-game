from pygame.math import Vector2
from app.Fruit import Fruit
import pickle
import pygame


class Snake:
    def __init__(self, hidden=8):
        self.body = [Vector2(5, 8), Vector2(4, 8), Vector2(3, 8)]
        self.fruit = Fruit()

        self.score = 0
        self.fitness = 0

        self.life_time = 0
        self.steps = 0
        self.hidden = hidden
        
        self.head_up = pygame.image.load('images/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('images/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('images/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('images/head_left.png').convert_alpha()
        
        self.head_up_eating = pygame.image.load('images/head_up_eating.png').convert_alpha()
        self.head_down_eating = pygame.image.load('images/head_down_eating.png').convert_alpha()
        self.head_right_eating = pygame.image.load('images/head_right_eating.png').convert_alpha()
        self.head_left_eating = pygame.image.load('images/head_left_eating.png').convert_alpha()
		
        self.tail_up = pygame.image.load('images/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('images/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('images/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('images/tail_left.png').convert_alpha()
        
        self.body_vertical = pygame.image.load('images/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('images/body_horizontal.png').convert_alpha()
        
        self.body_tr = pygame.image.load('images/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('images/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('images/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('images/body_bl.png').convert_alpha()
        
        
        self.eat_sound = pygame.mixer.Sound('sounds/carrotnom.mp3')


    def save_model(self, network, name):
        with open(name, "wb") as file:
            pickle.dump(network, file)

    def load_model(self, name):
        with open(name, 'rb') as file:
            self.network = pickle.load(file)

    def reset(self):
        self.body = [Vector2(5, 8), Vector2(4, 8), Vector2(3, 8)]
        self.fruit.reset_seed()

        self.score = 0
        self.fitness = 0
        self.steps = 0

    def get_x(self):
        return self.body[0].x

    def get_y(self):
        return self.body[0].y

    def get_fruit(self):
        return self.fruit.position

    def ate_fruit(self):
        if self.fruit.position == self.body[0]:
            self.score += 1
            self.life_time -= 40
            return True
        return False

    def create_fruit(self):
        self.fruit.generate_fruit()

    def move_ai(self, x, y):
        self.life_time += 1
        self.steps += 1
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x = x
        self.body[0].y = y

    def add_body_ai(self):
        last_indx = len(self.body) - 1
        tail = self.body[-1]
        before_last = self.body[-2]

        if tail.x == before_last.x:
            if tail.y < before_last.y:
                self.body.append(Vector2(tail.x, tail.y-1))
            else:
                self.body.append(Vector2(tail.x, tail.y+1))
        elif tail.y == before_last.y:
            if tail.x < before_last.x:
                self.body.append(Vector2(tail.x - 1, tail.y))
            else:
                self.body.append(Vector2(tail.x + 1, tail.y))

    def ate_body(self):
        for body in self.body[1:]:
            if self.body[0] == body:
                return True
        return False

    def play_sound(self):
        self.eat_sound.play()