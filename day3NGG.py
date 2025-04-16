import random

# 🔁 Constants for difficulty levels
EASY_ATTEMPTS = 10
MEDIUM_ATTEMPTS = 7
HARD_ATTEMPTS = 5

def choose_difficulty():
    """Prompt the user to choose a difficulty level and return the number of allowed attempts."""
    print("Choose difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    while True:
        level = input("Enter 1, 2 or 3: ")
        if level == "1":
            return EASY_ATTEMPTS
        elif level == "2":
            return MEDIUM_ATTEMPTS
        elif level == "3":
            return HARD_ATTEMPTS
        else:
            print("❌ Invalid input. Please choose 1, 2, or 3.")

def get_user_guess():
    """Get a number guess from the user, handling invalid input."""
    while True:
        try:
            return int(input("Guess a number from 1 to 100: "))
        except ValueError:
            print("❌ Please enter a valid number.")

def play_game():
    """Main function to run the game logic."""
    secret_number = random.randint(1, 100)
    attempts_left = choose_difficulty()

    while attempts_left > 0:
        guess = get_user_guess()

        if guess == secret_number:
            print(f"🎉 Correct! The number was {secret_number}.")
            return
        elif guess > secret_number:
            print("📈 Too high.")
        elif guess < secret_number:
            print("📉 Too low.")

        attempts_left -= 1

        if attempts_left > 0:
            print(f"🔄 Attempts left: {attempts_left}")
        else:
            print(f"💀 Game Over! The correct number was {secret_number}.")

# 🚀 Start the game
play_game()
