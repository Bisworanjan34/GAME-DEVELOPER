# main.py
import pygame
import sys
from settings import (
    WIDTH,
    HEIGHT,
    FPS,
    INITIAL_LIVES,
    WINNING_SCORE,
    TARGET2_SPEED,
    TARGET3_SPEED,
)
from player import Player
from target import Target

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Professional OOP 2D Game")
clock = pygame.time.Clock()

game_state = "START"
score = 0
life = INITIAL_LIVES

# Instances create karna (Objects)
player = Player()
target1 = Target(400, 500, 60, 60, speed=0, color="yellow")
target2 = Target(200, 300, 50, 50, speed=TARGET2_SPEED, color="red")
target3 = Target(300, 450, 40, 40, speed=TARGET3_SPEED, color="blue")

# Assets Load
bg_img = pygame.image.load("../images/green.jpg")
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

game_start_img = pygame.image.load("../images/home.jpg")
game_start_img = pygame.transform.scale(game_start_img, (WIDTH, HEIGHT))

# Sounds
pygame.mixer.music.load("../sounds/forest.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.6)

GAME_START_SOUND = pygame.mixer.Sound("../sounds/game_start.mp3")
GAME_POINT_SOUND = pygame.mixer.Sound("../sounds/recive.mp3")
GAME_OVER_SOUND = pygame.mixer.Sound("../sounds/game_over.mp3")
PLAYER_FOOTSTEP = pygame.mixer.Sound("../sounds/game1.wav")
BOOMB_SOUND = pygame.mixer.Sound("../sounds/boomb.mp3")

# Fonts
game_start_title = pygame.font.Font("../fonts/robot.otf", 30)
game_score_title = pygame.font.Font("../fonts/font2.otf", 25)
game_life = pygame.font.Font("../fonts/font3.otf", 20)
game_over_title = pygame.font.Font("../fonts/designer.otf", 80)
game_over_score = pygame.font.Font("../fonts/designer.otf", 30)
game_over_description = pygame.font.Font("../fonts/font9.ttf", 30)
game_restart = pygame.font.Font("../fonts/font17.ttf", 25)

start_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 30, 200, 60)
restart_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 90, 200, 60)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if game_state == "START" and event.key == pygame.K_RETURN:
                game_state = "PLAYING"
                GAME_START_SOUND.play()
            elif game_state == "GAMEOVER" and event.key == pygame.K_r:
                life = INITIAL_LIVES
                score = 0
                player.reset(50, 50)
                game_state = "PLAYING"
                GAME_START_SOUND.play()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "START" and start_button_rect.collidepoint(event.pos):
                game_state = "PLAYING"
                GAME_START_SOUND.play()
            elif game_state == "GAMEOVER" and restart_button_rect.collidepoint(
                event.pos
            ):
                life = INITIAL_LIVES
                score = 0
                player.reset(50, 50)
                game_state = "PLAYING"
                GAME_START_SOUND.play()

    if game_state == "START":
        screen.fill("black")
        screen.blit(game_start_img, (0, 0))
        pygame.draw.rect(screen, "white", start_button_rect, border_radius=10)
        btn_text = game_start_title.render("GAME START", True, "black")
        btn_text_rect = btn_text.get_rect(center=start_button_rect.center)
        screen.blit(btn_text, btn_text_rect)

    elif game_state == "PLAYING":
        # Target updates
        target2.update()
        target3.update()

        # Player Movement
        keys = pygame.key.get_pressed()
        moving = player.update(keys)

        # Footstep Sound Control
        if moving:
            if not pygame.mixer.Channel(1).get_busy():
                pygame.mixer.Channel(1).play(PLAYER_FOOTSTEP)
        else:
            pygame.mixer.Channel(1).stop()

        # Collision Offsets & Masks
        offset1 = (target1.rect.x - player.rect.x, target1.rect.y - player.rect.y)
        offset2 = (target2.rect.x - player.rect.x, target2.rect.y - player.rect.y)
        offset3 = (target3.rect.x - player.rect.x, target3.rect.y - player.rect.y)

        # Collisions Logic
        if player.mask.overlap(target1.mask, offset1):
            target1.respawn()
            score += 5
            GAME_POINT_SOUND.play()

        elif player.mask.overlap(target2.mask, offset2):
            life -= 1
            BOOMB_SOUND.play()
            target2.respawn()
            if life <= 0:
                game_state = "GAMEOVER"
                GAME_OVER_SOUND.play()

        elif player.mask.overlap(target3.mask, offset3):
            life -= 1
            BOOMB_SOUND.play()
            target3.respawn()
            if life <= 0:
                game_state = "GAMEOVER"
                GAME_OVER_SOUND.play()

        if score >= WINNING_SCORE:
            game_state = "GAMEOVER"
            GAME_OVER_SOUND.play()

        # Drawing Everything
        screen.fill("black")
        screen.blit(bg_img, (0, 0))

        score_surface = game_score_title.render(f"score : {score}", True, "black")
        game_life_sur = game_life.render(f"Life : {life}", True, "black")
        screen.blit(game_life_sur, (150, 25))
        screen.blit(score_surface, (20, 20))

        # Blit Sprites using their rects and images
        screen.blit(player.image, player.rect.topleft)
        screen.blit(target1.image, target1.rect.topleft)
        screen.blit(target2.image, target2.rect.topleft)
        screen.blit(target3.image, target3.rect.topleft)

    elif game_state == "GAMEOVER":
        screen.fill("black")
        game_over_sur = game_over_title.render(f"GAME OVER", True, "red")
        game_text_rect1 = game_over_sur.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        game_des_sur = game_over_description.render(
            "PRESS [R] TO RESTART GAME", True, "white"
        )
        game_text_rect2 = game_des_sur.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
        g_over_score = game_over_score.render(f"score : {score}", True, "white")
        g_over_score_rect = g_over_score.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 200)
        )

        pygame.draw.rect(screen, "red", restart_button_rect, border_radius=7)
        game_restart_sur = game_restart.render("RESTART", True, "white")
        game_restart_r = game_restart_sur.get_rect(center=restart_button_rect.center)

        screen.blit(game_restart_sur, game_restart_r)
        screen.blit(game_over_sur, game_text_rect1)
        screen.blit(game_des_sur, game_text_rect2)
        screen.blit(g_over_score, g_over_score_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
