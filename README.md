# Rock - Paper - Scissors Game

## 🎮 Project Description

This project is a simple terminal application that makes the classic game of "Rock - Paper - Scissors" playable in Python.

The user chooses between rock/paper/scissors; the computer makes a random choice, and the result is displayed on the screen.
The goal is to learn algorithmic thinking and conditional statements (if-elif-else).


## 🧠 Game Rules

User Selection      Computer Selection      Result

Rock                Scissors                User Wins
Scissors            Paper                   User Wins
Paper               Stone                   User Wins
Scissors            Rock                    Computer Wins
Paper               Scissors                Computer Wins
Rock                Paper                   Computer Wins
Same Election       Same Election           Draw


## Pseudocode
Start
Get user's choice (rock/paper/scissors)
Randomize computer's choice

If user == computer:
Write "Draw"

If (user == "rock" and computer == "scissors") or
   (user == "scissors" and computer == "paper") or
   (user == "paper" and computer == "rock"):
   Write "User wins!"

Otherwise:
Write "Computer wins!"

Finish


## ⚙️ How Does It Work?

1) The program uses the random module to make the computer make a selection.

2) Input is received from the user (input() function).

3) The two selections are compared.

4) The result is printed to the terminal.


## 🧩 Code Sample

# Loading the library file
import random

print("Welcome to the Rock-Paper-Scissors Game")
print()

# Choosing the game
options = ["rock", "paper", "scissors.py"]

# Receiving data from the user
user = input("What is your choice? (rock/paper/scissors): ").lower()
# The .lower() method converts the entered letters to lowercase. (STONE → stone)
# This way, we avoid uppercase/lowercase errors.


# The random.choice() function chooses a random element from the "choices" list
computer = random.choice(options)

print(f"Selection of computer: {computer}")

if user == computer:
    print("Draw!")
    # If both sides made the same choice, the game ends in a draw.

elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
    print("Congratulations! You won!")
    # We check the user's winning conditions.
    # Each 'or' expression represents a different winning scenario.

else:
    print("Computer won!")
   # If neither of the above two cases occur (a draw or the user did not win),
   # Then the computer won.


## Running in Terminal

Go to the project folder and run the following command:
python rock_paper_scissors.py

## 👨‍💻 Developer

Furkan İPEK
📂 Python Classic Projects Series