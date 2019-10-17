#!/usr/bin/env python

# some paddle yoke
# Created by some wee man

import pygame


#we got em colours

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)

#application is here
class Paddle(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
	def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
		super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)
		self.collision = [False]
 
        # Draw the paddle (a rectangle!)
		pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
		self.rect = self.image.get_rect()
        
	def moveUp(self, pixels):
		self.rect.y -= pixels
		#Check that you are not going too far (off the screen)
		if self.rect.y < 0:
			self.rect.y = 0
          
	def moveDown(self, pixels):
		self.rect.y += pixels
	#Check that you are not going too far (off the screen)
		if self.rect.y > 415:
			self.rect.y = 415
            
	def moveLeft(self, pixels):
		self.rect.x -= pixels
		if self.rect.x < 0:
			self.rect.x = 0
            
	def moveRight(self, pixels):
		self.rect.x += pixels
		if self.rect.x > 600:
			self.rect.x = 600
