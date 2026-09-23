import pygame
import sys
import random
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../image_load"))
)
from gradient_function import render_gradient_text

pygame.init()

height = 600
width = 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Professional Pygame with States")
clock = pygame.time.Clock()

# --- GAME STATES VARIABLE ---
# Yeh track karega ki abhi kaun si screen dikhani hai ("START", "PLAYING", "GAMEOVER")
game_state = "START"

# Player aur Targets ki Positions / Sizes
man_x, man_y = 100, 100
man_w, man_h = 100, 100

c_x, c_y = 300, 200
c_w, c_h = 100, 100
c_radius = c_w // 2

r_x, r_y = 400, 300
r_w, r_h = 60, 40

speed = 5
score = 0

total_time = 30
start_tick = 0
pause_start_tick = 0
floating_texts = []
particles = []

floating_font = pygame.font.Font("../fonts/designer.otf", 30)
# Assets Loading (Images & Sounds)
bg_img = pygame.image.load("../images/green.jpg")
bg_img = pygame.transform.scale(bg_img, (width, height))

man_img = pygame.image.load("../images/man.png").convert_alpha()
man_img = pygame.transform.scale(man_img, (man_w, man_h))

game_timer = pygame.font.Font("../fonts/font2.otf", 25)
game_paused = pygame.font.Font("../fonts/designer.otf", 40)

game_start_sound = pygame.mixer.Sound("../sounds/game_start.mp3")
game_over_sound = pygame.mixer.Sound("../sounds/game_over.mp3")
point1_sound = pygame.mixer.Sound("../sounds/pop.mp3")
point2_sound = pygame.mixer.Sound("../sounds/recive.mp3")

