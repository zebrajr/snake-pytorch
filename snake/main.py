#import pygame
#import random
import json
#import sys
from components.snake import Snake
from components.game import Game
from components.fruit import Fruit


if __name__ == "__main__":
    with open('./snake/config.json', 'r') as file:
        config = json.load(file)

    snake = Snake(config)
    game = Game(snake, config)
    game.run()
