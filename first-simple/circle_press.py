import pygame
import sys

pygame.init()

HEIGHT = 600
WIDTH = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("circle key press move testing")
clock = pygame.time.Clock()
c_x = 100
c_y = 100
c_speed = 5
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        c_x -= c_speed
    if keys[pygame.K_RIGHT]:
        c_x += c_speed
    if keys[pygame.K_UP]:
        c_y -= c_speed
    if keys[pygame.K_DOWN]:
        c_y += c_speed

    if c_x > WIDTH:
        c_x = -100
    if c_x < -100:
        c_x = WIDTH
    if c_y > HEIGHT:
        c_y = -100
    if c_y < -100:
        c_y = HEIGHT

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, "green", [c_x, c_y], 100)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
