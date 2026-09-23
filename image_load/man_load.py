import pygame
import sys
import random
from gradient_function import render_gradient_text

pygame.init()
# info = pygame.display.Info()
# width = info.current_w
# height = info.current_h
height = 600
width = 1000
# screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("this is testing code to show man on the screen")
clock = pygame.time.Clock()

man_x, man_y = 100, 100
man_w, man_h = 100, 100

c_x, c_y = 300, 200
c_w, c_h = 100, 100
c_radius = c_w // 2

r_x, r_y = 400, 300
r_w, r_h = 60, 40

speed = 5

bg_img = pygame.image.load("../images/home.jpg")
bg_img = pygame.transform.scale(bg_img, (width, height))

man_img = pygame.image.load("../images/man.png").convert_alpha()
man_img = pygame.transform.scale(man_img, (man_w, man_h))

game_start_sound = pygame.mixer.Sound("../sounds/game_start.mp3")
game_start_sound.play()

point1_sound = pygame.mixer.Sound("../sounds/pop.mp3")
point2_sound = pygame.mixer.Sound("../sounds/recive.mp3")


font = pygame.font.Font(None, 30)
score = 0

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        man_x -= speed
    if keys[pygame.K_RIGHT]:
        man_x += speed
    if keys[pygame.K_UP]:
        man_y -= speed
    if keys[pygame.K_DOWN]:
        man_y += speed

    c_surface = pygame.Surface((c_w, c_h), pygame.SRCALPHA)
    pygame.draw.circle(c_surface, "yellow", (c_radius, c_radius), c_radius)

    r_surface = pygame.Surface((r_w, r_h), pygame.SRCALPHA)
    pygame.draw.rect(r_surface, "lime", (0, 0, r_w, r_h))

    man_mask = pygame.mask.from_surface(man_img)
    c_mask = pygame.mask.from_surface(c_surface)
    r_mask = pygame.mask.from_surface(r_surface)

    offset1 = (c_x - man_x, c_y - man_y)
    offset2 = (r_x - man_x, r_y - man_y)
    if man_mask.overlap(c_mask, offset1):
        c_x = random.randint(0, width - c_w)
        c_y = random.randint(0, height - c_h)
        score += 5
        point2_sound.play()
    elif man_mask.overlap(r_mask, offset2):
        r_x = random.randint(0, width - r_w)
        r_y = random.randint(0, height - r_h)
        score += 1
        point1_sound.play()

    font_text = render_gradient_text(font, f"score : {score}", (255, 0, 0), (0, 0, 255))

    screen.fill("black")
    screen.blit(bg_img, (0, 0))
    screen.blit(c_surface, (c_x, c_y))
    screen.blit(r_surface, (r_x, r_y))
    screen.blit(man_img, (man_x, man_y))
    screen.blit(font_text, (20, 10))
    pygame.display.flip()
    clock.tick(100)
pygame.quit()
sys.exit()
# if c_x > width:
#     c_x = -c_w
# if c_x < -c_w:
#     c_x = width
