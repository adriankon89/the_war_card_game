from player import Player
from deck import Deck


class Game:
    __card_pool = []

    def __init__(self, players):
        self.players = players

    def play(self):
        turn_amount = 0
        while len(self.players) != 1:
            print("start")

            self.remove_player_without_cards()
            self.draw_card_by_players()

            user_who_won = self.battle()
            self.add_cards_to_winner_of_battle(user_who_won)

            self.__card_pool.clear()
            turn_amount += 1

        winner = self.players.pop()
        print(f"won {winner} {len(winner.cards)} with turn of {turn_amount}")

    def remove_player_without_cards(self):
        self.players = [player for player in self.players if player.has_cards()]

    def draw_card_by_players(self):
        for player in players:
            card = player.draw_card()
            if card:
                self.__card_pool.append((player, card))

    def battle(self):
        # todo TIE/draw
        for player, card in self.__card_pool:
            print(f"Player {player} card {card.rank}")

        highest_card_player, highest_card = max(
            self.__card_pool, key=lambda x: x[1].strength
        )

        return highest_card_player

    def add_cards_to_winner_of_battle(self, winner_player):
        for card_owner, card in self.__card_pool:
            winner_player.add_card(card)


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

"""players numbers VALUE OBJECT"""
