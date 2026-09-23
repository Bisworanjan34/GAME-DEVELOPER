import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("pygame testing ")
clock = pygame.time.Clock()

# colors
BLACK = "black"
RED = "red"
LIME = "lime"
BLUE = "blue"

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_c:
                print("u click c ")
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_b:
                print("u hold press b key")
    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, [500, 100, 300, 100])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
