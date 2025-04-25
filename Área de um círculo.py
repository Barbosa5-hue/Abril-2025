print("Verifique a área de um círculo")
r = float(input("Digite o valor do raio: "))
area = 3.14 * (r ** 2)
print("A área do círculo é igual a:",area)
if area < 0:
    print("Não foi possíver resolver a operação")