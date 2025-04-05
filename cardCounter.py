from deck import Card

class cardCounter:    
    def __init__(self, num_decks: int):
        self.running_count = 0
        self.num_decks = num_decks
        self.known_cards = 0
        self.initial_num_cards = num_decks * 52
        
    def update_count(self, card: Card) -> None:
        self.running_count += card.get_count()
        self.known_cards += 1
        
    def get_true_count(self) -> float:
        return self.running_count / self.get_decks_remaining()
    
    def get_decks_remaining(self) -> float:
        return (self.initial_num_cards - self.known_cards) / 52
    
    #betting strategy should be more sophisticated, this is a simple implementation
    def get_bet_size(self, min_bet: int, bet_unit: int) -> int:
        true_count = self.get_true_count()
        if true_count <= 1:
            return min_bet
        return bet_unit * int(true_count) #multiply betting unit by true count
    
    def reset(self) -> None:
        self.running_count = 0
        self.known_cards = 0 