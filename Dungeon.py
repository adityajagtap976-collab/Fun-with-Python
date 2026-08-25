import random #This library gives us tools to generate unpredictible numbers.

secret_number = random.randint(1, 20)
attempts = 0

print("Welcome to the Secret Number Guessing Game!")
print("I am thinking of a number between 1 and 20.")

while True:
  guess = int(input("Take a guess: "))
  attempts += 1

  if guess < secret_number:
    print("Too low! Try again.")
  elif guess > secret_number:
    print("Too high! Try again.")
  else:
    print(f"Congratulations! You guessed it in {attempts} attempts!")
    break