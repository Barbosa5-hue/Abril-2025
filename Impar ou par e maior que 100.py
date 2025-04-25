num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
#Verificar se são pares
if(num1 % 2 == 0 and num2 % 2 != 0):
    print("O primeiro valor é par e o segundo é impar")
elif(num1 % 2 != 0 and num2 % 2 == 0):
    print("O primeiro valor é impar e o segundo é par")
elif(num1 % 2 != 0 and num2 != 0):
    print("Os dois valores são impares")
elif(num1 % 2 == 0 and num2 % 2 == 0):
    print("Os dois valores são pares")
#Verificar se são maiores que 100
if(num1 > 100 and num2 <= 100):
    print("Apenas o pimeiro valor é maior que 100")
elif(num1 <= 100 and num2 > 100):
    print("Apenas o segundo valor é maior que 100")
elif(num1 <+ 100 and num2 <= 100):
    print("Nenhum dos dois valores são maiores que 100")
elif(num1 > 100 and num2 > 100):
    print("Os dois valores são maiores que 100")