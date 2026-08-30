import random
from enum import Enum


class Choice(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


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

player_score = 0
computer_score = 0
ties = 0

print(f"\nFirst player to reach {target_score} wins! Let's start.")

while True:
    print(
        f"\nSCOREBOARD | You: {player_score}/{target_score} | Computer: {computer_score}/{target_score} | Ties: {ties}"
    )
    print("Select:\n0 for Rock\n1 for Paper\n2 for Scissors\nq to Quit early")

    user_input = input("\nEnter your choice (0-2): ").strip()

    if user_input.lower() == "q":
        print("\nGame ended early by player.")
        break

    if user_input in ["0", "1", "2"]:
        player_choice = Choice(int(user_input))
    else:
        print("Invalid choice! Please enter 0, 1, 2, or 'q'.")
        continue

    computer_choice = random.choice(list(Choice))

    print(f"\nYou chose: {player_choice.name}")
    print(f"Computer chose: {computer_choice.name}")

    # --- Modulo Arithmetic Win/Loss Logic ---
    # Formula: (Player - Computer) % 3
    # Result == 0 -> Tie
    # Result == 1 -> Player Win
    # Result == 2 -> Computer Win
    result = (player_choice.value - computer_choice.value) % 3

    if result == 0:
        print("Result: It's a tie!")
        ties += 1
    elif result == 1:
        print("Result: You win this round! 🎉")
        player_score += 1
    else:  # result == 2
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
