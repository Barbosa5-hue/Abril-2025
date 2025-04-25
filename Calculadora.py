print("Calculadora")
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
operação = input("Selecione a operação desejada: ")
#Determinar operação e calcular
if operação == "+":
    resultado = num1 + num2
    print(resultado)
elif operação == "-":
    resultado = num1 - num2
    print(resultado)
elif operação =="*":
    resultado = num1 * num2
    print(resultado)
elif operação == "/":
    resultado = num1 / num2
    print(resultado)