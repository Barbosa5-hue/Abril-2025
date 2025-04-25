def eh_perfeito(numero):
    Soma_divisores = 0
    for i in range (1,numero):
        if numero % i == 0:
            Soma_divisores += i
        return Soma_divisores == numero
    
#Exemplo de uso
numero =int(input("Digite um número:"))
if eh_perfeito(numero):
    print(f"O número {numero} é perfeito.")
else:
    print(f"O número {numero} não é perfeito.")