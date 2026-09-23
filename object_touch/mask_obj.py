import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Professional Mask Collision")
clock = pygame.time.Clock()

# Player aur Target ki positions
player_x, player_y = 100, 100
player_speed = 6

target_x, target_y = 500, 300
surf_size = 50

p_h, p_w = 50, 50
p_r = p_w // 2
t_w, t_h = 350, 230
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    # Keyboard Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # --- PROFESSIONAL MASK LOGIC ---

    # 1. Player ke liye surface aur uska exact Mask banana
    player_surf = pygame.Surface((p_h, p_w), pygame.SRCALPHA)
    pygame.draw.circle(player_surf, (0, 150, 255), (p_r, p_r), p_r)
    player_mask = pygame.mask.from_surface(player_surf)

    # 2. Target ke liye surface aur uska exact Mask banana
    target_surf = pygame.Surface((t_w, t_h), pygame.SRCALPHA)
    pygame.draw.polygon(
        target_surf, ("limegreen"), [(t_w // 2, 0), (0, t_h), (t_w, t_h)]
    )
    target_mask = pygame.mask.from_surface(target_surf)

    # 3. Dono ke beech ka distance (offset) nikalna
    offset = (target_x - player_x, target_y - player_y)

    # 4. Exact Pixel Collision Check (`overlap` function)
    if player_mask.overlap(target_mask, offset):
        target_x = random.randint(100, 900)
        target_y = random.randint(100, 500)

    # Screen clear karo
    screen.fill((15, 15, 15))

    # Surfaces ko screen par draw (blit) karna
    screen.blit(player_surf, (player_x, player_y))
    screen.blit(target_surf, (target_x, target_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
