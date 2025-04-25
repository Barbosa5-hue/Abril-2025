idade = float(input("Digite a idade: "))
#Determinar necessidade do voto
if (0 <= idade < 16):
    print("Não pode votar, pois é menor de 16 anos")
elif (16 <= idade <18):
    print("O voto é opcional, mas não obrigatório")
elif (18 <= idade < 70):
    print("O voto é obrigatório")
elif (70 <= idade):
    print("O voto já não é obrigatório")