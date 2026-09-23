import pygame
import sys

pygame.init()
height = 600
width = 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("this is a code for text in center of screen")

text = pygame.font.Font("../fonts/font2.otf", 20)
button_rect = pygame.Rect(width // 2 - 150, height // 2 - 25, 300, 50)

button_sound = pygame.mixer.Sound("../sounds/pop.mp3")

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(e.pos):
                button_sound.play()
            else:
                pass

    screen.fill("black")
    pygame.draw.rect(screen, "red", button_rect, border_radius=6)

    text_sur = text.render(("button click").title(), True, ("white"))
    text_rect = text_sur.get_rect(center=button_rect.center)
    screen.blit(text_sur, text_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(100)
pygame.quit()
sys.exit()
