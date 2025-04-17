import random
import os

# Constant
EASY_ATTEMPTS = 10
MEDIUM_ATTEMPTS = 7
HARD_ATTEMPTS = 5

SCORE_FILE = "scoreboard.txt"


def display_scoreboard():
    if os.path.exists(SCORE_FILE):
        print("\n previous scores: ")
        with open(SCORE_FILE, "r") as file:
            scores = file.readlines()
            for score in scores:
                print(score.strip())
    else:
        print("\n No previous scores yet.")

def choose_difficulty():
    print("\nchoose difficulty: ")
    print("1. Easy (10 attempts)")
    print("2. Easy (7 attempts)")
    print("3. Easy (5 attempts)")
    
    while True:
        level = input("Enter 1, 2 or 3: ")
        if level == "1":
            return EASY_ATTEMPTS
        elif level == "2":
            return MEDIUM_ATTEMPTS
        elif level == "3":
            return HARD_ATTEMPTS
        else:
            print("Invalid input. Please choose 1, 2 or 3")

      
def get_user_guess():
    while True:
       try:
            return int(input("Guess a number(1-100): "))
       except ValueError:
           print("Invalid input. Enter a number")

def save_score(username, result, attempts_used):
    """Save user's game result to scoreboard file."""
    with open(SCORE_FILE, "a") as file:
        file.write(f"{username} - {result} - {attempts_used} attempts\n")

def play_game():
    """Main game logic with scoreboard integration."""
    display_scoreboard()
    secret_number = random.randint(1, 100)
    attempts_allowed = choose_difficulty()
    attempts_used = 0

    while attempts_allowed > 0:
        guess = get_user_guess()
        attempts_used += 1

        if guess == secret_number:
            print(f" Correct! The number was {secret_number}.")
            result = "Won"
            break
        elif guess > secret_number:
            print(" Too high.")
        else:
            print(" Too low.")

        attempts_allowed -= 1
        print(f" Attempts left: {attempts_allowed}")

    else:
        print(f" Game Over! The number was {secret_number}.")
        result = "Lost"

    username = input(" Enter your name for the scoreboard: ")
    save_score(username, result, attempts_used)

# Start game
play_game()