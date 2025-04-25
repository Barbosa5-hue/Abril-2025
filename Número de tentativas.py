def adivinhar_numero(valor_predefinido):
    Tentativas += 0
    while True:
        Numero = int(input("Digite um número:"))
        Tentativas += 1
        if Numero == valor_predefinido:
            print(f"Você acertou o número em {Tentativas} tentetivas.")
            
            break
        
        elif Numero < valor_predefinido:
            print("O número é maior")
        else:
            print("O número é menor")
            
#Exemplo de uso
valor_predefinido = 42 #Defina o valor prdefinido aqui
adivinhar_numero(valor_predefinido)