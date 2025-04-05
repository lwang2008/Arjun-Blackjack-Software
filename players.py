from deck import Deck, Card, Rank, Hand
from strategy import Action, blackjack_strategy
from cardCounter import cardCounter

class Dealer:
    deck: Deck
    hand: Hand

    def __init__(self, deck: Deck):
        self.deck = deck
        self.hand = []
        self.deck.shuffle()

    def start_round(self, count: cardCounter):
        card = self.deck.cards.pop()
        self.hand.append(card)
        count.update_count(card) #update count
        card = self.deck.cards.pop()
        self.hand.append(card)
        count.update_count(card) #update count

    #dealer always shows first card
    def show_hand(self) -> Card:
        return self.hand[0]  
    
    def reveal_hand(self) -> Hand:
        return self.hand
    
    def draw(self, count: cardCounter):
        card = self.deck.draw()
        self.hand.append(card)
        count.update_count(card)

    def deal(self) -> Card:
        return self.deck.draw()
    
    def play(self, count: cardCounter):
        #dealer also hits on soft 17
        while self.total_hand() < 17 or (self.total_hand() == 17 and any(card.rank == Rank.ACE for card in self.hand)):
            self.draw(count)
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

    def play(self, dealer: Dealer, count: cardCounter, hand: Hand = None):
        #fixed if logic, we should process hand passed in
        if hand is None:
            if self.hands != []:
                hand = self.hands[0]
            else:
                return

        action = get_strategy(hand, dealer)
        if action == Action.S:
            return
        elif action == Action.H:
            card = dealer.deal()
            hand.draw(card)
            count.update_count(card) #update count
        elif action == Action.D or action == Action.Ds:
            self.balance -= hand.bet
            hand.bet *= 2
            card = dealer.deal()
            hand.draw(card)
            count.update_count(card)
            return  # player's turn is over after doubling down
        elif action == Action.Y:
            new_hand = hand.split()
            card = dealer.deal()
            new_hand.draw(card)
            count.update_count(card) #update count
            card = dealer.deal()
            hand.draw(card)
            count.update_count(card) #update count
            self.place_bet(new_hand, hand.bet)
            self.play(dealer, count, self.hands[-1])
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
      if player_hand.total() >= 17: #use total() not sum
            return Action.S
        
        if player_hand.total() <= 8:  #use total() not sum
            return Action.H

        return blackjack_strategy["hard_totals"][player_hand.total()][dealer_upcard.rank]  #use total() not sum