# Deck + card utilities
"""
Manages deck creation, shuffling, and hand dealing.
"""

# 📌 Imports
import random


class Deck:
    """Represents a standard 52-card deck."""

    def __init__(self):
        """TODO: Create & shuffle the deck."""
        self.cards = self._generate_deck()
        self.shuffle()

    def _generate_deck(self):
        """TODO: Generate a 52-card deck."""
        pass

    def shuffle(self):
        """TODO: Shuffle the deck."""
        pass

    def deal_hand(self):
        """TODO: Deal two cards to a player.
        Returns:
            tuple: The player's hole cards.
        """
        pass
