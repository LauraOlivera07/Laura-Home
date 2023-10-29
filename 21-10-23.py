import random

def get_choices():
    player_choice= input("Enter a choice (rock, paper, scissors): ")
    options=["rock", "paper", "scissors"]
    computer_choice= random.choice(options)
    choices={"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"Has elegido {player}, el ordenador ha elegido {computer}")
    if player==computer:
      return "¡Empate!"

#check_win("rock", "paper")
