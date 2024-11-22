import pygame
#from card import Card
import random
from enum import Enum

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Card Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 16)

#card name - the cards unique name 
#card type - ticket, event, team 
#card duration - how many rounds the card is active 1-6 
#card description - detailing the card

class CardType(Enum):
    TICKET = "Ticket"
    EVENT = "Event"
    TEAM = "Team"

# Define a Pre-Defined Deck of Cards
"""PREDEFINED_DECK = [
    Card("time reporting", CardType.EVENT, 1, "you need to do this."),
    Card("reorganization", CardType.EVENT, 6, "this is better."),
    Card("access denied", CardType.EVENT, 1, "you need to make a ticket to access this."),
    Card("sprint planning", CardType.EVENT, 1, "Quick and agile."),
    Card("wrong board", CardType.EVENT, 1, "your ticekt is in the wrong board, make new"),
    Card("performance evaluation", CardType.EVENT, 1, "you suck."),
    Card("do you have a ticket?", CardType.EVENT, 1, "Lurks in the darkness."),
    Card("more meetings!", CardType.EVENT, 3, "this meeting series is good."),
    Card("work in silos", CardType.EVENT, 3, "this."),
    Card("technical break", CardType.EVENT, 1, "this."),
    Card("work in silos", CardType.EVENT, 3, "this."),
    Card("work in silos", CardType.EVENT, 3, "this."),
        
]"""

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

# Deck class to manage the predefined deck
class Deck:
    def __init__(self):
        #self.cards = cards  # List of Card objects
        self.cards = load_cards()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)  # Draw the top card
        else:
            return None  # Deck is empty

# Create a deck and shuffle it
deck = Deck()
deck.shuffle()

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
        card_text = font.render(str(card), True, BLACK)
        screen.blit(card_text, (10, y_offset))
        y_offset += 30

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
