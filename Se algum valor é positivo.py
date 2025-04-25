num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segund valor: "))
#Verificar se algum valor é positivo
if (num1 > 0 and num2 > 0):
    print("Os dois valores são positivos")
elif (num1 > 0 and num2 < 0):
    print("O primeiro valor é positivo")
elif (num2 > 0 and num1 < 0):
    print("O segundo valor é positivo")
elif (num1 < 0 and num2 < 0):
    print("Nenhum valor é positivo")