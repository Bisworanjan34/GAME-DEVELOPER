import pygame
import sys
import random

# starting the engine
pygame.init()

height = 600
width = 1000
world_w = 3000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("this is for tasting jump+gravity and moving and collision")
clock = pygame.time.Clock()

p_x, p_y = 100, 100
p_r = 20
speed = 6
camera_x = 0

gravity = 0.6
vel_y = 0
jump_s = -16
is_jump = False
# Upar wale pillars (Top se shuru honge)
platforms1 = []
for i in range(200, world_w, 150):
    h = random.randint(100, 250)
    platforms1.append([i, 0, 80, h])

# Neeche wale pillars (Bottom se shuru honge) - Yahan pehle platforms1 likh diya tha tune!
platforms2 = []
for i in range(180, world_w, 180):
    h = random.randint(100, 250)
    platforms2.append([i, height - h, 80, h])

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and not is_jump:
                vel_y = jump_s
                is_jump = True
            if e.key == pygame.K_UP:
                vel_y = jump_s // 2
                # is_jump = True
        # ----------------------------
    keys = pygame.key.get_pressed()
    dx = 0
    if keys[pygame.K_LEFT]:
        dx -= speed
    elif keys[pygame.K_RIGHT]:
        dx += speed
    p_x += dx

    p_sur = pygame.Surface((p_r * 2, p_r * 2), pygame.SRCALPHA)
    pygame.draw.circle(p_sur, "red", (p_r, p_r), p_r)
    p_mask = pygame.mask.from_surface(p_sur)

    # x axis collision
    for plat in platforms1:
        t_x, t_y, t_w, t_h = plat
        t_sur = pygame.Surface((t_w, t_h), pygame.SRCALPHA)
        t_sur.fill("green")
        t_mask = pygame.mask.from_surface(t_sur)

        offset_x = (t_x - (p_x - p_r), t_y - (p_y - p_r))

        if p_mask.overlap(t_mask, offset_x):
            p_x -= dx
    for plat in platforms2:
        t_x, t_y, t_w, t_h = plat
        t_sur = pygame.Surface((t_w, t_h), pygame.SRCALPHA)
        t_sur.fill("green")
        t_mask = pygame.mask.from_surface(t_sur)

        offset_x = (t_x - (p_x - p_r), t_y - (p_y - p_r))

        if p_mask.overlap(t_mask, offset_x):
            p_x -= dx

    vel_y += gravity
    p_y += vel_y

    # y axis collision ....
    for plat in platforms1:
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
            print("game_ver...")
            break
    for plat in platforms2:
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
    ground_level = height - p_r
    if p_y > ground_level:
        p_y = ground_level
        is_jump = False
        vel_y = 0

    p_x = max(p_r, min(p_x, world_w - p_r))
    camera_x = max(0, min(p_x - (width // 2), world_w - width))

    screen.fill("blue")
    for plat in platforms1:
        t_x, t_y, t_w, t_h = plat
        pygame.draw.rect(screen, "yellow", (t_x - camera_x, t_y, t_w, t_h))
    for plat in platforms2:
        t_x, t_y, t_w, t_h = plat
        pygame.draw.rect(screen, "white", (t_x - camera_x, t_y, t_w, t_h))
    pygame.draw.circle(screen, "red", (p_x - camera_x, p_y), p_r)
    pygame.display.flip()
    clock.tick(100)
pygame.quit()
sys.exit()
