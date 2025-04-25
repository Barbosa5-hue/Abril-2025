def verificar_senha(senha_correta):
    while True:
        Senha = input("Diite a senha: ")
        if Senha == senha_correta:
            print("A senha está correta! Acesso pemitido.")
            break
        else:
            print("Senha incorreta. Tente novamente.")
            
#Exemplo de uso
senha_correta = "8429384" #Defina a senha correta aqui
verificar_senha(senha_correta)