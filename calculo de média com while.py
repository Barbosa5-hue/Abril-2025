def calcular_media():
    numeros = []
    while True:
        Entrada = input("Digite um número(ou fim para terminar): ")
        if Entrada.lower() == "fim":
            break
        try:
            numero = float(Entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida, por favor, digite um número ou 'fim' para terminar: ")
            
            if numeros:
                media = sum(numeros)/len(numeros)
                print(f"A média dos números digitados é {media:2f}")
            else:
                print("Nenhum número foi digitado.")
                
                #Exemplo de uso
                calcular_media()