import pygame
import sys

pygame.init()

sc = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Dynamic move pygame ")
clock = pygame.time.Clock()
box_x = 100
box_y = 100

run = True
while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    box_x += 10

    if box_x > 800:
        box_x = -100
    sc.fill("blue")

    pygame.draw.rect(sc, "lime", [box_x, box_y, 100, 100])

    pygame.display.flip()

    clock.tick(60)
pygame.quit()
sys.exit()
