import random
lista = ["pedra", "papel", "tesoura"]

def start_game():
    print("Pedra, papel ou tesoura?")
    
def roll_dice():
    return (random.choice(lista))
    
def resposta(x):
    if x in lista:
        print(x)
        return roll_dice()
    
    else:
        print("Insira uma escolha válida")
        

start_game()

resposta(input())
