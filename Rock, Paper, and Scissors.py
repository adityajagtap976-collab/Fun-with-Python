import random
from enum import Enum


class Choice(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class ScoreBoard:
    """Manages player scores and ties across rounds."""

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

    def display(self):
        print(
            f"\nSCOREBOARD | You: {self.player_score}/{self.target_score} | "
            f"Computer: {self.computer_score}/{self.target_score} | Ties: {self.ties}"
        )

    def display_summary(self):
        print("\n================ FINAL MATCH SUMMARY ================")
        print(f" Target Score:  {self.target_score}")
        print(f" Player Score:  {self.player_score}")
        print(f" Computer Score:{self.computer_score}")
        print(f" Total Ties:    {self.ties}")
        print("=====================================================")


class RockPaperScissorsGame:
    """Encapsulates game setup, user interaction, and round execution."""

    def __init__(self):
        self.scoreboard = None

    def _get_target_score(self) -> int:
        """Prompts and validates the target score from user input."""
        while True:
            try:
                score = int(
                    input(
                        "Enter target score to win (e.g., 3 for First to 3): "
                    ).strip()
                )
                if score > 0:
                    return score
                print("Please enter a positive number greater than 0.")
            except ValueError:
                print("Invalid input! Please enter a whole number.")

    def _get_player_choice(self) -> Choice | str:
        """Prompts for input, converts 1-3 menu choices to 0-indexed Enum, or handles quit."""
        print("\nSelect:\n1 for Rock\n2 for Paper\n3 for Scissors\nq to Quit early")
        while True:
            user_input = input("\nEnter your choice (1-3): ").strip().lower()
            if user_input == "q":
                return "q"
            if user_input in ["1", "2", "3"]:
                zero_indexed = int(user_input) - 1
                return Choice(zero_indexed)
            print("Invalid choice! Please enter 1, 2, 3, or 'q'.")

    def _evaluate_round(self, player_choice: Choice, computer_choice: Choice):
        """Uses zero-indexed modulo arithmetic to evaluate the winner."""
        print(f"\nYou chose: {player_choice.name}")
        print(f"Computer chose: {computer_choice.name}")

        result = (player_choice.value - computer_choice.value) % 3

        if result == 0:
            print("Result: It's a tie!")
            self.scoreboard.record_tie()
        elif result == 1:
            print("Result: You win this round! 🎉")
            self.scoreboard.record_win()
        else:
            print("Result: Computer wins this round! 🤖")
            self.scoreboard.record_loss()

    def start(self):
        """Main game loop launcher."""
        print("----- Welcome to Rock, Paper, and Scissors game! -----")
        target_score = self._get_target_score()
        self.scoreboard = ScoreBoard(target_score)

        print(f"\nFirst player to reach {target_score} wins! Let's start.")

        while not self.scoreboard.is_game_over():
            self.scoreboard.display()

            player_choice = self._get_player_choice()
            if player_choice == "q":
                print("\nGame ended early by player.")
                break

            computer_choice = random.choice(list(Choice))
            self._evaluate_round(player_choice, computer_choice)

        # Check final winner if match wasn't quit early
        if self.scoreboard.player_score == target_score:
            print(
                f"\n🏆 CONGRATULATIONS! You reached {target_score} points first and won the match!"
            )
        elif self.scoreboard.computer_score == target_score:
            print(
                f"\n💻 GAME OVER! Computer reached {target_score} points first and won the match."
            )

        self.scoreboard.display_summary()
        print("Thanks for playing! Goodbye.")


if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.start()
