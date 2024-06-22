class Player:
    name = ""

    def __init__(self, cards) -> None:
        import string
        import random

        self.cards = cards
        self.name = "".join(random.choices(string.ascii_uppercase + string.digits, k=7))

    def draw_card(self):
        return self.cards.pop() if self.cards else None

    def add_card(self, card):
        self.cards.append(card)

    def has_cards(self):
        return len(self.cards) > 0

    def __repr__(self):
        return f"Player: {self.name}"
