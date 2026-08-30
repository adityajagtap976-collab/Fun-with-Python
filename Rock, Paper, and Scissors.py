import unittest
from enum import Enum


# Import or include classes to test
class Choice(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class ScoreBoard:
    def __init__(self, target_score: int):
        self.target_score = target_score
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0

    def record_win(self):
        self.player_score += 1

    def record_loss(self):
        self.computer_score += 1

    def record_tie(self):
        self.ties += 1

    def is_game_over(self) -> bool:
        return (
            self.player_score == self.target_score
            or self.computer_score == self.target_score
        )


# Helper function encapsulating the modulo evaluation for direct testing
def evaluate_round(player_choice: Choice, computer_choice: Choice) -> str:
    result = (player_choice.value - computer_choice.value) % 3
    if result == 0:
        return "TIE"
    elif result == 1:
        return "WIN"
    else:
        return "LOSS"


# =====================================================================
# UNIT TESTS
# =====================================================================


class TestScoreBoard(unittest.TestCase):
    """Tests for the ScoreBoard class state and win-condition checks."""

    def setUp(self):
        """Runs before every test method."""
        self.scoreboard = ScoreBoard(target_score=3)

    def test_initial_state(self):
        """Ensure counters start at 0 and game is not over initially."""
        self.assertEqual(self.scoreboard.player_score, 0)
        self.assertEqual(self.scoreboard.computer_score, 0)
        self.assertEqual(self.scoreboard.ties, 0)
        self.assertFalse(self.scoreboard.is_game_over())

    def test_record_win(self):
        """Ensure player win counter increments properly."""
        self.scoreboard.record_win()
        self.assertEqual(self.scoreboard.player_score, 1)

    def test_record_loss(self):
        """Ensure computer win counter increments properly."""
        self.scoreboard.record_loss()
        self.assertEqual(self.scoreboard.computer_score, 1)

    def test_record_tie(self):
        """Ensure tie counter increments properly."""
        self.scoreboard.record_tie()
        self.assertEqual(self.scoreboard.ties, 1)

    def test_is_game_over_when_player_reaches_target(self):
        """Game should end when player hits target score."""
        self.scoreboard.record_win()
        self.scoreboard.record_win()
        self.assertFalse(self.scoreboard.is_game_over())

        self.scoreboard.record_win()  # 3rd win
        self.assertTrue(self.scoreboard.is_game_over())

    def test_is_game_over_when_computer_reaches_target(self):
        """Game should end when computer hits target score."""
        for _ in range(3):
            self.scoreboard.record_loss()
        self.assertTrue(self.scoreboard.is_game_over())


class TestModuloWinLossLogic(unittest.TestCase):
    """Tests all combinations of (Player choice - Computer choice) % 3."""

    def test_ties(self):
        """Same choices must result in a TIE."""
        self.assertEqual(evaluate_round(Choice.ROCK, Choice.ROCK), "TIE")
        self.assertEqual(evaluate_round(Choice.PAPER, Choice.PAPER), "TIE")
        self.assertEqual(evaluate_round(Choice.SCISSORS, Choice.SCISSORS), "TIE")

    def test_player_wins(self):
        """Verify all three winning scenarios for the player."""
        # Rock (0) vs Scissors (2) -> (0 - 2) % 3 = -2 % 3 = 1
        self.assertEqual(evaluate_round(Choice.ROCK, Choice.SCISSORS), "WIN")
        # Paper (1) vs Rock (0) -> (1 - 0) % 3 = 1
        self.assertEqual(evaluate_round(Choice.PAPER, Choice.ROCK), "WIN")
        # Scissors (2) vs Paper (1) -> (2 - 1) % 3 = 1
        self.assertEqual(evaluate_round(Choice.SCISSORS, Choice.PAPER), "WIN")

    def test_computer_wins(self):
        """Verify all three losing scenarios for the player."""
        # Rock (0) vs Paper (1) -> (0 - 1) % 3 = -1 % 3 = 2
        self.assertEqual(evaluate_round(Choice.ROCK, Choice.PAPER), "LOSS")
        # Paper (1) vs Scissors (2) -> (1 - 2) % 3 = -1 % 3 = 2
        self.assertEqual(evaluate_round(Choice.PAPER, Choice.SCISSORS), "LOSS")
        # Scissors (2) vs Rock (0) -> (2 - 0) % 3 = 2
        self.assertEqual(evaluate_round(Choice.SCISSORS, Choice.ROCK), "LOSS")


if __name__ == "__main__":
    unittest.main()
