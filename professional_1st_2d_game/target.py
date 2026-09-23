# target.py
import pygame
import random
from settings import WIDTH, HEIGHT


class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed=0, color="yellow"):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed

        # Create surface for circular target
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        radius = self.width // 2
        pygame.draw.circle(self.image, color, (radius, radius), radius)

        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # Agar target ki koi speed hai toh wo horizontally move karega
        if self.speed != 0:
            self.rect.x -= self.speed

            # Screen limits cross hone par wrap karna
            if self.rect.x > WIDTH:
                self.rect.x = -self.width
                self.rect.y = random.randint(50, HEIGHT - 100)
            elif self.rect.x < -self.width:
                self.rect.x = WIDTH
                self.rect.y = random.randint(50, HEIGHT - 100)

    def respawn(self):
        # Random location par teleport karna (jab player touch kare)
        self.rect.x = random.randint(0, WIDTH - self.width)
        self.rect.y = random.randint(0, HEIGHT - self.height)
