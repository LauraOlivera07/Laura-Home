import random
player_name=input("¿Cómo te llamas? ")

def get_starter():
    starter=["Bulbasaur", "Charmander", "Pikachu", "Squirtle"]
    selected_starter= random.choice(starter)
    return selected_starter
your_starter=get_starter()
print(f"Tu inicial para esta aventura será {your_starter}, "+player_name)
