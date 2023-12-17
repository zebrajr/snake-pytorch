import pygame
import sys

from components.fruit import Fruit

class Game:
    def __init__(self, snake, config):
        pygame.init()
        pygame.display.set_caption(config['gameSettings']['title'])
        self.screen = pygame.display.set_mode((config['gameSettings']['width'], config['gameSettings']['height']))
        self.clock = pygame.time.Clock()
        self.config = config
        self.snake = snake
        self.fruit = Fruit(config['gameSettings'])
        self.paused = False  # Paused state
        self.score = 0
        self.start_ticks = pygame.time.get_ticks()  # Start time
        self.font = pygame.font.SysFont(None, 24)  # Initialize font

    def run(self):
        while True:
            self.handle_events()
            if not self.paused:  # Only update and draw if not paused
                self.update_game_state()
                self.draw_elements()
            pygame.display.update()
            self.clock.tick(self.config['gameSettings']['fps'])

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.lose_game()

            if event.type == pygame.KEYDOWN:
                if not self.paused:  # Handle direction changes only if not paused
                    if event.key == pygame.K_UP:
                        self.snake.change_direction('UP')
                    if event.key == pygame.K_DOWN:
                        self.snake.change_direction('DOWN')
                    if event.key == pygame.K_LEFT:
                        self.snake.change_direction('LEFT')
                    if event.key == pygame.K_RIGHT:
                        self.snake.change_direction('RIGHT')
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    self.lose_game()
                if event.key == pygame.K_p:  # Toggle pause state
                    self.paused = not self.paused


    def lose_game(self):
        pygame.quit()
        sys.exit()

    def update_game_state(self):
        invalid_move_flag = self.snake.move(self.config)
        if invalid_move_flag:
            self.lose_game()
        if self.snake.position == self.fruit.position:
            self.snake.grow()
            self.fruit = Fruit(self.config['gameSettings'])
            self.score += self.config['gameSettings']['pointsPerFruit']

    def draw_elements(self):
        self.screen.fill(self.config['gameColors']['backgroundColor'])
        for pos in self.snake.body:
            pygame.draw.rect(self.screen, self.config['gameColors']['snakeColor'], pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(self.screen, self.config['gameColors']['fruitColor'], pygame.Rect(self.fruit.position[0], self.fruit.position[1], 10, 10))

        # Display score and time
        self.display_score()
        self.display_time()


    def display_score(self):
        #score = len(self.snake.body) - 3  # Subtract initial length
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))  # Position top left


    def display_time(self):
        elapsed_time = (pygame.time.get_ticks() - self.start_ticks) // 1000  # Convert milliseconds to seconds
        time_text = self.font.render(f'Time: {elapsed_time}s', True, (255, 255, 255))
        self.screen.blit(time_text, (self.config['gameSettings']['width'] - 100, 10))  # Position top right