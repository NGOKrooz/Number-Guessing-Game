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


## Day 5 - #100DaysOfPython

Today, I took a deliberate step back to **review and deeply understand the Day 4 code**, which introduced a number guessing game with features like difficulty levels, scoreboard persistence, and user input validation.

### What I Focused On:
- Carefully walked through each line of code.
- Studied the use of Python modules like `random` and `os`.
- Understood key concepts such as:
  - Functions and how they modularize code.
  - File handling (`open`, `readlines`, `write`).
  - Conditional logic for game flow.
  - Input validation using `try/except`.
  - Use of constants to manage game settings.

### Reflection:
Instead of rushing into the upgrade task, I prioritized clarity over speed. This review not only helped solidify the fundamentals but also gave me confidence to build more complex features in upcoming days.

**Next Up:** Enhancing the game with new functionalities!

Stay tuned for Day 6!


# 🚀 Day 6 – Final Polish for the Number Guessing Game 🎯

Today, I focused on improving the **User Experience** of my terminal-based Python game. The goal was to make the interaction feel smoother and more engaging for the player.

### ✅ What I Added:
- **👋 Welcome Message** at the start of the game to greet the player.
- **🧼 Cleaner Prompts** using emojis and clear formatting for inputs.
- **📜 Guess History Tracker** – After each guess, players now see a list of all previous guesses.

### 🧠 What I Learned:
- How to structure user-friendly prompts in CLI games.
- How to use lists to keep track of guess history.
- The value of small UX improvements in creating delightful software.

### 🛠️ Next Steps:
In the upcoming days, I’ll look into adding more feedback (like colors using `colorama`) and possibly wrapping the game in a simple GUI.

---

👣 Follow along my journey: #100DaysOfCode  
📂 This project is part of my beginner Python series.

