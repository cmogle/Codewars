import time
import random
from getpass import getpass

def get_choice(prompt):
    return getpass(prompt).upper()

print("Welcome to Rock Paper Scissors!")
print("This game is for 2 local players.")
print("Each player will enter their choice of R, P, or S.")
print("R = Rock, P = Paper, S = Scissors")
print("The game will be played 5 times.")
print("The player with the most wins will be the winner.")
print("Good luck!")

player1_name = input("Enter Player 1 name: ").title()
player2_name = input("Enter Player 2 name: ").title()

player1_score = 0
player2_score = 0
rounds = 5

win_conditions = {
    "R": "S",
    "P": "R",
    "S": "P"
}

for i in range(rounds):
    print(f"Round {i + 1}:")
    player1_choice = get_choice(f"{player1_name}, enter your choice: ")
    player2_choice = get_choice(f"{player2_name}, enter your choice: ")

    if player1_choice == player2_choice:
        print("It's a tie!")
    elif win_conditions[player1_choice] == player2_choice:
        print(f"{player1_name} wins this round!")
        player1_score += 1
    else:
        print(f"{player2_name} wins this round!")
        player2_score += 1

    print(f"Current score: {player1_name}: {player1_score} | {player2_name}: {player2_score}\n")
    time.sleep(random.randint(1, 3))

print(f"Final score:\n{player1_name}: {player1_score}\n{player2_name}: {player2_score}")

if player1_score == player2_score:
    print("The game is a tie!")
elif player1_score > player2_score:
    print(f"{player1_name} is the winner!")
else:
    print(f"{player2_name} is the winner!")
