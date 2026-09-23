import pygame
import sys

pygame.init()
height = 600
width = 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("this is a code for text in center of screen")
game_state = "START"

p_x, p_y = 100, 20
p_w, p_h = 100, 100

e_x, e_y = 400, 300
e_w, e_h = 60, 60

e_speed = 3
speed = 5

game_start_bg = pygame.image.load("../images/home.jpg")
pygame.transform.scale(game_start_bg, (width, height))
game_playing_bg = pygame.image.load("../images/home.jpg")
pygame.transform.scale(game_playing_bg, (width, height))

p_sur = pygame.image.load("../images/man.png").convert_alpha()
p_sur = pygame.transform.scale(p_sur, (p_w, p_h))
e_sur = pygame.image.load("../images/gunman.png").convert_alpha()
e_sur = pygame.transform.scale(e_sur, (e_w, e_h))


text = pygame.font.Font("../fonts/font2.otf", 20)
button_rect = pygame.Rect(width // 2 - 150, height // 2 - 25, 300, 50)
game_over_text = pygame.font.Font("../fonts/designer.otf", 60)
game_over_text_p = pygame.font.Font("../fonts/font2.otf", 20)

button_sound = pygame.mixer.Sound("../sounds/pop.mp3")
game_start_sound = pygame.mixer.Sound("../sounds/game_start.mp3")
game_over_sound = pygame.mixer.Sound("../sounds/game_over.mp3")
enemy_collision_sound = pygame.mixer.Sound("../sounds/boomb.mp3")
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "START" and button_rect.collidepoint(e.pos):
                game_state = "PLAYING"
                button_sound.play()
                game_start_sound.play()

        if e.type == pygame.KEYDOWN:
            if game_state == "GAMEOVER" and e.key == pygame.K_r:
                game_state = "PLAYING"
                p_x, p_y = 100, 100
                game_start_sound.play()

    if game_state == "START":
        screen.fill("black")
        screen.blit(game_start_bg, (0, 0))
        pygame.draw.rect(screen, "blue", button_rect, border_radius=6)
        text_sur = text.render(("button click").title(), True, ("white"))
        text_rect = text_sur.get_rect(center=button_rect.center)
        screen.blit(text_sur, text_rect)
    elif game_state == "PLAYING":
        e_x += e_speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            p_y -= speed
        if keys[pygame.K_DOWN]:
            p_y += speed

        p_mask = pygame.mask.from_surface(p_sur)
        e_mask = pygame.mask.from_surface(e_sur)

        offset = (e_x - p_x, e_y - p_y)
        if p_mask.overlap(e_mask, offset):
            game_state = "GAMEOVER"
            game_over_sound.play()
        if e_x > width:
            e_x = -e_w
        if e_x < -e_w:
            e_x = width
        screen.fill("black")
        screen.blit(game_playing_bg, (0, 0))
        screen.blit(p_sur, (p_x, p_y))
        screen.blit(e_sur, (e_x, e_y))

    elif game_state == "GAMEOVER":
        screen.fill("black")
        g_over_t = game_over_text.render("GAME OVER", True, "red")
        g_over_t_rect = g_over_t.get_rect(center=(width // 2, height // 2))
        g_over_p = game_over_text_p.render("PRESS R TO RESTART GAME", True, "white")
        g_over_p_rect = g_over_p.get_rect(center=(width // 2, height // 2 + 100))

        screen.blit(g_over_t, g_over_t_rect)
        screen.blit(g_over_p, g_over_p_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(100)
pygame.quit()
sys.exit()
