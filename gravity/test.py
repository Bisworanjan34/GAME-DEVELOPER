import pygame
import sys

pygame.init()
width, height = 1000, 600
world_width, world_height = 3000, height
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("tasting gravity power - Fixed")
clock = pygame.time.Clock()

# Player Properties (Circle ke badle hum Rect bhi use karenge collision ke liye)
p_x, p_y = 100, 400
p_r = 25
p_w, p_h = p_r * 2, p_r * 2
speed = 6

gravity = 0.6
vel_y = 0
jump_s = -20
is_jump = False

# Pillars / Platforms Data (Multiple pillars with different heights)
# Format: [x, y, width, height]
platforms = []
for i in range(400, world_width - 200, 300):
    p_h_val = 300
    p_y_val = height - p_h_val
    platforms.append(pygame.Rect(i, p_y_val, 90, p_h_val))

camera_x = 0

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and not is_jump:
                vel_y = jump_s
                is_jump = True

    # --- 1. X-AXIS MOVEMENT & COLLISION ---
    keys = pygame.key.get_pressed()
    dx = 0
    if keys[pygame.K_LEFT]:
        dx = -speed
    elif keys[pygame.K_RIGHT]:
        dx = speed

    p_x += dx

    # Create player rect for X check
    player_rect = pygame.Rect(p_x - p_r, p_y - p_r, p_w, p_h)

    # Check side collisions with platforms
    for plat in platforms:
        if player_rect.colliderect(plat):
            if dx > 0:  # Right ja raha hai aur pillar se takraya
                p_x = plat.left - p_r
            elif dx < 0:  # Left ja raha hai aur pillar se takraya
                p_x = plat.right + p_r

    # --- 2. Y-AXIS MOVEMENT & GRAVITY / COLLISION ---
    vel_y += gravity
    p_y += vel_y

    # Update player rect for Y check
    player_rect = pygame.Rect(p_x - p_r, p_y - p_r, p_w, p_h)

    # Floor collision (Screen bottom)
    ground_level = height - p_r
    if p_y >= ground_level:
        p_y = ground_level
        vel_y = 0
        is_jump = False

    # Platform Y collisions (Upar land karna ya neeche se takrana)
    for plat in platforms:
        if player_rect.colliderect(plat):
            if (
                vel_y > 0
            ):  # Jab player neeche gir raha ho aur pillar ke top par land kare
                p_y = plat.top - p_r
                vel_y = 0
                is_jump = False
            elif vel_y < 0:  # Jab player upar jump kare aur pillar ke neeche se takraye
                p_y = plat.bottom + p_r
                vel_y = 0
    if p_y < 0:
        p_y = vel_y

    # World boundaries
    p_x = max(p_r, min(p_x, world_width - p_r))

    # --- 3. CAMERA LOGIC ---
    camera_x = p_x - (width // 2)
    camera_x = max(0, min(camera_x, world_width - width))

    # --- 4. DRAWING ---
    screen.fill("black")

    # Draw all platforms/pillars
    for plat in platforms:
        # Screen position ke liye camera_x minus karna zaroori hai
        screen_rect = pygame.Rect(plat.x - camera_x, plat.y, plat.width, plat.height)
        pygame.draw.rect(screen, "yellow", screen_rect)

    # Draw Player (Orange Circle)
    pygame.draw.circle(screen, "orange", (int(p_x - camera_x), int(p_y)), p_r)

    pygame.display.flip()
    clock.tick(80)

pygame.quit()
sys.exit()
