import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("circle dynamically move")
clock = pygame.time.Clock()
c_x = 100
c_y = 200

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    c_x += 5
    if c_x > 1000:
        c_x = -100
    screen.fill("navyblue")

    pygame.draw.circle(screen, "yellow", [c_x, c_y], 50)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
