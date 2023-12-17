import random

class Fruit:
    def __init__(self, game_config):
        self.position = self.spawn_new_fruit(game_config)

    def spawn_new_fruit(self, game_config):
        return [random.randrange(1, (game_config['width'] // 10)) * 10,
                random.randrange(1, (game_config['height'] // 10)) * 10]
