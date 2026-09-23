import pygame
import sys
import random

pygame.init()
width, height = 1000, 600
world_width = 3000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("tasting gravity power - Mask Logic")
clock = pygame.time.Clock()

p_x, p_y = 100, 100
p_r = 25
speed = 5

gravity = 0.5
vel_y = 0
jump_s = -19
is_jump = False

platforms = []
for i in range(300, world_width, 200):
    r = random.randint(0, 600)
    platforms.append([i, r, 100, 300])

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and not is_jump:
                vel_y = jump_s
                is_jump = True

    keys = pygame.key.get_pressed()
    dx = 0
    if keys[pygame.K_LEFT]:
        dx = -speed
    elif keys[pygame.K_RIGHT]:
        dx = speed

    # --- 1. X-AXIS MOVEMENT & MASK COLLISION ---
    p_x += dx

    # Player Mask
    p_sur = pygame.Surface((p_r * 2, p_r * 2), pygame.SRCALPHA)
    p_sur.fill("green")
    p_mask = pygame.mask.from_surface(p_sur)

    # Target/Pillar Surface & Mask (Ek single pillar example ke liye)
    for plat in platforms:
        t_x, t_y, t_w, t_h = plat
        t_sur = pygame.Surface((t_w, t_h), pygame.SRCALPHA)
        t_sur.fill("green")
        t_mask = pygame.mask.from_surface(t_sur)

        offset_x = (t_x - (p_x - p_r), t_y - (p_y - p_r))
        if p_mask.overlap(t_mask, offset_x):
            p_x -= dx
            break

    # --- 2. Y-AXIS MOVEMENT & MASK COLLISION ---
    vel_y += gravity
    p_y += vel_y

    # Y collision check
    for plat in platforms:
        t_x, t_y, t_w, t_h = plat
        t_sur = pygame.Surface((t_w, t_h), pygame.SRCALPHA)
        t_sur.fill("orange")
        t_mask = pygame.mask.from_surface(t_sur)

        offset_y = (t_x - (p_x - p_r), t_y - (p_y - p_r))
        if p_mask.overlap(t_mask, offset_y):
            p_y -= vel_y
            if vel_y > 0:
                is_jump = False
            vel_y = 0
            break

    # Floor collision
    ground_level = height - p_r
    if p_y >= ground_level:
        p_y = ground_level
        vel_y = 0
        is_jump = False

    p_x = max(p_r, min(p_x, world_width - p_r))
    camera_x = max(0, min(p_x - (width // 2), world_width - width))
    # --- DRAWING ---
    screen.fill("black")
    # Pillar draw
    for plat in platforms:
        t_x, t_y, T_w, t_h = plat
        pygame.draw.rect(screen, "yellow", (t_x - camera_x, t_y, t_w, t_h))
    # Player draw
    pygame.draw.circle(screen, "orange", (int(p_x - camera_x), int(p_y)), p_r)
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
sys.exit()
