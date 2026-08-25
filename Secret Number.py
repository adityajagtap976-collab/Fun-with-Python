import random #This library gives us tools to generate unpredictible numbers.

secret_number = random.randint(1, 20)
max_attempts = 5
attempts = 0

print("Welcome to the Secret Number Guessing Game!")
print(f"I am thinking of a number between 1 and 20. You have {max_attempts} attempts!")

while True:
  guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Take a guess: "))
  attempts += 1

  if guess < secret_number:
    print("Too low! Try again.")
  elif guess > secret_number:
    print("Too high! Try again.")
  else:
    print(f"Congratulations! You guessed it in {attempts} attempts!")
    break
else:
  print(f"Game over! You ran out of attempts. The secret number was {secret_number}.")