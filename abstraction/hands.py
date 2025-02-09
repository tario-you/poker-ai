# generate sets of roughly equal hands
"""
Uses Monte Carlo sampling to abstract starting hands.
Groups similar hands together to reduce strategy complexity.
"""

# 📌 Imports
import random

# 📌 Example hand groups (e.g., premium, mid, low tier)
# don't actually do it like this. find the best way to do this. this is just a chat gpt example 🤣.
HAND_GROUPS = {
    "strong": [("A", "A"), ("K", "K"), ("Q", "Q")],
    "medium": [("A", "K"), ("Q", "J"), ("10", "10")],
    "weak": [("2", "7"), ("3", "8"), ("4", "9")]
}


class HandAbstraction:
    """Abstraction for grouping starting hands."""

    def __init__(self):
        """TODO: Initialize hand categories."""
        # hi
        pass

    def sample_starting_hand(self):
        """TODO: Sample a starting hand based on predefined groups.
        Returns:
            tuple: Chosen starting hand.
        """
        pass

    def categorize_hand(self, hole_cards):
        """TODO: Categorize a hand into a pre-defined abstraction group.
        Args:
            hole_cards (tuple): The player's hole cards.
        Returns:
            str: Hand category ("strong", "medium", "weak").
        """
        pass
