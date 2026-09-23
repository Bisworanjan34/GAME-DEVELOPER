import pygame
import sys
import random

pygame.init()
info = pygame.display.Info()
height = 600
width = 1000
# screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("this is testing code to show car on the screen")
clock = pygame.time.Clock()
c_x, c_y = 100, 500
t_x, t_y = 400, 400
ball_x, ball_y = 900, 550
ball_radius = 10
b2_x, b2_y = 800, 500
b2_radius = 10

speed = 7
bg_img = pygame.image.load("../images/akas.png")
bg_img = pygame.transform.scale(bg_img, (width, height))

car_img = pygame.image.load("../images/redcar.png").convert_alpha()
car_img = pygame.transform.scale(car_img, (50, 50))
car_mask = pygame.mask.from_surface(car_img)

target_img = pygame.image.load("../images/man.png").convert_alpha()
target_img = pygame.transform.scale(target_img, (200, 200))
target_mask = pygame.mask.from_surface(target_img)


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        c_x -= speed
    if keys[pygame.K_RIGHT]:
        c_x += speed
    if keys[pygame.K_UP]:
        c_y -= speed
    if keys[pygame.K_DOWN]:
        c_y += speed

    ball_x -= 3
    b2_x -= 5
    if ball_x > width:
        ball_x = -ball_radius
    if ball_x < -ball_radius:
        ball_x = width
    if b2_x > width:
        b2_x = -b2_radius
    if b2_x < -b2_radius:
        b2_x = width

    offset = (t_x - c_x, t_y - c_y)
    if car_mask.overlap(target_mask, offset):
        t_x = random.randint(100, width - t_x)
        # t_y = random.randint(100, height - t_y)
    if c_x < 0:
        c_x = 0
    if c_x > width - 50:
        c_x = width - 50
    if c_y < height // 2:
        c_y = height // 2
    if c_y > height - 50:
        c_y = height - 50

    screen.fill("black")
    screen.blit(bg_img, (0, -100))
    pygame.draw.circle(screen, "yellow", [160, 80], 20)
    pygame.draw.circle(screen, "lime", [ball_x, ball_y], ball_radius)
    pygame.draw.circle(screen, "cyan", [b2_x, b2_y], b2_radius)
    screen.blit(car_img, (c_x, c_y))
    screen.blit(target_img, (t_x, t_y))
    pygame.display.flip()
    clock.tick(180)
pygame.quit()
sys.exit()
