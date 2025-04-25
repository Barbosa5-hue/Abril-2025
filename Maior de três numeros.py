num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))
#Verificar o maior valor
if (num2 < num1 > num3):
    print("O primeiro número é o maior valor")
elif (num3 < num2 > num1):
    print("O segundo número é o maior valor")
elif (num1 < num3 > num2):
    print("O terceiro número é o maior valor")