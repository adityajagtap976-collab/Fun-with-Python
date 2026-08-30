import random
from enum import Enum


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# Ask the user for target score before starting
print("----- Welcome to Rock, Paper, and Scissors game! -----")
while True:
    try:
        target_score = int(
            input("Enter target score to win (e.g., 3 for First to 3): ").strip()
        )
        if target_score > 0:
            break
        print("Please enter a positive number greater than 0.")
    except ValueError:
        print("Invalid input! Please enter a whole number.")

# Score Tracker Variables
player_score = 0
computer_score = 0
ties = 0

print(f"\nFirst player to reach {target_score} wins! Let's start.")

while True:
    # Display running scoreboard at the start of each round
    print(
        f"\nSCOREBOARD | You: {player_score}/{target_score} | Computer: {computer_score}/{target_score} | Ties: {ties}"
    )
    print("Select:\n1 for Rock\n2 for Paper\n3 for Scissors\nq to Quit early")

    user_input = input("\nEnter your choice (1-3): ").strip()

    if user_input.lower() == "q":
        print("\nGame ended early by player.")
        break

    if user_input in ["1", "2", "3"]:
        player_choice = Choice(int(user_input))
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 'q'.")
        continue

    computer_choice = random.choice(list(Choice))

    print(f"\nYou chose: {player_choice.name}")
    print(f"Computer chose: {computer_choice.name}")

    # Determine winner & update score counters
    if player_choice == computer_choice:
        print("Result: It's a tie!")
        ties += 1
    elif (
        (player_choice == Choice.ROCK and computer_choice == Choice.SCISSORS)
        or (player_choice == Choice.PAPER and computer_choice == Choice.ROCK)
        or (player_choice == Choice.SCISSORS and computer_choice == Choice.PAPER)
    ):
        print("Result: You win this round! 🎉")
        player_score += 1
    else:
        print("Result: Computer wins this round! 🤖")
        computer_score += 1

    # Check for target score victory condition
    if player_score == target_score:
        print(
            f"\n🏆 CONGRATULATIONS! You reached {target_score} points first and won the match!"
        )
        break
    elif computer_score == target_score:
        print(
            f"\n💻 GAME OVER! Computer reached {target_score} points first and won the match."
        )
        break

# Final Summary Display
print("\n================ FINAL MATCH SUMMARY ================")
print(f" Target Score: {target_score}")
print(f" Player Score: {player_score}")
print(f" Computer Score: {computer_score}")
print(f" Total Ties: {ties}")
print("=====================================================")
print("Thanks for playing! Goodbye.")
