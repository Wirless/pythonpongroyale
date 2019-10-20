import pygame

import settings


# application is here
class Goal(pygame.sprite.Sprite):

    def __init__(self, color, size, pos):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface(size)
        self.image.fill(settings.BLACK)
        self.image.set_colorkey(settings.BLACK)

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, size[0], size[1]])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.topleft = pos