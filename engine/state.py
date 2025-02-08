# Tracks the game state
"""
Tracks overall game state including active players and pot size.
"""


class GameState:
    """Encapsulates the current state of the poker game."""

    def __init__(self):
        """TODO: Initialize state variables (players, pot, actions)."""
        self.players = []
        self.pot = 0
        self.current_betting_round = "preflop"

    def update_state(self):
        """TODO: Update game state after each action."""
        pass
