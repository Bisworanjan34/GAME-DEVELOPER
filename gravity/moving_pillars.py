print("gravity practice jump coding..........")
import pygame
import sys
import random

# starting the engine
pygame.init()

height = 600
width = 1000
world_w = 3000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Platforms - Perfect Standing Logic")
clock = pygame.time.Clock()

p_x, p_y = 100, 100
p_r = 20
speed = 6
camera_x = 0

gravity = 0.6
vel_y = 0
jump_s = -20
is_jump = False

# Moving Horizontal Platforms (Format: [x, y, w, h, min_y, max_y, move_speed])
platforms = []
for i in range(200, world_w, 350):
    y = random.randint(200, 450)
    platforms.append([i, y, 200, 20, y - 80, y + 80, 2])

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
    p_x += dx

    # --- 1. PLATFORMS POSITION UPDATE ---
    for plat in platforms:
        plat[1] += plat[6]  # y position change
        if plat[1] < plat[4] or plat[1] > plat[5]:
            plat[6] *= -1  # Reverse direction

    # Player Mask
    p_sur = pygame.Surface((p_r * 2, p_r * 2), pygame.SRCALPHA)
    pygame.draw.circle(p_sur, "red", (p_r, p_r), p_r)
    p_mask = pygame.mask.from_surface(p_sur)

    # --- 2. X-AXIS COLLISION ---
    for plat in platforms:
        t_x, t_y, t_w, t_h = plat[:4]
        t_sur = pygame.Surface((t_w, t_h), pygame.SRCALPHA)
        t_sur.fill("green")
        t_mask = pygame.mask.from_surface(t_sur)
        offset_x = (t_x - (p_x - p_r), t_y - (p_y - p_r))
        if p_mask.overlap(t_mask, offset_x):
            p_x -= dx
            break

    # --- 3. Y-AXIS COLLISION & GRAVITY ---
    vel_y += gravity
    p_y += vel_y

    on_platform = False
    for plat in platforms:
        t_x, t_y, t_w, t_h = plat[:4]
        t_sur = pygame.Surface((t_w, t_h), pygame.SRCALPHA)
        t_sur.fill("green")
        t_mask = pygame.mask.from_surface(t_sur)
        offset_y = (t_x - (p_x - p_r), t_y - (p_y - p_r))

        if p_mask.overlap(t_mask, offset_y):
            # Agar player upar se aa raha hai (falling down) aur platform ke upar land kar raha hai
            if vel_y > 0 and (p_y - p_r) <= t_y + 10:
                p_y = t_y - p_r  # Player ko bilkul platform ke upar chipka do
                vel_y = plat[
                    6
                ]  # Platform ki speed ke sath player ko bhi move karao taaki hold rahe!
                is_jump = False
                on_platform = True
            else:
                # Agar side ya bottom se takraya
                p_y -= vel_y
                if vel_y > 0:
                    is_jump = False
                vel_y = 0
            break

    # Ground level collision
    ground_level = height - p_r
    if p_y > ground_level:
        p_y = ground_level
        is_jump = False
        vel_y = 0

    p_x = max(p_r, min(p_x, world_w - p_r))
    camera_x = max(0, min(p_x - (width // 2), world_w - width))

    # --- DRAWING ---
    screen.fill("blue")

    for plat in platforms:
        t_x, t_y, t_w, t_h = plat[:4]
        pygame.draw.rect(screen, "yellow", (t_x - camera_x, t_y, t_w, t_h))

    pygame.draw.circle(screen, "red", (int(p_x - camera_x), int(p_y)), p_r)
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
sys.exit()
