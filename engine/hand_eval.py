# Hand strength evaluation
"""
Evaluates poker hands and determines the winner.
"""

# 📌 Imports
from engine.deck import Deck


class HandEvaluator:
    """Evaluates the best hand in a game."""

    def evaluate_hand(self, hole_cards, community_cards):
        """TODO: Determine the best five-card poker hand.
        Args:
            hole_cards (list): The player's hole cards.
            community_cards (list): Shared community cards.
        Returns:
            int: Hand ranking score.
        """
        pass

    def compare_hands(self, players_hands):
        """TODO: Compare multiple hands to determine the winner.
        Args:
            players_hands (dict): Mapping of player IDs to hands.
        Returns:
            int: Winning player ID.
        """
        pass
