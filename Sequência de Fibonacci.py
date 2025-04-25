quantidade_vezes = int(input("Digite quantos elemntos você deseja ques seja exibido: "))
anterior = 1
atual = 0

for X in range(1, quantidade_vezes + 1):
    próximo = atual + anterior
    anterior = atual
    atual = próximo
    
    print(próximo)