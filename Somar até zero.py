def somar_ate_zero():
    soma = 0
    while True:
        Numero = int(input('Digite um número qualquer(0 para sair): '))
        if Numero == 0:
            break
        for i in range(1,Numero):
            Numero += i
        print(f"A soma total é: {Numero}")
        
    #Exemplo de uso
somar_ate_zero()