#Tabuada de um número
def tabuada (num):
    print(f"Tabuada do {num}:")
    for i in range(1,11):
        resultado = num * i
        print(f"Tabuada de {i} x número = {resultado}")
        
num = int(input("Digite um número para ver a tabuada: "))
tabuada(num)