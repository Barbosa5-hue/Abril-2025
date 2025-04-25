num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
#Verificar se são pares
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos os valors são pares")
elif num1 % 2 == 0:
    print("O primeiro valor é par")
elif num2 % 2 == 0:
    print("O segundo valor é par")
elif num1 and num2 % 2 != 0:
    print("Nenhum dos valores é par")