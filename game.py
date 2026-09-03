import random

print("\n--- Pedra, Papel, Tesoura ----")

# Variables definition
options = ["pedra", "papel", "tesoura"]
player_points : int = 0
computer_points : int = 0
player_name : str = ""

# Points method to show on the interface
def show_points():
    print(f"Player: {player_points} x Bot : {computer_points}")

# Condition game and start.
player_name : str = input("Insira seu nome jogador: ")
while player_points < 5 and computer_points < 5:
    computer = random.choice(options)
    player = input("Escolha (pedra/papel/tesoura): ").lower()
    if player not in options:
        print("Opção inválida!")
    elif player == computer:
        print("Empate")
    elif (player == "pedra" and computer == "tesoura" or player == "papel" and computer == "pedra" or
    player == "tesoura" and computer == "papel"):
        print("Você ganhou!")
        player_points += 1
    else:
        print("Bot ganhou!")
        computer_points += 1
    show_points()

# Condition winner
if player_points == 5:
    print(f"Jogador: {player_name} Vencedor!")
else:
    print(f"Você perdeu ;-;")