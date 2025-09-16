player_wins = 0
computer_wins = 0
import random

print("Let's play rock, paper, or scissors")
print('First to 3 wins')
print()

while player_wins < 3 and computer_wins < 3:
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)
  player_choice = input("Choose rock, paper, or scissors:\n").lower()

  print(f"Computer chose: {computer_choice}")
  if (player_choice == "rock" and computer_choice == "scissors") or    (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
    winner = "Player"
  elif (player_choice == "rock" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "paper"):
    winner = "Tie"
  else:
    winner = "Computer"

  if (winner == "Player"):
    player_wins += 1
    print("You won")
  elif (winner == "Computer"):
    computer_wins += 1
    print("Computer won")
  else:
    print("It's a tie")
  
  print()
  print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")
  print()

  if player_wins == 3:
    print("Congratulations! You won.")
    print('Thank you for playing!')
    break
  elif computer_wins == 3:
    print("Computer won!")
    print('Thank you for playing!')
    break
