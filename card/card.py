import yaml
"""
# Define the Card class
class Card:
    def __init__(self, id, name, description, flavor_text, point_value, card_type, rarity, health, mana_cost, abilities):
        self.id = id
        self.name = name
        self.description = description
        self.flavor_text = flavor_text
        self.point_value = point_value
        self.card_type = card_type
        self.rarity = rarity
        self.health = health
        self.mana_cost = mana_cost
        self.abilities = abilities  # Now a list of ability dictionaries

    def __repr__(self):
        return f"Card(id={self.id}, name={self.name}, type={self.card_type})"

# Load YAML data from the file
def load_cards(filename='carddata.yaml'):
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)  # Read the YAML file
    cards = {}
    
    # Loop through each card in the YAML data and create Card objects
    for card_data in data['cards']:
        card = Card(**card_data)  # Use unpacking to pass data to the Card constructor
        cards[card.id] = card
    
    return cards

# Example of loading cards from the YAML file
#cards = load_cards()

# Example: Display abilities for each card
#for card in cards.values():
    print(f"Card: {card.name}")
    for ability in card.abilities:
        print(f" - {ability['name']}: {ability['effect']} (Mana cost: {ability['mana_cost']})")
"""
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