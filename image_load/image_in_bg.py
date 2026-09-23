import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("iamge load in background screen full size")
clock = pygame.time.Clock()
image_load = pygame.image.load("../images/leaf.jpg")
bg_image = pygame.transform.scale(image_load, (1000, 600))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    screen.blit(bg_image, (0, 0))
    # screen.fill("black")
    pygame.draw.circle(screen, "limegreen", [450, 300], 100)
    # pygame.draw.circle(screen, "orange", [150, 150], 50)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
