import pygame
import random
import json
import sys


# Load variables from a JSON file
with open('./snake/config.json', 'r') as file:
    config = json.load(file)

# Initialize Pygame
pygame.init()
pygame.display.set_caption(config['gameSettings']['title'])

# Set up the screen
screen = pygame.display.set_mode((config['gameSettings']['width'], config['gameSettings']['height']))

# Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction


# Food
food_pos = [random.randrange(1, (config['gameSettings']['width']//10)) * 10,
            random.randrange(1, (config['gameSettings']['height']//10)) * 10]
food_spawn = True


# Game loop
clock = pygame.time.Clock()
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Control the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Move the snake
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    # Food Spawning
    if not food_spawn:
        food_pos = [random.randrange(1, (config['gameSettings']['width']//10)) * 10,
                    random.randrange(1, (config['gameSettings']['height']//10)) * 10]
    food_spawn = True

    # Graphics
    screen.fill(config['gameColors']['backgroundColor'])
    for pos in snake_body:
        pygame.draw.rect(screen, config['gameColors']['snakeColor'], pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, config['gameColors']['fruitColor'], pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresher
    clock.tick(30)