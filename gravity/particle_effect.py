print("gravity practice jump coding with Particles..........")
import pygame
import sys
import random

# starting the engine
pygame.init()

height = 600
width = 1000
world_w = 3000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Platforms + Dust Particle Effects")
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

# --- PARTICLE LIST ---
# Format: [x, y, vx, vy, radius, life]
particles = []


def create_particles(x, y):
    # Jab jump kare ya land kare, toh 6-8 particles nikalenge
    for _ in range(8):
        vx = random.uniform(-2, 2)
        vy = random.uniform(-1, -3)  # Thoda upar ki taraf udhenge
        radius = random.randint(3, 6)
        life = 25  # Kitne frames tak particle zinda rahega
        particles.append([x, y, vx, vy, radius, life])


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and not is_jump:
                vel_y = jump_s
                is_jump = True
                # Jump karte waqt particles create karo (player ke pero ke paas)
                create_particles(p_x, p_y + p_r)

    keys = pygame.key.get_pressed()
    dx = 0
    if keys[pygame.K_LEFT]:
        dx -= speed
    elif keys[pygame.K_RIGHT]:
        dx += speed
    p_x += dx

    # --- 1. PLATFORMS POSITION UPDATE ---
    for plat in platforms:
        plat[1] += plat[6]
        if plat[1] < plat[4] or plat[1] > plat[5]:
            plat[6] *= -1

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
    old_vel_y = vel_y  # Check karne ke liye ki pehle gir raha tha ya nahi
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
            if vel_y > 0 and (p_y - p_r) <= t_y + 10:
                # Agar pehle hawa mein tha aur abhi land hua hai, toh landing particles banao
                if is_jump or old_vel_y > 2:
                    create_particles(p_x, t_y)

                p_y = t_y - p_r
                vel_y = plat[6]
                is_jump = False
                on_platform = True
            else:
                p_y -= vel_y
                if vel_y > 0:
                    is_jump = False
                vel_y = 0
            break

    # Ground level collision
    ground_level = height - p_r
    if p_y > ground_level:
        if is_jump or old_vel_y > 2:
            create_particles(p_x, ground_level + p_r)

        p_y = ground_level
        is_jump = False
        vel_y = 0

    p_x = max(p_r, min(p_x, world_w - p_r))
    camera_x = max(0, min(p_x - (width // 2), world_w - width))

    # --- 4. UPDATE PARTICLES ---
    for p in particles[:]:
        p[0] += p[2]  # x movement (vx)
        p[1] += p[3]  # y movement (vy)
        p[4] -= 0.1  # Radius kam hota jayega (shrum hoga)
        p[5] -= 1  # Life kam hoti jayegi
        if p[5] <= 0 or p[4] <= 0:
            particles.remove(p)

    # --- DRAWING ---
    screen.fill("blue")

    # Draw Platforms
    for plat in platforms:
        t_x, t_y, t_w, t_h = plat[:4]
        pygame.draw.rect(screen, "yellow", (t_x - camera_x, t_y, t_w, t_h))

    # Draw Dust Particles (White/Gray dots)
    for p in particles:
        p_draw_x = int(p[0] - camera_x)
        p_draw_y = int(p[1])
        pygame.draw.circle(
            screen, (200, 200, 200), (p_draw_x, p_draw_y), max(1, int(p[4]))
        )

    # Draw Player
    pygame.draw.circle(screen, "red", (int(p_x - camera_x), int(p_y)), p_r)

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
sys.exit()
