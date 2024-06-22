from card import Card


class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        import random

        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None

    def dealCards(self, num_players):
        self.shuffle()
        hands = [[] for _ in range(num_players)]

        for i, card in enumerate(self.cards):
            hands[i % num_players].append(card)

        return hands
