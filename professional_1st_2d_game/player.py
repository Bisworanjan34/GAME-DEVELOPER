# player.py
import pygame
from settings import WIDTH, HEIGHT, PLAYER_SPEED


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 100

        # Load and scale image
        self.image = pygame.image.load("../images/boy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect(topleft=(100, 100))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = PLAYER_SPEED

    def update(self, keys):
        moving = False
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            moving = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            moving = True
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            moving = True
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            moving = True

        # Screen wrapping (Modulus)
        self.rect.x %= WIDTH
        self.rect.y %= HEIGHT

        return moving

    def reset(self, x, y):
        self.rect.topleft = (x, y)
