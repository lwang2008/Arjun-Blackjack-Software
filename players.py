from .deck import Deck, Card, Rank, Hand
from .strategy import Action, blackjack_strategy

class Dealer:
    deck: Deck
    hand: Hand

    def __init__(self, deck: Deck):
        self.deck = deck
        self.hand = []
        self.deck.shuffle()

    def start_round(self):
        self.hand = [self.deck.cards.pop(), self.deck.cards.pop()]

    def show_hand(self) -> Card:
        if len(self.hand) >= 2: return self.hand[0]
        else: return None
    
    def reveal_hand(self) -> Hand:
        return self.hand
    
    def draw(self):
        self.hand.append(self.deck.draw())

    def deal(self) -> Card:
        return self.deck.draw()
    
    def play(self):
        while sum(self.hand) < 17:
            self.draw()
        return self.hand
    
    def total_hand(self) -> int:
        total = sum(self.hand)
        if total > 21 and any(card.rank == Rank.ACE for card in self.hand):
            total -= 10
        return total
    
    def clear(self):
        self.hand = []
    
class Player:
    hands: list[Hand]
    balance: int
    id: int

    def __init__(self, id: int, balance: int = 100):
        self.hands = []
        self.balance = balance
        self.id = id

    def place_bet(self, hand: Hand, amount: int):
        self.balance -= amount
        hand.place_bet(amount)
        self.hands.append(hand)

    def play(self, dealer: Dealer, hand: Hand = None):
        if hand is None and self.hands != []:
            hand = self.hands[0]
        else:
            return
        action = get_strategy(hand, dealer)
        if action == Action.S:
            return
        elif action == Action.H:
            hand.draw(dealer.deal())
        elif action == Action.D or action == Action.Ds:
            self.balance -= hand.bet
            hand.bet *= 2
            hand.draw(dealer.deal())
        elif action == Action.Y:
            new_hand = hand.split()
            new_hand.draw(dealer.deal())
            hand.draw(dealer.deal())
            self.place_bet(new_hand, hand.bet)
            self.play(self.hands[-1], dealer)
        elif action == Action.YN:
            if dealer.show_hand().rank == Rank.ACE:
                return
            self.split()
        elif action == Action.SUR:
            return
        
    

    def show_hands(self) -> list[Hand]:
        return self.hands
    
    def clear(self):
        self.hands = []
        self.bet = 0

    def __str__(self):
        return f"Player {self.id} ({[hand.bet for hand in self.hands]}, {self.balance})"

def get_strategy(player_hand: Hand, dealer: Dealer) -> Action:
    dealer_upcard = dealer.show_hand()
    if len(player_hand) == 2 and player_hand[0].rank == player_hand[1].rank:
        return blackjack_strategy["pair_splitting"][player_hand[0].rank][dealer_upcard.rank]
    elif any(card.rank == Rank.ACE for card in player_hand):
        return blackjack_strategy["soft_totals"][sum(card.get_value() for card in player_hand if card.rank != Rank.ACE)][dealer_upcard.rank]
    else:
        if sum(player_hand) >= 17:
            return Action.S
        
        if sum(player_hand) <= 8:
            return Action.H

        return blackjack_strategy["hard_totals"][sum(player_hand)][dealer_upcard.rank]