from enum import Enum
import random

class Suit(Enum):
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"

class Rank(Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"
    ACE = "Ace"

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank.value} of {self.suit.value}"

    def __repr__(self):
        return f"{self.rank.value} of {self.suit.value}"
    
    def __add__(self, other) -> int:
        if isinstance(other, int):
            return self.get_value() + other
        
        if isinstance(other, Card):
            return self.get_value() + other.get_value()
        
    def __radd__(self, other) -> int:
        if isinstance(other, int):
            return self.get_value() + other
        
        if isinstance(other, Card):
            return self.get_value() + other.get_value()
    
    def get_value(self):
        if self.rank in [Rank.JACK, Rank.QUEEN, Rank.KING]:
            return 10
        elif self.rank == Rank.ACE:
            return 11
        else:
            return int(self.rank.value)

    def get_count(self):
        if self.get_value() >=10:
            return -1
        elif self.get_value() <=6:
            return 1
        else:
            return 0
    
type Hand = list[Card]

class Deck:
    cards: list[Card]
    discard_pile: list[Card]
    num_decks: int
    
    def __init__(self, num_decks: int):  
        self.num_decks = num_decks
        self.cards = []
        self.discard_pile = []
        for _ in range(num_decks):
            self.cards.extend([Card(suit, rank) for suit in Suit for rank in Rank])
        self.shuffle()  #shuffle when initializing 

    def __str__(self):
        return f"{self.cards}"

    def __repr__(self):
        return f"{self.cards}"
    
    def draw(self) -> Card:
        card = self.cards.pop()
        self.discard_pile.append(card)
        return card
    
    def shuffle(self):
        random.shuffle(self.cards)

class Hand:
    cards: list[Card]
    bet: int
    can_draw: bool = True

    def __init__(self, card: Card = None):
        if card is None:
            self.cards = []
        else:
            self.cards = [card]

    def end_drawing(self):
        self.can_draw = False

    def draw(self, card: Card):
        self.cards.append(card)

    def split(self):
        return Hand(self.cards.pop())
    
    def place_bet(self, amount: int):
        self.bet = amount
    
    #if there are multiple aces, only count one as 11
    #simply subtracting 10 will not suffice
    def total(self) -> int:
        total = sum(card.get_value() for card in self.cards)
        num_aces = sum(1 for card in self.cards if card.rank == Rank.ACE)
        while total > 21 and num_aces > 0:
            total -= 10
            num_aces -= 1
        return total
    
    def __str__(self) -> str:
        return f"{self.cards}"
    
    def __repr__(self) -> str:
        return f"{self.cards}"
    
    def __len__(self) -> int:
        return len(self.cards)
    
    def __iter__(self):
        return iter(self.cards)
    
    def __getitem__(self, key):
        return self.cards[key]