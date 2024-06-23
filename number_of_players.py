class NumberOfPlayers:
    def __init__(self, number_of_players):
        if not isinstance(number_of_players, int):
            raise TypeError("Number of players must be an integer.")
        if number_of_players < 0:
            raise ValueError("Number of players cannot be negative.")
        self._number_of_players = number_of_players

    @property
    def number_of_players(self):
        return self._number_of_players

    def __repr__(self):
        return f"NumberOfPlayers(number_of_players={self._number_of_players})"
