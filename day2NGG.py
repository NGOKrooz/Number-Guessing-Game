import random

def choose_difficulty():
    print("Choose difficulty level: ")
    print("1. Easy (10 attempts) ")
    print("2. Medium (7 attempts) ")
    print("3. Hard (5 attempts) ")

    while True:
        level = input("Enter 1, 2 or 3? ")
        if level == "1":
            return 10
        if level == "2":
            return 7
        if level == "3":
            return 5
        else:
            print("❌ Invalid input. Please choose 1, 2, or 3.")

def play_game():
    secret_number = random.randint(1,100)
    attempts_left = choose_difficulty()
    guess = None
    

    while attempts_left > 0:
        try:
                guess = int(input("Guess a number from 1-100 ?"))
        except ValueError:
                print("❌ Please enter a valid number.")
                continue
        if guess == secret_number:
                print(f"Correct! The number was {secret_number}. ")
                return
        elif guess > secret_number:
                    print("Number is too high")
        elif guess < secret_number:
                    print("Number is too small")

        attempts_left -= 1
        if attempts_left > 0:
              print(f"Attempts left: {attempts_left}")
        else:
              print(f"Game over! The number was {secret_number}.   ")

play_game()