from enum import Enum
<<<<<<< HEAD
from .deck import Rank
=======
from deck import Rank
>>>>>>> 325f1b0 (fixed game logic)

class Action(Enum):
    H = "Hit"
    S = "Stand"
    D = "Double if allowed, otherwise hit"
    Ds = "Double if allowed, otherwise stand"
    N = "Don’t split the pair"
    Y = "Split the Pair"
    YN = "Split only if `DAS` is offered"
    SUR = "Surrender"

# Basic strategy lookup table based on the provided chart
blackjack_strategy = {
    "hard_totals": {
        17: {Rank.TWO: Action.S, Rank.THREE: Action.S, Rank.FOUR: Action.S, Rank.FIVE: Action.S, Rank.SIX: Action.S, Rank.SEVEN: Action.S, Rank.EIGHT: Action.S, Rank.NINE: Action.S, Rank.TEN: Action.S, Rank.ACE: Action.S},
        16: {Rank.TWO: Action.S, Rank.THREE: Action.S, Rank.FOUR: Action.S, Rank.FIVE: Action.S, Rank.SIX: Action.S, Rank.SEVEN: Action.H, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        15: {Rank.TWO: Action.S, Rank.THREE: Action.S, Rank.FOUR: Action.S, Rank.FIVE: Action.S, Rank.SIX: Action.S, Rank.SEVEN: Action.H, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        14: {Rank.TWO: Action.S, Rank.THREE: Action.S, Rank.FOUR: Action.S, Rank.FIVE: Action.S, Rank.SIX: Action.S, Rank.SEVEN: Action.H, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        13: {Rank.TWO: Action.S, Rank.THREE: Action.S, Rank.FOUR: Action.S, Rank.FIVE: Action.S, Rank.SIX: Action.S, Rank.SEVEN: Action.H, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        12: {Rank.TWO: Action.H, Rank.THREE: Action.H, Rank.FOUR: Action.S, Rank.FIVE: Action.S, Rank.SIX: Action.S, Rank.SEVEN: Action.H, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        11: {Rank.TWO: Action.D, Rank.THREE: Action.D, Rank.FOUR: Action.D, Rank.FIVE: Action.D, Rank.SIX: Action.D, Rank.SEVEN: Action.D, Rank.EIGHT: Action.D, Rank.NINE: Action.D, Rank.TEN: Action.D, Rank.ACE: Action.H},
        10: {Rank.TWO: Action.D, Rank.THREE: Action.D, Rank.FOUR: Action.D, Rank.FIVE: Action.D, Rank.SIX: Action.D, Rank.SEVEN: Action.D, Rank.EIGHT: Action.D, Rank.NINE: Action.D, Rank.TEN: Action.H, Rank.ACE: Action.H},
        9: {Rank.TWO: Action.H, Rank.THREE: Action.D, Rank.FOUR: Action.D, Rank.FIVE: Action.D, Rank.SIX: Action.D, Rank.SEVEN: Action.H, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        **{total: {Rank.TWO: Action.H, Rank.THREE: Action.H, Rank.FOUR: Action.H, Rank.FIVE: Action.H, Rank.SIX: Action.H, Rank.SEVEN: Action.H, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H} 
            for total in range(5, 9)}
    },
    "soft_totals": {
        9: {Rank.TWO: Action.S, Rank.THREE: Action.S, Rank.FOUR: Action.S, Rank.FIVE: Action.S, Rank.SIX: Action.S, Rank.SEVEN: Action.S, Rank.EIGHT: Action.S, Rank.NINE: Action.S, Rank.TEN: Action.S, Rank.ACE: Action.S},
        8: {Rank.TWO: Action.S, Rank.THREE: Action.S, Rank.FOUR: Action.S, Rank.FIVE: Action.S, Rank.SIX: Action.S, Rank.SEVEN: Action.S, Rank.EIGHT: Action.S, Rank.NINE: Action.S, Rank.TEN: Action.S, Rank.ACE: Action.S},
        7: {Rank.TWO: Action.Ds, Rank.THREE: Action.Ds, Rank.FOUR: Action.Ds, Rank.FIVE: Action.Ds, Rank.SIX: Action.Ds, Rank.SEVEN: Action.S, Rank.EIGHT: Action.S, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        6: {Rank.TWO: Action.H, Rank.THREE: Action.D, Rank.FOUR: Action.D, Rank.FIVE: Action.D, Rank.SIX: Action.D, Rank.SEVEN: Action.H, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        5: {Rank.TWO: Action.H, Rank.THREE: Action.H, Rank.FOUR: Action.D, Rank.FIVE: Action.D, Rank.SIX: Action.D, Rank.SEVEN: Action.H, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        4: {Rank.TWO: Action.H, Rank.THREE: Action.H, Rank.FOUR: Action.D, Rank.FIVE: Action.D, Rank.SIX: Action.D, Rank.SEVEN: Action.H, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        3: {Rank.TWO: Action.H, Rank.THREE: Action.H, Rank.FOUR: Action.H, Rank.FIVE: Action.D, Rank.SIX: Action.D, Rank.SEVEN: Action.H, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        2: {Rank.TWO: Action.H, Rank.THREE: Action.H, Rank.FOUR: Action.H, Rank.FIVE: Action.D, Rank.SIX: Action.D, Rank.SEVEN: Action.H, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
    },
    "pair_splitting": {
        Rank.ACE: {Rank.TWO: Action.Y, Rank.THREE: Action.Y, Rank.FOUR: Action.Y, Rank.FIVE: Action.Y, Rank.SIX: Action.Y, Rank.SEVEN: Action.Y, Rank.EIGHT: Action.Y, Rank.NINE: Action.Y, Rank.TEN: Action.Y, Rank.ACE: Action.Y},
        **{rank: {Rank.TWO: Action.N, Rank.THREE: Action.N, Rank.FOUR: Action.N, Rank.FIVE: Action.N, Rank.SIX: Action.N, Rank.SEVEN: Action.N, Rank.EIGHT: Action.N, Rank.NINE: Action.N, Rank.TEN: Action.N, Rank.ACE: Action.N}
            for rank in [Rank.KING, Rank.QUEEN, Rank.JACK, Rank.TEN]},
        Rank.NINE: {Rank.TWO: Action.Y, Rank.THREE: Action.Y, Rank.FOUR: Action.Y, Rank.FIVE: Action.Y, Rank.SIX: Action.Y, Rank.SEVEN: Action.N, Rank.EIGHT: Action.Y, Rank.NINE: Action.Y, Rank.TEN: Action.N, Rank.ACE: Action.N},
        Rank.EIGHT: {Rank.TWO: Action.Y, Rank.THREE: Action.Y, Rank.FOUR: Action.Y, Rank.FIVE: Action.Y, Rank.SIX: Action.Y, Rank.SEVEN: Action.Y, Rank.EIGHT: Action.Y, Rank.NINE: Action.Y, Rank.TEN: Action.Y, Rank.ACE: Action.Y},
        Rank.SEVEN: {Rank.TWO: Action.Y, Rank.THREE: Action.Y, Rank.FOUR: Action.Y, Rank.FIVE: Action .Y, Rank.SIX: Action.Y, Rank.SEVEN: Action.Y, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        Rank.SIX: {Rank.TWO: Action.YN, Rank.THREE: Action.YN, Rank.FOUR: Action.Y, Rank.FIVE: Action.Y, Rank.SIX: Action.Y, Rank.SEVEN: Action.H, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        Rank.FIVE: {Rank.TWO: Action.D, Rank.THREE: Action.D, Rank.FOUR: Action.D, Rank.FIVE: Action.D, Rank.SIX: Action.D, Rank.SEVEN: Action.D, Rank.EIGHT: Action.D, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        Rank.FOUR: {Rank.TWO: Action.N, Rank.THREE: Action.N, Rank.FOUR: Action.N, Rank.FIVE: Action.YN, Rank.SIX: Action.YN, Rank.SEVEN: Action.N, Rank.EIGHT: Action.N, Rank.NINE: Action.N, Rank.TEN: Action.N, Rank.ACE: Action.N},
        Rank.THREE: {Rank.TWO: Action.YN, Rank.THREE: Action.YN, Rank.FOUR: Action.Y, Rank.FIVE: Action.Y, Rank.SIX: Action.Y, Rank.SEVEN: Action.Y, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
        Rank.TWO: {Rank.TWO: Action.YN, Rank.THREE: Action.YN, Rank.FOUR: Action.Y, Rank.FIVE: Action.Y, Rank.SIX: Action.Y, Rank.SEVEN: Action.Y, Rank.EIGHT: Action.H, Rank.NINE: Action.H, Rank.TEN: Action.H, Rank.ACE: Action.H},
    },
    "surrender": {
        16: {Rank.NINE: Action.SUR, Rank.TEN: Action.SUR, Rank.ACE: Action.SUR},
        15: {Rank.TEN: Action.SUR},
    },
    "insurance_or_even_money": "Don’t Take"
}