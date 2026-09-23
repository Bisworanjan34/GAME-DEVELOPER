import pygame
import sys
import random

pygame.init()

height = 600
width = 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("this a simaple 2d-game man get point")
clock = pygame.time.Clock()

game_state = "START"
player1_x, player1_y = 100, 100
player1_w, player1_h = 100, 100

target1_x, target1_y = 400, 500
target1_w, target1_h = 60, 60
target1_radius = target1_w // 2

target2_x, target2_y = 200, 300
target2_w, target2_h = 50, 50
target2_radius = target2_w // 2

target3_x, target3_y = 300, 450
target3_w, target3_h = 40, 40
target3_radius = target3_w // 2

target4_x, target4_y = 360, 400
target4_w, target4_h = 40, 40
target4_radius = target4_w // 2

target2_speed = 2
target3_speed = 1
target4_speed = 3


speed = 5
score = 0
life = 3

floating_texts = []  # [{ 'text': '+5', 'x': 100, 'y': 200, 'timer': 30 }, ...]
floating_font = pygame.font.Font(None, 28)

total_time = 30  # 30 seconds ka timer
start_ticks = 0  # Jab game shuru hoga tab ka time track karne ke liye
pause_start_tick = 0
try:
    with open("highscore.txt", "r") as f:
        high_score = int(f.read())
except:
    high_score = 0

bg_img = pygame.image.load("../images/green.jpg")
bg_img = pygame.transform.scale(bg_img, (width, height))

game_start_img = pygame.image.load("../images/home.jpg")
game_start_img = pygame.transform.scale(game_start_img, (width, height))

player1_img = pygame.image.load("../images/boy.png").convert_alpha()
player1_img = pygame.transform.scale(player1_img, (player1_w, player1_h))

