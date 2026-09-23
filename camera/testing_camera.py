import pygame
import sys
import random

pygame.init()

height = 600
width = 1000

world_w = 3000
world_h = height
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("testing camera position big map")
bg_img = pygame.image.load("../images/green.jpg")
c_x, c_y = 100, 400
c_w, c_h = 30, 30
c_r = 30
speed = 5
camera_x = 0
clock = pygame.time.Clock()
pillar_data = []
for i in range(0, world_w, 100):
    p_height = random.randint(150, 500)
    pillar_data.append((i, p_height))
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        c_x += speed
    elif keys[pygame.K_LEFT]:
        c_x -= speed
    c_x = max(0, min(c_x, world_w - c_w))
    camera_x = c_x - (width // 2) + (c_w // 2)
    camera_x = max(0, min(camera_x, world_w - width))

    screen.fill("black")
    screen.blit(bg_img, (0, 0))
    # for i in range(0, world_w, 200):
    #     pygame.draw.rect(screen, (10, 156, 8), (i - camera_x, 0, 80, 300))
    for i, p_height in pillar_data:
        # Y position aisi rakhi hai ki pillars zameen (bottom) se upar ki taraf uthe hon
        p_y = height - p_height
        pygame.draw.rect(screen, "orange", (i - camera_x, p_y, 50, p_height))
    pygame.draw.circle(screen, "yellow", (c_x - camera_x, c_y), c_r)

    pygame.display.flip()
    clock.tick(100)
pygame.quit()
sys.exit()
