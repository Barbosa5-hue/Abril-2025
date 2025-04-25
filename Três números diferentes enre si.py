num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o sgundo valor: "))
num3 = float(input("Diite o terceiro valor: "))
#Determinar quais valores são iguais ou diferentes
if (num1 == num2 != num3):
    print("O primeiro e segundo valor são iguais e diferentes do terceiro")
elif (num1 != num2 == num3):
    print("O segundo e terceiro valor são igualis e diferntes do primeiro")
elif (num1 == num3 != num2):
    print("O primeiro e o terceiro valor são iguais e diferentes do segundo")
elif (num1 == num2 == num3):
    print("Todos os valores são iguais")
elif (num1 != num2 != num3):
    print("Os três valores são diferentes")