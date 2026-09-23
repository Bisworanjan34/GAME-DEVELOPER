import pygame
import sys
import random
import math

pygame.init()
HEIGHT = 600
WIDTH = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("this is circle touch test between two circle")
clock = pygame.time.Clock()

c_x = 100
c_y = 100
c_radius = 15
speed = 5

t_x = 400
t_y = 300
t_radius = 70

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        c_x -= speed
    if keys[pygame.K_RIGHT]:
        c_x += speed
    if keys[pygame.K_UP]:
        c_y -= speed
    if keys[pygame.K_DOWN]:
        c_y += speed

    distance = math.hypot(c_x - t_x, c_y - t_y)
    if distance < (c_radius + t_radius):
        t_x = random.randint(100, WIDTH)
        t_y = random.randint(100, HEIGHT)
    screen.fill("navy")

    pygame.draw.circle(screen, "red", (c_x, c_y), c_radius)
    pygame.draw.circle(screen, "limegreen", (t_x, t_y), t_radius)
    pygame.display.flip()
    clock.tick(140)
pygame.quit()
sys.exit()
