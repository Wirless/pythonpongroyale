import pygame
from sounds import SoundEffect
import settings
from random import randint


# application is here
class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, size, pos):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface(size)
        self.image.fill(settings.BLACK)
        self.image.set_colorkey(settings.BLACK)
        self.collision = [False]

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, size[0], size[1]])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.sfx = SoundEffect(settings.DEAD, 1.0)
        self.sfx2 = SoundEffect(settings.OOF, 1.0)
        self.sfx3 = SoundEffect(settings.DOH, 1.0)
        self.sfx4 = SoundEffect(settings.BRUH, 1.0)
        self.sfx5 = SoundEffect(settings.MIF, 1.0)

    def sound_effect(self):
        if settings.AUDIO == True:
            generate = randint(1,6)
            if generate == 1:
                self.sfx.play()
            elif generate == 2:
                self.sfx2.play()
            elif generate == 3:
                self.sfx3.play()
            elif generate == 4:
                self.sfx4.play()
            elif generate == 5:
                self.sfx5.play()
            else:
                self.sfx.play()
        """Sound effect for the hitmark when on collision. or pong"""
        
    def moveUp(self, pixels):
        self.rect.y -= pixels
        # Check that you are not going too far (off the screen)
        if self.rect.y < 0:
            self.rect.y = 0
    def moveDown(self, pixels):
        self.rect.y += pixels
        # Check that you are not going too far (off the screen)
        if self.rect.y > 615:
            self.rect.y = 615

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 615:
            self.rect.x = 615
