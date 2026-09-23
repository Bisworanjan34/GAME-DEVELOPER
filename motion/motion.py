import pygame
import sys
import random

pygame.init()
height = 600
width = 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("this is tasting motion walk")
clock = pygame.time.Clock()
man_x, man_y = 100, 300
man_w, man_h = 250, 250
speed = 3

sheet_img = pygame.image.load("../images/sheet/ninja-walk-down.png")
total_frame = 25
cols = 5
rows = 5
frame_w = sheet_img.get_width() // cols
frame_h = sheet_img.get_height() // rows

animation_frames = []
try:
    for i in range(total_frame):
        col = i % cols
        row = i // cols
        x = col * frame_w
        y = row * frame_h

        frame = sheet_img.subsurface((x, y, frame_w, frame_h))
        frame = pygame.transform.scale(frame, (man_w, man_h))
        animation_frames.append(frame)

except Exception as e:
    frame = pygame.Surface((man_w, man_h).pygame.SRCALPHA)
    pygame.draw.circle(frame, "red", (man_x, man_w), 50)
    animation_frames.append(frame)
current_frame = 0
timer = 0
right_face = True
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    is_moving = False
    if keys[pygame.K_LEFT]:
        man_x -= speed
        right_face = False
        is_moving = True
    if keys[pygame.K_RIGHT]:
        man_x += speed
        is_moving = True
        right_face = True
    if keys[pygame.K_UP]:
        man_y -= speed
        is_moving = True
    if keys[pygame.K_DOWN]:
        man_y += speed
        is_moving = True
    man_x %= width
    man_y %= height
    if is_moving:
        timer += 1
        if timer >= 5:
            timer = 0
            current_frame = (current_frame + 1) % total_frame
    else:
        timer = 0
        current_frame = 0
    screen.fill("brown")
    current_img = animation_frames[current_frame]

    if not right_face:
        current_img = pygame.transform.flip(current_img, True, False)
    screen.blit(current_img, (man_x, man_y))
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
sys.exit()
