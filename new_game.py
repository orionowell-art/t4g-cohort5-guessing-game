import random

print("=" * 40)
print("      NUMBER GUESSING GAME")
print("=" * 40)


def guessing_loop(secret_number):
    attempts = 0

    while True:
        guess = input("\nEnter your guess (1-100): ")

        # Check for empty input
        if guess == "":
            print("Input cannot be empty. Please enter a number.")
            continue

        # Check if input is an integer
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        # Check if number is within range
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("\nCongratulations! You guessed the correct number!")
            print(f"The secret number was {secret_number}.")
            print(f"You guessed it in {attempts} attempt(s).")
            return


def replay():
    while True:
        play_again = input("\nWould you like to play again? (yes/no): ").lower()

        if play_again in ("yes", "y"):
            return True
        elif play_again in ("no", "n"):
            print("\nThank you for playing! Goodbye.")
            return False
        else:
            print("Please enter 'yes' or 'no'.")


while True:
    secret_number = random.randint(1, 100)

    print("\nI have chosen a number between 1 and 100.")
    print("Try to guess it!")

    guessing_loop(secret_number)

    if not replay():
        break