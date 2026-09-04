import random  # This library gives us tools to generate unpredictible numbers.

# 1. MASTER LOOP: Wraps everything so 'Play Again' can actually restart the whole game
while True:
    secret_number = random.randint(1, 20)
    max_attempts = 0
    attempts = 0

    print("\n----- Welcome to the Secret Number Guessing Game! -----")
    print("Select Difficulty: Easy(1), Medium (2), Hard(3)")

    # Difficulty Selection Logic
    while True:
        choice = input("Enter difficulty (1, 2, or 3): ")
        if choice == "1":
            max_attempts = 10
            print("Easy mode selected: You have 10 attempts.")
            break
        elif choice == "2":
            max_attempts = 5
            print("Medium mode selected: You have 5 attempts.")
            break
        elif choice == "3":
            max_attempts = 3
            print("Hard mode selected: You have 3 attempts.")
            break
        else:
            print("Invalid choice! Please type 1, 2, or 3.")

    # 2. FIXED INDENTATION: This block is now completely aligned outside of the difficulty check!
    # Game Loop
    while attempts < max_attempts:
        try:
            guess = int(
                input(f"Attempt {attempts + 1}/{max_attempts} - Take a guess: ")
            )
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")
            continue
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break
    else:
        print(
            f"Game over! You ran out of attempts. The secret number was {secret_number}."
        )

    # Play Again Option
    play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
    if play_again not in ["y", "yes"]:
        print("Thanks for playing! Goodbye!")
        break  # This breaks the master loop and closes the game cleanly
