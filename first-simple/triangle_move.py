import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 630))
pygame.display.set_caption(title="triangle pygame move")
clock = pygame.time.Clock()

t_x = 0
t_y = 500

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    t_x += 5
    if t_x > 1000:
        t_x = -100
    screen.fill("black")

    pygame.draw.polygon(
        screen,
        "lime",
        [(400 + t_x, 240), (500 + t_x, 400), (300 + t_x, 400)],
    )

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
