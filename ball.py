import pygame
from random import randint
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)

class Ball(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)
		
		pygame.draw.rect(self.image, color, [0, 0, width, height])
		self.velocity = [randint(2,4),randint(-2,6)]
		self.rect = self.image.get_rect()
		self.rotation = 0
		
	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]
		
	def bounce(self):
		#delay to let the ball move before it rebounces itself.
		pygame.time.delay(100)
		self.velocity[0] = -self.velocity[0]
		self.velocity[1] = randint(-8,8)

