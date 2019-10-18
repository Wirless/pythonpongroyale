from random import randint
from random import uniform
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, size, pos):
        super().__init__()

        self.image = pygame.Surface(size)
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, size[0], size[1]])
        self.velocity = [uniform(2.3, 6.3), uniform(-2.3, 6.3)]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.rotation = 0

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        # delay to let the ball move before it rebounces itself.
        # depracated pygame.time.delay(100)
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = uniform(-8.0, 8.4)
