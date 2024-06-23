from player import Player
from deck import Deck


class Game:
    __card_pool = []
    __stash_card_pool = []

    def __init__(self, players):
        self.players = players

    def play(self):
        turn_counter = 0
        while len(self.players) != 1:
            self.draw_card_by_players()
            user_who_won = self.battle()
            if user_who_won:
                self.add_cards_to_winner_of_battle(user_who_won)

            self.remove_player_without_cards()
            self.__card_pool.clear()
            turn_counter += 1
        winner = self.players.pop()
        print(f"won {winner} {len(winner.cards)} with turn of {turn_counter}")

    def remove_player_without_cards(self):
        self.players = [player for player in self.players if player.has_cards()]

    def draw_card_by_players(self):
        for player in self.players:
            card = player.draw_card()
            if card:
                self.__card_pool.append((player, card))

    def battle(self):
        for player, card in self.__card_pool:
            print(f"Player {player} card {card.rank}")
        highest_cards = self.get_highest_pool_cards(self.__card_pool)
        if len(highest_cards) > 1:
            player_who_win_battle = self.resolve_tie(highest_cards)
        else:
            player_who_win_battle, _ = highest_cards[0]

        return player_who_win_battle

    def get_highest_pool_cards(self, card_pool):
        highest_strength = max(card.strength for _, card in card_pool)

        return [
            (player, card)
            for player, card in card_pool
            if card.strength == highest_strength
        ]

    def resolve_tie(self, highest_cards):
        print("It's a tie between the following players:")
        tied_players = []
        """check if users has a card if not remove them, draw a card get a highest card
        """
        for player, card in highest_cards:
            print(f"TIE: Player {player} with card {card.rank}")
            self.__stash_card_pool.append(card)
            if player.has_cards():
                tied_players.append(player)

        self.__card_pool.clear()

        tied_players_amount = len(tied_players)
        if tied_players_amount == 1:
            return tied_players.pop()
        if tied_players_amount == 0:
            return False

        self.tie_battle(tied_players)

    def tie_battle(self, players):
        for player in players:
            print("player len cards ", len(player.cards))
            card = player.draw_card()
            if card:
                self.__card_pool.append((player, card))
        highest_cards = self.get_highest_pool_cards(self.__card_pool)

        if len(highest_cards) > 1:
            self.resolve_tie(highest_cards)
            return False
        player_who_win_battle, _ = highest_cards[0]

        return player_who_win_battle

    def add_cards_to_winner_of_battle(self, winner_player):
        for _, card in self.__card_pool:
            winner_player.add_card(card)

        for card in self.__stash_card_pool:
            winner_player.add_card(card)

        self.__card_pool.clear()
        self.__stash_card_pool.clear()


num_players = 4


def create_players(num_players):
    deck = Deck()
    deck.shuffle()
    hands = deck.dealCards(num_players)
    players = [Player(hand) for hand in hands]
    return players


players = create_players(num_players)
game = Game(players)
game.play()

"""players numbers VALUE OBJECT"""
