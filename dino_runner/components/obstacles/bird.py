import random

from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0)
        self.rect.y = random.choice([250, 100, 175, 300])
        self.index = 0

    def draw (self, screen):
        screen.blit(self.image[self.index // 5], self.rect)
        self.index += 1

        if self.index >= 9:
            self.index = 0