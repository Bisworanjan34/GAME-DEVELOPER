print("gravity practice jump coding..........")
import pygame
import sys
import random

pygame.init()
width = 1000
height = 600
world_width = 3000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("this is for jumping test and gravity....")
clock = pygame.time.Clock()

p_x, p_y = 100, 100
p_r = 25
speed = 5
camera_x = 0

gravity = 0.5
vel_y = 0
jump_s = -20
is_jump = False

platforms = []
for i in range(300, world_width, 150):
    y = random.randint(100, 400)
    platforms.append([i, y, 70, 300])

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
        dx -= speed
    elif keys[pygame.K_RIGHT]:
        dx += speed

    # --- X-AXIS MOVEMENT & COLLISION ---
    p_x += dx

    p_sur = pygame.Surface((p_r * 2, p_r * 2), pygame.SRCALPHA)
    p_sur.fill("green")
    p_mask = pygame.mask.from_surface(p_sur)

    for plat in platforms:
        t_x, t_y, t_w, t_h = plat
        t_sur = pygame.Surface((t_w, t_h), pygame.SRCALPHA)
        t_sur.fill("green")
        t_mask = pygame.mask.from_surface(t_sur)

        offset_x = (t_x - (p_x - p_r), t_y - (p_y - p_r))
        if p_mask.overlap(t_mask, offset_x):
            p_x -= dx
            break

    # --- Y-AXIS MOVEMENT & GRAVITY / COLLISION ---
    vel_y += gravity
    p_y += vel_y

    for plat in platforms:
        t_x, t_y, t_w, t_h = plat
        t_sur = pygame.Surface((t_w, t_h), pygame.SRCALPHA)
        t_sur.fill("green")
        t_mask = pygame.mask.from_surface(t_sur)

        offset_y = (t_x - (p_x - p_r), t_y - (p_y - p_r))
        if p_mask.overlap(t_mask, offset_y):
            p_y -= vel_y
            if vel_y > 0:
                is_jump = False
            vel_y = 0
            break

    # Floor collision
    ground = height - p_r
    if p_y > ground:
        p_y = ground
        vel_y = 0
        is_jump = False

    # Screen boundary restriction (Radius ke barabar taaki player screen ke bahar na jaye)
    p_x = max(p_r, min(p_x, world_width - p_r))

    # Camera logic fix (Correct clamping)
    camera_x = p_x - (width // 2)
    # camera_x = max(0, min(camera_x, (world_width - width)))
    camera_x = max(0, min(p_x - (width // 2), (world_width - width)))
    # --- DRAWING ---
    screen.fill("blue")

    for plat in platforms:
        t_x, t_y, t_w, t_h = plat
        pygame.draw.rect(screen, "yellow", (t_x - camera_x, t_y, t_w, t_h))

    # Player drawing fix (camera_x minus karna zaroori hai taaki circle screen par sahi jagah dikhe)
    pygame.draw.circle(screen, "red", (int(p_x - camera_x), int(p_y)), p_r)

    pygame.display.flip()
    clock.tick(140)

pygame.quit()
sys.exit()
