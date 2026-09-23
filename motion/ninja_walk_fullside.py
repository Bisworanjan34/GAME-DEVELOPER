import pygame
import sys

pygame.init()
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("this for ninja ful side animationa walking tasing")
clock = pygame.time.Clock()
ninja_x, ninja_y = 100, 300
ninja_w, ninja_h = 150, 150
speed = 1
bg_img = pygame.image.load("../images/green.jpg")

side_sheet = pygame.image.load("../images/sheet/ninja_walk.png").convert_alpha()
up_sheet = pygame.image.load("../images/sheet/ninja-walk-up.png").convert_alpha()
down_sheet = pygame.image.load("../images/sheet/ninja-walk-down.png").convert_alpha()

total_frame = 25
cols = 5
rows = 5
try:

    def load_frames(sheet):
        frames = []
        frame_w = sheet.get_width() // cols
        frame_h = sheet.get_height() // rows
        for i in range(total_frame):
            col = i % cols
            row = i // cols
            x = col * frame_w
            y = row * frame_h

            frame = sheet.subsurface(x, y, frame_w, frame_h)
            frame = pygame.transform.scale(frame, (ninja_w, ninja_h))
            frames.append(frame)
        return frames
except Exception as e:
    pass

side_frames = load_frames(side_sheet)
up_frames = load_frames(up_sheet)
down_frames = load_frames(down_sheet)

current_frame = 0
timer = 0
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    right_face = True
    moving = False
    animation_frame = side_frames

    if keys[pygame.K_LEFT]:
        ninja_x -= speed
        moving = True
        right_face = False
        animation_frame = side_frames

    elif keys[pygame.K_RIGHT]:
        ninja_x += speed
        moving = True
        right_face = True
        animation_frame = side_frames
    elif keys[pygame.K_UP]:
        ninja_y -= speed
        moving = True
        animation_frame = up_frames
    elif keys[pygame.K_DOWN]:
        ninja_y += speed
        moving = True
        animation_frame = down_frames
    ninja_x %= width
    ninja_y %= height

    if moving:
        timer += 1
        if timer >= 5:
            timer = 0
            current_frame = (current_frame + 1) % total_frame
    else:
        current_frame = 0
        timer = 0

    current_img = animation_frame[current_frame]
    if not right_face and animation_frame == side_frames:
        current_img = pygame.transform.flip(current_img, True, False)
    screen.fill("black")
    screen.blit(bg_img, (0, 0))
    screen.blit(current_img, (ninja_x, ninja_y))
    pygame.display.flip()
    clock.tick(100)
pygame.quit()
sys.exit()
