# generate the decision tree
"""
Implements Monte Carlo Decision Tree using bet sizing and hand abstraction.
Used for action selection in self-play.
"""

# 📌 Imports
from .bet_sizing import BetSizing
from .hands import HandAbstraction


class DecisionTree:
    """Monte Carlo Decision Tree for selecting poker actions."""

    def __init__(self):
        """TODO: Initialize bet sizing & hand abstraction."""
        self.bet_sizer = BetSizing()
        self.hand_abstraction = HandAbstraction()

    def build_tree(self, game_state):
        """TODO: Construct the decision tree for a given game state.
        Args:
            game_state (dict): Encapsulated state of the game.
        Returns:
            dict: Decision tree for possible actions.
        """
        pass

    def select_action(self, game_state):
        """TODO: Use Monte Carlo sampling to select the best action.
        Args:
            game_state (dict): Encapsulated state of the game.
        Returns:
            str: Chosen action.
        """
        pass
