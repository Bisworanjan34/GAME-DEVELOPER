import pygame
import sys

pygame.init()

sc = pygame.display.set_mode((500, 500))
pygame.display.set_caption("this is normal things pygame")

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_c:
                print("hello is is  c key")
