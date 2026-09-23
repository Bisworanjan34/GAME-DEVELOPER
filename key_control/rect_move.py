import pygame
import sys

pygame.init()
HEIGHT = 600
WIDTH = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("THIS IS RECTANGULAR MOVING BY KEY CONTROL")
clock = pygame.time.Clock()

rect_x = 100
rect_y = 100
rect_speed = 1
more_speed = 22
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                rect_y -= more_speed
            if e.key == pygame.K_DOWN:
                rect_y += more_speed

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    if rect_x > WIDTH:
        rect_x = -400
    if rect_x < -400:
        rect_x = WIDTH
    if rect_y > HEIGHT:
        rect_y = -100
    if rect_y < -100:
        rect_y = HEIGHT

    screen.fill("navy")
    pygame.draw.rect(screen, "yellow", [rect_x, rect_y, 400, 100])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
