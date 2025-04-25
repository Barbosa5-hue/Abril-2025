lado1 = float(input("Digite o valoe do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite  valor do terceiro lado: "))
if (lado1 > lado2 and lado3) and (lado1 ** 2 == lado2 ** 2 + lado3 ** 2):
    print("O triângulo é retângulo")
if (lado2 > lado1 and lado3) and (lado2 ** 2 == lado1 ** 2 + lado3 ** 2):
    print("O triângulo é retângulo")
if (lado3 > lado1 and lado2) and (lado3 ** 2 == lado1 ** 2 + lado2 ** 2):
    print("O triângulo é retângulo")
if lado1 != lado2 != lado3:
    print("O triângulo é escaleno")
if lado1 == lado2 == lado3:
    print("O triângulo é equilátero")
if lado1 == lado2 != lado3 or lado2 == lado3  != lado1 or lado1 == lado3 != lado2:
    print("O triângolo é isósceles")
if (lado1 > lado2 and lado3) and (lado1 ** 2 == lado2 ** 2 + lado3 ** 2):
    print("O triângulo é retângulo")