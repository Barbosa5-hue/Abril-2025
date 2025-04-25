#Descobrir número
import random
def adivinhar_numero():
    Numero_secreto = random.randint(1,100)
    Tentativa = None
    
    while Tentativa != Numero_secreto:
        Tentativa = int(input("Digite um número entre 1 e 100: "))
        if Tentativa < Numero_secreto:
            print("O número é maior")
        elif Tentativa > Numero_secreto:
            print("O número é menor")
        else:
            print("Número correto!")
            
           
#Exemplo de uso
adivinhar_numero()