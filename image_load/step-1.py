import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Image Loading Example")
clock = pygame.time.Clock()

# --- STEP 1: Image Load karo ---
# (Apne folder ki kisi bhi PNG image ka naam yahan daal dena)
player_img = pygame.image.load("../images/nbg.webp")

# Agar image bohot badi hai, toh use chhota bhi kar sakte hain (Optional):
# player_img = pygame.transform.scale(player_img, (100, 100))

# --- STEP 2: Image ka rectangle (position) lo ---
player_rect = player_img.get_rect()
player_rect.x = 400  # Initial X position
player_rect.y = 250  # Initial Y position
speed = 5

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    # Keyboard se image ko move karane ke liye magic function
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if keys[pygame.K_UP]:
        player_rect.y -= speed
    if keys[pygame.K_DOWN]:
        player_rect.y += speed

    # Screen ko saaf karo
    screen.fill((30, 30, 30))

    # --- STEP 3: Image ko screen par draw (blit) karo ---
    screen.blit(player_img, player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
