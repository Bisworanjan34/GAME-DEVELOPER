import pygame
import sys
import random

pygame.init()
HEIGHT = 600
WIDTH = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("this is rect touch test between two rect")
clock = pygame.time.Clock()

r_x, r_y = 100, 100
t_x, t_y = 500, 400
speed = 5

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        r_x -= speed
    if keys[pygame.K_RIGHT]:
        r_x += speed
    if keys[pygame.K_UP]:
        r_y -= speed
    if keys[pygame.K_DOWN]:
        r_y += speed

    player_rect = pygame.Rect(r_x, r_y, 100, 50)
    target_rect = pygame.Rect(t_x, t_y, 150, 55)

    if player_rect.colliderect(target_rect):
        t_x = random.randint(100, WIDTH - 150)
        t_y = random.randint(100, HEIGHT - 150)
    screen.fill("white")

    pygame.draw.rect(screen, "limegreen", player_rect)
    pygame.draw.rect(screen, "blue", target_rect)

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
sys.exit()
