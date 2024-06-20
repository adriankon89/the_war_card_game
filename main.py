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


class Player:
    name = ""

    def __init__(self, cards) -> None:
        import string
        import random

        self.cards = cards
        self.name = "".join(random.choices(string.ascii_uppercase + string.digits, k=7))

    def draw_card(self):
        return self.cards.pop() if self.cards else None

    def add_card(self, new_cards):
        pass

    def has_cards(self):
        return len(self.cards) > 0

    def __repr__(self):
        return f"Player: {self.name}"


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


class Game:
    __card_pool = []

    def __init__(self, players):
        self.players = players

    def play(self):
        while len(players) != 1:
            print("start")
            self.__card_pool.clear()

            for player in players:
                card = player.draw_card()
                if card:
                    print(f"Player {player} played: {card}")
                    self.__card_pool.append((player, card))
            self.battle()
            self.players = [player for player in self.players if player.has_cards()]
            for player in self.players:
                print(f"Player starts with cards: {player.cards}")

    def battle(self):
        for player, card in self.__card_pool:
            print(f"Player {player} card {card.rank}")

        highest_card_player, highest_card = max(
            self.__card_pool, key=lambda x: x[1].strength
        )
        print(
            f"Player {self.players.index(highest_card_player) + 1} wins this round with {highest_card}"
        )
        # print(self.__card_pool)
        exit()
        pass


# Example usage
num_players = 4

# deck = Deck(num_players)


def create_players(num_players):
    deck = Deck()
    deck.shuffle()
    hands = deck.dealCards(num_players)
    players = [Player(hand) for hand in hands]
    return players


players = create_players(num_players)
game = Game(players)
game.play()


# num_players = input("How many players play")
# print(type(deck.cards))
# print(deck.draw_card())


"""players numbers VALUE OBJECT"""