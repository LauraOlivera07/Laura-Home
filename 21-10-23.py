import random

def get_choices():
    player_choice= input("Enter a choice (rock, paper, scissors): ")
    options=["rock", "paper", "scissors"]
    computer_choice= random.choice(options)
    return player_choice,computer_choice

def check_win(player, computer):
    print(f"Has elegido {player}, el ordenador ha elegido {computer}")
    if player==computer:
      return "¡Empate!"
    else:
        match player:
            case 'rock':
                match computer:
                    case 'paper': return "¡Has perdido!"
                    case 'scissors': return "¡Has ganado!"
            case 'paper':
                match computer:
                    case 'rock': return "¡Has ganado!"
                    case 'scissors': return "¡Has perdido!"
            case 'scissors':
                match computer:
                    case 'rock': return "¡Has perdido!"
                    case 'paper': return "¡Has ganado!"

player,computer=get_choices()
resultado=check_win(player,computer)
print(resultado)
