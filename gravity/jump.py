import pygame
import sys
import random

pygame.init()

height = 600
width = 1000

world_w = 3000
world_h = height
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Platformer Physics: Gravity & Jumping")
clock = pygame.time.Clock()

c_x, c_y = 100, 300
c_w, c_h = 30, 30
c_r = 30
speed = 5
camera_x = 0

# --- PHYSICS VARIABLES ---
gravity = 0.6  # Neeche khichne ki taakat
vel_y = 0  # Vertical speed (upar ya neeche jane ki raftaar)
jump_strength = -15  # Jump lagane par kitna upar jayega
is_jumping = False  # Check karne ke liye ki player hawa mein hai ya nahi

# Pillars data
pillar_data = []
for i in range(250, world_w, 200):
    p_height = random.randint(150, 400)
    pillar_data.append((i, p_height))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        # Jab Space key dabayein aur player zameen par ho tabhi jump ho
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and not is_jumping:
                vel_y = jump_strength
                is_jumping = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        c_x += speed
    elif keys[pygame.K_LEFT]:
        c_x -= speed

    c_x = max(0, min(c_x, world_w - c_w))

    # --- GRAVITY LOGIC ---
    vel_y += gravity  #  Har frame par gravity speed badhayegi
    c_y += vel_y  # Player ki position mein vertical speed jod do

    # Temporary Ground Level (Zameen - line 450)
    ground_level = height - c_h
    if c_y >= ground_level:
        c_y = ground_level
        # vel_y = 0
        is_jumping = False  # Zameen par aate hi jump reset ho jayega

    # Camera Logic
    camera_x = c_x - (width // 2) + (c_w // 2)
    camera_x = max(0, min(camera_x, world_w - width))

    screen.fill("blue")

    # Draw Pillars
    for i, p_height in pillar_data:
        p_y = height - p_height
        pygame.draw.rect(screen, "yellow", (i - camera_x, p_y, 120, p_height))

    # Draw Player (Red Circle)
    pygame.draw.circle(screen, "red", ((c_x - camera_x), c_y), c_r)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
