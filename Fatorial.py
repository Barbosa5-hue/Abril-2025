num = int(input('Digite o número: '))
print(f'Fatorial de {num}')

Fatorial = num
for i in range(num - 1,1,-1):
    Fatorial = (Fatorial * i)
 
print(Fatorial)