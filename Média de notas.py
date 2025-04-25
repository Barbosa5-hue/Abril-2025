acumulador = 0
for i in range(1,6):
    nota = int(input("Coloque sua nota: "))
    acumulador = acumulador + nota

media = acumulador/5
print(media)