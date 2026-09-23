import pygame
import sys
import random

height = 600
width = 1000
world_width = 2000
world_height = height

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("tasting camera angle scrolling animation")
clock = pygame.time.Clock()

p_x, p_y = 100, 100
p_r = 30
speed = 5
camera_x = 0

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        p_x -= speed
    elif keys[pygame.K_RIGHT]:
        p_x += speed

    p_x = max(0, min(p_x, (world_width - p_r)))
    camera_x = p_x - (width // 2) + (p_r // 2)
    camera_x = max(0, min(camera_x, world_width - width))

    screen.fill("brown")
    for i in range(0, world_width, 200):
        pygame.draw.rect(screen, "yellow", (i - camera_x, p_y, 150, 300))
    pygame.draw.circle(screen, "red", (p_x - camera_x, 100), p_r)

    pygame.display.flip()
    clock.tick(100)
pygame.quit()
sys.exit()
