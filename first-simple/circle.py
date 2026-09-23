import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("circle fill color")
clock = pygame.time.Clock()

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    screen.fill("lime")

    pygame.draw.circle(screen, "blue", [200, 100], 100)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
