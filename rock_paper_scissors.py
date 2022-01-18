import random
lista = ["pedra", "papel", "tesoura"]

def start_game():
    print("Pedra, papel ou tesoura?")
    
def roll_dice():
    return (random.choice(lista))
    
def resposta():
    x = input()
    while True:
        if x in lista:
            print(roll_dice())
            break
        else:
            print("Insira uma escolha válida entre (Pedra, papel ou tesoura)!")
            return resposta()
        

start_game()

resposta()
