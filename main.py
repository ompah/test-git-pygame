import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Project")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Circle properties
circle_x, circle_y = WIDTH // 2, HEIGHT // 2
circle_radius = 30
circle_speed = 5

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keys for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed

    # Clear screen
    screen.fill(WHITE)

    # Draw the circle
    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
