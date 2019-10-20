from random import randint, uniform
from sounds import SoundEffect
import pygame

import settings


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, size, pos):
        super().__init__()

        self.image = pygame.Surface(size)
        self.image.fill(settings.BLACK)
        self.image.set_colorkey(settings.BLACK)

        pygame.draw.rect(self.image, color, [0, 0, size[0], size[1]])
        self.velocity = [uniform(2.0, 6.0), uniform(2.0, 6.0)]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.rotation = 0
        self.bouncecount = 0
        self.sfx = SoundEffect(settings.HIT, 1.0)
        self.sfx2 = SoundEffect(settings.PONG, 1.0)
    def sound_effect(self):
        """Sound effect for the hitmark when on collision. or pong"""
        self.sfx.play()
    def sound_effect2(self):
        self.sfx2.play()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = uniform(settings.BALLSPEED1, settings.BALLSPEED2)
        self.bouncecount+=1
    def bouncedouble(self):
        if self.velocity[0] != -self.velocity[0]:
            self.velocity[0] = -self.velocity[0]
        if self.velocity[1] != -self.velocity[0]:
            self.velocity[1] = -self.velocity[1]
        self.bouncecount+=1
    def bouncedouble2(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = +self.velocity[1]
    def bouncedouble3(self):
        self.velocity[0] = +self.velocity[0]
        self.velocity[1] = -self.velocity[1]