pygame.mixer.music.load("../sounds/forest.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.6)

GAME_START_SOUND = pygame.mixer.Sound("../sounds/game_start.mp3")
GAME_POINT_SOUND = pygame.mixer.Sound("../sounds/recive.mp3")
GAME_OVER_SOUND = pygame.mixer.Sound("../sounds/game_over.mp3")
PLAYER_FOOTSTEP = pygame.mixer.Sound("../sounds/game1.wav")
BOOMB_SOUND = pygame.mixer.Sound("../sounds/boomb.mp3")

game_start_title = pygame.font.Font("../fonts/robot.otf", 30)
game_score_title = pygame.font.Font("../fonts/font2.otf", 25)
game_life = pygame.font.Font("../fonts/font3.otf", 20)
game_timer_font = pygame.font.Font("../fonts/font2.otf", 25)
paused_time_font = pygame.font.Font("../fonts/designer.otf", 20)
game_over_title = pygame.font.Font("../fonts/designer.otf", 80)
game_over_score = pygame.font.Font("../fonts/designer.otf", 30)
game_over_description = pygame.font.Font("../fonts/font9.ttf", 30)
game_restart = pygame.font.Font("../fonts/font17.ttf", 25)
start_button_rect = pygame.Rect(width // 2 - 100, height // 2 - 30, 200, 60)
restart_button_rect = pygame.Rect(width // 2 - 100, height // 2 + 90, 200, 60)
paused_button = pygame.Rect(width // 2 - 100, height // 2 - 30, 200, 60)
run = True
footstep_counter = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if game_state == "START" and event.key == pygame.K_RETURN:
                game_state = "PLAYING"
                start_ticks = pygame.time.get_ticks()
                GAME_START_SOUND.play()
            elif game_state == "PLAYING" and event.key == pygame.K_p:
                game_state = "PAUSED"
                pause_start_tick = pygame.time.get_ticks()
            elif game_state == "PAUSED" and event.key == pygame.K_p:
                game_state = "PLAYING"
                paused_duration = pygame.time.get_ticks() - pause_start_tick
                start_ticks += paused_duration

            elif game_state == "GAMEOVER" and event.key == pygame.K_r:
                life = 3
                score = 0
                player1_x, player1_y = 50, 50
                game_state = "PLAYING"
                start_ticks = pygame.time.get_ticks()
                GAME_START_SOUND.play()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "START" and start_button_rect.collidepoint(event.pos):
                game_state = "PLAYING"
                start_ticks = pygame.time.get_ticks()
                GAME_START_SOUND.play()
            elif game_state == "PLAYING" and paused_button.collidepoint(event.pos):
                game_state = "PAUSED"
                pause_start_tick = pygame.time.get_ticks()
            elif game_state == "PAUSED" and paused_button.collidepoint(event.pos):
                game_state = "PLAYING"
                paused_duration = pygame.time.get_ticks() - pause_start_tick
                start_ticks += paused_duration

            if game_state == "GAMEOVER" and restart_button_rect.collidepoint(event.pos):
                life = 3
                score = 0
                player1_x, player1_y = 50, 50
                game_state = "PLAYING"
                start_ticks = pygame.time.get_ticks()
                GAME_START_SOUND.play()

    if game_state == "START":
        screen.fill("black")
        screen.blit(game_start_img, (0, 0))
        pygame.draw.rect(screen, "white", start_button_rect, border_radius=10)
        btn_text = game_start_title.render("GAME START", True, "black")
        btn_text_rect = btn_text.get_rect(center=start_button_rect.center)
        screen.blit(btn_text, btn_text_rect)

    elif game_state == "PLAYING":
        seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
        time_left = total_time - seconds_passed

        if time_left <= 0:
            time_left = 0
            game_state = "GAMEOVER"
            GAME_OVER_SOUND.play()
            if score > high_score:
                high_score = score
                with open("highscore.txt", "w") as f:
                    f.write(str(high_score))

        if score >= 10:
            target2_x -= target2_speed + 2
        if score >= 20:
            target2_x -= target2_speed + 3
        else:
            target2_x -= target2_speed

        target3_x -= target3_speed
        target4_x += target4_speed

        keys = pygame.key.get_pressed()
        moving = False
        if keys[pygame.K_LEFT]:
            player1_x -= speed
            moving = True
        if keys[pygame.K_RIGHT]:
            player1_x += speed
            moving = True
        if keys[pygame.K_UP]:
            player1_y -= speed
            moving = True
        if keys[pygame.K_DOWN]:
            player1_y += speed
            moving = True

        if moving:
            # Check karo ki kya footstep channel busy nahi hai (taki aawaz fate na)
            if not pygame.mixer.Channel(1).get_busy():
                pygame.mixer.Channel(1).play(PLAYER_FOOTSTEP)
        else:
            pygame.mixer.Channel(1).stop()

        # surface & mask..............
        target1_surface = pygame.Surface((target1_w, target1_h), pygame.SRCALPHA)
        pygame.draw.circle(
            target1_surface, "yellow", (target1_radius, target1_radius), target1_radius
        )
        target2_sur = pygame.Surface((target2_w, target2_h), pygame.SRCALPHA)
        pygame.draw.circle(
            target2_sur, "red", (target2_radius, target2_radius), target2_radius
        )

        target3_sur = pygame.Surface((target3_w, target3_h), pygame.SRCALPHA)
        pygame.draw.circle(
            target3_sur, "blue", (target3_radius, target3_radius), target3_radius
        )
        target4_sur = pygame.Surface((target4_w, target4_h), pygame.SRCALPHA)
        pygame.draw.circle(
            target4_sur, "green", (target4_radius, target4_radius), target4_radius
        )

        player1_mask = pygame.mask.from_surface(player1_img)
        target1_mask = pygame.mask.from_surface(target1_surface)
        target2_mask = pygame.mask.from_surface(target2_sur)
        target3_mask = pygame.mask.from_surface(target3_sur)
        target4_mask = pygame.mask.from_surface(target4_sur)

        # always remember that (Target-Player) ........
        offset = (target1_x - player1_x, target1_y - player1_y)
        offset2 = (target2_x - player1_x, target2_y - player1_y)
        offset3 = (target3_x - player1_x, target3_y - player1_y)
        offset4 = (target4_x - player1_x, target4_y - player1_y)

        if player1_mask.overlap(target1_mask, offset):
            target1_x = random.randint(0, width - target1_w)
            target1_y = random.randint(0, height - target1_h)
            score += 5
            GAME_POINT_SOUND.play()
            floating_texts.append(
                {
                    "text": "+5",
                    "x": target1_x,
                    "y": target1_y,
                    "timer": 50,  # Kitne frames tak ye screen par dikhega
                }
            )

        elif player1_mask.overlap(target2_mask, offset2):
            life -= 1
            BOOMB_SOUND.play()
            target2_x = random.randint(0, width - target2_w)
            target2_y = random.randint(0, height - target2_h)
            if life <= 0:
                game_state = "GAMEOVER"
                GAME_OVER_SOUND.play()
                if score > high_score:
                    high_score = score
                    with open("highscore.txt", "w") as f:
                        f.write(str(high_score))

        elif player1_mask.overlap(target3_mask, offset3):
            life -= 1
            BOOMB_SOUND.play()
            target3_x = random.randint(0, width - target3_w)
            target3_y = random.randint(0, height - target3_h)
            if life <= 0:
                game_state = "GAMEOVER"
                GAME_OVER_SOUND.play()
                if score > high_score:
                    high_score = score
                    with open("highscore.txt", "w") as f:
                        f.write(str(high_score))
        elif player1_mask.overlap(target4_mask, offset4):
            if life == 3:
                GAME_POINT_SOUND.stop()
                pass
            else:
                life += 1
                GAME_POINT_SOUND.play()
            target4_x = random.randint(0, width - target4_w)
            target4_y = random.randint(0, height - target4_h)

        player1_x %= width
        player1_y %= height

        if target2_x > width:
            target2_x = -target2_w
            target2_y = random.randint(50, height - 100)
        elif target2_x < -target2_w:
            target2_x = width
            target2_y = random.randint(50, height - 100)

        if target3_x > width:
            target3_x = -target3_w
            target3_y = random.randint(50, height - 100)
        elif target3_x < -target3_w:
            target3_x = width
            target3_y = random.randint(50, height - 100)

        if target4_x > width:
            target4_x = -target4_w
            target4_y = random.randint(50, height - 100)
        elif target4_x < -target4_w:
            target4_x = width
            target4_y = random.randint(50, height - 100)

        if score >= 100:
            game_state = "GAMEOVER"
            GAME_OVER_SOUND.play()
            if score > high_score:
                high_score = score
                with open("highscore.txt", "w") as f:
                    f.write(str(high_score))

        screen.fill("black")
        screen.blit(bg_img, (0, 0))
        score_surface = game_score_title.render(f"score : {score}", True, "black")
        game_life_sur = game_life.render(f"Life : {life}", True, "black")
        timer_surface = game_timer_font.render(f"Time: {time_left}s", True, "black")
        screen.blit(game_life_sur, (150, 25))
        screen.blit(score_surface, (20, 20))
        screen.blit(timer_surface, (300, 20))
        screen.blit(player1_img, (player1_x, player1_y))
        screen.blit(target1_surface, (target1_x, target1_y))
        screen.blit(target2_sur, (target2_x, target2_y))
        screen.blit(target3_sur, (target3_x, target3_y))
        screen.blit(target4_sur, (target4_x, target4_y))

        for item in floating_texts[:]:
            item["y"] -= 1.5
            item["timer"] -= 1

            floating_sur = floating_font.render(item["text"], True, "yellow")
            screen.blit(floating_sur, (item["x"], item["y"]))

            if item["timer"] <= 0:
                floating_texts.remove(item)

    elif game_state == "GAMEOVER":
        screen.fill("black")
        game_over_sur = game_over_title.render(f"GAME OVER", True, "red")
        game_text_rect1 = game_over_sur.get_rect(center=(width // 2, height // 2))
        game_des_sur = game_over_description.render(
            "PRESS [R] TO RESTART GAME", True, "white"
        )
        game_text_rect2 = game_des_sur.get_rect(center=(width // 2, height // 2 + 60))
        g_over_score = game_over_score.render(f"score : {score}", True, "white")
        g_over_score_rect = g_over_score.get_rect(
            center=(width // 2, height // 2 - 200)
        )
        pygame.draw.rect(screen, "red", restart_button_rect, border_radius=7)
        game_restart_sur = game_restart.render("RESTART", True, "white")
        game_restart_r = game_restart_sur.get_rect(center=restart_button_rect.center)

        # High score render karne ke liye font aur text
        g_over_highscore = game_over_score.render(
            f"High Score : {high_score}", True, "yellow"
        )
        g_over_highscore_rect = g_over_highscore.get_rect(
            center=(width // 2, height // 2 - 150)
        )
        screen.blit(g_over_highscore, g_over_highscore_rect)

        screen.blit(game_restart_sur, game_restart_r)
        screen.blit(game_over_sur, game_text_rect1)
        screen.blit(game_des_sur, game_text_rect2)
        screen.blit(g_over_score, g_over_score_rect)

    elif game_state == "PAUSED":
        screen.fill("black")
        pygame.draw.rect(screen, "red", paused_button, border_radius=8)
        paused_t = paused_time_font.render("RESUME", True, "white")
        paused_t_rec = paused_t.get_rect(center=paused_button.center)
        screen.blit(paused_t, paused_t_rec)

    pygame.display.flip()
    clock.tick(100)
pygame.quit()
sys.exit()
