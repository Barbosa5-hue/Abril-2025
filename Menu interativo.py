def menu():
    print("Ecolha uma opção: ")
    print("1.Somar")
    print("2.Subtrair")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Sair")
    
def somar (a,b):
    return a + b

def subtrair (a,b):
    return a - b

def multiplicar (a,b):
    return a * b

def divivir (a,b):
    return a/b

while True:
    menu()
    Opção = input("Digite a opção desejada: ")
    
    if Opção == '5':
        print("Saindo do programa...")
                            
        break
                        
    elif Opção in ['1','2','3','4']:
        Num1 = float(input("Digite o primeiro número: "))
        Num2 = float(input("Digite o segundo número: "))
                            
        if Opção == '1':
            Resultado = somar(Num1,Num2)
            print(f"O resultado da soma é {Resultado}")
                                
            break
                        
        if Opção == '2':
            Resultado = subtrair(Num1,Num2)
            print(f"O reultado da soma é {Resultado}")
                            
            break
                        
        if Opção == '3':
            Resultado = multiplicar(Num1,Num2)
            print(f"O resultado da multiplicação é {Resultado}")
                    
            break
                    
        if Opção == '4':
            Resultado = divivir(Num1,Num2)
            print(f"O resultado da divisão é {Resultado}")
        
        break
    
    else:
        print("Opção inválida. Tente novamente.")
        
print("Programa encerrado.")