import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("keyboard to control move the object......")
clock = pygame.time.Clock()
c_x = 100
c_y = 200
c_speed = 6

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                c_x -= c_speed
            if e.key == pygame.K_RIGHT:
                c_x += c_speed
            if e.key == pygame.K_UP:
                c_y -= c_speed
            if e.key == pygame.K_DOWN:
                c_y += c_speed

    screen.fill("navyblue")

    pygame.draw.circle(screen, "yellow", [c_x, c_y], 50)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
