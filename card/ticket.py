import os
import yaml
import pygame
from enum import Enum
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Card Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)

# Fonts
font = pygame.font.Font(None, 16)

class CardType(Enum):
    TICKET = "Ticket"
    EVENT = "Event"
    TEAM = "Team"

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
        self.abilities = abilities

    def __repr__(self):
        return f"Card(id={self.id}, name={self.name}, type={self.card_type})"

def load_cards(filename=None):
    if filename is None:
        filename = os.path.join(os.path.dirname(__file__), 'carddata.yaml')
    if not os.path.exists(filename):
        raise FileNotFoundError(f"'{filename}' not found.")
    
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)

    cards = []
    for card_data in data['cards']:
        card = Card(**card_data)
        cards.append(card)
    return cards

class Deck:
    def __init__(self):
        self.cards = load_cards()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        return None

# Create a deck and shuffle it
deck = Deck()
deck.shuffle()

for card in deck.cards:
    print(f"Card: {card.name}")
    print(f"Descr: {card.description}")
    if not card.abilities:
        print(" - No abilities")
    else:
        for ability in card.abilities:
            print(f" - {ability['name']}: {ability['effect']} (cost: {ability['cost']})")

# Game Loop
running = True
player_hand = []  # List to hold player's drawn cards

while running:
    screen.fill(WHITE)

    # Draw game title
    text = font.render("Card Game: Draw Cards", True, BLACK)
    screen.blit(text, (10, 10))

    # Draw player's hand
    y_offset = 50
    for card in player_hand:
        text_to_render = [card.name, card.description]
        joined_text = ", ".join(text_to_render)
        card_text = font.render(joined_text, True, GRAY)

        screen.blit(card_text, (10, y_offset))
        y_offset += 20

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Press SPACE to draw a card
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                drawn_card = deck.draw_card()
                if drawn_card:
                    player_hand.append(drawn_card)
                else:
                    print("The deck is empty!")

    pygame.display.flip()

pygame.quit()
