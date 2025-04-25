import random
import time
from colorama import init, Fore, Style

#Initialize colorama for colored output
init(autoreset=True)

# List of valid choices
choices = ["rock", "paper", "scissors"]

# ASCII art representations
ascii_art = {
    "rock": "🪨 Rock\n   _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)",
    "paper": "📄 Paper\n   _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)",
    "scissors": "✂️ Scissors\n   _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"
}


# Game Logic Functions

def print_seperator():
    print(Fore.BLUE + "=" * 50)

def countdown():
    print(Fore.YELLOW + "Get Ready!")
    for i in range(3, 0, -1):
        print(Fore.YELLOW + f"{i}...")
        time.sleep(0.5)

def get_player_choice():
    while True:
        choice = input(Fore.CYAN + "👉 Choose Rock, Paper, or Scissors: ").strip().lower()
        if choice not in choices:
            print(Fore.RED + "❌ Invalid input. Try again!")
        else:
            return choice
        
def display_ascii(choice):
    print(Fore.MAGENTA + ascii_art[choice])

# Main Game Logic   
def play_game():
    print_seperator() 
    name = input(Fore.CYAN + "What's your name, Player?: ").strip().title()

    user_wins = computer_wins = ties = total_rounds = 0
    round_number = 1

    print(Fore.YELLOW + f"\n🎮 Welcome {name}! First to 3 wins the crown  👑\n")

    while user_wins < 3 and computer_wins < 3:
        print_seperator()
        print(Fore.CYAN + f"\n🎯 Round {round_number}")
        countdown()

        user_choice = get_player_choice()
        computer_choice = random.choice(choices)

        print("\nYou Chose:")
        display_ascii(user_choice)
        print("\nComputer Chose:")
        display_ascii(computer_choice)

        if user_choice == computer_choice:
            print(Fore.YELLOW + "🤝 it's a tie!")
            ties += 1
        elif(
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print(Fore.GREEN + "✅ You win this round!")  
            user_wins += 1
        else:
            print(Fore.RED + "💻 Computer wins this round!")
            computer_wins += 1

        round_number += 1
        total_rounds += 1

        print_seperator()
        print(Fore.CYAN + Style.BRIGHT + f"📊 Game Over, {name}!")
        print(Fore.CYAN + f"Total Rounds: {total_rounds}")
        print(Fore.GREEN + f"Wins: {user_wins}")
        print(Fore.RED + f"Losses: {computer_wins}")
        print(Fore.YELLOW + f"Ties: {ties}")

        win_rate = (user_wins / total_rounds) * 100
        print(Fore.MAGENTA + f"🏅 Win Rate: {win_rate: .2f}%")

    print_seperator()
    replay = input(Fore.YELLOW + "🔁 Want to play? (yes or no): ").lower().strip()
    if replay == "yes":
        play_game()
    else:
        print(Fore.MAGENTA + "👋 Thanks for playing! See you next time!\n")


# Run the game
play_game()                         