import pygame
import sys

pygame.init()
height = 600
width = 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("this is a code for text in center of screen")

text1 = pygame.font.Font("../fonts/designer.otf", 60)
text2 = pygame.font.Font("../fonts/font2.otf", 20)
text3 = pygame.font.Font("../fonts/font2.otf", 25)

button_rect = pygame.Rect(width // 2 - 150, height // 2 - 140, 300, 80)


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    screen.fill("black")
    pygame.draw.rect(screen, "red", button_rect, border_radius=10)
    text_sur = text1.render(("welcome biswo-dev").upper(), True, "red")
    text_sur1 = text2.render(("universe game developer").upper(), True, "white")
    text_rect = text_sur.get_rect(center=(width // 2, height // 2))
    text_rect1 = text_sur1.get_rect(center=(width // 2, height // 2 + 80))
    text_sur3 = text3.render("start game", True, "white")
    text_rect3 = text_sur3.get_rect(center=button_rect.center)
    screen.blit(text_sur3, text_rect3)

    screen.blit(text_sur, text_rect)
    screen.blit(text_sur1, text_rect1)

    pygame.display.flip()
    pygame.time.Clock().tick(100)
pygame.quit()
sys.exit()
