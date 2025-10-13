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