class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.strength = self.calculate_strength(rank)

    def calculate_strength(self, rank):
        rank_strengths = {
            "2": 1,
            "3": 2,
            "4": 3,
            "5": 4,
            "6": 5,
            "7": 6,
            "8": 7,
            "9": 8,
            "10": 9,
            "J": 10,
            "Q": 11,
            "K": 12,
            "A": 13,
        }
        return rank_strengths.get(rank, 0)

    def __repr__(self):
        return f"{self.rank} of {self.suit} (Strength: {self.strength})"
