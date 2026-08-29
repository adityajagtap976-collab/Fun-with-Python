import random
from enum import Enum


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


while True:

    print("\n-----Welcome to Rock, Paper, and Scissors game!-----")
    print("Select: 1 for Rock, 2 for Paper, 3 for Scissors, and q to Quit")

    # 1. Take input from the user
    user_choice = input("\nEnter your choice (1-3): ").strip()

    # Allow user to quit the loop
    if user_choice.lower() == "q":
        print("Thanks for playing! Goodbye.")
        break
    # 2. Validate input and convert to Enum
    if user_choice in ["1", "2", "3"]:
        player_choice = Choice(int(user_choice))
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 'q'.")
        continue

    # 3. Generate random choice for the computer
    computer_choice = random.choice(list(Choice))

    print(f"\nYou choose: {player_choice.name}")
    print(f"Computer chose: {computer_choice.name}")

    # 4. Determine the winner
    if player_choice == computer_choice:
        print("Result: It's a tie!")
    elif (
        (player_choice == Choice.ROCK and computer_choice == Choice.SCISSORS)
        or (player_choice == Choice.PAPER and computer_choice == Choice.ROCK)
        or (player_choice == Choice.SCISSORS and computer_choice == Choice.PAPER)
    ):
        print("Result: You Win! 🎉")
    else:
        print("Result: Computer wins! 🤖")
