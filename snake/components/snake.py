class Snake:
    def __init__(self, game_config):
        self.position = game_config['snakeSettings']['initialPosition']
        self.body = [self.position[:], [self.position[0] - 10, self.position[1]], [self.position[0] - 20, self.position[1]]]
        self.direction = 'RIGHT'
        self.wrap_around = game_config['gameSettings']['wrapAround']

    def move(self, game_config):
        # Change direction based on self.direction
        if self.direction == 'UP':
            self.position[1] -= 10
        elif self.direction == 'DOWN':
            self.position[1] += 10
        elif self.direction == 'LEFT':
            self.position[0] -= 10
        elif self.direction == 'RIGHT':
            self.position[0] += 10

        # Snake wrapping logic
        if self.wrap_around == True:
            self.position[0] = self.position[0] % game_config['gameSettings']['width']
            self.position[1] = self.position[1] % game_config['gameSettings']['height']
        else:
             if (self.position[0] < 0 or self.position[0] >= game_config['gameSettings']['width'] or
                self.position[1] < 0 or self.position[1] >= game_config['gameSettings']['height']):
                # Handle game over condition here
                return True

        # Move snake body
        self.body.insert(0, list(self.position))
        self.body.pop()
        return False

    def grow(self):
        self.body.insert(0, list(self.position))

    def change_direction(self, new_direction):
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction
