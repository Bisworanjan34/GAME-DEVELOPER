import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("this is a program to show the text on the screen")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

# pygame.mixer.music.load("../sounds/game_start.mp3")
# pygame.mixer.music.play(1)
# pygame.mixer.music.set_volume(0.5)

game_start_sound = pygame.mixer.Sound("../sounds/game_start.mp3")
game_start_sound.play()
game_over_sound = pygame.mixer.Sound("../sounds/game_over.mp3")


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            game_over_sound.play()
            pygame.time.delay(2000)

    font_surface = font.render("Welcome to pygame", True, "white")
    screen.fill("black")
    screen.blit(font_surface, (1000 // 2, 20))
    pygame.draw.circle(screen, "red", (300, 200), 100)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
