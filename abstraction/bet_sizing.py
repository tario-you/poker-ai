# generate betting amounts in mcs
"""
Handles bet sizing abstraction using Monte Carlo sampling.
Limits bet options to a subset (e.g., 10%, 30%, 60%, 100% of pot).
"""

# 📌 Imports
import random

# 📌 Constants (Example pot fractions)
BET_SIZES = [0.1, 0.3, 0.6, 1.0]


class BetSizing:
    """Abstraction for bet sizing using Monte Carlo sampling."""

    def __init__(self):
        """TODO: Initialize any necessary parameters."""
        pass

    def sample_bet_size(self, pot_size):
        """TODO: Sample a bet size from the predefined set.
        Args:
            pot_size (float): The size of the current pot.
        Returns:
            float: Chosen bet amount.
        """
        pass

    def round_off_tree_bet(self, opponent_bet, pot_size):
        """TODO: Round an off-tree bet to the closest allowed bet size.
        Args:
            opponent_bet (float): The actual bet placed by an opponent.
            pot_size (float): The current pot size.
        Returns:
            float: Adjusted bet amount.
        """
        pass
