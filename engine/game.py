# main game loop
"""
Main game loop that orchestrates gameplay.
"""

# 📌 Imports
from engine.deck import Deck
from engine.state import GameState
from engine.betting import Betting


class PokerGame:
    """Main poker game loop."""

    def __init__(self):
        """TODO: Initialize game components (deck, players, state)."""
        self.deck = Deck()
        self.state = GameState()
        self.betting = Betting(self.state)

    def play_round(self):
        """TODO: Execute a full round of poker (preflop to showdown)."""
        pass
