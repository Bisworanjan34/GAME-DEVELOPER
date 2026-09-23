import pygame
import sys

# 1. Pygame ko start karo
pygame.init()

# 2. Screen ki Width aur Height set karo (Pixels mein)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# Window create karo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Python Game Window - Pro Mode On")

# Colors define karo (RGB Format: Red, Green, Blue)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)

# Frame rate control karne ke liye clock object
clock = pygame.time.Clock()

# 3. Game Loop (Yahan poora game chalega jab tak tu band na kare)
running = True
while running:
    # Event handling: Keyboard ya Mouse ki activity check karna
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Cross button dabane par game band ho jayega
    # Screen ko background color se fill karo (Clear screen)
    screen.fill("blue")

    # Yahan hum apne characters ya shapes draw karenge (Filhal ek rectangle)
    # pygame.draw.rect(surface, color, [x, y, width, height])
    pygame.draw.rect(screen, "red", [450, 200, 200, 200])

    # Display ko update karo taaki screen par sab kuch dikhe
    pygame.display.flip()

    # FPS lock karo taaki game smooth chale (60 Frames Per Second)
    clock.tick(60)

# Game close hone par pygame ko safely band karo
pygame.quit()
sys.exit()
