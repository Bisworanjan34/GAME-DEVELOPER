import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("this is a time concept ")
timer_font = pygame.font.Font(None, 30)
start_tick = 0
total_time = 5

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.K_s:
            pass
    pygame.time.get_ticks()
    screen.fill("black")
    seconds = (pygame.time.get_ticks() - start_tick) // 1000
    time_left = total_time - seconds
    if time_left <= 0:
        time_sur = timer_font.render("time end", True, "white")
        screen.blit(time_sur, (1000 // 2, 600 // 2))

    pygame.draw.circle(screen, "red", (50, 50), 50)
    if time_left >= 0:
        time_sur = timer_font.render(f"time start : {time_left}", True, "white")
        screen.blit(time_sur, (1000 // 2, 600 // 2))
    else:
        pass
    pygame.display.flip()
    pygame.time.Clock().tick(50)
pygame.quit()
sys.exit()
