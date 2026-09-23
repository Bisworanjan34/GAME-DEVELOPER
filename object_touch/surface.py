import pygame
import sys
import random

pygame.init()
HEIGHT = 600
WIDTH = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("this is circle touch test between two circle")
clock = pygame.time.Clock()

p_x, p_y = 100, 100
p_h, p_w = 50, 50
p_radius = p_w // 2
speed = 5

t_x, t_y = 400, 100
t_h, t_w = 100, 300
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        p_x -= speed
    if keys[pygame.K_RIGHT]:
        p_x += speed
    if keys[pygame.K_UP]:
        p_y -= speed
    if keys[pygame.K_DOWN]:
        p_y += speed
    # surface
    p_surface = pygame.Surface((p_w, p_h), pygame.SRCALPHA)
    pygame.draw.circle(p_surface, "red", [p_radius, p_radius], p_radius)
    p_mask = pygame.mask.from_surface(p_surface)

    t_surface = pygame.Surface((t_w, t_h), pygame.SRCALPHA)
    pygame.draw.polygon(t_surface, "lime", [(t_w // 2, 0), (0, t_h), (t_w, t_h)])
    t_mask = pygame.mask.from_surface(t_surface)

    offset = (t_x - p_x, t_y - p_y)

    if p_mask.overlap(t_mask, offset):
        t_x = random.randint(0, WIDTH - t_w)
        t_y = random.randint(0, HEIGHT - t_h)

    if p_x > WIDTH:
        p_x = -p_w
    if p_x < -p_w:
        p_x = WIDTH
    if p_y > HEIGHT:
        p_y = -p_h
    if p_y < -p_h:
        p_y = HEIGHT

    screen.fill("navy")
    screen.blit(p_surface, (p_x, p_y))
    screen.blit(t_surface, (t_x, t_y))

    pygame.display.flip()
    clock.tick(100)
pygame.quit()
sys.exit()
