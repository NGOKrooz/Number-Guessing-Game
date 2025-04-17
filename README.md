# Number-Guessing-Game
Welcome to my **90 Days of Python Coding Challenge**!  
This repository documents my daily progress as I build mini-projects to master Python.

---

## ✅ Day 1: Basic Number Guessing Game

### 🔧 Features:
- Program randomly selects a number between **1 and 14**.
- User is prompted to guess the number.
- Program gives feedback:
  - "Too high"
  - "Too low"
  - "Correct!"
- Tracks the number of attempts until the correct guess.
- Handles invalid inputs using `try` and `except`.

### 🧠 Concepts Practiced:
- `random` module (`random.randint()`)
- `input()`, `int()`, variables
- `while` loop and conditionals
- Basic error handling with `try` / `except`

---

## ✅ Day 2: Difficulty Levels + Limited Attempts

### 🔧 Features:
- Added **difficulty levels**:
  - Easy: 10 attempts
  - Medium: 7 attempts
  - Hard: 5 attempts
- User selects difficulty using a menu.
- Limited number of guesses based on difficulty.
- Remaining attempts are displayed after each incorrect guess.
- Game ends with a **"Game Over"** message if all attempts are used.
- Handles non-numeric input with proper error messaging.

### 🧠 Concepts Practiced:
- Function creation (`choose_difficulty()`, `play_game()`)
- User input and menu navigation
- Looping with attempt limits
- Better exception handling and game logic

  🧩 Day 3: Functions & Clean Code
Refactored the number guessing game by organizing code into reusable functions:

choose_difficulty() handles level selection

get_user_guess() manages user input and validation

play_game() runs the main game logic

Also introduced constants for difficulty levels to avoid magic numbers and improve clarity.

📍Lesson: Clean code, function structure, input validation, game logic.


✅ Day 4: Scoreboard with File Handling
What I Did:

🎯 Added a scoreboard to my number guessing game!

Display previous scores at the start using display_scoreboard().

Save the player's name, result (Won/Lost), and number of attempts used with save_score().

Used Python's os.path.exists() to check if the score file exists.

Used with open() for safe reading and writing to scoreboard.txt.

📚 What I Learned:

File I/O (reading/writing to files).

Appending and formatting strings for logs.

How to persist data across game sessions.

Importance of clean functions and modular code.
