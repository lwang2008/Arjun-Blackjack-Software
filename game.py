from deck import Deck, Rank, Hand
from players import Dealer, Player
from cardCounter import cardCounter
    
class Game:
    round_in_progress: bool = False
    deck: Deck
    dealer: Dealer
    players: list[Player]
    count: cardCounter
    minimum_bet: int #add minimum bet
    active_players: list[Player] #active players in game
    bj_payout_ratio: float
    

    def __init__(self, num_players: int, num_decks: int, minimum_bet: int = 10, bj_payout_ratio: float = 1.5):
        self.deck = Deck(num_decks)
        self.count = cardCounter(num_decks)
        self.dealer = Dealer(self.deck)
        self.players = [Player(i) for i in range(num_players)]
        self.minimum_bet = minimum_bet
        self.active_players = []
        self.bj_payout_ratio = bj_payout_ratio

    def start_round(self):
        self.round_in_progress = True
        self.active_players = []  # reset active players
        self.dealer.start_round(self.count)
        for player in self.players:
            if player.balance < self.minimum_bet:
                print(f"Player {player.id} does not have enough money to play")
                continue
            hand = Hand()
            hand.draw(self.dealer.deal())
            hand.draw(self.dealer.deal())
            player.place_bet(hand, self.minimum_bet) #bet miniumum bet by default
            self.active_players.append(player)

            #player blackjack does not mean round is over, dealer may also have blackjack
            #move handling of blackjack to end_round

        self.show_table()

    def play_round(self):
        if not self.round_in_progress:
            raise Exception("Round not started")
        for player in self.active_players:  #only active players play
            player.play(self.dealer, self.count)
        self.dealer.play(self.count)
        self.show_table()

    def end_round(self):
        if not self.round_in_progress:
            raise Exception("Round not started")
        dealer_hand = self.dealer.reveal_hand() 
        print(f"Dealer {dealer_hand}")
        dealer_total = self.dealer.total_hand()
        for player in self.active_players:  #only process active players
            for hand in player.show_hands():
                hand_total = hand.total()
                if hand_total > 21:
                    print(f"Player {player} {hand} busts!")
                elif hand_total == 21 and len(hand) == 2:  # blackjack means only 2 cards add to 21
                    if dealer_total == 21 and len(dealer_hand) == 2:  # Use stored hand
                        print(f"Player {player} pushes!")
                        player.balance += hand.bet
                    else:
                        print(f"Player {player} has blackjack!")
                        player.balance += hand.bet + (hand.bet * self.bj_payout_ratio)  # original bet + payout, can be configured
                elif dealer_total > 21 or hand_total > dealer_total: #if dealer busts and player does not, or player has higher count -> player wins
                    print(f"Player {player} wins!")
                    player.balance += hand.bet * 2
                elif hand_total == dealer_total:
                    print(f"Player {player} pushes!")
                    player.balance += hand.bet
                else:
                    print(f"Player {player} loses!")
            player.clear()
        self.dealer.clear()
        self.round_in_progress = False
        self.active_players = []  # clear active players

    def show_table(self):
        print(f"Dealer: {self.show_dealer_hand()}")
        
        for player in self.active_players:  #only show active players
            print(f"Player: {player} {player.show_hands()}")

    def show_dealer_hand(self):
        return self.dealer.show_hand()
