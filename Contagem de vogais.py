def contar_vogais(string):
    Vogais = "a,e,i,o,u,A,E,I,O,U"
    contador = 0
    for caracterre in string:
        if caracterre in Vogais:
            contador +=1
    return contador

    #Exmplo de uso
Texto = input("Digite uma string: ")
Numero_de_vogais = contar_vogais(Texto)
print(f"A string fornecida contém {Numero_de_vogais} vogais.")