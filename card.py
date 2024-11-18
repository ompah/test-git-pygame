#card name - the cards unique name 
#card type - ticket, event, team 
#card duration - how many rounds the card is active 
#card description - detailing the card


#card class
class Card:
    def __init__(self, name, type, duration, description=""):
        self.name = name
        self.type = type
        self.duration = duration
        self.description = description

    def __str__(self):
        return f"{self.name} (Type: {self.type}, Duration: {self.duration}, Description: {self.description})"


""" import pygame

# Initialize Pygame
pygame.init()
# Colors and font for rendering (if needed, can be passed dynamically or imported from a constants file)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

font = pygame.font.Font(None, 36)  # Ensure Pygame is initialized before this is called

class Card:
    def __init__(self, name, attack, health, x, y):
        self.name = name
        self.attack = attack
        self.health = health
        self.rect = pygame.Rect(x, y, 100, 150)

    def draw(self, screen):
        # Draw card background
        pygame.draw.rect(screen, BLUE, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

        # Render text (name, attack, health)
        name_text = font.render(self.name, True, WHITE)
        screen.blit(name_text, (self.rect.x + 5, self.rect.y + 5))

        attack_text = font.render(f"Atk: {self.attack}", True, WHITE)
        screen.blit(attack_text, (self.rect.x + 5, self.rect.y + 40))

        health_text = font.render(f"HP: {self.health}", True, WHITE)
        screen.blit(health_text, (self.rect.x + 5, self.rect.y + 75))
 """