import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption(
    "this is press key test which key press that will auto detect using magic function"
)
clock = pygame.time.Clock()
box_x = 100
box_y = 100
box_speed = 8

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        box_x -= box_speed
    if keys[pygame.K_RIGHT]:
        box_x += box_speed
    if keys[pygame.K_UP]:
        box_y -= box_speed
    if keys[pygame.K_DOWN]:
        box_y += box_speed

    if box_x > 1000:
        box_x = -300
    if box_x < -300:
        box_x = 1000

    screen.fill("black")

    pygame.draw.rect(screen, "lime", [box_x, box_y, 300, 100])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