# Fonts
font = pygame.font.Font(None, 30)
title_font = pygame.font.Font(None, 50)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        # Keyboard inputs se Game States ko control karna
        if e.type == pygame.KEYDOWN:
            # Agar Start screen par hai aur Enter dabaya, toh game shuru ho jayega
            if game_state == "START" and e.key == pygame.K_RETURN:
                game_state = "PLAYING"
                start_tick = pygame.time.get_ticks()
                game_start_sound.play()
            elif game_state == "PLAYING" and e.key == pygame.K_p:
                game_state = "PAUSED"
                pause_start_tick = pygame.time.get_ticks()
            elif game_state == "PAUSED" and pygame.K_p:
                game_state = "PLAYING"
                game_start_sound.play()
                paused_duration = pygame.time.get_ticks() - pause_start_tick
                start_tick += paused_duration

            # Agar Game Over screen par hai aur 'R' dabaya, toh game restart ho jayega
            elif game_state == "GAMEOVER" and e.key == pygame.K_r:
                score = 0
                man_x, man_y = 100, 100
                game_state = "PLAYING"
                start_tick = pygame.time.get_ticks()
                game_start_sound.play()

    # ==========================================
    # 1. START SCREEN STATE
    # ==========================================
    if game_state == "START":
        screen.fill("black")
        # screen.blit(bg_img, (0, 0))

        # Gradient text se professional start message
        start_text = render_gradient_text(
            title_font, "PRESS ENTER TO START GAME", (0, 255, 255), (255, 0, 255)
        )
        text_rect = start_text.get_rect(center=(width // 2, height // 2))
        screen.blit(start_text, text_rect.topleft)

    # ==========================================
    # 2. PLAYING STATE (Asli Game Logic)
    # ==========================================
    elif game_state == "PLAYING":
        # Player Movement Logic
        seconds = (pygame.time.get_ticks() - start_tick) // 1000
        time_left = total_time - seconds
        if time_left <= 0:
            game_state = "GAMEOVER"
            game_over_sound.play()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            man_x -= speed
        if keys[pygame.K_RIGHT]:
            man_x += speed
        if keys[pygame.K_UP]:
            man_y -= speed
        if keys[pygame.K_DOWN]:
            man_y += speed

        # Surfaces & Masks
        c_surface = pygame.Surface((c_w, c_h), pygame.SRCALPHA)
        pygame.draw.circle(c_surface, "yellow", (c_radius, c_radius), c_radius)
        r_surface = pygame.Surface((r_w, r_h), pygame.SRCALPHA)
        pygame.draw.rect(r_surface, "lime", (0, 0, r_w, r_h))

        man_mask = pygame.mask.from_surface(man_img)
        c_mask = pygame.mask.from_surface(c_surface)
        r_mask = pygame.mask.from_surface(r_surface)

        # Collision Checking
        offset1 = (c_x - man_x, c_y - man_y)
        offset2 = (r_x - man_x, r_y - man_y)

        if man_mask.overlap(c_mask, offset1):
            c_x = random.randint(0, width - c_w)
            c_y = random.randint(0, height - c_h)
            score += 5
            point2_sound.play()
            for _ in range(15):  # 15 sparks niklenge
                particles.append(
                    {
                        "x": c_x + c_w // 2,
                        "y": c_y + c_h // 2,
                        "vx": random.uniform(-4, 4),  # Horizontal speed/direction
                        "vy": random.uniform(-4, 4),  # Vertical speed/direction
                        "life": 25,  # Kitni der tak zinda rahega
                        "color": (255, 255, 0),  # Yellow sparks
                        "size": random.randint(4, 7),
                    }
                )
            floating_texts.append(
                {
                    "text": "+5",
                    "x": c_x,
                    "y": c_y,
                    "timer": 50,
                    "color": "yellow",
                }
            )
        elif man_mask.overlap(r_mask, offset2):
            r_x = random.randint(0, width - r_w)
            r_y = random.randint(0, height - r_h)
            score += 1
            point1_sound.play()
            for _ in range(10):
                particles.append(
                    {
                        "x": r_x + r_w // 2,
                        "y": r_y + r_h // 2,
                        "vx": random.uniform(-3, 3),
                        "vy": random.uniform(-3, 3),
                        "life": 20,
                        "color": (0, 255, 0),  # Green sparks
                        "size": random.randint(3, 5),
                    }
                )
            floating_texts.append(
                {
                    "text": "+1",
                    "x": r_x,
                    "y": r_y,
                    "timer": 50,
                    "color": "green",
                }
            )

        # Example condition: Agar score 50 ho jaye toh Game Over screen par chale jao
        if score >= 20:
            game_state = "GAMEOVER"
            game_over_sound.play()

        # Rendering Play Elements
        font_text = render_gradient_text(
            font, f"score : {score}", (255, 0, 0), (0, 0, 255)
        )
        game_timer_sur = game_timer.render(f"time : {time_left}", True, "black")

        screen.fill("black")
        screen.blit(bg_img, (0, 0))
        screen.blit(c_surface, (c_x, c_y))
        screen.blit(r_surface, (r_x, r_y))
        screen.blit(man_img, (man_x, man_y))
        screen.blit(font_text, (20, 10))
        screen.blit(game_timer_sur, (200, 20))
        for p in particles[:]:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["life"] -= 1
            p["size"] = max(0, p["size"] - 0.15)  # Dheere-dheere chote hote jayenge

            # Agar life ya size khatam ho jaye toh list se uda do
            if p["life"] <= 0 or p["size"] <= 0:
                particles.remove(p)
            else:
                # Screen par spark circle draw karo
                pygame.draw.circle(
                    screen, p["color"], (int(p["x"]), int(p["y"])), int(p["size"])
                )
        for item in floating_texts[:]:
            item["y"] -= 1.5
            item["timer"] -= 1
            floating_sur = floating_font.render(item["text"], True, item["color"])
            screen.blit(floating_sur, (item["x"], item["y"]))
            if item["timer"] <= 0:
                floating_texts.remove(item)
    # ==========================================
    # 3. GAME OVER STATE
    # ==========================================
    elif game_state == "GAMEOVER":
        screen.fill("black")
        # screen.blit(bg_img, (0, 0))
        # game_over_sound.play(1)
        over_text = render_gradient_text(
            title_font, "GAME OVER! PRESS 'R' TO RESTART", (255, 0, 0), (255, 255, 0)
        )
        text_rect = over_text.get_rect(center=(width // 2, height // 2))
        screen.blit(over_text, text_rect.topleft)

    elif game_state == "PAUSED":
        screen.fill("black")
        screen.blit(bg_img, (0, 0))
        screen.blit(c_surface, (c_x, c_y))
        screen.blit(r_surface, (r_x, r_y))
        screen.blit(man_img, (man_x, man_y))
        paused_text = game_paused.render("PAUSE", True, "white")
        screen.blit(paused_text, (width // 2 - 100, 100))

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
sys.exit()
