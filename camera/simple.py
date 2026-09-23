import pygame
import sys

pygame.init()
screen_width, screen_height = 1000, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Virtual Camera & Scrolling Test")
clock = pygame.time.Clock()

# World size screen se bada hai
world_width = 3000
world_height = 600

man_x, man_y = 100, 350
man_w, man_h = 200, 200
speed = 5

# Camera offset variable
cam_x = 0

side_sheet = pygame.image.load("../images/sheet/ninja_walk.png").convert_alpha()
total_frame = 25
cols, rows = 5, 5


def load_frames(sheet):
    frames = []
    frame_w = sheet.get_width() // cols
    frame_h = sheet.get_height() // rows
    for i in range(total_frame):
        col = i % cols
        row = i // cols
        frame = sheet.subsurface((col * frame_w, row * frame_h, frame_w, frame_h))
        frame = pygame.transform.scale(frame, (man_w, man_h))
        frames.append(frame)
    return frames


side_frames = load_frames(side_sheet)
current_frame = 0
timer = 0
right_face = True

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    moving = False

    if keys[pygame.K_LEFT]:
        man_x -= speed
        moving = True
        right_face = False
    if keys[pygame.K_RIGHT]:
        man_x += speed
        moving = True
        right_face = True

    # Player ko world ke andar rokna (boundaries)
    man_x = max(0, min(man_x, world_width - man_w))
    # --- VIRTUAL CAMERA LOGIC ---
    # Camera player ko screen ke center mein rakhne ki koshish karega
    cam_x = man_x - (screen_width // 2) + (man_w // 2)

    # Camera ko world ke bahar jane se rokna
    cam_x = max(0, min(cam_x, world_width - screen_width))

    if moving:
        timer += 1
        if timer >= 5:
            timer = 0
            current_frame = (current_frame + 1) % total_frame
    else:
        current_frame = 0
        timer = 0

    screen.fill((40, 40, 40))

    # Background mein kuch objects banate hain taaki scrolling saaf dikhe
    # Har object ke X coordinate mein se 'cam_x' minus karna zaroori hai!
    for i in range(0, world_width, 200):
        pygame.draw.rect(screen, ("green"), (i - cam_x, 300, 60, 200))
        # Pata chalane ke liye pillar par numbers draw kar sakte hain

    # Player draw karte waqt bhi '- cam_x' use hoga
    current_img = side_frames[current_frame]
    if not right_face:
        current_img = pygame.transform.flip(current_img, True, False)
    screen.blit(current_img, (man_x - cam_x, man_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
